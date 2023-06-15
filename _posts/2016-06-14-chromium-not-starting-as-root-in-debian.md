---
layout: post
title: Chromium not starting as root in Debian
categories:
 - Debian
date: 2016-06-14 14:17:00 +0100
---

Problem:
  

<pre>root@debian:~# chromium
[1:1:0614/091456:FATAL:sandbox_linux.cc(178)] Check failed: sandbox::Credentials::MoveToNewUserNS(). 
#0 0x0000b0587b0d <unknown>
#1 0x0000b05a01c0 <unknown>
#2 0x0000b4c6cf33 <unknown>
#3 0x0000b34d75dc <unknown>
</unknown></unknown></unknown></unknown></pre>

Solution:
  

<pre>root@debian:~# chromium --user-data-dir=/root/chromium --no-sandbox 
</pre>