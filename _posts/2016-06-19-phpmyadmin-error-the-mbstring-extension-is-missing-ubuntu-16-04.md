---
layout: post
title: phpMyAdmin - Error | The mbstring extension is missing. Ubuntu-16.04
categories:
 - post
date: 2016-06-19 16:30:00 +0100
---

Try using:
  

<pre>sudo apt-get install php-gettext
sudo phpenmod mcrypt 
sudo phpenmod mbstring 
sudo service apache2 restart
</pre>