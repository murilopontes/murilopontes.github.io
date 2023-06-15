---
layout: post
title: Ubuntu 14.04 x64 / AMD64 install 32 bit support packages
categories:
 - Linux
date: 2014-05-06 19:14:00 +0100
---

  

aptitude -y install $(aptitude search lib32 | cut -f4 -d " ")  

  

  