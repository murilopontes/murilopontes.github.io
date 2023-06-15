---
layout: post
title: Google Cloud Plataform - Compute engine - comand line examples
categories:
 - Command Line
date: 2016-03-27 20:26:00 +0100
---

  

  

#list machine types  

gcloud compute machine-types list  

  

#list created instances  

gcloud compute instances list  

  

#create a redhat-6 instance with default machine type  

gcloud compute instances create example-instance --image rhel-6 --zone us-central1-a  

  

#delete redhat-6 instance  

gcloud compute instances delete example-instance --zone us-central1-a  

  

#create a ubuntu 15.10 instance with f1-micro machine type  

gcloud compute instances create ubuntu1510-f1micro --image ubuntu-15-10 --zone us-central1-a --machine-type f1-micro  

  

#create a ubuntu 15.10 instance with f1-micro machine type with HTTP/HTTPS enabled  

gcloud compute instances create ubuntu1510-f1micro --image ubuntu-15-10 --zone us-central1-a --machine-type f1-micro &nbsp;--tags http-server,https-server  

<div>
<br/></div>

#stop ubuntu 15.10 instance  

gcloud compute instances stop ubuntu1510-f1micro &nbsp;--zone us-central1-a  

  

#start ubuntu 15.10 instance  

gcloud compute instances start ubuntu1510-f1micro &nbsp;--zone us-central1-a  

  

#hardware reboot ubuntu 15.10 instance  

gcloud compute instances reset ubuntu1510-f1micro &nbsp;--zone us-central1-a  

  

  

#ubuntu 15.10 instance change machine type to n1-standard-1  

gcloud compute instances set-machine-type ubuntu1510-f1micro --machine-type n1-standard-1 --zone us-central1-a  

  

#ubuntu 15.10 instance change machine type to g1-small  

gcloud compute instances set-machine-type ubuntu1510-f1micro --machine-type g1-small &nbsp;--zone us-central1-a  

  

#ubuntu 15.10 instance change machine type to f1-micro  

gcloud compute instances set-machine-type ubuntu1510-f1micro --machine-type f1-micro &nbsp;--zone us-central1-a  

  

#ubuntu 15.10 instance enable HTTP/HTTPS access  

gcloud compute instances add-tags ubuntu1510-f1micro --zone us-central1-a --tags http-server,https-server  

<div>
<br/></div>

<div>
<br/></div>

<div>
<br/></div>

  

  

  

  