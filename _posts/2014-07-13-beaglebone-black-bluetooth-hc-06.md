---
layout: post
title: Beaglebone Black Bluetooth HC-06
categories:
 - Bluetooth
date: 2014-07-13 18:32:00 +0100
---

<span style="background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px; text-align: justify;">Módulo Bluetooth HC-06 para debug da Beaglebone Black (BBB)&nbsp;</span>  

<div style="orphans: auto; text-align: start; text-indent: 0px; widows: auto;">
<div class="separator" style="-webkit-text-stroke-width: 0px; clear: both; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; text-align: center; text-transform: none; white-space: normal; word-spacing: 0px;">
</div>
<a name="more"></a><br/><br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; margin-left: auto; margin-right: auto; text-align: center; text-transform: none; white-space: normal; word-spacing: 0px;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-E5x6nh5ZrXk/U8K-OI8ufnI/AAAAAAAAsXM/x-bh7sfHdG4/s1600/IMG_20140713_141136.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-E5x6nh5ZrXk/U8K-OI8ufnI/AAAAAAAAsXM/x-bh7sfHdG4/s1600/IMG_20140713_141136.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Conexão do HC-06 no conector J1 da BBB,<br/>
também usando o VCC do P9.</td></tr>
</tbody></table>
<div style="-webkit-text-stroke-width: 0px; background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 18.479999542236328px; text-align: justify; text-transform: none; white-space: normal; word-spacing: 0px;">
No PC é usado o blueman-applet para conectar no HC-06. Na versão 1.23 é possível ver a potência de TX do PC e do HC-06, e a qualidade do link entre eles. O controle de energia otimizado utiliza a menor potência de TX que maximizar a qualidade do link.&nbsp;</div>
<div align="center" style="-webkit-text-stroke-width: 0px; background-color: white; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 18.479999542236328px; text-transform: none; white-space: normal; word-spacing: 0px;">
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; margin-left: auto; margin-right: auto; text-align: center; text-transform: none; white-space: normal; word-spacing: 0px;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-1QR03A5wIqs/U8K-s4tXrBI/AAAAAAAAsXU/GYnVThQz8w0/s1600/beaglebone-bluetooth.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="237" src="http://2.bp.blogspot.com/-1QR03A5wIqs/U8K-s4tXrBI/AAAAAAAAsXU/GYnVThQz8w0/s1600/beaglebone-bluetooth.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Blueman-applet conectado ao HC-06</td></tr>
</tbody></table>
<div align="center" style="background-color: white;">
<div style="text-align: justify;">
<span style="color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: x-small;"><span style="line-height: 18.479999542236328px;">O led do HC-06 pisca até que o link seja estabelecido. Após estabelecido o link o led ficará acesso.</span></span></div>
<div style="text-align: justify;">
<span style="color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: x-small;"><span style="line-height: 18.479999542236328px;"><br/></span></span></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-5ozOnksR7xw/U8LBUEvmJYI/AAAAAAAAsXk/KCacDusq2eM/s1600/beaglebone-bluetooth-minicom.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="231" src="http://1.bp.blogspot.com/-5ozOnksR7xw/U8LBUEvmJYI/AAAAAAAAsXk/KCacDusq2eM/s1600/beaglebone-bluetooth-minicom.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">minicom -c on -o -D /dev/rfcomm0<br/>
Console da Beaglebone Black acessado por Bluetooth</td></tr>
</tbody></table>
<div style="text-align: justify;">
<span style="color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; line-height: 18.479999542236328px;">Tabela de comandos do HC-06 para configuração.</span></div>
<div style="text-align: justify;">
<span style="color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: x-small;"><span style="line-height: 18.479999542236328px;">O HC-06 permanece em modo de configuração enquanto o link não é estabelecido.</span></span></div>
<br/>
<table border="1" style="-webkit-text-stroke-width: 0px; color: #222222; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 18.479999542236328px; text-transform: none; white-space: normal; word-spacing: 0px;"><tbody>
<tr><th><div style="margin: 0px;">
Command</div>
</th><th><div style="margin: 0px;">
Response</div>
</th><th><div style="margin: 0px;">
Comment</div>
</th></tr>
<tr><td><div style="margin: 0px;">
AT</div>
</td><td><div style="margin: 0px;">
OK</div>
</td><td><div style="margin: 0px;">
Serial test</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+VERSION</div>
</td><td><div style="margin: 0px;">
OKlinvor1.8</div>
</td><td><div style="margin: 0px;">
The firmware version</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+NAMExyz</div>
</td><td><div style="margin: 0px;">
OKsetname</div>
</td><td><div style="margin: 0px;">
Sets the module name to "xyz"</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+PIN1234</div>
</td><td><div style="margin: 0px;">
OKsetPIN</div>
</td><td><div style="margin: 0px;">
Sets the module PIN to 1234</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD1</div>
</td><td><div style="margin: 0px;">
OK1200</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 1200</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD2</div>
</td><td><div style="margin: 0px;">
OK2400</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 2400</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD3</div>
</td><td><div style="margin: 0px;">
OK4800</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 4800</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD4</div>
</td><td><div style="margin: 0px;">
OK9600</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 9600</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD5</div>
</td><td><div style="margin: 0px;">
OK19200</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 19200</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD6</div>
</td><td><div style="margin: 0px;">
OK38400</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 38400</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD7</div>
</td><td><div style="margin: 0px;">
OK57600</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 57600</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD8</div>
</td><td><div style="margin: 0px;">
OK115200</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 115200</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUD9</div>
</td><td><div style="margin: 0px;">
OK230400</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 230400</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUDA</div>
</td><td><div style="margin: 0px;">
OK460800</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 460800</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUDB</div>
</td><td><div style="margin: 0px;">
OK921600</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 921600</div>
</td></tr>
<tr><td><div style="margin: 0px;">
AT+BAUDC</div>
</td><td><div style="margin: 0px;">
OK1382400</div>
</td><td><div style="margin: 0px;">
Sets the baud rate to 1382400</div>
</td></tr>
</tbody></table>
</div>
</div>