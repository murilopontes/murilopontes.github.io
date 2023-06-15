---
layout: page
title: Drone- Arduino Nano GY86 MWC
categories:
 - page
date: 2016-07-31 19:53:00 +0100
---

Playlist dos experimentos do&nbsp;Drone DIY com Arduino Nano  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/videoseries?list=PLB_uIxBF0dCeErZgY-4U7MLb8el9x2myX" width="560"></iframe>

  

<div dir="ltr" style="text-align: left;" trbidi="on">
<br class="Apple-interchange-newline"/>
<br/>
<h3>
Drone 2015.05 com multiwii 2.4</h3>
Arduino Nano v3.0 com GY-86 e um receptor FrSky X8R, o transmissor é um Frsky Taranis Plus.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-z2Uh-prwFFY/VWcKKE3QbbI/AAAAAAABI1s/TLxWj_qNki8/s1600/IMG_20150510_011817.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="https://1.bp.blogspot.com/-z2Uh-prwFFY/VWcKKE3QbbI/AAAAAAABI1s/TLxWj_qNki8/s320/IMG_20150510_011817.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Arduino Nano 3.0 com GY-86 e receptor Frsky X8R</td></tr>
</tbody></table>
<br/>
<h3>
Drone 2014.04 com multiwii 2.3</h3>
<div>
Na falta de um receptor e transmissor/controle de RF, substitui em ambos por placas Stellaris com o Anaren RF Boost Pack. No lado do transmissor/controle/PC, um controle de Xbox envia os comandos para porta serial de uma das placas stellaris através de um programa simples em C# que usa o SlimDX para ler os eventos do controle. No lado Arduino (receptor) outra placa Stellaris recebe os pacotes RF e gera os sinais PWM para o Throttle, Roll, Pich e Yaw, ou seja, uma emulação completa e funcional de um sistema de controle RF tradicional.</div>
<br/>
<h3>
Guia rápido</h3>
- Download Arduino.<br/>
- Download Multiwii.<br/>
- Editar o config.h para Arduino Nano com GY86.<br/>
- Upload do multiwii configurado para o Arduino.<br/>
- Abrir o MultiwiiConf<br/>
- Calibrar o acelerometro<br/>
- Calibrar o magnetometro<br/>
- Marca as checkbots dos chaves AUX<br/>
- Verificar se uma das chaves AUX está configurada para armar os motores<br/>
- Verificar se uma das chaves AUX está configurada para ativar o autotune do PID<br/>
- Verificar se uma das chaves AUX está configurada para mudar entre os modos de voo<br/>
- Gravar as configurações para placa.<br/>
- Antes de conectar a bateria, verificar no MultiwiiConf se os comandos enviados pelo transmissor estão agindo como esperado.<br/>
<br/>
<h3>
Calibrar os ESCs:</h3>
- Remover as hélices<br/>
- Editar config.h e descomentar #define ESC_CALIB_CANNOT_FLY<br/>
- Re-upload o código para o Arduino<br/>
- Desconectar o Arduino do PC. Plugar a bateria e esperar os ESCs parar de beepar.<br/>
- Desconectar a bateria.<br/>
- Editar config.h e comentar #define ESC_CALIB_CANNOT_FLY<br/>
- Re-upload o código para o Arduino<span class="Apple-tab-span" style="white-space: pre;"> </span><br/>
<br/>
<h3>
Calibrar os PIDs:</h3>
- Enquanto estiver planando, ativar a chave AUX do autotune<br/>
- Esperar oscilar por cerca de 30 segundos<br/>
- Desligar a chave AUX do autotune<br/>
- Reativer a chave AUX do autotune<br/>
- Esperar oscilar por cerca de 30 segundos<br/>
- Desligar a chave AUX do autotune<br/>
- Pausar<br/>
- Desarmar os motores usando a chave AUX<br/>
- Ligar e desligar a chave AUX do autotune para gravar os valores na EEPROM.<br/>
<h3>
</h3>
<h3>
Montagem do Drone DIY com Arduino Nano</h3>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-LTnWPxwEfoI/U4xJ4qnNPxI/AAAAAAAArUI/MxSwlAwRxqM/s1600/quadX.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="https://4.bp.blogspot.com/-LTnWPxwEfoI/U4xJ4qnNPxI/AAAAAAAArUI/MxSwlAwRxqM/s1600/quadX.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">Esquema de ligação do MWC<br/>
<a href="http://www.multiwii.com/connecting-elements">http://www.multiwii.com/connecting-elements</a></td></tr>
</tbody></table>
Os pinos do Arduino nano são distribuídos da seguinte forma:<br/>
D2 - RF PWM entrada THROTTLE<br/>
D4 - RF PWM entrada ROLL<br/>
D5 - RF PWM entrada PITCH<br/>
D6 - RF PWM entrada YAW<br/>
A4 - I2C SDA GY-86<br/>
A5 - I2C SCL GY-86<br/>
D3 - ESC PWM saida / MOTOR<br/>
D9 -&nbsp;ESC&nbsp;PWM saida&nbsp;&nbsp;/&nbsp;MOTOR<br/>
D10 -&nbsp;ESC PWM saida&nbsp;/&nbsp;MOTOR<br/>
D11 - &nbsp;ESC PWM saida&nbsp;/&nbsp;MOTOR<br/>
D8 - LIVRE (pode ser buzzer/AUX2)<br/>
D7 - LIVRE (pode ser RF PWM MODE)<br/>
D12 - LIVRE (pode ser AUX2)<br/>
A6&nbsp;- LIVRE<br/>
A7&nbsp;- LIVRE<br/>
A0 - LIVRE<br/>
A1&nbsp;- LIVRE<br/>
A2&nbsp;- LIVRE (pode ser PSENSOR)<br/>
A3&nbsp;- LIVRE (pode ser V_BAT)<br/>
D13 - LED (MWC STATUS)<br/>
TX - USART (IDE/DEBUG/BLUETOOTH)<br/>
RX - USART (IDE/DEBUG/BLUETOOTH)<br/>
<br/>
<h3>
Configuração dos ESCs</h3>
<div>
Também é necessário revisar a configuração dos ESC usando um cartão de programação</div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://1.bp.blogspot.com/-xsmPqxUaHGA/U5Tgh_8f6tI/AAAAAAAArbY/6qQG42MHyyo/s1600/IMG_20140608_183512.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="https://1.bp.blogspot.com/-xsmPqxUaHGA/U5Tgh_8f6tI/AAAAAAAArbY/6qQG42MHyyo/s1600/IMG_20140608_183512.jpg" width="300"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">ESC programming card: configuração recomendada para o MWC é ajustar o "Timming" para "Middle"</td></tr>
</tbody></table>
<br/>
<h3>
Calibração dos ESCs</h3>
<div>
É preciso calibrar os ESC para que os todos os quatro estejam sincronizados.&nbsp;</div>
<div>
<br/></div>
<br/>
<br/>
<h3>
Configuração do MWC</h3>
No config.h é preciso:<br/>
<br/>
1) descomentar as seguintes linhas:<br/>
#define QUADX<br/>
#define GY_86<br/>
<br/>
2) alterar as seguintes linhas<br/>
#define MINCOMMAND &nbsp;900<br/>
<br/>
<h3>
Calibração do acelerômetro e magnetômetro</h3>
Para calibrar o GY-86 é preciso usar a MultiWiiConf, depois de aberta a conexão serial, é só colocar o drone em um local plano aperta o botão CALIB_ACC e esperar o LED D13 apagar, então use o botão WRITE para gravar a calibração na EEPROM interna do Arduino. Também é necessário calibrar o magnetômetro. Aperte o botão CALIB_MAG enquanto o LED D13 pisca, gire o drone em 360 graus nos eixos X,Y,Z. Quando apagar o LED D13 grave a calibração no botão WRITE.<br/>
Na esqueça de conferir na instrumentação do MultiWiiConf se quando você mexe no Drone os ângulos estão corretos. O altímetro do GY-86 não precisa calibrar.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://3.bp.blogspot.com/-T72QYLZyouM/U5NUJjFm6xI/AAAAAAAArX0/2JSCuzMMX8w/s1600/multiwiiconf-gy86.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="376" src="https://3.bp.blogspot.com/-T72QYLZyouM/U5NUJjFm6xI/AAAAAAAArX0/2JSCuzMMX8w/s1600/multiwiiconf-gy86.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">MultiWiiConf &nbsp;conectado ao Arduino Nano&nbsp;<complete id="goog_1596444549">+<span id="goog_1596444550"></span><span id="goog_1596444551"></span></complete>&nbsp;GY-86</td></tr>
</tbody></table>
<br/>
<br/>
<!------><!------><!------></div>