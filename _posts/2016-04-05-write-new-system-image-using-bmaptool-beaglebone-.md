---
layout: post
title: Write new system image using bmaptool (beaglebone)
categories:
 - post
date: 2016-04-05 15:57:00 +0100
---

  

#install   

sudo apt-get -y install bmap-tools  

  

# download image and bmap file  

wget <https://debian.beagleboard.org/images/bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.img.xz>  

wget&nbsp;<https://debian.beagleboard.org/images/bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.bmap>  

  

&nbsp;#write system image  

bmaptool copy bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.img.xz /dev/sdb  

  

  

#results  

bmaptool: info: discovered bmap file 'bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.bmap'  

bmaptool: info: block map format version 2.0  

bmaptool: info: 870400 blocks of size 4096 (3.3 GiB), mapped 743361 blocks (2.8 GiB or 85.4%)  

bmaptool: info: copying image 'bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.img.xz' to block device '/dev/sdb' using bmap file 'bone-debian-8.3-lxqt-4gb-armhf-2016-01-24-4gb.bmap'  

bmaptool: info: 1% copied