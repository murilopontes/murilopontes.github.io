---
layout: post
title: ardrone v1 teardown - hardware / sofware / firmware
categories:
 - post
date: 2013-12-04 13:38:00 +0000
---

Coletando informações para facilitar a engenharia reversa  

  

<a name="more"></a>  
  

# Linux 2.6.27.47 + BusyBox v1.14.0 + gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203)  

  

# Main board  

Parrot 6 ARM9 468 MHz 32-bit processor - [ARM926EJ-S rev 5 (v5l) - BogoMIPS: 233.47]  

Atheros AR6102G-BM2D b/g Wi-Fi module  

Micron OGA17 D9HSJ (128MB FLASH)  

Micron 29F1G08AAC (128MB RAM)  

Horizontal camera 640x480 (OmniVision ov7725 ) - I2C - /dev/video0  

Vertical camera 176x144 (cresyn qcif) - I2C - /dev/video1  

Atmel AT73C246 ﻿﻿﻿Power Management and Analog Companions (PMAAC) - I2C  

ON Semiconductor CAT24C32WI eeprom﻿ (4KB) - I2C  

  

segundo http://www.clifton.nl/index.html?bogomips.html  

este processador é equivalente ao Pentium II/233,Cyrix 6x86MII/233 P300,AMD K5/116 PR166  

em termos de desempenho.  

  

# Navigation board (via /dev/ttyPA2)  

Microchip PIC24HJ16GP304 (16-bit-RISC-40MHZ 2KB-RAM 16KB-FLASH &nbsp;12-bit-ADC)  

Invensense IDG 500 (XY-axis gyroscope)  

Epson XV-3500CB (Z-axis gyroscope)  

Bosh BMA150 (3-axis accelerometer)  

Ultrasom (depois de muitos testes a média de detecção empírica é entre 24 cm e 423 cm )  

  

# ESC boards (via /dev/ttyPA1)  

ESC ATmega8a (8-bit-RISC-16MHz 1KB-RAM 8KB-FLASH 10-bit-ADC).  

28,000 RPM hovering  

41,400 RPM full acceleration.  

  

#  

bateria Lipo 1000mAh 3S1P 11.1v - 12 minutos de vôo / 90 minutos de carga  

  

  

Potência consumida total de 15Watt, corrente máxima consumida ~3A.  

Velocidade máxima 5 m/s ou 18 km/h ou 11 mph  

Autonomia com a bateria padrão de até 3,6 km ou 12 minutos.  

Camera frontal: VGA, 93° lens, 30 frame/s (v4l-utils detecta somente 25fps)  

Camera vertical: QCIF, 64° lens, 60 frame/s (v4l-utils detecta somente 25fps)  

  

O processador também possui um acelerador de compressão de vídeo P264 em HW,  

acessível através do &nbsp;/dev/p264_p6