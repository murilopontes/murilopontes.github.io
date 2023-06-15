---
layout: post
title: How to fix - (EE) intel(0)- sna_mode_shutdown_crtc- invalid state found on pipe 0, disabling CRTC-21
categories:
 - bugfix
date: 2016-10-16 15:05:00 +0100
---

Screen sleep resulting in black screen of death (ubuntu 16.04 / intel i7 4790k / ga-z97x-ud3h-bk )  

Possible fixes are:  

1) restart X and loose current session  

2) replace SNA with UXA and be happy foverer (best solution)  

  

How to detect bug:  

cat /var/log/Xorg.0.log | grep sna_mode_shutdown_crtc  

(EE) intel(0): sna_mode_shutdown_crtc: invalid state found on pipe 0, disabling CRTC:21  

  

How to fix:  

<script src="https://gist.github.com/murix/09dde4f50f14670186a42cdeccd580a0.js"></script>

 Copy and save script above, and do:  

sudo sh replace-sna-with-uxa.sh