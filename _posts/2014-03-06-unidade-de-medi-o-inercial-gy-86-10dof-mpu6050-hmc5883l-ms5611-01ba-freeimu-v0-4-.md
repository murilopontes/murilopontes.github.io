---
layout: post
title: Unidade de Medição Inercial GY-86 10DOF (MPU6050/HMC5883L/MS5611-01BA) FreeIMU v0.4  
categories:
 - level shift
date: 2014-03-06 04:49:00 +0000
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: left;">
<span style="font-family: inherit;"><b style="background-color: white; line-height: 19.2000007629395px;">inertial measurement unit (IMU) </b><b style="line-height: 19.200000762939453px;">- &nbsp; </b><span style="line-height: 19.200000762939453px;">é o hardware&nbsp;responsável por medir a velocidade, orientação, forças gravitacionais que aguem sobre o drone.</span></span><span style="font-family: inherit; line-height: 19.2000007629395px;">&nbsp;</span><br/>
<a name="more"></a><span style="font-family: inherit; line-height: 19.2000007629395px;">Basicamente todos os dispositivos IMU possuem&nbsp;acelerômetros,&nbsp;giroscópios e magnetômetros. As versões&nbsp;estendidas também incluem&nbsp;barômetro</span><span style="font-family: inherit; line-height: 19.2000007629395px;">&nbsp;e GPS.</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;"><span style="line-height: 19.200000762939453px;">A parte mais importante de uma IMU são os&nbsp;giroscópios&nbsp;pois todas&nbsp;estratégias</span><span style="line-height: 19.200000762939453px;">&nbsp;de estabilização de uma aeronave passam por&nbsp;anular a velocidade angular em todos os eixos.</span></span></div>
<div style="text-align: left;">
<span style="font-family: inherit; line-height: 19.200000762939453px;"><br/></span></div>
<div style="text-align: left;">
<span style="font-family: inherit; line-height: 19.200000762939453px;">O projeto freeIMU, é um implementação completa de uma IMU. Não apenas os drivers para os sensores, mas também toda a parte de fusão dos sensores para obter a velocidade, orientação e forças com o máximo de precisão&nbsp;possível, na mair taxa de atualização&nbsp;possível (cerca de 500Hz)&nbsp;</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;">http://www.varesano.net/projects/hardware/FreeIMU</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;"><br/></span></div>
<div style="text-align: left;">
<span style="font-family: inherit;">O projeto freeIMU desenvolveu também o hardware, que atualmente está na quarta revisão.</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;">http://www.varesano.net/files/FreeIMU_v0.4.1_schematics_0.pdf</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;"><br/></span></div>
<div style="text-align: left;">
<span style="font-family: inherit;">Montar o hardware proposto pelo projeto estando no Brasil é muito complicado devido a todos os fatores que impedem o desenvolvimento da ciência nacional. Embora tenha melhorado muito, o Brasil está distante de virar uma potência em desenvolvimento de ciência. A melhor alternativa para contornar as mazelas que impedem o desenvolvimento da ciência nacional é entrar em contato com nossos amigos na China. Na China além de não existir problemas para o desenvolvimento da ciência, tudo pode ser fabricado na quantidade e qualidade que se deseja! &nbsp;No caso do projeto freeIMU, nem é preciso encomendar nada, um dos nossos amigos de lá, já copiou e renomeou o projeto para GY-86.</span></div>
<div style="text-align: left;">
<span style="font-family: inherit;"><br/></span></div>
<div style="text-align: left;">
<b><span style="font-family: inherit; line-height: 19.200000762939453px;">Aqui vai o esquemático&nbsp;elétrico&nbsp;do GY-86, que já conta com level shift para I/O de 5V.</span></b></div>
<div style="text-align: left;">
<span style="font-family: inherit; line-height: 19.2000007629395px;">Que torna&nbsp;compatível com o arduino/AVR [gpio de 5v] e com a Stellaris / Tiva C Series [gpio tolerante a 5v].</span></div>
<div>
<span style="font-family: sans-serif; font-size: x-small; line-height: 19.200000762939453px;">&nbsp;</span><span style="font-family: sans-serif; font-size: x-small; line-height: 19.200000762939453px;">&nbsp;</span></div>
<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-CdIgYZJIn7E/UxfwYegZwoI/AAAAAAAAo_8/szYT2_AkNvk/s1600/GY-86-Schematic.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="366" src="http://4.bp.blogspot.com/-CdIgYZJIn7E/UxfwYegZwoI/AAAAAAAAo_8/szYT2_AkNvk/s1600/GY-86-Schematic.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-86 Esquemático</td></tr>
</tbody></table>
O GY-86 tem passo de 2.54 mm, que facilita a montagem é protoboards / breadboards.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-6zA4v0QuQvc/UxfxH-Cl0-I/AAAAAAAApAE/qX8X6OLN7f8/s1600/GY-86-board.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-6zA4v0QuQvc/UxfxH-Cl0-I/AAAAAAAApAE/qX8X6OLN7f8/s1600/GY-86-board.jpg" width="271"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-86 Board</td></tr>
</tbody></table>
E você pode estar comprando um GY-86 por aqui, dá para encontrar vários por menos de $15<br/>
http://www.aliexpress.com/w/wholesale-gy%25252d86.html?SearchText=gy-86&amp;CatId=0&amp;initiative_id=SB_20140305195722&amp;SortType=price_asc&amp;filterCat=523,4099&amp;groupsort=1<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-zKUU2xiw15c/Uxf7TeNXEaI/AAAAAAAApAU/JuEntjOQcMU/s1600/gy86-front-back.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="181" src="http://3.bp.blogspot.com/-zKUU2xiw15c/Uxf7TeNXEaI/AAAAAAAApAU/JuEntjOQcMU/s1600/gy86-front-back.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Frente e verso do GY-86</td></tr>
</tbody></table>
<br/>
Conforme especificado na quarta revisão do FreeIMU, o GY-86 também é baseado no MPU-6050 (acelerômetro + giroscópio)&nbsp;, HMC5883L (magnetômetro) &nbsp;e MS5611 (barômetro).<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-5bW-KxvQ53A/Uxf95a54DQI/AAAAAAAApAg/RW-Rw8CNrrU/s1600/freeimu_gui_3d_1.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="340" src="http://2.bp.blogspot.com/-5bW-KxvQ53A/Uxf95a54DQI/AAAAAAAApAg/RW-Rw8CNrrU/s1600/freeimu_gui_3d_1.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Parte do software do FreeIMU, para calibração dos sensores.</td></tr>
</tbody></table>
<br/>
<br/></div>
</div>