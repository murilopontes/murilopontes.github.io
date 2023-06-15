---
layout: page
title: Drone- open AR.Drone autopilot
categories:
 - page
date: 2016-07-31 19:50:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: center;">
<div style="text-align: justify;">
This is one of my personal projects, which aims to implement an opensource autopilot to replace ardrone standart program.elf.<br/>
<br/>
Playlist of the experiments with the opensource autopilot</div>
<div style="text-align: justify;">
<br/></div>
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/videoseries?list=PLB_uIxBF0dCc0KjIUzelhXK7nCjqYKMhJ" width="560"></iframe>
</div>
<div style="text-align: center;">
<br/></div>
<div style="text-align: center;">
<span style="font-size: small; font-weight: normal;"><br/></span></div>
<span style="font-size: small; font-weight: normal;">New opensource firmware and software build from scratch.</span>
<br/>
<h2>
<span style="font-size: large;">
Current state</span></h2>
<ul>
<li><span style="color: #38761d;">End-to-end opensource (Ardrone side and PC side)</span></li>
<li><span style="color: #38761d;">Working </span>(<span style="color: #cc0000;">needs better PID tunning</span> - as show in the video)</li>
<li><span style="color: #38761d;">Reconfigurable PID using PC application</span></li>
<li><span style="color: #cc0000;">Online Self-Tuning PID Controller&nbsp;(unfinished)</span> &nbsp;</li>
<li><span style="color: #38761d;">Realtime monitor all Ardrone sensors (Accels, Gyros, Sonar, Voltages) and motors (feedback)</span></li>
<li><span style="color: #38761d;">On-the-fly motor recovery in case of failure</span></li>
<li><span style="color: #38761d;">Photo: Vertical and horizontal cameras support (V4L2)</span></li>
<li><span style="color: #cc0000;">Video: H264 hardware codec and realtime video still unstable</span></li>
<li><span style="color: #38761d;">All communication is done using JSON</span><span style="color: #cc0000;">&nbsp;</span></li>
<li><b><span style="color: #38761d;">Remote Debugging using gdbserver (GDB)</span></b></li>
</ul>
<br/>
<div style="text-align: center;">
<br/></div>
<h2>
<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-5mx4D5MPQBY/U3jrnipcQ1I/AAAAAAAArQw/iZaPN_Uv4gU/s1600/openuav-ardrone-control.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="275" src="https://4.bp.blogspot.com/-5mx4D5MPQBY/U3jrnipcQ1I/AAAAAAAArQw/iZaPN_Uv4gU/s1600/openuav-ardrone-control.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">OpenUAV realtime: Xbox controller sender and &nbsp;Ardrone telemetric system<br/>
<br/>
<div>
<br/></div>
</td></tr>
</tbody></table>
</h2>
<h2>
<span style="font-size: large;">
Hardware</span></h2>
<ul>
<li>Xbox 360 Controller</li>
<li style="text-align: justify;">Ardrone v1 - main target tested (started in june/2012)</li>
<li>Ardrone v2 - work in progress (started in october/2014 with <a class="g-profile" href="https://plus.google.com/111653744412699215748" target="_blank">+Alan Carvalho de Assis</a>&nbsp;)</li>
</ul>
<h2>
<span style="font-size: large;">
Software</span></h2>
<div>
Required tools and frameworks for build:</div>
<div>
<br/>
<ul>
<li>Visual Studio 2013 (PC)</li>
<li>SlimDX (PC)</li>
<li>Eclipse CDT</li>
<li>Sourcery G++ Lite 2009q1-203 (Ardrone v1)</li>
<li>Boost C++ 1.55</li>
<li>Firmware oficial 1.11.5 (Ardrone v1) - opensource navboard parser is designed for 1.11.5</li>
</ul>
</div>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
<div style="margin: 0px;">
<br/></div>
</div>
OpenUAV for AR.Drone - Windows control application<br/>
<div>
<a href="https://github.com/murix/dronespersonalizados/tree/master/workspace-visual-studio/OpenUAV-ardrone">https://github.com/murix/dronespersonalizados/tree/master/workspace-visual-studio/OpenUAV-ardrone</a><br/>
<br/>
OpenUAV for AR.Drone - Firmware replacement<br/>
<a href="https://github.com/murix/dronespersonalizados/tree/master/workspace-eclipse-cdt/OpenUAV-ardrone">https://github.com/murix/dronespersonalizados/tree/master/workspace-eclipse-cdt/OpenUAV-ardrone</a><br/>
<br/>
<br/>
<h2>
Software oficial - Ardrone v1</h2>
<div>
O ardrone v1 foi lançado na CES em janeiro de 2010.<br/>
Comprei o ardrone v1 em junho de 2012, em agosto de 2012 teve o último update oficial.<br/>
na CES em janeiro de 2012 foi lançado o Ardrone v2.</div>
<div>
<br/></div>
Versão 1.11.5 &nbsp;- &nbsp;Aug 20 2012 14:37:42</div>
<div>
(descontinuado? com a liberação do Ardrone v2)<br/>
<a href="http://download.parrot.com/drone_soft_update/ardrone_update.plf">http://download.parrot.com/drone_soft_update/ardrone_update.plf</a><br/>
<br/>
<br/>
Extrator de PLF<br/>
<a href="https://code.google.com/p/ardrone-tool/">https://code.google.com/p/ardrone-tool/</a><span style="background-color: white; line-height: 18.2000007629395px;"><span style="color: #666666; font-family: Trebuchet MS, Trebuchet, sans-serif; font-size: x-small;"><br/></span></span>
<span style="background-color: white; line-height: 18.2000007629395px;"><span style="color: #666666; font-family: Trebuchet MS, Trebuchet, sans-serif; font-size: x-small;"><br/></span></span>
<span style="background-color: white; line-height: 18.2000007629395px;"><span style="color: #666666; font-family: Trebuchet MS, Trebuchet, sans-serif; font-size: x-small;"><br/></span></span>
<br/>
<h2 style="text-align: left;">
<b>Gravação de flash do V1 sem Wifi</b></h2>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-FM8SIFFgDgs/VEpc9pQf3UI/AAAAAAAAtec/momgVARGik8/s1600/ARDrone-USB-Cable.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="210" src="https://3.bp.blogspot.com/-FM8SIFFgDgs/VEpc9pQf3UI/AAAAAAAAtec/momgVARGik8/s1600/ARDrone-USB-Cable.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pino 2 é VBAT (11,1 ~12V)<br/>
Pino 4 é RX 3.3V<br/>
Pino 6 é TX 3.3V</td></tr>
</tbody></table>
<br/>
<br/>
<h2 style="text-align: left;">
<b>v1: Processador, sensores e Linux</b></h2>
AR.Drone 1.0 : Mykonos card,<br/>
Processor&nbsp;&nbsp;ARM926EJ-S rev 5 (v5l)<br/>
Wi-Fi: AR6000<br/>
RAM: 128MB<br/>
FLASH: 128MB<br/>
<br/>
Navboard:<br/>
Microchip PIC24HJ16GP304 40MHZ 16-bit microprocessor<br/>
Ultrasonic&nbsp;Sonar<br/>
<br/>
<div>
Bosh BMA150 Accelerometer</div>
<div>
Invensense IDG 500 gyroscope</div>
<div>
Epson XV-3500CB gyroscope<br/>
<br/>
Camera horizontal 640x480 (VGA)</div>
Camera vertical 176x144 (QCIF)<br/>
<br/>
Linux: 2.6.27.47-parrot-01227-g93dde09 \#1 preempt Fri Jul 2 15:23:06 CEST 2010 armv5tejl GNU/Linux<br/>
<div>
<br/></div>
<h2>
<b>v2: Processador, sensores e Linux</b></h2>
AR.Drone 2.0 : Mykonos2 card,<br/>
Processor OMAP 3640 1GHz 32 bit ARM Cortex A8 with a video DSP 800MHz TMS320DMC64x<br/>
Wi-Fi: AR6000<br/>
RAM: 256MB<br/>
FLASH: 128MB<br/>
<div>
<br/></div>
<div>
Navboard:</div>
<div>
<div>
Microchip PIC24HJ Microcontroller</div>
<div>
Ultrasonic Sonar</div>
</div>
<div>
<br/></div>
<div>
Bosch BMA150 Accelerometer</div>
<div>
<div>
Invensense IMU-3000 Gyro</div>
</div>
<div>
AKM Semiconductor 3-Axis Compass</div>
<div>
BMP180 Barometric Pressure Sensor&nbsp;</div>
<div>
<br/>
<div>
Camera horizontal 1080p</div>
Camera vertical 720p<br/>
<br/></div>
<div>
Telit Wireless Solutions GPS receiver&nbsp;</div>
<div>
4GB of user-accessible NAND flash for storing video and picture captures.</div>
<div>
<br/></div>
Linux: 2.6.32.9-g0d605ac \#1 preempt Fri Apr 6 12:01:59 CEST 2012 armv7l GNU/Linux<br/>
<div>
<br/>
<br/>
<a href="http://www.eetimes.com/document.asp?doc_id=1323541&amp;page_number=1">http://www.eetimes.com/document.asp?doc_id=1323541&amp;page_number=1</a><br/>
<a href="https://bitbucket.org/multidest/ardronetools/wiki/Home">https://bitbucket.org/multidest/ardronetools/wiki/Home</a><br/>
<br/></div>
<div>
<br/>
<br/></div>
<h2 style="text-align: left;">
<b><u>Como abrir o Ardrone v1</u></b></h2>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-7SLp3lJyIck/VEhgVahMs0I/AAAAAAAAtao/K4B9gF0Gth8/s1600/IMG_20141022_225544.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://4.bp.blogspot.com/-7SLp3lJyIck/VEhgVahMs0I/AAAAAAAAtao/K4B9gF0Gth8/s1600/IMG_20141022_225544.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Para abrir o Ardrone v1 - é preciso de uma chave Torx T-6<br/>
remover os 4 parafusos torx da tampa de plástico</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-AReMdKF3_Bw/VEhg6p1zFKI/AAAAAAAAtbE/JtqCd3OJN5U/s1600/IMG_20141022_225832.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://4.bp.blogspot.com/-AReMdKF3_Bw/VEhg6p1zFKI/AAAAAAAAtbE/JtqCd3OJN5U/s1600/IMG_20141022_225832.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Agora chegou na placa da CPU que está encima da placa navboard.<br/>
E preciso tirar mais 4 parafusos torx.<br/>
Depois soltar o cablo flat da camera frontal.<br/>
Depois desencaixar a cpu board da nav board.<br/>
E retirar a navboard, depois de removida a navboard que estava por baixo.<br/>
Remover os cabos de dados e de força dos motores.</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-Z_jPKUC4Igk/VEhj8MzsxrI/AAAAAAAAtbg/QHBGukLUunM/s1600/IMG_20141022_231131.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://2.bp.blogspot.com/-Z_jPKUC4Igk/VEhj8MzsxrI/AAAAAAAAtbg/QHBGukLUunM/s1600/IMG_20141022_231131.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Descobri de removidas as duas placas vai ficar só a carcaça com as conexões dos motores,<br/>
e o flat da camera frontal.</td></tr>
</tbody></table>
&gt;&gt;&gt;<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-sFL1tordXt8/VEhlx_hBgCI/AAAAAAAAtcU/j4Bz8qEeQok/s1600/IMG_20141022_231832.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://1.bp.blogspot.com/-sFL1tordXt8/VEhlx_hBgCI/AAAAAAAAtcU/j4Bz8qEeQok/s1600/IMG_20141022_231832.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na Navboard ( MYKONOS_NAV_04) dá para ver os seguintes componentes:<br/>
Microchip PIC24HJ16GP304 40MHZ 16-bit microprocessor<br/>
MEMS gyroscope, the Invensense IDG 500<br/>
&nbsp;Epson XV-3500CB gyroscope<br/>
Bosh BMA150<br/>
<br/>
Na CPU board (MYKONOS_MB_11) :<br/>
Parrot 6 ARM926EJ-S 468 MHz processor<br/>
ROCm Atheros AR6102G-BM2D b/g Wi-Fi<br/>
Micron OGA17 D9HSJ (128 mbytes RAM)<br/>
Camera horizontal 640x480 (VGA)<br/>
Camera vertical 176x144 (QCIF)</td></tr>
</tbody></table>
&gt;&gt;&gt;<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-31AOTGYwNzg/VEhlx_WqLCI/AAAAAAAAtcU/sguSqW55ERw/s1600/IMG_20141022_231909.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://3.bp.blogspot.com/-31AOTGYwNzg/VEhlx_WqLCI/AAAAAAAAtcU/sguSqW55ERw/s1600/IMG_20141022_231909.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na Navboard&nbsp;( MYKONOS_NAV_04) dá para ver os seguintes componentes:<br/>
2 sonares gigantes<br/>
<br/>
Na CPU board &nbsp;(MYKONOS_MB_11)&nbsp;:<br/>
Micron 29F1G08AAC&nbsp;&nbsp;(128 mbytes FLASH)<br/>
<br/>
<br/></td></tr>
</tbody></table>
<br/>
<br/>
<br/>
Referências<br/>
<a href="http://blog.perquin.com/blog/ardrone-motor-controller/">http://blog.perquin.com/blog/ardrone-motor-controller/</a><br/>
<a href="http://embedded-software.blogspot.com.br/">http://embedded-software.blogspot.com.br/</a><br/>
<br/>
<br/>
SDK<br/>
<a href="https://projects.ardrone.org/projects/show/ardrone-api">https://projects.ardrone.org/projects/show/ardrone-api</a><br/>
<br/>
Ardrone v1 teardown<br/>
<a href="http://www.kapejod.org/en/category/ardrone/">http://www.kapejod.org/en/category/ardrone/</a><br/>
<br/>
<br/>
<br/>
Pinout dos motores<br/>
<a href="http://fenrir.naruoka.org/archives/000805.html">http://fenrir.naruoka.org/archives/000805.html</a><br/>
<a href="http://www.ardrone-flyers.com/forum/viewtopic.php?f=13&amp;t=1025&amp;start=15">http://www.ardrone-flyers.com/forum/viewtopic.php?f=13&amp;t=1025&amp;start=15</a><br/>
<br/>
<pre style="background-color: #f7f7f7; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border: 1px solid rgb(221, 221, 221); font-family: 'Courier New', Courier, Monaco, 'Lucida Console', monospace; font-size: 14px; line-height: 1.5em; margin-bottom: 1.5em; margin-top: 1.5em; outline: 0px; overflow: auto; padding: 1em;">Pin 1 Battery 11.4V
Pin 2 VCC 5V (ATMega8a VCC Pin4+5)
Pin 3 TX+RX (ATmega8a Pin30+31)
Pin 4 IRQ to main board (ATmega8a PC3 Pin26)
Pin 5 GND

