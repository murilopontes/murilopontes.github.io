---
layout: post
title: Arduino MWC fly test with GY-86 10DOF IMU
categories:
 - post
date: 2014-06-01 20:32:00 +0100
---

O GY-86 é um array de sensores que pode ser usando com o MWC.  

  

<a name="more"></a>  
  

Na falta de um receptor e transmissor/controle de RF, substitui em ambos por placas Stellaris com o Anaren RF Boost Pack. No lado do transmissor/controle/PC, um controle de Xbox envia os comandos para porta serial de uma das placas stellaris através de um programa simples em C# que usa o SlimDX para ler os eventos do controle. No lado Arduino (receptor) outra placa Stellaris recebe os pacotes RF e gera os sinais PWM para o Throttle, Roll, Pich e Yaw, ou seja, uma emulação completa e funcional de um sistema de controle RF tradicional.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-LTnWPxwEfoI/U4xJ4qnNPxI/AAAAAAAArUI/MxSwlAwRxqM/s1600/quadX.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://4.bp.blogspot.com/-LTnWPxwEfoI/U4xJ4qnNPxI/AAAAAAAArUI/MxSwlAwRxqM/s1600/quadX.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema de ligação do MWC<br/>
<a href="http://www.multiwii.com/connecting-elements">http://www.multiwii.com/connecting-elements</a></td></tr>
</tbody></table>

Para o MWC 2.3 no Arduino nano o esquema é um pouco diferente, boa parte disso está no def.h  

D2 - RF PWM entrada THROTTLE  

D4 - RF PWM entrada ROLL  

D5 - RF PWM entrada PITCH  

D6 - RF PWM entrada YAW  

A4 - I2C SDA GY-86  

A5 - I2C SCL GY-86  

D3 - ESC PWM saida / MOTOR  

D9 -&nbsp;ESC&nbsp;PWM saida&nbsp;&nbsp;/&nbsp;MOTOR  

D10 -&nbsp;ESC PWM saida&nbsp;/&nbsp;MOTOR  

D11 - &nbsp;ESC PWM saida&nbsp;/&nbsp;MOTOR  

D8 - LIVRE (pode ser buzzer/AUX2)  

D7 - LIVRE (pode ser RF PWM MODE)  

D12 - LIVRE (pode ser AUX2)  

A6&nbsp;- LIVRE  

A7&nbsp;- LIVRE  

A0 - LIVRE  

A1&nbsp;- LIVRE  

A2&nbsp;- LIVRE (pode ser PSENSOR)  

A3&nbsp;- LIVRE (pode ser V_BAT)  

D13 - LED (MWC STATUS)  

TX - USART (IDE/DEBUG/BLUETOOTH)  

RX - USART (IDE/DEBUG/BLUETOOTH)  

  

No config.h é preciso descomentar e alterar algumas coisas  

#define QUADX  

#define MINCOMMAND &nbsp;900  

#define GY_86  

  

Meus ESCs são Hobbywing Flyfun 30A, não armaram com MINCOMMAND &nbsp;em 1000,  

com MINCOMMAND &nbsp;em 900 os motores armaram perfeitamente.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-xsmPqxUaHGA/U5Tgh_8f6tI/AAAAAAAArbY/6qQG42MHyyo/s1600/IMG_20140608_183512.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://1.bp.blogspot.com/-xsmPqxUaHGA/U5Tgh_8f6tI/AAAAAAAArbY/6qQG42MHyyo/s1600/IMG_20140608_183512.jpg" width="300"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">ESC programming card: configuração recomendada para o MWC é ajustar o "Timming" para "Middle"</td></tr>
</tbody></table>

  

  

Da para ativar o controle dos motores pela GUI, mas cuidado.  

Quando ativei para testar os motores no máximo (2000 de throttle), depois de alguns segundos saiu fumaça dos motores. Até uns 1700 é seguro sem risco de sobre aquecimento.  

#define DYNBALANCE  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-T72QYLZyouM/U5NUJjFm6xI/AAAAAAAArX0/2JSCuzMMX8w/s1600/multiwiiconf-gy86.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="376" src="http://3.bp.blogspot.com/-T72QYLZyouM/U5NUJjFm6xI/AAAAAAAArX0/2JSCuzMMX8w/s1600/multiwiiconf-gy86.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">MultiWiiConf &nbsp;conectado ao Arduino Nano <complete id="goog_1596444549">+<span id="goog_1596444550"></span><span id="goog_1596444551"></span></complete>&nbsp;GY-86</td></tr>
</tbody></table>

  

  

Para calibrar o GY-86 é preciso usar a MultiWiiConf, depois de aberta a conexão serial, é só colocar o drone em um local plano aperta o botão CALIB_ACC e esperar o LED D13 apagar, então use o botão WRITE para gravar a calibração na EEPROM interna do Arduino. Também é necessário calibrar o magnetômetro. Aperte o botão CALIB_MAG enquanto o LED D13 pisca, gire o drone em 360 graus nos eixos X,Y,Z. Quando apagar o LED D13 grave a calibração no botão WRITE.  

Na esqueça de conferir na instrumentação do MultiWiiConf se quando você mexe no Drone os ângulos estão corretos. O altímetro do GY-86 não precisa calibrar.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-5brjREV5Eic/U5DwUBKCAlI/AAAAAAAArWI/YgFfPEfTqXs/s1600/arduino-com-multiwii.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-5brjREV5Eic/U5DwUBKCAlI/AAAAAAAArWI/YgFfPEfTqXs/s1600/arduino-com-multiwii.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Placa mãe do drone com Arduino e GY-86.<br/>
O controle RF do Multiwii (MWC) é feito pela Stellaris com Anaren Boost Pack gravada com RF RX</td></tr>
</tbody></table>

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-06TzLE2viw8/U5MeMjb9YgI/AAAAAAAArXc/vVEOI82b0ew/s1600/stellaris_RF.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="221" src="http://1.bp.blogspot.com/-06TzLE2viw8/U5MeMjb9YgI/AAAAAAAArXc/vVEOI82b0ew/s1600/stellaris_RF.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Stellaris com Anaren Boost Pack para fazer o enlace RF entre o Drone e o PC</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-x2qXOhkXZUk/U5MfDpbL1yI/AAAAAAAArXk/11h0QNJNic0/s1600/xbox-rf-serial.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="http://3.bp.blogspot.com/-x2qXOhkXZUk/U5MfDpbL1yI/AAAAAAAArXk/11h0QNJNic0/s1600/xbox-rf-serial.JPG"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Enviador de controle de xbox para a porta serial da Stellaris com Anaren boost pack gravada com RF TX</td></tr>
</tbody></table>

  

  

No PC o controle do Xbox é lido, os valores dos sticks analógicos são enviados para a porta serial da Stellaris com Anaren boost pack que vai empacotar e enviar para o drone.  

No drone a Stellaris com Anaren boost recebe o pacote do PC e gera os PWMs esperados pelo Multiwii.  

O alcance do link RF usando o Anaren boost é de cerca de 400 metros.  

  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/bBi8mVFvGcs" width="420"></iframe>

  

Para um primeiro teste no Arduino com MWC diria que o hardware está ok, mas precisa ajustar o firmware para resolver a instabilidade do quadx.  

  

  

  

  