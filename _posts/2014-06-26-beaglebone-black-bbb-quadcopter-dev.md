---
layout: post
title: BeagleBone Black (BBB) - Quadcopter Dev
categories:
 - gps
date: 2014-06-26 06:27:00 +0100
---

BeagleBone Black é uma plataforma de desenvolvimento de baixo custo (entenda-se cerca R$330).  

Capaz de dar boot em 10 segundos e pronta para desenvolver em 5 minutos através de conexão USB e API semelhamente ao Arduino.  

O processador é um ARM Cortex-A8 de 1GHz com 512MB de DDR3 e 2GB de flash.  

  

<a name="more"></a>  
  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-l6Y2uNQvA8o/U6twcG-r4AI/AAAAAAAAr4w/_8vUSi0MJg8/s1600/IMG_20140625_214405.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="150" src="http://1.bp.blogspot.com/-l6Y2uNQvA8o/U6twcG-r4AI/AAAAAAAAr4w/_8vUSi0MJg8/s1600/IMG_20140625_214405.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Caixa da Beaglebone Black</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-KCmbmT8XB4M/U6twfKtZIjI/AAAAAAAAr44/mWik38Am4iI/s1600/IMG_20140625_214529.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="150" src="http://4.bp.blogspot.com/-KCmbmT8XB4M/U6twfKtZIjI/AAAAAAAAr44/mWik38Am4iI/s1600/IMG_20140625_214529.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tudo que vem na caixa: encarte, a placa e o cabo USB.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-gMifQA4XSpE/U6twiEQZMiI/AAAAAAAAr5A/0bayAheJ8rk/s1600/IMG_20140625_214751.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="150" src="http://4.bp.blogspot.com/-gMifQA4XSpE/U6twiEQZMiI/AAAAAAAAr5A/0bayAheJ8rk/s1600/IMG_20140625_214751.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Face inferior</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-xvN_5taPbvE/U6twlYzYewI/AAAAAAAAr5I/5cXLxosNn7Q/s1600/IMG_20140625_214808.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="150" src="http://4.bp.blogspot.com/-xvN_5taPbvE/U6twlYzYewI/AAAAAAAAr5I/5cXLxosNn7Q/s1600/IMG_20140625_214808.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Face superior<br/>
2 conectores fêmeas de 46 pinos cada.<br/>
1 conector macho de 6 pinos (UART para debug)<br/>
4 Leds</td></tr>
</tbody></table>

  

A instalação é fácil.  

Plugue o cabo USB e instale os drivers (somente para Windows, no Linux é automático):  

  

Windows 7/8/8.1 32 bits  