Pin 1 Red
Pin 2 White
Pin 3 Motor1=Yellow,M2=Orange,M3=Blue,M4=Green
Pin 4 Motor1=Purple,M2=Gray,M3=Brown,M4=Pink
Pin 5 Black</pre>
Quando ocorre um problema nos motores o pino 106 é setado para 1.<br/>
Para resetar o status de problema é preciso setar o pino 107 e resetar o pino 107.<br/>
<br/>
Cameras<br/>
<a href="http://blog.perquin.com/blog/ar-drone-video/">http://blog.perquin.com/blog/ar-drone-video/</a><br/>
<h2 style="background-color: white; border: 0px; color: #333333; font-family: Arial, Helvetica, sans-serif; font-size: 25px; font-weight: normal; line-height: 1.1em; margin: 0.5em 0px; outline: 0px; padding: 0px;">
Bottom Camera Initialization</h2>
<pre style="background-color: #f7f7f7; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border: 1px solid rgb(221, 221, 221); font-family: 'Courier New', Courier, Monaco, 'Lucida Console', monospace; font-size: 14px; line-height: 1.5em; margin-bottom: 1.5em; margin-top: 1.5em; outline: 0px; overflow: auto; padding: 1em;">i2cset -y 0 0x49 0x0a 0x85&nbsp;&nbsp;&nbsp;&nbsp; - sets Vdd4 to 3.0V
gpio 59 -d ho 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- set CE enabled</pre>
<h2 style="background-color: white; border: 0px; color: #333333; font-family: Arial, Helvetica, sans-serif; font-size: 25px; font-weight: normal; line-height: 1.1em; margin: 0.5em 0px; outline: 0px; padding: 0px;">
Front Camera Initialization</h2>
<pre style="background-color: #f7f7f7; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border: 1px solid rgb(221, 221, 221); font-family: 'Courier New', Courier, Monaco, 'Lucida Console', monospace; font-size: 14px; line-height: 1.5em; margin-bottom: 1.5em; margin-top: 1.5em; outline: 0px; overflow: auto; padding: 1em;">gpio 101 -d ho&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - set PWDN_H&nbsp;1=power down,0=active
gpio 109 -d ho&nbsp;1&nbsp;&nbsp;&nbsp; &nbsp; - set CE_H 1=enabled,0=not enabled</pre>
GPIO<br/>
<pre style="background-color: #f7f7f7; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border: 1px solid rgb(221, 221, 221); font-family: 'Courier New', Courier, Monaco, 'Lucida Console', monospace; font-size: 14px; line-height: 1.5em; margin-bottom: 1.5em; margin-top: 1.5em; outline: 0px; overflow: auto; padding: 1em;"><strong style="border: 0px; margin: 0px; outline: 0px; padding: 0px;">I/O Description
</strong> 29 O ??? disable NAND flash write protection on P6 dev 1=disable write prot (FC6050 Parrot platform) fc6050.c
 34 O ??? disable NAND flash write protection on P6 dev 1=disable write prot
 43 O ??? Reset_Wlan 1=reset
 59 O Camera1 (Facing Down) CE 1=enabled,0=not enabled
 63 O Red LED 0=off,1=on
 64 O Green LED 0=off,1=on
 68 O Motor1 /Select 0=selected,1=deselected
 69 O Motor2 /Select 0=selected,1=deselected
 70 O Motor3 /Select 0=selected,1=deselected
 71 O Motor4 /Select 0=selected,1=deselected
 89 ? ??? CAM0_VSYNC
