---
layout: page
title: Drone- MCU, IMU, GPS e WiFi
categories:
 - page
date: 2016-07-31 20:00:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
MCU (ARM Cortex-M) ou CPU (ARM Cortex-A): o custo é praticamente o mesmo. A diferença é praticamente quantidade de memória externa.<br/>
<br/>
Usando um MCU provavelmente a melhor escolha é usar um RTOS como o FreeRTOS ou o Nuttx.<br/>
O FreeRTOS é bem simples, digamos que ele tem somente 3 arquivos de código fonte.<br/>
O Nuttx é praticamente um Linux em miniatura.<br/>
Também existe a possibilidade de não usar nenhum sistema ou RTOS, e programar no "bare-metal" fazendo máquinas de estado complexas que nem sempre tem o resultado desejado.<br/>
<br/>
Como exemplo de sistemas bare-metal temos o Multiwii (nos Atmega) e o Baseflight (nos STM32).<br/>
Como exemplo de sistemas que usam RTOS temos o OpenPilot (com FreeRTOS) e o PX4 Autopilot (com Nuttx) ambos rodando em MCUs STM32.<br/>
Como exemplo de sistemas que usam Linux temos o Ardrone v1 (arm926ej-s) e Ardrone v2 (omap cortex-a8).<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-DuHPzsly5Ek/VFOdyRx1oHI/AAAAAAAAtiQ/gnRfuh52M5w/s1600/stm32f429i.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="160" src="https://2.bp.blogspot.com/-DuHPzsly5Ek/VFOdyRx1oHI/AAAAAAAAtiQ/gnRfuh52M5w/s1600/stm32f429i.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">STM32f429i-disco : Cortex-M4F com 256kb ram e 2048kb flash + 8mb sdram&nbsp;+ lcd<br/>
Funciona com Nuttx ou ucLinux</td></tr>
</tbody></table>
<a href="http://www.aliexpress.com/item/STM32F429I-DISCO-STM32F4-Discovery-with-touch-screen-STM32F429ZIT6-STM32-ARM-Evaluation-Development-Board-Embedded-ST-LINK/1632521166.html">http://www.aliexpress.com/item/STM32F429I-DISCO-STM32F4-Discovery-with-touch-screen-STM32F429ZIT6-STM32-ARM-Evaluation-Development-Board-Embedded-ST-LINK/1632521166.html</a><br/>
<br/>
<br/>
IMU (sistema de navegação) ou MARG (array de sensores): a diferença aqui fica por conta do processamento dos sensores. Uma IMU engloba os sensores (MARG) e os algoritmos para estimativa de orientação.<br/>
<br/>
Como exemplo de MARG temos o GY-86 que é um array de sensores 10 dof, composto por um acelerômetro (3 dof), giroscópio (3dof), magnetômetro (3dof), barômetro (1dof). Quando usamos este MARG com algoritmo algoritmo de orientação, temos uma IMU 10 dof. Um projeto muito bom é o FreeIMU, que implementa uma IMU 10 dof, ferramentas de calibração e um teste de orientação com um cubo 3d.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-h--1dMqGfTk/VFObup4MlLI/AAAAAAAAtiE/OKlVKFadn2w/s1600/gy86.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="184" src="https://4.bp.blogspot.com/-h--1dMqGfTk/VFObup4MlLI/AAAAAAAAtiE/OKlVKFadn2w/s1600/gy86.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-86 MARG 10 DOF<br/>
Melhor do que arrancar os sensores do seu smartphone</td></tr>
</tbody></table>
<a href="http://www.aliexpress.com/item/GY-86-10DOF-BMP085-Module-MS5611-HMC5883L-MPU6050-Module-MWC-Flight-Control-Sensor-Module-Free-Shipping/602122957.html">http://www.aliexpress.com/item/GY-86-10DOF-BMP085-Module-MS5611-HMC5883L-MPU6050-Module-MWC-Flight-Control-Sensor-Module-Free-Shipping/602122957.html</a><br/>
<br/>
<br/>
<br/>
GPS: localização global com boa precisão só com GPS. A FreeIMU 10DOF fornece a orientação 3d, mas não fornece a localização. É possível até estimar a posição relativa integrando 2 vezes o acelerômetro, mas a precisão deixa a desejar. Existe a possibilidade de estimar a posição usar o fluxo ótico das câmeras.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-r2Fr7J9BsSE/VFo8uetxBHI/AAAAAAAAtlA/VvjpiNrEF30/s1600/gps.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="140" src="https://2.bp.blogspot.com/-r2Fr7J9BsSE/VFo8uetxBHI/AAAAAAAAtlA/VvjpiNrEF30/s1600/gps.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-GPS6MV1 pronto para seguir os pontos no mapa</td></tr>
</tbody></table>
<br/>
<a href="http://www.aliexpress.com/item/Free-Shipping-NEO-6M-Ublox-u-blox-GPS-Module-for-MWC-AeroQuad-Flight-Control-Board/1211036215.html">http://www.aliexpress.com/item/Free-Shipping-NEO-6M-Ublox-u-blox-GPS-Module-for-MWC-AeroQuad-Flight-Control-Board/1211036215.html</a><br/>
<br/>
<br/>
<br/>
Sonar: Altitude e distância até 5 metros. É muito útil para auxilar no pouso automático. Como o Barômetro só informa a altitude relativa, é sempre com ter um sonar para inicializar ou ajudar na hora do pouso.<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-oDWBjYFscGQ/VFo9ugkyB-I/AAAAAAAAtlI/JMAn2KcD-xs/s1600/sonar.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="202" src="https://4.bp.blogspot.com/-oDWBjYFscGQ/VFo9ugkyB-I/AAAAAAAAtlI/JMAn2KcD-xs/s1600/sonar.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">HC-SR04 de 2cm a 450cm</td></tr>
</tbody></table>
<br/>
<br/>
<a href="http://www.aliexpress.com/item/1pcs-Ultrasonic-Module-HC-SR04-Distance-Measuring-Transducer-Sensor-for-Arduino-HC-SR04-HCSR04/558618295.html">http://www.aliexpress.com/item/1pcs-Ultrasonic-Module-HC-SR04-Distance-Measuring-Transducer-Sensor-for-Arduino-HC-SR04-HCSR04/558618295.html</a><br/>
<br/>
WiFi ou RF: este é um tema polêmico. RF é um clássico em projetos de RC. Cada um implementa do seu jeito, e na maioria dos casos não existe um conceito de rede. Com WiFi temos uma tecnologia padronizada e presente em todos os lugares, tem um conceito de rede e protocolos bem definidos, além de capacidade suficiente para transmitir vídeo HD ao vivo , telemetria, joystick, ...<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-mrO90xtNhtk/VFOa3hp6BrI/AAAAAAAAth8/qPHrIo_rgVM/s1600/esp8266.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="225" src="https://2.bp.blogspot.com/-mrO90xtNhtk/VFOa3hp6BrI/AAAAAAAAth8/qPHrIo_rgVM/s1600/esp8266.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">ESP8266 WiFi para IoT por menos de 5 dólares. Como direito a WiFi, serial e gpio em um soc Xtensa.<br/>
Tem SDK com GCC e tudo mais.</td></tr>
</tbody></table>
<a href="http://www.aliexpress.com/item/Free-shipping-ESP8266-serial-WIFI-wireless-module-wireless-transceiver/2031529724.html">http://www.aliexpress.com/item/Free-shipping-ESP8266-serial-WIFI-wireless-module-wireless-transceiver/2031529724.html</a><br/>
<br/>
<br/>
<br/></div>