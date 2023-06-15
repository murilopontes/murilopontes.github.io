

import os
import requests
import re
import sys
from urllib.parse import urlsplit
from lxml import etree
import xml.etree.ElementTree as ET
from datetime import datetime
from html2markdown import convert



def convert_html_to_markdown(html_content):
    # Convert HTML to Markdown
    markdown_content = convert(html_content)
    return markdown_content


def substituir_caracteres(texto):
    padrao = r'[^a-zA-Z0-9-]'
    return re.sub(padrao, '-', texto)

def download_image(url, path='images'):
    """Downloads an image and saves it in the specified directory."""
    os.makedirs(path, exist_ok=True)
    response = requests.get(url, stream=True)
    filename = os.path.join(path, urlsplit(url).path.split('/')[-1])

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    return filename

def convert_blog_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        #for child in entry:
        #    child_tag = child.tag
        #    print(child_tag)
        
        id = entry.find('{http://www.w3.org/2005/Atom}id').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        updated = entry.find('{http://www.w3.org/2005/Atom}updated').text
        category = entry.find('{http://www.w3.org/2005/Atom}category').attrib['term']
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        content = entry.find('{http://www.w3.org/2005/Atom}content').text
        author = entry.find('{http://www.w3.org/2005/Atom}author').text

        if category == "http://schemas.google.com/blogger/2008/kind#post":
            category = "post"
            #continue
        if category == "http://schemas.google.com/blogger/2008/kind#page":
            category = "page"
            #continue

        #ignore blogger settings
        if category == "http://schemas.google.com/blogger/2008/kind#settings":
            continue
        #ignore blogger templates
        if category == "http://schemas.google.com/blogger/2008/kind#template":
            continue
        #ignore blogger comments
        if category == "http://schemas.google.com/blogger/2008/kind#comment":
            continue


        if published is None:
            continue
        if title is None:
            continue
        if content is None:
            continue
        if category is None:
            continue

        # Format the date in Jekyll's filename format
        date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S.%f%z")
        filename = date.strftime("%Y-%m-%d") + "-" + re.sub(r'\W+', '-', substituir_caracteres(title.lower())) + ".md"

        filepath = ""
        if category == "page":
            filepath = os.path.join("_pages", filename)
        else:
            filepath = os.path.join("_posts", filename)
 
        #print(filename)
        # Generate the Jekyll post file

        title = title.replace(':', '-')

        with open(filepath, 'w', encoding='utf-8', errors='replace') as f:
            f.write('---\n')
            if category == "page":
                f.write('layout: page\n')
            else:
                f.write('layout: post\n')
            
            f.write('title: {}\n'.format(title))
            f.write('categories:\n')
            f.write(' - {}\n'.format(category))

            f.write('date: {}\n'.format(date.strftime("%Y-%m-%d %H:%M:%S %z")))
            f.write('---\n')
            f.write('\n')
            f.write(convert_html_to_markdown(content))
            #f.write("")

        print("Converted '{}' to '{}'".format(title, filepath))

# Specify the input XML file and output directory for Jekyll files
xml_file = 'blog-06-15-2023.xml'
# Convert the blog XML file to Jekyll posts
convert_blog_xml(xml_file)