[http://beagleboard.org/static/Drivers/Windows/BONE\_DRV.exe](http://beagleboard.org/static/Drivers/Windows/BONE_DRV.exe)  

Windows 7/8/8.1 64 bits  

[http://beagleboard.org/static/Drivers/Windows/BONE\_D64.exe](http://beagleboard.org/static/Drivers/Windows/BONE_D64.exe)  

  

Para entrada no ambiente de desenvolvimento estilo Arduino, basta acessar a placa pela rede USB em:  

<http://192.168.7.2:3000/>  

  

<div class="separator" style="clear: both; text-align: center;">
</div>

O processador possui 8 saídas PWM, 6 delas podem ser multiplexadas para sair em pinos diferentes do padrão. Usando a tabela fica mais fácil de escolher os pinos, pois além da multiplexação existem conflitos em potencial, ou seja, somente 6 pinos estão completamente livres para fazer PWM, se não for a UART2, caso contrário só restam 4 pinos de PWM livres.  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="100"/><col width="195"/><col width="206"/></colgroup><tbody>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Sa\u00edda PWM"]' style="background-color: black; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">Saída PWM</td><td data-sheets-value='[null,2,"pino padr\u00e3o"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">pino padrão</td><td data-sheets-value='[null,2,"pino alternativo"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">pino alternativo</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"ECAPPWM0"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">ECAPPWM0</td><td data-sheets-value='[null,2,"P9_42"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_42 (provável conflito)</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"ECAPPWM2"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">ECAPPWM2</td><td data-sheets-value='[null,2,"P9_28"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_28 (LCD)</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM0A"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM0A</td><td data-sheets-value='[null,2,"P9_31"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_31 (LCD)</td><td data-sheets-value='[null,2,"P9_22"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_22 / USART2_RXD</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM0B"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM0B</td><td data-sheets-value='[null,2,"P9_21"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_21 / USART2_TXD</td><td data-sheets-value='[null,2,"P9_29"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_29 (LCD)</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM1A"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM1A</td><td data-sheets-value='[null,2,"P9_14"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_14</td><td data-sheets-value='[null,2,"P8_36 (sys_boot / LCD)"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_36 (sys_boot / LCD)</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM1B"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM1B</td><td data-sheets-value='[null,2,"P9_16"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P9_16</td><td data-sheets-value='[null,2,"P8_34 (sys_boot / LCD)"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_34 (sys_boot / LCD)</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM2A"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM2A</td><td data-sheets-value='[null,2,"P8_19"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_19</td><td data-sheets-value='[null,2,"P8_45 (sys_boot / LCD)"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_45 (sys_boot / LCD)</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"EHRPWM2B"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">EHRPWM2B</td><td data-sheets-value='[null,2,"P8_13"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_13</td><td data-sheets-value='[null,2,"P8_46 (sys_boot / LCD)"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 100%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom;">P8_46 (sys_boot / LCD)</td></tr>
</tbody></table>

  

Também é importante olhar o esquemático elétrico da placa, pois alguns pinos compartilhados podem causar problemas no futuro.  

[https://github.com/CircuitCo/BeagleBone-Black/blob/master/BBB\_SCH.pdf?raw=true](https://github.com/CircuitCo/BeagleBone-Black/blob/master/BBB_SCH.pdf?raw=true)  

Os pinos 31 a 46 do P8 configuração o processador na hora do boot.  

Portanto para evitar problemas não conecte pull-up/down e nem tente usar como entrada, o jeito mais seguro é usar esses 16 pinos como saídas e se possível adiciona proteção contra entrada (por exemplo usando diodos de sinal 1n4148).  

Os pinos 27,28,29,30 do P8 também estão em uso pelo LCD / HDMI.  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-fyZ4SE1Wwvk/U6utarw0D8I/AAAAAAAAr5s/7nASZDoS9P8/s1600/beagleboneblack-murix.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="175" src="http://3.bp.blogspot.com/-fyZ4SE1Wwvk/U6utarw0D8I/AAAAAAAAr5s/7nASZDoS9P8/s1600/beagleboneblack-murix.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pinout da beaglebone black com todos conflitos comentados</td></tr>
</tbody></table>

  

A situação do P8 é bem confortável após remover os conflitos.  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="40"/><col width="67"/><col width="104"/><col width="59"/><col width="89"/></colgroup><tbody>
<tr style="height: 21px;"><td style="background-color: black; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"HEADER"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">HEADER</td><td data-sheets-value='[null,2,"GPIO (3.3V)"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO (3.3V)</td><td data-sheets-value='[null,2,"TIMER"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER</td><td data-sheets-value='[null,2,"PWM"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">PWM</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,1]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">1</td><td data-sheets-value='[null,2,"P8_7"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_7</td><td data-sheets-value='[null,2,"GPIO2_2"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO2_2</td><td data-sheets-value='[null,2,"TIMER4"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER4</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,2]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">2</td><td data-sheets-value='[null,2,"P8_8"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_8</td><td data-sheets-value='[null,2,"GPIO2_3"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO2_3</td><td data-sheets-value='[null,2,"TIMER7"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER7</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,3]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">3</td><td data-sheets-value='[null,2,"P8_9"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_9</td><td data-sheets-value='[null,2,"GPIO2_5"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO2_5</td><td data-sheets-value='[null,2,"TIMER5"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER5</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,4]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">4</td><td data-sheets-value='[null,2,"P8_10"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_10</td><td data-sheets-value='[null,2,"GPIO2_4"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO2_4</td><td data-sheets-value='[null,2,"TIMER6"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER6</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,5]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">5</td><td data-sheets-value='[null,2,"P8_11"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_11</td><td data-sheets-value='[null,2,"GPIO1_13"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_13</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,6]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">6</td><td data-sheets-value='[null,2,"P8_12"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_12</td><td data-sheets-value='[null,2,"GPIO1_12"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_12</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,7]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">7</td><td data-sheets-value='[null,2,"P8_13"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_13</td><td data-sheets-value='[null,2,"GPIO0_23"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_23</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM2B"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM2B</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,8]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">8</td><td data-sheets-value='[null,2,"P8_14"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_14</td><td data-sheets-value='[null,2,"GPIO0_26"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_26</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,9]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">9</td><td data-sheets-value='[null,2,"P8_15"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_15</td><td data-sheets-value='[null,2,"GPIO1_15"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_15</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,10]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">10</td><td data-sheets-value='[null,2,"P8_16"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_16</td><td data-sheets-value='[null,2,"GPIO1_14"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_14</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,11]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">11</td><td data-sheets-value='[null,2,"P8_17"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_17</td><td data-sheets-value='[null,2,"GPIO0_27"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_27</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,12]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">12</td><td data-sheets-value='[null,2,"P8_18"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_18</td><td data-sheets-value='[null,2,"GPIO2_1"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO2_1</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,13]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">13</td><td data-sheets-value='[null,2,"P8_19"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_19</td><td data-sheets-value='[null,2,"GPIO0_22"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_22</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM2A"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM2A</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,14]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">14</td><td data-sheets-value='[null,2,"P8_26"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P8_26</td><td data-sheets-value='[null,2,"GPIO1_29"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_29</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
</tbody></table>

  

A situação do P9 é mais complicada, após remover os conflitos a multiplexação de funcionalidades nos pinos não permite usar todas as funcionalidades ao mesmo tempo.  

Ativar a interface SPI0 implica em perder a UART2 e 2 PWMs e remanejar o I2C1 e I2C2.  

Ativar a interface DCAN1 implica em perder a UART1.  

Ativar a interface DCAN0 implica em remanejar o I2C2.  

Ativar a interface UART1 implica em perder o DCAN1 e remanejar o I2C1.  

Ativar a interface UART2 implica em perder o SPI0 e 2 PWMs e remanejar o I2C2.  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="40"/><col width="67"/><col width="104"/><col width="59"/><col width="89"/><col width="100"/><col width="100"/><col width="100"/><col width="100"/></colgroup><tbody>
<tr style="height: 21px;"><td style="background-color: black; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"HEADER"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">HEADER</td><td data-sheets-value='[null,2,"GPIO (3.3V)"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO (3.3V)</td><td data-sheets-value='[null,2,"TIMER"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER</td><td data-sheets-value='[null,2,"PWM"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">PWM</td><td data-sheets-value='[null,2,"I2C"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C</td><td data-sheets-value='[null,2,"UART"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART</td><td data-sheets-value='[null,2,"SPI"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI</td><td data-sheets-value='[null,2,"CAN"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">CAN</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,1]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">1</td><td data-sheets-value='[null,2,"P9_11"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_11</td><td data-sheets-value='[null,2,"GPIO0_30"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_30</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"UART4_RXD"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART4_RXD</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,2]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">2</td><td data-sheets-value='[null,2,"P9_12"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_12</td><td data-sheets-value='[null,2,"GPIO1_28"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_28</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,3]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">3</td><td data-sheets-value='[null,2,"P9_13"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_13</td><td data-sheets-value='[null,2,"GPIO0_31"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_31</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"UART4_TXD"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART4_TXD</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,4]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">4</td><td data-sheets-value='[null,2,"P9_14"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_14</td><td data-sheets-value='[null,2,"GPIO1_18"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_18</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM1A"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM1A</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,5]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">5</td><td data-sheets-value='[null,2,"P9_16"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_16</td><td data-sheets-value='[null,2,"GPIO1_19"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_19</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM1B"]' style="background-color: #6aa84f; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM1B</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,6]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">6</td><td data-sheets-value='[null,2,"P9_17"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_17</td><td data-sheets-value='[null,2,"GPIO0_5"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_5</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C1_SCL"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C1_SCL</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"SPI0_CS0"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI0_CS0</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,7]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">7</td><td data-sheets-value='[null,2,"P9_18"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_18</td><td data-sheets-value='[null,2,"GPIO0_4"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_4</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C1_SDA"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C1_SDA</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"SPI0_D1"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI0_D1</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,8]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">8</td><td data-sheets-value='[null,2,"P9_19"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_19</td><td data-sheets-value='[null,2,"GPIO0_13"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_13</td><td data-sheets-value='[null,2,"TIMER5"]' style="background-color: #f4cccc; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER5</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C2_SCL"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C2_SCL</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"SPI1_CS1"]' style="background-color: #f4cccc; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI1_CS1</td><td data-sheets-value='[null,2,"DCAN0_RX"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">DCAN0_RX</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,9]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">9</td><td data-sheets-value='[null,2,"P9_20"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_20</td><td data-sheets-value='[null,2,"GPIO0_12"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_12</td><td data-sheets-value='[null,2,"TIMER6"]' style="background-color: #f4cccc; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">TIMER6</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C2_SDA"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C2_SDA</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"SPI1_CS0"]' style="background-color: #f4cccc; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI1_CS0</td><td data-sheets-value='[null,2,"DCAN0_TX"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">DCAN0_TX</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,10]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">10</td><td data-sheets-value='[null,2,"P9_21"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_21</td><td data-sheets-value='[null,2,"GPIO0_3"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_3</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM0B"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM0B</td><td data-sheets-value='[null,2,"I2C2_SCL"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C2_SCL</td><td data-sheets-value='[null,2,"UART2_TXD"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART2_TXD</td><td data-sheets-value='[null,2,"SPI0_D0"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI0_D0</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,11]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">11</td><td data-sheets-value='[null,2,"P9_22"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_22</td><td data-sheets-value='[null,2,"GPIO0_2"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_2</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"EHRPWM0A"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">EHRPWM0A</td><td data-sheets-value='[null,2,"I2C2_SDA"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C2_SDA</td><td data-sheets-value='[null,2,"UART2_RXD"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART2_RXD</td><td data-sheets-value='[null,2,"SPI0_SCLK"]' style="background-color: #d9ead3; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">SPI0_SCLK</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,12]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">12</td><td data-sheets-value='[null,2,"P9_23"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_23</td><td data-sheets-value='[null,2,"GPIO1_17"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO1_17</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,13]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">13</td><td data-sheets-value='[null,2,"P9_24"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_24</td><td data-sheets-value='[null,2,"GPIO0_15"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_15</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C1_SCL"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C1_SCL</td><td data-sheets-value='[null,2,"UART1_TXD"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART1_TXD</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"DCAN1_RX"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">DCAN1_RX</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,14]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">14</td><td data-sheets-value='[null,2,"P9_26"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_26</td><td data-sheets-value='[null,2,"GPIO0_14"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO0_14</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C1_SDA"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">I2C1_SDA</td><td data-sheets-value='[null,2,"UART1_RXD"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">UART1_RXD</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"DCAN1_TX"]' style="background-color: #93c47d; border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">DCAN1_TX</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,15]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">15</td><td data-sheets-value='[null,2,"P9_27"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_27</td><td data-sheets-value='[null,2,"GPIO3_19"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO3_19</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,16]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">16</td><td data-sheets-value='[null,2,"P9_30"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_30</td><td data-sheets-value='[null,2,"GPIO3_16"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">GPIO3_16</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
</tbody></table>

  

  

A parte analógica do P9 não tem conflitos, mas só aceita tensão até 1,8V.  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="40"/><col width="67"/><col width="104"/></colgroup><tbody>
<tr style="height: 21px;"><td style="background-color: black; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"HEADER"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">HEADER</td><td data-sheets-value='[null,2,"ANALOG (1.8V)"]' style="background-color: black; border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; color: white; padding: 2px 3px 2px 3px; vertical-align: bottom;">ANALOG (1.8V)</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,1]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">1</td><td data-sheets-value='[null,2,"P9_33"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_33</td><td data-sheets-value='[null,2,"A4"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A4</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,2]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">2</td><td data-sheets-value='[null,2,"P9_35"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_35</td><td data-sheets-value='[null,2,"A6"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A6</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,3]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">3</td><td data-sheets-value='[null,2,"P9_36"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_36</td><td data-sheets-value='[null,2,"A5"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A5</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,4]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">4</td><td data-sheets-value='[null,2,"P9_37"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_37</td><td data-sheets-value='[null,2,"A2"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A2</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,5]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">5</td><td data-sheets-value='[null,2,"P9_38"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_38</td><td data-sheets-value='[null,2,"A3"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A3</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,6]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">6</td><td data-sheets-value='[null,2,"P9_39"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_39</td><td data-sheets-value='[null,2,"A0"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A0</td></tr>
<tr style="height: 21px;"><td data-sheets-value="[null,3,null,7]" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; text-align: right; vertical-align: bottom;">7</td><td data-sheets-value='[null,2,"P9_40"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">P9_40</td><td data-sheets-value='[null,2,"A1"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">A1</td></tr>
</tbody></table>

  

Os ESC dos motores aceita frequências de 50Hz a 490Hz.  

A rotação mínima é obtida com pulsos de 1ms.  

A rotação máxima é obtida com pulsos de 2ms.  

  

Calcular o 'duty cycle' para os motores  

[http://www.optical-calculation.com/calculations/duty\_cycle\_of\_a\_pulsed\_laser.php](http://www.optical-calculation.com/calculations/duty_cycle_of_a_pulsed_laser.php)  

<div>
<br/></div>

<div>
<div>
Para 50Hz um pulso de 1ms é equivalente a 5% =&gt; 0.05 no formato da analogWrite</div>
<div>
Para 50Hz um pulso de 2ms é equivalente a 10% =&gt; 0.1 no formato da analogWrite</div>
</div>

<div>
<br/></div>

<div>
<div>
<div>
Para 490Hz um pulso de 1ms é equivalente a 49% =&gt; 0.49 no formato da analogWrite</div>
<div>
Para 490Hz um pulso de 2ms é equivalente a 98% =&gt; 0.98 no formato da analogWrite</div>
</div>
</div>

<div>
<br/></div>

Os pinos de PWM são:  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">ECAPPWM0 - P9\_42</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">ECAPPWM2 - P9\_28</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM0A - P9\_22 P9\_31</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM0B - P9\_21 P9\_29</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM1A - P9\_14 P8\_36</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM1B - P9\_16 P8\_34</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM2A - P8\_19 P8\_45</span>  

<span style="font-family: arial, sans, sans-serif; font-size: x-small;">EHRPWM2B - P8\_13 P8\_46</span>  

  

<script src="https://gist.github.com/murix/3b48d99111b273a63f4e.js"></script>

<span style="font-family: arial, sans, sans-serif; font-size: 13px;">Por algum motivo ainda em debug, os PWMs não funcionam como esperado.</span>  

<span style="font-family: arial, sans, sans-serif; font-size: 13px;">E os motores continuaram a beepar sem entrar no modo armado.</span>  

<span style="font-family: arial, sans, sans-serif; font-size: 13px;">  
</span>
  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-6U6Pbk0CB-4/U6zYKgf4FnI/AAAAAAAAr9w/b0Fu2guyp7Y/s1600/IMG_20140626_233221.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-6U6Pbk0CB-4/U6zYKgf4FnI/AAAAAAAAr9w/b0Fu2guyp7Y/s1600/IMG_20140626_233221.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">BeagleBone Black tentando armar os motores do Quadcopter.<br/>
Mas somente 2 motores armaram corretamente.</td></tr>
</tbody></table>

<span style="font-family: arial, sans, sans-serif; font-size: 13px;">  
</span>
<span style="font-family: arial, sans, sans-serif; font-size: x-small;">  
</span>
  

<div>
A minha BBB veio com um imagem antiga.<br/>
<span style="background-color: #cfe2f3;">root@beaglebone:/etc# cat /etc/version&nbsp;</span><br/>
<span style="background-color: #cfe2f3;">Angstrom v2012.12</span><br/>
<br/>
Talvez seja necessário atualizar a imagem do Linux instalada na BBB.<br/>
<a href="http://beagleboard.org/latest-images">http://beagleboard.org/latest-images</a><br/>
Estão disponíveis 4 images de cartão SD para atualizar a BBB.<br/>
Duas rodam direto do SD.<br/>
<a href="http://debian.beagleboard.org/images/bone-debian-7.5-2014-05-14-2gb.img.xz">http://debian.beagleboard.org/images/bone-debian-7.5-2014-05-14-2gb.img.xz</a><br/>
<a href="https://s3.amazonaws.com/angstrom/demo/beaglebone/Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.12-beaglebone-2013.06.20.img.xz">https://s3.amazonaws.com/angstrom/demo/beaglebone/Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.12-beaglebone-2013.06.20.img.xz</a><br/>
E duas se copiam para rodar dentro do EMMC.<br/>
<a href="http://debian.beagleboard.org/images/BBB-eMMC-flasher-debian-7.5-2014-05-14-2gb.img.xz">http://debian.beagleboard.org/images/BBB-eMMC-flasher-debian-7.5-2014-05-14-2gb.img.xz</a><br/>
<a href="https://s3.amazonaws.com/angstrom/demo/beaglebone/BBB-eMMC-flasher-2013.09.04.img.xz">https://s3.amazonaws.com/angstrom/demo/beaglebone/BBB-eMMC-flasher-2013.09.04.img.xz</a><br/>
<br/>
Todas as beaglebones novas passaram a usar o Debian como imagem padrão desde de maio de 2014.<br/>
<br/>
Um das novidades do Debian é o "Userspace Arduino libraries", que transforma BBB em Arduino.<br/>
<a href="http://elinux.org/Userspace_Arduino#new_Debian_images">http://elinux.org/Userspace_Arduino#new_Debian_images</a><br/>
<br/>
Depois de instalar o Debian 7.5 no EMMC da BBB, é preciso rotear o acesso da placa pelo USB.<br/>
No Linux isso é feito com apenas dois comandos:<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# sysctl -w net.ipv4.ip_forward=1</span><br/>
<span style="background-color: #cccccc;">root@beaglebone:~# iptables -t nat -A POSTROUTING -j MASQUERADE</span><br/>
E no lado da BBB, tudo deveria estar ok, mas a rota para padrão e o dns não vem configurados.<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# route add default gw 192.168.7.1</span><br/>
<span style="background-color: #cccccc;">root@beaglebone:~# echo nameserver 8.8.8.8 &gt; /etc/resolv.conf</span><br/>
<br/>
Agora que a internet está funcionando na BBB, é preciso atualizar o Debian.<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# aptitude update</span><br/>
<span style="background-color: #cccccc;">root@beaglebone:~# aptitude dist-upgrade</span><br/>
<br/>
Editar ambiente do uBoot para desativar a interface HDMI e liberar alguns pinos.<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# nano /boot/uboot/uEnv.txt</span><br/>
<span style="background-color: #cccccc;">##Disable HDMI</span><br/>
<span style="background-color: #cccccc;">cape_disable=capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN</span><br/>
<div>
<br/></div>
Instalar alguma pacotes adicionais<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# aptitude install ipython mc python-serial</span><br/>
<br/>
Instalação do&nbsp;Adafruit BeagleBone IO Python library<br/>
<br/>
<a href="https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu">https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu</a><br/>
<br/>
<span style="background-color: #cccccc;">root@beaglebone:~#&nbsp;apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y</span><br/>
<span style="background-color: #cccccc;">root@beaglebone:~# pip install Adafruit_BBIO --upgrade</span><br/>
<br/>
Testando o ADC com ipython<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-bR-fFj9l86g/U64so5sjs7I/AAAAAAAAr-g/fAEH_QFu0ho/s1600/ipython-bbb-adc.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-bR-fFj9l86g/U64so5sjs7I/AAAAAAAAr-g/fAEH_QFu0ho/s1600/ipython-bbb-adc.png" width="224"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Testando com todos os pinos no AGND, depois no VREF_ANALOG, e por fim aberto.<br/>
O resultado é um percentual, para descobrir a tensão real é preciso multiplicar por 1.8V</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-QKpVOFdMvo0/U64tbiiGsGI/AAAAAAAAr-0/D7glhpwZA5U/s1600/IMG_20140627_235001.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-QKpVOFdMvo0/U64tbiiGsGI/AAAAAAAAr-0/D7glhpwZA5U/s1600/IMG_20140627_235001.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligações de todos os pinos do ADC juntos.</td></tr>
</tbody></table>
Instalar o PirateScope, é preciso de um osciloscópio para testar o PWM.<br/>
<a href="https://github.com/tgvaughan/PirateScope">https://github.com/tgvaughan/PirateScope</a><br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-yS33YxCKjD8/U641bmwNj0I/AAAAAAAAr_Y/KDmFH7juzrk/s1600/pirate-scope-beaglebone.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="250" src="http://4.bp.blogspot.com/-yS33YxCKjD8/U641bmwNj0I/AAAAAAAAr_Y/KDmFH7juzrk/s1600/pirate-scope-beaglebone.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">PirateScope capturando PWM de 50Hz (20ms) com duty-cycle 50% (10ms)</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Hj5bIt0KaHQ/U64162Q-DEI/AAAAAAAAr_k/23-LOd3SASE/s1600/IMG_20140628_002111.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-Hj5bIt0KaHQ/U64162Q-DEI/AAAAAAAAr_k/23-LOd3SASE/s1600/IMG_20140628_002111.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate conectado:<br/>
GND -&gt; BBB: GND<br/>
ADC -&gt; &nbsp;BBB: P9_14</td></tr>
</tbody></table>
Testando o PWM pelo ipython<br/>
<span style="background-color: #cccccc;">root@beaglebone:~# ipython</span><br/>
<span style="background-color: #cccccc;">Python 2.7.3 (default, Mar 14 2014, 17:55:54)&nbsp;</span><br/>
<span style="background-color: #cccccc;">Type "copyright", "credits" or "license" for more information.</span><br/>
<span style="background-color: #cccccc;">IPython 0.13.1 -- An enhanced Interactive Python.</span><br/>
<span style="background-color: #cccccc;">? &nbsp; &nbsp; &nbsp; &nbsp; -&gt; Introduction and overview of IPython's features.</span><br/>
<span style="background-color: #cccccc;">%quickref -&gt; Quick reference.</span><br/>
<span style="background-color: #cccccc;">help &nbsp; &nbsp; &nbsp;-&gt; Python's own help system.</span><br/>
<span style="background-color: #cccccc;">object? &nbsp; -&gt; Details about 'object', use 'object??' for extra details.</span><br/>
<span style="background-color: #cccccc;">In [1]: import Ada</span><br/>
<span style="background-color: #cccccc;">Adafruit_BBIO &nbsp;Adafruit_I2C &nbsp;&nbsp;</span><br/>
<span style="background-color: #cccccc;">In [1]: import Adafruit_BBIO.</span><br/>
<span style="background-color: #cccccc;">Adafruit_BBIO.ADC &nbsp; Adafruit_BBIO.PWM &nbsp; Adafruit_BBIO.UART</span><br/>
<span style="background-color: #cccccc;">Adafruit_BBIO.GPIO &nbsp;Adafruit_BBIO.SPI &nbsp;&nbsp;</span><br/>
<span style="background-color: #cccccc;">In [1]: import Adafruit_BBIO.PWM as PWM</span><br/>
<span style="background-color: #cccccc;">In [2]: PWM.start("P9_14",50,50)</span><br/>
<span style="background-color: #cccccc;">In [3]:&nbsp;</span><br/>
<br/>
<br/>
P8_13<br/>
P8_19<br/>
P8_34<br/>
P8_36<br/>
P8_45<br/>
P8_46<br/>
<br/>
P9_14<br/>
P9_16<br/>
P9_21<br/>
P9_22<br/>
P9_28<br/>
P9_29<br/>
P9_31<br/>
P9_42<br/>
<div>
<br/></div>
<br/>
<br/>
<br/></div>