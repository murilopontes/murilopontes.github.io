---
layout: post
title: Bluetooth / Serial / USART / HC-06 AT Commands cheat sheet
categories:
 - Bluetooth
date: 2014-04-24 20:23:00 +0100
---

O HC-06 é um módulo Bluetooth com porta serial / usart TTL.  

<a name="more"></a>  

É muito útil para depuração e/ou interligação com um sistema microcontrolado e/ou embarcado.  

Enquanto o computador ou Android não estiver conectado ao módulo o led piscará e poderão ser enviados comandos de configuração para ajuste do nome, PIN e baudrate.  

Quando o computador ou Android conecta ao módulo, o led ficará acesso sem piscar, passará a funcionar como um portal serial transparente entre o sistema embarcado e o computador/Android.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-PXI5q7ycvBw/U1rNgQZRJ0I/AAAAAAAAqNQ/DMv-C0duW-k/s1600/IMG_20140425_175220.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-PXI5q7ycvBw/U1rNgQZRJ0I/AAAAAAAAqNQ/DMv-C0duW-k/s1600/IMG_20140425_175220.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Módulo HC-06 soldado numa placa de suporte.</td></tr>
</tbody></table>

Quer comprar um igual a este veja o link:  

<a href="http://www.aliexpress.com/item/HC-06-Bluetooth-serial-pass-through-module-wireless-serial-communication-from-machine-Wireless-HC06-for-arduino/802475117.html" target="_blank">http://www.aliexpress.com/item/HC-06-Bluetooth-serial-pass-through-module-wireless-serial-communication-from-machine-Wireless-HC06-for-arduino/802475117.html</a>  

  

Lista de comandos do módulo Bluetooth Serial.  

  

<div>
<div align="center" style="background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px;">
<table border="1"><tbody>
<tr><th>Command</th><th>Response</th><th>Comment</th></tr>
<tr><td>AT</td><td>OK</td><td>Serial test</td></tr>
<tr><td>AT+VERSION</td><td>OKlinvor1.8</td><td>The firmware version</td></tr>
<tr><td>AT+NAMExyz</td><td>OKsetname</td><td>Sets the module name to "xyz"</td></tr>
<tr><td>AT+PIN1234</td><td>OKsetPIN</td><td>Sets the module PIN to 1234</td></tr>
<tr><td>AT+BAUD1</td><td>OK1200</td><td>Sets the baud rate to 1200</td></tr>
<tr><td>AT+BAUD2</td><td>OK2400</td><td>Sets the baud rate to 2400</td></tr>
<tr><td>AT+BAUD3</td><td>OK4800</td><td>Sets the baud rate to 4800</td></tr>
<tr><td>AT+BAUD4</td><td>OK9600</td><td>Sets the baud rate to 9600</td></tr>
<tr><td>AT+BAUD5</td><td>OK19200</td><td>Sets the baud rate to 19200</td></tr>
<tr><td>AT+BAUD6</td><td>OK38400</td><td>Sets the baud rate to 38400</td></tr>
<tr><td>AT+BAUD7</td><td>OK57600</td><td>Sets the baud rate to 57600</td></tr>
<tr><td>AT+BAUD8</td><td>OK115200</td><td>Sets the baud rate to 115200</td></tr>
<tr><td>AT+BAUD9</td><td>OK230400</td><td>Sets the baud rate to 230400</td></tr>
<tr><td>AT+BAUDA</td><td>OK460800</td><td>Sets the baud rate to 460800</td></tr>
<tr><td>AT+BAUDB</td><td>OK921600</td><td>Sets the baud rate to 921600</td></tr>
<tr><td>AT+BAUDC</td><td>OK1382400</td><td>Sets the baud rate to 1382400</td></tr>
</tbody></table>
</div>
</div>

<div style="background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px; text-align: justify;">
<br/>
Funciona tranquilamente até 10 metros, depois disso fica falhando um pouco até perder o sinal completamente.</div>

<div style="background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px; text-align: justify;">
<br/></div>

<div style="background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px; text-align: justify;">
<br/></div>