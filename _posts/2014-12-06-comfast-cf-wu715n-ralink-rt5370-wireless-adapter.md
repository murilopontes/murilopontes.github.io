---
layout: post
title: Comfast CF-WU715N  - Ralink RT5370 Wireless Adapter
categories:
 - post
date: 2014-12-06 23:59:00 +0000
---

<div>
Estava procurando um adaptador WiFi USB barato para notebook e embarcados, e encontrei o CF-WU715N, custa cerca de $3.<br/>
<br/>
<a name="more"></a><br/>
Que logo ao espetar na USB mostra que na verdade é um Ralink RT5370.</div>

<div>
No Debian testing do notebook e da beaglebone black funcionou "out-of-the-box"</div>

<div>
<br/></div>

<div>
root@beaglebone:~# lsusb&nbsp;</div>

<div>
Bus 001 Device 002: ID 148f:5370 Ralink Technology, Corp. RT5370 Wireless Adapter</div>

<div>
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub</div>

<div>
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub</div>

<div>
root@beaglebone:~#&nbsp;</div>

<div>
<br/></div>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-LGKlhtJZHi8/VIOVVQCh7ZI/AAAAAAAAt3M/vXMYtDfUpG0/s1600/IMG_20141206_193616.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-LGKlhtJZHi8/VIOVVQCh7ZI/AAAAAAAAt3M/vXMYtDfUpG0/s1600/IMG_20141206_193616.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Meus 3 adaptadores CF-WU715N</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-79Z-hLgcBmo/VIOVVbSTeaI/AAAAAAAAt3M/RQF2egZUO9Q/s1600/IMG_20141206_193516.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://4.bp.blogspot.com/-79Z-hLgcBmo/VIOVVbSTeaI/AAAAAAAAt3M/RQF2egZUO9Q/s1600/IMG_20141206_193516.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">3 adaptadores CF-WU715N funcionando no notebook</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-iKSW4n8EuOU/VIOVoFaS0FI/AAAAAAAAt3o/teltnv05Zb8/s1600/IMG_20141206_204706.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://4.bp.blogspot.com/-iKSW4n8EuOU/VIOVoFaS0FI/AAAAAAAAt3o/teltnv05Zb8/s1600/IMG_20141206_204706.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CF-WU715N funcionando na Beaglebone Black<br/>
Dependendo do kernel da beaglebone é preciso que o adaptador esteja conectado antes de ligar a energia,<br/>
o USB Hot-plug da BBBé desabilitado por padrão.&nbsp;</td></tr>
</tbody></table>

  