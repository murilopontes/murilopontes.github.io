---
layout: post
title: Controle de xbox no Ubuntu
categories:
 - post
date: 2014-10-18 22:13:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
# não permitir que o joystick funcione como mouse<br/>
sudo aptitude remove xserver-xorg-input-joystick<br/>
<br/>
# não carregar driver xpad para o controle do xbox360<br/>
echo "blacklist xpad" &gt; &nbsp;/etc/modprobe.d/black-xpad.conf<br/>
<br/>
# instalar o driver em userspace para o controle do xbox360<br/>
sudo aptitude install xboxdrv<br/>
<br/>
<br/></div>