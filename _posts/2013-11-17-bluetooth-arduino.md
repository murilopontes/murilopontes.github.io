---
layout: post
title: Bluetooth arduino
categories:
 - Bluetooth
date: 2013-11-17 18:20:00 +0000
---

<div class="separator" style="clear: both; text-align: justify;">
A forma mais prática de depurar um sistema é usando o tradicional printf do C/C++.</div>

<a name="more"></a>  

<div class="separator" style="clear: both; text-align: justify;">
No cenário depuração de um drone em vôo a solução é usar uma serial bluetooth para receber as mensagens de depuração, do sistema e tudo mais, além de ser possível enviar comandos para o Drone.</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-k4FukYqHkd8/UmxcCOXi-VI/AAAAAAAAm0U/TT6UbohrV_U/s1600/IMG_20131026_185054.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-k4FukYqHkd8/UmxcCOXi-VI/AAAAAAAAm0U/TT6UbohrV_U/s320/IMG_20131026_185054.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Meu módulo bluetooth serial &nbsp;EGBT-046S (HC-06) ligado no Bus Pirate.<br/>
Vale lembrar que o RX não é tolerante a 5V, para ligar no arduino precisa fazer um divisor de tensão.<br/>
[&nbsp;<a href="http://www.e-gizmo.com/KIT/egbt-04.htm">http://www.e-gizmo.com/KIT/egbt-04.htm</a>&nbsp;]</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-REpobMYku_o/UmxcttlcuPI/AAAAAAAAm0k/3aaxb4NVgus/s1600/FFM2LM8HHS9W6IV.LARGE.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="265" src="http://2.bp.blogspot.com/-REpobMYku_o/UmxcttlcuPI/AAAAAAAAm0k/3aaxb4NVgus/s320/FFM2LM8HHS9W6IV.LARGE.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema para ligar&nbsp;EGBT-046S (HC-06)&nbsp;no I/O de Arduino</td></tr>
</tbody></table>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-nK9VDuqZheI/Umxb5sUOYGI/AAAAAAAAm0M/_5n8phHXLCE/s1600/bluetooth.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="640" src="http://2.bp.blogspot.com/-nK9VDuqZheI/Umxb5sUOYGI/AAAAAAAAm0M/_5n8phHXLCE/s640/bluetooth.PNG" width="340"/></a></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-UpfQod7gx-Q/UmvaSe6-cmI/AAAAAAAAmyM/Q-raR9d-Z3c/s1600/bc417-pinout.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="250" src="http://4.bp.blogspot.com/-UpfQod7gx-Q/UmvaSe6-cmI/AAAAAAAAmyM/Q-raR9d-Z3c/s400/bc417-pinout.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pinout EGBT-046S (HC-06)<br/>
<br/></td></tr>
</tbody></table>

  

  