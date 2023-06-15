---
layout: post
title: fix gitlab with letsencrypt certificate
categories:
 - post
date: 2016-08-13 05:08:00 +0100
---

Cannot register Go Runner because of x509: certificate signed by unknown authority
If you are using a letsencrypt certificate the bug is trigged by curl.

curl  https://gitlab.example.com:9999/ci/api/v1/runners/register.json
curl: (60) SSL certificate problem: unable to get local issuer certificate

To fix this, add letsencrypt root certificates to system

<pre>
sudo curl https://letsencrypt.org/certs/isrgrootx1.pem.txt -o /usr/local/share/ca-certificates/isrgrootx1.crt
sudo curl https://letsencrypt.org/certs/letsencryptauthorityx1.pem.txt -o /usr/local/share/ca-certificates/letsencryptauthorityx1.crt
sudo curl https://letsencrypt.org/certs/letsencryptauthorityx2.pem.txt -o /usr/local/share/ca-certificates/letsencryptauthorityx2.crt
sudo curl https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem.txt -o /usr/local/share/ca-certificates/letsencryptx1.crt
sudo curl https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.pem.txt -o /usr/local/share/ca-certificates/letsencryptx2.crt
sudo curl https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem.txt -o /usr/local/share/ca-certificates/letsencryptx3.crt
sudo curl https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.pem.txt -o /usr/local/share/ca-certificates/letsencryptx4.crt
sudo dpkg-reconfigure ca-certificates
</pre>

<pre>
gitlab-ci-multi-runner register
Running in system-mode.

Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/ci):
https://gitlab.example.com:9999/ci
Please enter the gitlab-ci token for this runner:
5454353453453453534
Please enter the gitlab-ci description for this runner:
[example2]:
Please enter the gitlab-ci tags for this runner (comma separated):
shared
Registering runner... succeeded                     runner=43242342
Please enter the executor: parallels, shell, ssh, virtualbox, docker+machine, docker-ssh+machine, docker, docker-ssh:
docker
Please enter the default Docker image (eg. ruby:2.1):
ubuntu:16.04
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
</pre>