101 O Camera0 (Horizontal) PWDN_H 1=power down,0=active
106 I Motor Cutout
107 O Motor Enable 1=Enable
108 I Reset Button 0=unpressed,1=pressed
109 O Camera0 (Horizontal) CE_H 1=enabled,0=not enabled
127 O USB Connector Pin1 - Vusb
130 O Navboard Connector Pin2 - PGED2
131 O Navboard Connector Pin4 - PGEC2
132 O Navboard Connector Pin6 - /MCLR
158 I Pair Button 0=unpressed,1=pressed</pre>
<h2 style="background-color: white; border: 0px; color: #333333; font-family: Arial, Helvetica, sans-serif; font-size: 25px; font-weight: normal; line-height: 1.1em; margin: 0.5em 0px; outline: 0px; padding: 0px;">
Extension Port Pinout</h2>
<pre style="background-color: #f7f7f7; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border: 1px solid rgb(221, 221, 221); font-family: 'Courier New', Courier, Monaco, 'Lucida Console', monospace; font-size: 14px; line-height: 1.5em; margin-bottom: 1.5em; margin-top: 1.5em; outline: 0px; overflow: auto; padding: 1em;">Pin1 Vusb +5V (USB red)
Pin2 Vbat +11.7
Pin3 USB D- (USB white)
Pin4 RX (Serial data input to Drone)
Pin5 USB D+ (USB green)
Pin6 TX (Serial data output from Drone)
Pin7 GRD (USB black)
Pin8 No Pin</pre>
I2C<br/>
<br/>
/dev/i2c-0<br/>
0×49 Atmel AT73C246 ﻿﻿﻿Power Management and Analog Companions (PMAAC)<br/>
0×50 24C32WI eeprom﻿<br/>
0x5d Bottom camera<br/>
<br/>
/dev/i2c-1<br/>
&nbsp;0×21 Horizontal Camera – OmniVision ov7725<br/>
<br/>
<br/></div>
</div>