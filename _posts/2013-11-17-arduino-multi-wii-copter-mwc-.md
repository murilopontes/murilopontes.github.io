---
layout: post
title: Arduino Multi Wii Copter (MWC)
categories:
 - MPU-6050
date: 2013-11-17 18:58:00 +0000
---

<div dir="ltr" style="text-align: left;" trbidi="on">
O arduino é uma plataforma de hardware aberta.<br/>
<div>
Existem diversas placas com diversos processadores.&nbsp;</div>
<div>
Um das mais baratas é a Arduino Nano V3.0.<br/>
<a name="more"></a></div>
<div>
Um das grandas vantagens do Arduino é uma extensa lista de bibliotecas que permitem criar sistemas inteiros em menos de um 1 dia.</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-IsxFcEuXR9I/UmvhfObhEJI/AAAAAAAAmy4/qpGONd4ceZI/s1600/IMG_20131026_121927.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://1.bp.blogspot.com/-IsxFcEuXR9I/UmvhfObhEJI/AAAAAAAAmy4/qpGONd4ceZI/s400/IMG_20131026_121927.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Arduino Nano V3.0&nbsp;+ GY-521 (MPU-6050)</td></tr>
</tbody></table>
<div>
Um UAV / VANT simples e barato pode ser composto de:<br/>
1) um Arduino Nano V3.0 (MCU de 8 bits) e;<br/>
2) um MPU6050 (IMU 6DOF : giroscópio+acelerômetro).<br/>
<br/>
O projeto Multiwii implementou um controlador de voo para Arduino, é só baixar e extrair na pasta de libraries do Arduino. Depois é só compilar ajustando para usar o Arduino Nano com MPU6050.<br/>
Um vez compilado e gravado, é preciso calibrar o Multwii com o MultiwiiConf conectada porta serial do Arduino.<br/>
[&nbsp;<a href="https://code.google.com/p/multiwii/">https://code.google.com/p/multiwii/</a>&nbsp;] .&nbsp;</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-mfIU_2Jadwg/UmvjGz72jwI/AAAAAAAAmzI/xgerG6WqwBE/s1600/murilo-mwc-2.22.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="226" src="http://2.bp.blogspot.com/-mfIU_2Jadwg/UmvjGz72jwI/AAAAAAAAmzI/xgerG6WqwBE/s400/murilo-mwc-2.22.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ferramenta de calibração e configuração MultiWiiConf</td></tr>
</tbody></table>
<div>
A leitura do MPU-6050 é feita via I2C e repassada para a ferramenta pela porta serial.<br/>
Dá para acompanhar o gráfico do giroscópio x, y, z e do acelerômetro x, y, z.<br/>
Conferir o pitch, roll e muito mais.<br/>
<br/>
O controle do Multiwii é feito usando um receptor RC de pelo menos 4 canais conectado aos pinos de entrada analógica do Arduino. Também é preciso um controle com transmissor de pelo menos 4 canais para enviar os comandos.<br/>
<br/></div>
<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-o0tIa08XG6Q/UmvZ_gG-8MI/AAAAAAAAmx0/ln4lO-lr2YY/s1600/arduino+pinout+(1).png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="282" src="http://1.bp.blogspot.com/-o0tIa08XG6Q/UmvZ_gG-8MI/AAAAAAAAmx0/ln4lO-lr2YY/s1600/arduino+pinout+(1).png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pinout do Arduino Nano V3 <br/>
Atmega 328P<br/>
2k RAM - 1K EEPROM - 32K Flash<br/>
MCU de 8-bits @ 20 MHz<br/>
6 PWMs de HW</td></tr>
</tbody></table>
<br/>
<div class="separator" style="clear: both; text-align: center;">
</div>
<br/>
<div class="separator" style="clear: both; text-align: center;">
</div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-s2Mca1UQwXo/UmwAmFLz73I/AAAAAAAAmzY/6hfbWXZ8YK0/s1600/nano.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="281" src="http://2.bp.blogspot.com/-s2Mca1UQwXo/UmwAmFLz73I/AAAAAAAAmzY/6hfbWXZ8YK0/s640/nano.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pinout do Arduino Nano V3</td></tr>
</tbody></table>
<br/>
<div class="separator" style="clear: both; text-align: center;">
</div>
<br/></div>
</div>