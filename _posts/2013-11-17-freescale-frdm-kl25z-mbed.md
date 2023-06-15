---
layout: post
title: Freescale FRDM-KL25Z + MBED
categories:
 - post
date: 2013-11-17 15:28:00 +0000
---

<div>
<span style="color: #222222; font-family: Helvetica Neue, Helvetica, Helvetica, Arial, sans-serif;"><span style="font-size: 14px; line-height: 22.3999996185303px;">MBED KL25Z<a name="more"></a></span></span></div>

<div>
<span style="color: #222222; font-family: Helvetica Neue, Helvetica, Helvetica, Arial, sans-serif;"><span style="font-size: 14px; line-height: 22.3999996185303px;"><br/></span></span></div>

<ul style="background-color: #fdfdfd; box-sizing: border-box; color: #222222; direction: ltr; font-family: 'Helvetica Neue', Helvetica, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6; list-style-position: outside; margin: 0px 0px 17px 2em; padding: 0px;">
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">Freescale KL25Z Kinetis KL2 MCU (MKL25Z128VLK4)<ul style="box-sizing: border-box; direction: ltr; line-height: 1.6; list-style-position: outside; margin: 0px 0px 0px 2em; padding: 0px;">
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">High performance ARM® Cortex™-M0+ Core</li>
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">48MHz, 16KB RAM, 128KB FLASH</li>
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">2xSPI, 2xI2C, 3xUART, 6xPWM, 6xADC, Touch Sensor, GPIO</li>
</ul>
</li>
</ul>

<ul style="background-color: #fdfdfd; box-sizing: border-box; color: #222222; direction: ltr; font-family: 'Helvetica Neue', Helvetica, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6; list-style-position: outside; margin: 0px 0px 17px 2em; padding: 0px;">
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">FRDM-KL25Z Onboard peripherals<ul style="box-sizing: border-box; direction: ltr; line-height: 1.6; list-style-position: outside; margin: 0px 0px 0px 2em; padding: 0px;">
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">MMA8451Q - 3-axis accelerometer (dá para estabilizar um drone)</li>
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">PWM Controlled RGB LED (até um hex-copter pode ser)</li>
<li style="box-sizing: border-box; direction: ltr; margin: 0px; padding: 0px;">Capacitive touch sensor</li>
</ul>
</li>
</ul>

  

[&nbsp;<http://mbed.org/handbook/mbed-FRDM-KL25Z>&nbsp;]  

  

[&nbsp;<http://mbed.org/handbook/mbed-FRDM-KL25Z-Getting-Started>&nbsp;]  

  

Firmware MBED no formato do OpenSDA.  

Basta resetar a placa com o SW1 precisado, quando aparecer o driver "BOOTLOADER", é só copiar o  

mbed_if_v2.0_frdm_kl25z.s19 para dentro e esperar o led D4 parar de piscar (gravar o FW)  

  

[&nbsp;http://mbed.org/media/uploads/samux/mbed_if_v2.0_frdm_kl25z.s19 ]  

  

Notas importantes:  

No linux o BOOTLOADER não tem partição, tem de montar direto device tipo:  

mount /dev/sdc /mbed  

  

No Windows 8.1 o OpenSDA ainda não funciona, o placa fica resetando em loop infinito.  

No Windows 8 também é fica bugado.  

No Windows 7 funciona tudo OK.  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-33xllmmm3zY/UnBijR1vCSI/AAAAAAAAm3o/bKlQqlqT7DU/s1600/IMG_20131029_222358.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-33xllmmm3zY/UnBijR1vCSI/AAAAAAAAm3o/bKlQqlqT7DU/s400/IMG_20131029_222358.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Avaliando Freescale FRDM-KL25Z + MBED no Linux com compilador WEB.<br/>
É tão fácil quanto Arduino.<br/>
O problema que encontrei é que até agora não encontrei o depurador.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-7zqiWO0_JYA/UnBnIu3jJhI/AAAAAAAAm4A/l0tVwKKYuW0/s1600/kl25z-pinout-revised.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="268" src="http://2.bp.blogspot.com/-7zqiWO0_JYA/UnBnIu3jJhI/AAAAAAAAm4A/l0tVwKKYuW0/s320/kl25z-pinout-revised.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">&nbsp;FRDM-KL25Z&nbsp;Pinout&nbsp;</td></tr>
</tbody></table>

  

  

  