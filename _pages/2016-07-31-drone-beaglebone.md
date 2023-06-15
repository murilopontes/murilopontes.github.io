---
layout: page
title: Drone- Beaglebone
categories:
 - page
date: 2016-07-31 19:42:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: center;">
<div style="text-align: justify;">
<span style="text-align: left;">Este é um dos meus projetos pessoais, que tem por finalidade implementar um Drone usando uma BeableboneBlack (BBB) e outras ferramentas de hardware e software opensource.</span></div>
<div style="text-align: justify;">
<br/></div>
Playlist dos experimentos com o Beaglebone Drone</div>
<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/videoseries?list=PLB_uIxBF0dCfkxBKF0ukLEwJ7IEpnvEXI" width="560"></iframe>
</div>
<div style="text-align: center;">
<br/></div>
<div>
</div>
<div style="text-align: center;">
Playlist testando 15 modelos de hélices no Beaglebone Drone e medindo o consumo de corrente<br/>
(<a href="http://dronespersonalizados.blogspot.com.br/2014/12/consumo-de-corrente-em-15-modelos-de.html">http://dronespersonalizados.blogspot.com.br/2014/12/consumo-de-corrente-em-15-modelos-de.html</a>)</div>
<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/videoseries?list=PLB_uIxBF0dCe1DDbgFvizunAutcuvVoQ4" width="560"></iframe>
</div>
<div style="text-align: center;">
<br/></div>
<br/>
<br/>
1) Introdução<br/>
<br/>
Porque desenvolver um Drone / UAV / VANT do zero, se já existem vários prontos como o Ardrone?<br/>
Pelo fato que entre a teoria e a prática existe um enorme diferença.<br/>
Qualquer um pode verificar este fato com o mínimo de pesquisa.<br/>
Basta tentar seguir um modelo teórico para iniciar um experimento prático para verificar que faltam tantos detalhes que seria necessário escrever outra teoria.<br/>
<br/>
Porque usar a Beaglebone para&nbsp;desenvolver&nbsp;um&nbsp;Drone / UAV / VANT?<br/>
Por ser uma plataforma aberta e 100% customizável.<br/>
Outra vantagem é o hardware, a Beaglebone possui 2 coprocessadores de tempo-real (PRU) que executam instruções com tempo fixo de 5 ns por instrução, isto permitir criar funcionalidades que só seriam possíveis com um FPGA.<br/>
<br/>
2) Modelo teórico<br/>
<br/>
Uma IMU é usada para obter a posição, orientação e velocidade (feedbacks).<br/>
O joystick é usado para configurar a posição, orientação e altitude (targets).<br/>
São usados 4 controladores PID para regular as velocidades.<br/>
São usados 3 controladores PID para regular os ângulos.<br/>
Um controlador PID para controlar altitude.<br/>
Dois controladores PID para controlar a posição.<br/>
Os motores são ajustados pelos PIDs (actuators).<br/>
Se todos os sensores e PIDs estiverem calibrados corretamente o drone irá voar estável.<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-7CbsM4MlU9U/VKflB8YgEfI/AAAAAAAAugg/v6aqtB32Yo0/s1600/quadcopter.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="200" src="https://2.bp.blogspot.com/-7CbsM4MlU9U/VKflB8YgEfI/AAAAAAAAugg/v6aqtB32Yo0/s1600/quadcopter.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Diagrama em blocos do Beaglebone Drone</td></tr>
</tbody></table>
<br/>
<br/>
3) Modelo prático<br/>
<br/>
3.1) Lista de material<br/>
<ul>
<li>Uma placa BeagleBoneBlack de preferência revisão C</li>
<li>Um placa GY-86: IMU 10DOF via I2C (inclui os sensores MPU6050,HMC5883,MS5611)</li>
<li>Um GPS para localização global, no caso usei o Ublox Neo6M</li>
<li>Um WiFi USB - para se comunicar com PC/Notebook/Android.</li>
<li>Um quadro/frame, no caso usei o Turnigy Talon v1 (feito de fibra de carbono).</li>
<li>4 x ESCs, no caso usei o modelo Hobbywing FlyFun 30A</li>
<li>4 x Motores brushless, no caso usei o mdelo A2212/13T 1000Kv</li>
<li>2 hélices CW e 2 hélices CCW - o usei os tamanhos: 8x4.5 (boa), 9x5 (boa),&nbsp;10x4.5 (ótimo).</li>
<li>Bateria de Lipo - usei uma ZOP Power 2200mah 30C&nbsp;</li>
<li>Um PCB universal, fios, parafusos e solda para fazer as conexões</li>
<li>Conectores banana, XT60, T-Deans e outros para fazer conexões elétricas&nbsp;</li>
<li>Um Bluetooth USB - para controlar o drone diretamente com joystick do PS3 sem PC ou notebok até 10 metros.</li>
<li>Rádio CC1101 433MHz / 915MHz para telemetria até 400 metros</li>
<li>Rádio Xbee 2.4 GHz para telemetria até 2 Km</li>
</ul>
<div>
3.2) Esquemático elétrico / manual de montagem</div>
<div>
<div>
<br/>
Ordem das conexões:<br/>
0) ligar fonte chaveada (LM2596S) DC-DC no 5V TPS-IN</div>
<div>
1) ligar o barramento GND e 5V TPS-OUT dos sensors/gps/bluetooth/xbee/cc1101<br/>
2) ligar o GY-86 no i2c-2<br/>
3) ligar o HC-06 no J1<br/>
4) ligar o GPS na uart4<br/>
5) ligar os ESCs na PRU0<br/>
6) ligar o divisor de tensão 1K/10K no ADC (para medir no máximo 18V)<br/>
7) ligar dongle bluetooth no USB Host, e parear com joystick do Playstation 3 ou<br/>
7) ligar dongle wifi no USB Host, e usar aplicativo enviador de controle de Xbox.</div>
<div>
8) ligar CC1101 na SPI0<br/>
9) ligar XBee na USART1 ou USART5<br/>
<br/>
<div class="separator" style="clear: both; text-align: center;">
</div>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-9qdmW-x8MdY/VN9xLhWtpqI/AAAAAAAAu18/W6Demtj8wrc/s1600/Capture.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="167" src="https://1.bp.blogspot.com/-9qdmW-x8MdY/VN9xLhWtpqI/AAAAAAAAu18/W6Demtj8wrc/s1600/Capture.PNG" width="400"/></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<br/></div>
<div>
</div>
<div>
<div class="separator" style="clear: both; text-align: center;">
</div>
</div>
</div>
<div>
<div>
3.3) Resultado da montagem<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-PdIOtzoi-5U/U7LNfaRgkZI/AAAAAAAAsCY/ZMi2wE1Rang/s1600/IMG_20140701_120206.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="https://4.bp.blogspot.com/-PdIOtzoi-5U/U7LNfaRgkZI/AAAAAAAAsCY/ZMi2wE1Rang/s1600/IMG_20140701_120206.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">Drone pesando 983 gramas no total (incluindo a bateria)</td></tr>
</tbody></table>
3.4) Software</div>
<br/>
Página de suporte ao Debian na Beaglebone Black<br/>
<a href="http://elinux.org/Beagleboard:BeagleBoneBlack_Debian">http://elinux.org/Beagleboard:BeagleBoneBlack_Debian</a><br/>
<br/>
<br/>
linux-image-3.8.13-bone70 &nbsp;=&gt; ok capemgr<br/>
linux-image-3.13.11-bone12 =&gt;<br/>
linux-image-3.14.17-bone8<br/>
linux-image-3.15.10-bone8<br/>
linux-image-3.16.3-bone6 <br/>
linux-image-3.17.2-bone5 <br/>
linux-image-3.18.5-bone1 <br/>
linux-image-3.19.0-bone3 &nbsp;=&gt; sem capemgr<br/>
<div>
<br/></div>
<br/>
# 2014-12-19<br/>
* Debian 7.7<br/>
* atualizado com kernel 3.8.3 bone 68<br/>
* GCC 4.6.3<br/>
<br/>
<a href="https://rcn-ee.net/rootfs/bb.org/testing/2014-12-19/lxde/BBB-eMMC-flasher-debian-7.7-lxde-armhf-2014-12-19-2gb.img.xz">https://rcn-ee.net/rootfs/bb.org/testing/2014-12-19/lxde/BBB-eMMC-flasher-debian-7.7-lxde-armhf-2014-12-19-2gb.img.xz</a><br/>
<br/>
# 2014-05-14<br/>
* Primeira imagem oficial do Debian 7.5 para Beaglebone<br/>
<br/>
<a href="https://rcn-ee.net/deb/testing/2014-05-14/BBB-eMMC-flasher-debian-7.5-2014-05-14-2gb.img.xz">https://rcn-ee.net/deb/testing/2014-05-14/BBB-eMMC-flasher-debian-7.5-2014-05-14-2gb.img.xz</a><br/>
<a href="https://rcn-ee.net/deb/testing/2014-05-14/bone-debian-7.5-2014-05-14-2gb.img.xz">https://rcn-ee.net/deb/testing/2014-05-14/bone-debian-7.5-2014-05-14-2gb.img.xz</a><br/>
<br/>
Toolchain Linaro - http://www.linaro.org/downloads/<br/>
Testado a versão 14.09<br/>
<a href="http://releases.linaro.org/14.09/components/toolchain/binaries/gcc-linaro-arm-linux-gnueabihf-4.9-2014.09-20140911_win32.exe">http://releases.linaro.org/14.09/components/toolchain/binaries/gcc-linaro-arm-linux-gnueabihf-4.9-2014.09-20140911_win32.exe</a><br/>
<br/>
O software de controle para Desktop<br/>
1) Plot dos sensores<br/>
2) Plot 3d da orientação calculada pela IMU<br/>
3) Envio do controle de Xbox em formato JSON<br/>
4) Recebimento de telemetria JSON<br/>
<br/>
O software de controle para Beaglebone é composto de 8 threads:<br/>
1) Os quatros PWM de 400 Hz são gerados na PRU da Beaglebone com steps de 5ns.<br/>
2) IMU GY-86 10 DOF com filtro completar ( MPU6050 , HMC5883L, MS5611 )<br/>
3) Ethernet e WiFi para telemetria JSON e joystick de Xbox JSON<br/>
4) Bluetooth usando dongle USB e joystick de PS3<br/>
5) Radio CC1101 433 MHz &nbsp;com interface TAP<br/>
6) GPS Ublox Neo-6M funcionando com o daemon gpsd<br/>
<div>
7) Monitor de bateria usando ADC<br/>
8) Piloto automático usando PIDs, limitador de motor baseado em uso da bateria<br/>
<br/>
Uma parte do código está no meu Github<br/>
<ul style="text-align: left;">
<li><a href="https://github.com/murix/bbb-quad">https://github.com/murix/bbb-quad</a></li>
</ul>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-A3kNetE34QA/VJyrBDm-iAI/AAAAAAAAueU/GBPiDXgcJHY/s1600/beaglebone-app.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="190" src="https://1.bp.blogspot.com/-A3kNetE34QA/VJyrBDm-iAI/AAAAAAAAueU/GBPiDXgcJHY/s1600/beaglebone-app.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><div style="font-size: medium;">
Aplicativo desktop de para enviar o JSON do joystick e receber o JSON da telemetria</div>
</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-_wpwtSLRBxk/VKhbCjPfsAI/AAAAAAAAug0/e03O9RbL_9M/s1600/beaglebonedrone-debug.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="215" src="https://1.bp.blogspot.com/-_wpwtSLRBxk/VKhbCjPfsAI/AAAAAAAAug0/e03O9RbL_9M/s1600/beaglebonedrone-debug.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Debug remoto do piloto automático da Beaglebone usando Eclipse CDT &nbsp;com &nbsp;GDB via SSH&nbsp;</td></tr>
</tbody></table>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-dQ94pkqm5gk/VJdsKcNB6RI/AAAAAAAAubw/qW9mOEZ3Wbk/s1600/thread-name.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="245" src="https://1.bp.blogspot.com/-dQ94pkqm5gk/VJdsKcNB6RI/AAAAAAAAubw/qW9mOEZ3Wbk/s1600/thread-name.PNG" width="400"/></a></div>
</td></tr>
<tr><td class="tr-caption" style="text-align: center;">Uso da CPU em cada thread do piloto</td></tr>
</tbody></table>
<div>
<div>
3.5) Resultados do experimento de consumo de energia</div>
<div>
<br/></div>
<div>
Fontes de corrente:</div>
<div>
<ul>
<li>BBB 3V3: 250mA</li>
<li>BBB 5V_SYS: 250mA&nbsp;</li>
<li>BBB 5V_VDD: 1000mA (Trilha que passa direto do AC para os pinos das CAPES)</li>
<li>Bateria Lipo 3S1P 2200mAh 30C: 12V @&nbsp;66A = &nbsp;792W</li>
<li>Fonte de PC: 12V&nbsp;@ 8A = 96W</li>
</ul>
</div>
<div>
<br/>
Consumidores de corrente:</div>
</div>
<div>
<ul>
<li>Ublox Neo-6M GPS: 67mA&nbsp;@ 3.3V</li>
<li>Motor A2212/13T 1000Kv: 12A por motor, 48A @&nbsp;12V = 576W (máximo teórico)</li>
<li>BBB+sensores+motores parados: 260mA&nbsp;@ 12V = 3W</li>
<li>BBB+sensores+motores com hélices 10x4,5 no máximo = 32A&nbsp;@ 12V = 384W</li>
</ul>
<div>
<br/>
Consumo de corrente por tamanho de hélice em cada motor A2212/13T 1000kv:<br/>
<ul>
<li>5x5e: pico em 2,36A - estável em 2,33A - empuxo fraco</li>
<li>6x3e: pico em 2,65A - estável em 2,55A - empuxo fraco</li>
<li>6x4: pico em 2,96A - estável em 2,80A - empuxo fraco</li>
<li>7x4hy: estável em 4,04A - empuxo fraco</li>
<li>7x4.5e: pico em 5,78A - estável em 5,06A - empuxo fraco</li>
<li>7x5: pico 5.02A - estável em 4,74A - empuxo fraco</li>
<li>8x4 slow: pico em 5,11 - estável em 4,80A - empuxo fraco</li>
<li>8x4 hy: estável em 4,81A - empuxo fraco</li>
<li>8x4.5: pico em 6,15A - estável em 4,90A - empuxo fraco</li>
<li>8x6 gemfan: pico em 5,86A - estável em 5,05A - empuxo fraco</li>
<li>9x3.8sf: pico em 5,66A - estável em 5,07A - empuxo fraco</li>
<li>9x5: pico em 5,75A - estável em 4,60A - empuxo fraco</li>
<li>9x5 gemfan: pico em 6,15A - estável em 5,10A - empuxo fraco</li>
<li>10x4.5: pico em 7,58A - estável em 5,24A - empuxo suficiente para levantar o drone</li>
<li>10x6 gemfan: 8,38A - estável em 7,36A - empuxo fraco</li>
</ul>
<br/>
<br/></div>
</div>
</div>
</div>
<div>
<br/></div>
</div>