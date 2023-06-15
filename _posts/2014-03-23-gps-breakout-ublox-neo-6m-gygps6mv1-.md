---
layout: post
title: GPS breakout - UBLOX NEO 6M - GYGPS6MV1 
categories:
 - GYGPS6MV1
date: 2014-03-23 19:12:00 +0000
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Levou 3 meses para chegar.<br/>
GPS Ublox Neo 6M<br/>
<br/>
<a name="more"></a><br/>
<blockquote class="tr_bq" style="clear: both; text-align: justify;">
<b>UPDATE 22/11/2014:</b><br/>
Novo ucenter 8.12<br/>
<a href="http://www.ublox.com/images/downloads/Product_Docs/u-centersetup_v8.12.zip">http://www.ublox.com/images/downloads/Product_Docs/u-centersetup_v8.12.zip</a></blockquote>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
Precisa de um GPS embarcado?</div>
<div class="separator" style="clear: both; text-align: justify;">
Recomendo o Ublox NEO-6M já montado no breakout GY-GPS6MV1</div>
<div class="separator" style="clear: both; text-align: justify;">
A placa é alimentada com 5V e já possui um LDO para 3.3V.</div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
É preciso presta atenção que a interface serial é de 3.3V e não tolerante a 5V, ou seja, não dá para ligar no Arduino Nano V3 diretamente. Na verdade qualquer microcontrolador com GPIO de 5V vai precisar de um level shift para fazer interface com este módulo.</div>
<div class="separator" style="clear: both; text-align: justify;">
No caso da Stellaris, Tiva C, STM32, FRDM-KL25Z &nbsp;pode conectar direto, pois o GPIO é 3.3V.</div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://1.bp.blogspot.com/-EaVAsrW86z8/Uy8jf0AjMsI/AAAAAAAApfY/v0H_Q9gg2Z8/s1600/IMG_20140323_150910.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-EaVAsrW86z8/Uy8jf0AjMsI/AAAAAAAApfY/v0H_Q9gg2Z8/s1600/IMG_20140323_150910.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">GY-GPS6MV1&nbsp;(Ublox NEO-6M) conectado com o Buspirate<br/>
<div>
<br/></div>
</td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-HAQZgCUUYI8/Uy8gEkC_vgI/AAAAAAAApe4/7PrfyuiLfs4/s1600/GYGPS6MV1-UBLOX-NEO-6M-breakout.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="282" src="http://2.bp.blogspot.com/-HAQZgCUUYI8/Uy8gEkC_vgI/AAAAAAAApe4/7PrfyuiLfs4/s1600/GYGPS6MV1-UBLOX-NEO-6M-breakout.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-GPS6MV1 Breakout</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-3GcvefpKtVY/Uy8gFZMZ2bI/AAAAAAAApfA/STnJYFqqhDs/s1600/GYGPS6MV1-UBLOX-NEO-6M-schematic.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="252" src="http://1.bp.blogspot.com/-3GcvefpKtVY/Uy8gFZMZ2bI/AAAAAAAApfA/STnJYFqqhDs/s1600/GYGPS6MV1-UBLOX-NEO-6M-schematic.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquemático do GY-GPS6MV1 (Ublox NEO-6M)</td></tr>
</tbody></table>
<br/>
<br/>
Vamos ao teardown usando o Buspirate, Putty e ferramentas de software da Ublox.<br/>
<br/>
<b>Resetando o buspirate</b><br/>
<div>
<div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;#</span></div>
<div>
<span style="background-color: #cfe2f3;">RE</span></div>
<div>
<span style="background-color: #cfe2f3;">Bus Pirate v3.5</span></div>
<div>
<span style="background-color: #cfe2f3;">Firmware v6.1 r1676 &nbsp;Bootloader v4.4</span></div>
<div>
<span style="background-color: #cfe2f3;">DEVID:0x0447 REVID:0x3046 (24FJ64GA002 B8)</span></div>
<div>
<span style="background-color: #cfe2f3;">http://dangerousprototypes.com</span></div>
<div>
<span style="background-color: #cfe2f3;">HiZ&gt;</span></div>
<div>
<span style="background-color: #cfe2f3;">HiZ&gt;</span></div>
</div>
<div>
<br/></div>
<div>
<div>
<b>Liga e desliga do 5V e 3.3V</b></div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;w</span></div>
<div>
<span style="background-color: #cfe2f3;">POWER SUPPLIES OFF</span></div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;W</span></div>
<div>
<span style="background-color: #cfe2f3;">POWER SUPPLIES ON</span></div>
<div>
<br/></div>
<div>
<b>Macros para UART</b></div>
<div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;(0)</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;0.Macro menu</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1.Transparent bridge</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2.Live monitor</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;3.Bridge with flow control</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;4.Auto Baud Detection</span></div>
</div>
<div>
<br/></div>
<div>
<b>Detecção automática de baudrate - descobrir o baurd do GPS</b></div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;(4)</span></div>
<div>
<span style="background-color: #cfe2f3;">Waiting activity...</span></div>
<div>
<span style="background-color: #cfe2f3;">Calculated: &nbsp; &nbsp; 9661 bps</span></div>
<div>
<span style="background-color: #cfe2f3;">Estimated: &nbsp; &nbsp; &nbsp;9600 bps</span></div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;</span></div>
</div>
<div>
<br/></div>
<div>
<b>Setup usando o baudrate estimado de 9600 bps</b></div>
<div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;m</span></div>
<div>
<span style="background-color: #cfe2f3;">1. HiZ</span></div>
<div>
<span style="background-color: #cfe2f3;">2. 1-WIRE</span></div>
<div>
<span style="background-color: #cfe2f3;">3. UART</span></div>
<div>
<span style="background-color: #cfe2f3;">4. I2C</span></div>
<div>
<span style="background-color: #cfe2f3;">5. SPI</span></div>
<div>
<span style="background-color: #cfe2f3;">6. 2WIRE</span></div>
<div>
<span style="background-color: #cfe2f3;">7. 3WIRE</span></div>
<div>
<span style="background-color: #cfe2f3;">8. LCD</span></div>
<div>
<span style="background-color: #cfe2f3;">x. exit(without change)</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;3</span></div>
<div>
<span style="background-color: #cfe2f3;">Set serial port speed: (bps)</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1. 300</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2. 1200</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;3. 2400</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;4. 4800</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;5. 9600</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;6. 19200</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;7. 38400</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;8. 57600</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;9. 115200</span></div>
<div>
<span style="background-color: #cfe2f3;">10. BRG raw value</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;5</span></div>
<div>
<span style="background-color: #cfe2f3;">Data bits and parity:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1. 8, NONE *default</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2. 8, EVEN</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;3. 8, ODD</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;4. 9, NONE</span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;</span></div>
<div>
<span style="background-color: #cfe2f3;">Stop bits:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1. 1 *default</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2. 2</span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;</span></div>
<div>
<span style="background-color: #cfe2f3;">Receive polarity:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1. Idle 1 *default</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2. Idle 0</span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;</span></div>
<div>
<span style="background-color: #cfe2f3;">Select output type:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;1. Open drain (H=Hi-Z, L=GND)</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;2. Normal (H=3.3V, L=GND)</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;">(1)&gt;2</span></div>
<div>
<span style="background-color: #cfe2f3;">Ready</span></div>
<div>
<br/></div>
<div>
<b>Ativar macro para bridge transparente</b></div>
<div>
<span style="background-color: #cfe2f3;">UART&gt;(1)</span></div>
<div>
<span style="background-color: #cfe2f3;">UART bridge</span></div>
<div>
<span style="background-color: #cfe2f3;">Reset to exit</span></div>
<div>
<span style="background-color: #cfe2f3;">Are you sure? y</span></div>
<div>
<br/></div>
<div>
<b>Dados recebidos do GPS - padrão NMEA</b></div>
<div>
<span style="background-color: #cfe2f3;">$GPRMC,,V,,,,,,,,,,N*53</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPVTG,,,,,,,,,N*30</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGGA,,,,,,0,00,99.99,,,,,,*48</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGSV,1,1,03,09,,,17,11,,,20,12,,,22*74</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGLL,,,,,,V,N*64</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPRMC,,V,,,,,,,,,,N*53</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPVTG,,,,,,,,,N*30</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGGA,,,,,,0,00,99.99,,,,,,*48</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGSV,1,1,02,11,,,17,12,,,19*76</span></div>
<div>
<span style="background-color: #cfe2f3;">$GPGLL,,,,,,V,N*64</span></div>
<div>
<br/></div>
</div>
</div>
<div>
<br/>
<br/>
<br/>
$GPVTG,,T,,M,0.126,N,0.233,K,A*24<br/>
<br/>
$GPGGA,023622.00,0801.83890,S,03453.84015,W,1,05,4.58,67.3,M,-10.4,M,,*48<br/>
<br/>
$GPGSA,A,3,18,21,22,27,16,,,,,,,,5.81,4.58,3.58*01<br/>
<br/>
$GPGSV,4,1,15,03,48,198,35,14,45,354,18,15,17,136,,16,20,250,33*7A<br/>
$GPGSV,4,2,15,18,44,181,33,21,36,153,27,22,48,243,38,24,07,081,19*7C<br/>
$GPGSV,4,3,15,25,08,017,19,27,10,213,32,29,46,048,20,31,05,333,*7D<br/>
$GPGSV,4,4,15,33,65,05,333,*7D<br/>
$GPGSV,4,4,15,33,65,068,29,37,25,084,29,39,22,085,29*43<br/>
<br/>
$GPGLL,0801.83886,S,03453.84014,W,023623.00,A,A*6C<br/>
<br/>
$GPRMC,023624.00,A,0801.83910,S,03453.84059,W,0.811,,221114,,,A*78<br/>
<br/>
<br/>
<br/>
$GPVTG,,T,,M,0.811,N,1.502,K,A*2D<br/>
$GPGGA,023624.00,0801.83910,S,03453.84059,W,1,05,4.57,67.6,M,-10.4,M,,*45<br/>
$GPGSA,A,3,18,21,22,27,16,,,,,,,,5.81,4.57,3.58*0E<br/>
$GPGSV,4,1,15,03,48,198,36,14,45,354,21,15,17,136,,16,20,250,34*74<br/>
$GPGSV,4,2,15,18,44,181,33,21,36,153,26,22,48,243,39,24,07,081,20*76<br/>
$GPGSV,4,3,15,25,08,01243,39*7B<br/>
$GPGSV,4,3,16,24,07,081,,25,08,017,,27,10,213,32,29,46,048,25*7F<br/>
$GPGSV,4,4,16,31,05,333,19,33,65,068,29,37,25,084,30,39,22,085,29*74<br/>
$GPGLL,0801.83909,S,03453.84060,W,023625.00,A,A*6F<br/>
$GPRMC,023626.00,A,0801.83897,S,03453.84052,W,0.194,,221114,,,A*7B<br/>
<br/>
$GPVTG,,T,,M,0.194,N,0.360,K,A*2A<br/>
$GPGGA,023626.00,0801.83897,S,03453.84052,W,1,05,4.57,67.5,M,-10.4,M,,*41<br/>
$GPGSA,A,3,18,21,22,27,16,,,,,,,,5.80,4.57,3.58*0F<br/>
$GPGSV,4,1,16,03,48,198,35,08,,,25,14,45,354,,15,17,136,*4D<br/>
$GPGSV,4,2,16,16,20,255,17,136,18*45<br/>
$GPGSV,4,2,16,16,20,250,35,18,44,181,32,21,36,153,27,22,48,243,40*75<br/>
$GPGSV,4,3,16,24,07,081,21,25,08,017,,27,10,213,32,29,46,048,22*7B<br/>
$GPGSV,4,4,16,31,05,333,20,33,65,068,28,37,25,084,28,39,22,085,28*77<br/>
$GPGLL,0801.83895,S,03453.84051,W,023627.00,A,A*6B<br/>
$GPRMC,023628.00,A,0801.83895,S,03453.84048,W,0.197,,221114,,,A*7F<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>
<div>
A família NEO-6M foi descontinuada para dar lugar a novos modelos, isso é bom pois fica mais barato para comprar os que sobraram no mercado chinês.</div>
<div>
Mesmo com a sensibilidade de -162 dBm, não consegui usar em ambiente fechado. Até encontra 10 satélites mas não consegue fazer o fix nem 2d e nem 3d.</div>
<div>
Se ficar do lado da janela já da para fazer o fix 2d e 3d.</div>
<div>
A céu aberto é o fix 2d e 3d leva menos de 10 segundos.</div>
<div>
<br/></div>
<div>
Página legada do NEO-6M</div>
<div>
<div>
http://www.u-blox.com/en/gps-modules/pvt-modules/previous-generations/neo-6-family.html</div>
</div>
<div>
<ul style="background-color: #e3e4e6; clear: both; color: #333333; font-family: Arial, Tahoma, sans-serif; font-size: 12px;">
<li>u-blox 6 position engine:</li>
<ul style="clear: both;">
<li>Navigate down to –162 dBm and –148 dBm coldstart</li>
<li>Faster acquisition with AssistNow Autonomous</li>
<li>Configurable power management</li>
<li>Hybrid GPS/SBAS engine (WAAS, EGNOS, MSAS)</li>
<li>Anti-jamming technology</li>
</ul>
<li>Simple integration with u-blox wireless modules</li>
<li>A-GPS: AssistNow Online and AssistNow Offline services, OMA SUPL compliant</li>
<li>Backward compatible (hardware and firmware); easy migration from NEO-5 family or NEO-4S</li>
<li>LCC package for reliable and cost effective manufacturing</li>
<li>Compatible with u-blox GPS Solution for Android</li>
<li>Based on GPS chips qualified according to AEC-Q100</li>
<li>Manufactured in ISO/TS 16949 certified sites</li>
<li>Qualified according to ISO 16750</li>
</ul>
</div>
<div>
Ferramenta U-Center da U-Blox para GPS</div>
<div>
https://www.u-blox.com/en/evaluation-tools-a-software/u-center/u-center.html</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-0RXS9zjIq4o/Uy8vp5999ZI/AAAAAAAApfw/c4cOxUhPSh8/s1600/u-center.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="167" src="http://3.bp.blogspot.com/-0RXS9zjIq4o/Uy8vp5999ZI/AAAAAAAApfw/c4cOxUhPSh8/s1600/u-center.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">U-center conectado no GPS através do Buspirate.<br/>
O Baudrate entre o GPS e buspirate é 9600 bps.<br/>
Entre o buspirate e o U-center é 115200 bps.</td></tr>
</tbody></table>
<div>
<br/></div>
<div>
<br/></div>
</div>