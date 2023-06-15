---
layout: post
title: Camera serial JPEG  ( TTL / RS232 / RS485 )  widmx / 3Geyes MC-7725 LED infrared
categories:
 - post
date: 2013-12-25 16:53:00 +0000
---

<b style="background-color: white;"><span style="color: red;">Depois de 34 dias de correios...</span></b>  

  

<a name="more"></a>  
  

Câmera para drone e outros sistemas embarcados.  

  

<http://www.aliexpress.com/item/300K-Pixel-Serial-JPEG-Camera-Module-JPEG-Color-Camera-Infrared-RS-232-Serial-Port-Camera-Module/1075779932.html>  

  

P1 = RS232 (vcc, rx, tx, gnd) "beepar" antes de conectar para encontrar o lado do VCC e GND.  

P2 = control infrared LED  

P3 = TTL (vcc, rx, tx, gnd) "beepar" antes de conectar &nbsp;para encontrar o lado do VCC e GND.  

R9,R10 = RS485.  

R11 = no function.  

  

A placa é composto pelo seguintes ICs:  

YS-7725 - custom asic da Widmx, parte da identificação removida com laser.  

  

STC 11L16XE - 8051 core 1280 bytes-RAM 16k-FLASH &nbsp;32k-EEPROM  

<http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC11F-10Fxx.pdf>  

  

MAX202 - bridge TTL - RS232  

<http://www.ti.com/lit/ds/symlink/max202.pdf>  

(usados os pinos 7,8,9,10)  

  

O protocolo é o mesmo da ponte serial JPEG Omnivision OV528.  

<http://www.synes.co.th/nicupload/20120302120132.pdf>  

[http://www.adrirobot.it/datasheet/processori/pdf/OV528\_DS\_1.3%20Camera%20chips.pdf](http://www.adrirobot.it/datasheet/processori/pdf/OV528_DS_1.3%20Camera%20chips.pdf)  

  

  

O link para o software de teste não documentado.  

http://www.widmx.com/OV528.rar  

  

Teste de resolução com serial-ttl configurada para 115200 bps  

160x120 = 2,3 fps  

320x240 = 0,75 fps  

640x320 = 0,474 fps  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-WGfLiNSXbKE/UrsGOISKPvI/AAAAAAAAn3U/4lxwEWLcvEk/s1600/camera-ov528.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="321" src="http://2.bp.blogspot.com/-WGfLiNSXbKE/UrsGOISKPvI/AAAAAAAAn3U/4lxwEWLcvEk/s400/camera-ov528.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Screenshot do software OV528 da Widmx</td></tr>
</tbody></table>

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-u6sw2sVSiN0/UrsCBibGwdI/AAAAAAAAn3I/tXU2UGo7_lM/s1600/IMG_20131225_022600.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-u6sw2sVSiN0/UrsCBibGwdI/AAAAAAAAn3I/tXU2UGo7_lM/s320/IMG_20131225_022600.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate conectado no P2 - serial TTL</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-t195s5gwHUA/UrsCBuudbiI/AAAAAAAAn3I/Lyy-C2VHpo0/s1600/IMG_20131225_022500.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-t195s5gwHUA/UrsCBuudbiI/AAAAAAAAn3I/Lyy-C2VHpo0/s320/IMG_20131225_022500.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate conectado no P2 - serial TTL - assim funciona perfeito.</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-JfpvngdQ88Y/UrsCBjm3KHI/AAAAAAAAn3I/Cf5QrDX0A1w/s1600/IMG_20131224_194604.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-JfpvngdQ88Y/UrsCBjm3KHI/AAAAAAAAn3I/Cf5QrDX0A1w/s320/IMG_20131224_194604.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate conectado no P1 - RS232 não estava funcionando,<br/>
nem iria funcionar, esse é o problema de comprar gadgets documentação fraca e não detalhada.<br/>
Depois de verificar que tinha um MAX202, e "beepar" as trilhas, encontrei o RX / TX - TTL no P2.</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-wCzEFdx38C4/UrsCBv1CxOI/AAAAAAAAn3I/E8mfXvRwsGI/s1600/IMG_20131224_183408.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-wCzEFdx38C4/UrsCBv1CxOI/AAAAAAAAn3I/E8mfXvRwsGI/s320/IMG_20131224_183408.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Parte de traseira</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-hbsGX67qHig/UrsCBvoSPgI/AAAAAAAAn3I/88sq-b3QVMo/s1600/IMG_20131224_183224.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-hbsGX67qHig/UrsCBvoSPgI/AAAAAAAAn3I/88sq-b3QVMo/s320/IMG_20131224_183224.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Parte da frente</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Z75z2RHU7pI/UrsCBv3GilI/AAAAAAAAn3I/hHgqm1EKwe4/s1600/IMG_20131224_194844.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-Z75z2RHU7pI/UrsCBv3GilI/AAAAAAAAn3I/hHgqm1EKwe4/s320/IMG_20131224_194844.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate fazendo as honras para comunicação&nbsp;</td></tr>
</tbody></table>

  

  

  

  