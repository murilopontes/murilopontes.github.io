---
layout: post
title: Transformando Stellaris / Tiva em Quadcopter / Hexacopter 
categories:
 - Ublox NEO-6M
date: 2014-03-23 01:12:00 +0000
---

<div class="separator" style="clear: both; text-align: left;">
<span style="text-align: justify;">Como transformar uma Stellaris ou Tiva&nbsp;em Quadcopter e Hexacopter?</span></div>

<div class="separator" style="clear: both; text-align: left;">
É simples, basta ligar todos os sensores, programar e voar.</div>

<div class="separator" style="clear: both; text-align: justify;">
</div>

<a name="more"></a>  
  

<div class="separator" style="clear: both; text-align: justify;">
Para programar é só usar o projeto Energia (http://www.energia.nu) com esta IDE toda API do Arduino ficou disponível para as placas Stellaris, Tiva e outras launchpads com MSP430.</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
O software para controlar o Quadcopter ou Hexacopter pode ser o Multi Wii Copter (MWC)</div>

<div class="separator" style="clear: both; text-align: justify;">
http://www.multiwii.com/connecting-elements</div>

<div class="separator" style="clear: both; text-align: justify;">
Alguma modificações são necessárias pois o MWC tem como plataforma os microcontroladores AVR.</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
O Hardware proposto está simplificado nas figuras que seguem, a ferramenta para criar placas, esquemáticos e figuras dos projetos é o Fritzing.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
http://fritzing.org/</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-M-fNAwYiPWQ/Uy4w2hH9iHI/AAAAAAAApdU/3TL2uGqeFWA/s1600/bootspack-tiva-murix-quad_bb.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="484" src="http://4.bp.blogspot.com/-M-fNAwYiPWQ/Uy4w2hH9iHI/AAAAAAAApdU/3TL2uGqeFWA/s1600/bootspack-tiva-murix-quad_bb.png" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema do Hexacopter simplificado para Quadcopter<br/>
<br/></td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://2.bp.blogspot.com/-Fn10EP-qmXI/Uy430DAY_KI/AAAAAAAApeA/YjwGR0P85Es/s1600/IMG_20140322_222233.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-Fn10EP-qmXI/Uy430DAY_KI/AAAAAAAApeA/YjwGR0P85Es/s1600/IMG_20140322_222233.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">Hardware para montar o Quadcopter<br/>
<br/>
PCB Universal 9 cm x 15 cm<br/>
Headers Male<br/>
Headers Female<br/>
Resistores para ADC,...<br/>
Capacitores, ...<br/>
Diodos 1N4007,...<br/>
Tiva C Series: ARM Cortex-M4F 32KB RAM 256KB FLASH (RTOS)<br/>
Air Boost Pack: rádio até 300 metros<br/>
JY-MCU Bluetooth: debug por serial até 2 metros<br/>
BMP085 (Barômetro): manter altitude até 10 km<br/>
HMC5883L (Magnetômetro): manter o norte<br/>
MPU6050 (Giroscópio e acelerômetro): manter estabilizado<br/>
HC-SR04 (Sonar): altitude até 5 metros usado para pousar.<br/>
Ublox Neo-6M (GPS): manter rota e posição<br/>
ESCs<br/>
Motores<br/>
Hélices<br/>
Frame<br/>
Baterias<br/>
Carregador de bateria<br/>
Notebook com bluetooth e joystick de Xbox ou Playstation</td></tr>
</tbody></table>

  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-aAmDIpgrevk/Uy4w5n_GMXI/AAAAAAAApdc/OxzYBMcFjH0/s1600/bootspack-tiva-murix-hexacopter_bb.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://3.bp.blogspot.com/-aAmDIpgrevk/Uy4w5n_GMXI/AAAAAAAApdc/OxzYBMcFjH0/s1600/bootspack-tiva-murix-hexacopter_bb.png" width="630"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema do hexacopter</td></tr>
</tbody></table>

  