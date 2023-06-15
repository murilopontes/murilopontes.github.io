---
layout: post
title: Quadcopter - nova revisão da placa de controle de voo com Stellaris/Tiva
categories:
 - Tiva C
date: 2014-03-26 19:20:00 +0000
---

Esquemático da Tiva C Series para controlar drone.  

<a name="more"></a>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-Pr3yAUQShYk/UzMj__dy6JI/AAAAAAAApnA/0oa_yrLycgc/s1600/bootspack-tiva-murix-quad-pack.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="253" src="http://1.bp.blogspot.com/-Pr3yAUQShYk/UzMj__dy6JI/AAAAAAAApnA/0oa_yrLycgc/s1600/bootspack-tiva-murix-quad-pack.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Distribuição dos pinos na placa de controle de voo</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-WKEwJmLYSec/UzMkaC_BjTI/AAAAAAAApnI/UumeeR8OTkU/s1600/IMG_20140326_154827.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-WKEwJmLYSec/UzMkaC_BjTI/AAAAAAAApnI/UumeeR8OTkU/s1600/IMG_20140326_154827.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Placa de controle de voo: vista superior, ainda falta soldar bluetooth e voltmeter-adc,<br/>
talvez fique sem eles.</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-xYz_81Yc0hQ/UzMkxOmnnaI/AAAAAAAApnU/F6oswiEWJkU/s1600/IMG_20140326_154849.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://3.bp.blogspot.com/-xYz_81Yc0hQ/UzMkxOmnnaI/AAAAAAAApnU/F6oswiEWJkU/s1600/IMG_20140326_154849.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Placa de controle de voo: vista inferior.</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-SY5bOm58QjA/UzMk75L722I/AAAAAAAApnc/WPrRAXFp_VQ/s1600/IMG_20140326_155053.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://4.bp.blogspot.com/-SY5bOm58QjA/UzMk75L722I/AAAAAAAApnc/WPrRAXFp_VQ/s1600/IMG_20140326_155053.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Placa de controle de voo - vista superior equipada com<br/>
Stellaris LM4F120XL removidos R9,R10,U4<br/>
Anaren Air Boost &nbsp;Pack 915 MHz<br/>
GY-65 / Bosh BMP085 (Barômetro/Altímetro)<br/>
GY-273 / Honeywell HMC5883L (Magnetômetro/Bússola)<br/>
GY-521 / Invisense MPU6050 (Giroscópio e acelerômetro / IMU)<br/>
GY-GPS-6M-V1 / Ublox Neo 6M (GPS)</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-LzYeVVf7X9M/UzMmXfwMQII/AAAAAAAApno/bPJW26mV8wA/s1600/IMG_20140326_155137.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-LzYeVVf7X9M/UzMmXfwMQII/AAAAAAAApno/bPJW26mV8wA/s1600/IMG_20140326_155137.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Placa de controle de voo - vista inferior equipada com:<br/>
HC-SR04 (Sonar/Altímetro)</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-R35FGN6MLlc/UzMms_RHaPI/AAAAAAAApnw/Lts9dyzIQY4/s1600/IMG_20140326_155759.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://4.bp.blogspot.com/-R35FGN6MLlc/UzMms_RHaPI/AAAAAAAApnw/Lts9dyzIQY4/s1600/IMG_20140326_155759.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Drone / Vant equipado com:<br/>
Placa de controle de voo,<br/>
Frame Talon v1 (fibra de carbono),<br/>
ESCs Hobbywing Flyfun 30A,<br/>
Motores A2212/13T 1000KV,<br/>
Hélices 10x6 (ABS),<br/>
Bateria LIPO 3S1P 2200mah 30C.</td></tr>
</tbody></table>
<br/></div>