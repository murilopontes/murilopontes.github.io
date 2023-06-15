---
layout: post
title: Debian / Ubuntu- build custom package with checkinstall
categories:
 - Debian
date: 2016-05-07 15:27:00 +0100
---

Using checkinstall is easy to manage/remove custom packages.  

  

apt-get -y install checkinstall  

  

wget custom-package.tar.gz  

tar xfvz custom-package.tar.gz  

cd custom-package  

./configure  

make  

checkinstall make install  

  

# list package contents  

dpkg -L custom-package  

  

# remove package  

dpkg -r custom-package