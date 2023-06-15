---
layout: page
title: Drone- FreeIMU calibração
categories:
 - page
date: 2016-07-31 20:00:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: center;">
<div style="text-align: justify;">
<div style="text-align: center;">
Testando FreeIMU calibrada com cubo 3d no Processing 2.2.1</div>
<div style="text-align: center;">
<br/></div>
<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/zizJOUMH_vE" width="560"></iframe></div>
<div style="text-align: center;">
<br/></div>
<div style="text-align: center;">
Calibração do FreeIMU com &nbsp;ferramenta em Python+Qt</div>
<div style="text-align: center;">
<br/></div>
<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/rlGxA3Hqn4Q" width="560"></iframe></div>
<br/>
Um dos requisitos básicos para fazer qualquer sistema que se estabilize automaticamente são os sensores de&nbsp;orientação, estabilização&nbsp;e navegação.<br/>
<br/>
Os principais sensores e suas principais funções:<br/>
1) Acelerômetro: principal função é calcular o pitch e roll absolutos em relação a gravidade.<br/>
2) Giroscópio: principal função é medir a velocidade angular para estabilizar o drone parado.<br/>
3) Magnetômetro: principal função é calcular o yaw absoluto em relação ao norte magnético.<br/>
4) Barômetro: principal função é medir a altitude absoluto com base na pressão atmosférica.<br/>
5) GPS: principal função é o posicionamento.<br/>
Existem vários outros sensores e funções alternativas para esses sensores, mas vai além do escopo do blog.<br/>
<br/>
Uma excelente comparação de praticamente todos sensores para IMU<br/>
<a href="http://snowcap.fi/blog/2012/01/04/imu-sensor-comparison/">http://snowcap.fi/blog/2012/01/04/imu-sensor-comparison/</a><br/>
<div>
<br/></div>
O projeto <a href="http://www.varesano.net/projects/hardware/FreeIMU" target="_blank">FreeIMU</a> desenvolveu uma&nbsp;<a href="http://en.wikipedia.org/wiki/Inertial_measurement_unit" target="_blank">IMU</a>&nbsp;<a href="http://en.wikipedia.org/wiki/Open_source_hardware" target="_blank">openhardware</a>&nbsp;com 10 <a href="http://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)" target="_blank">DOF</a>&nbsp;e o software <a href="http://en.wikipedia.org/wiki/Attitude_and_heading_reference_system" target="_blank">AHRS</a>&nbsp;que já entrega a orientação 3D no formato de <a href="http://en.wikipedia.org/wiki/Quaternion" target="_blank">Quaternations</a> e <a href="http://en.wikipedia.org/wiki/Euler_angles" target="_blank">ângulos de Euler</a>.<br/>
O algoritmo utilizado pelo FreeIMU é o <a href="http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/" target="_blank">filtro DCM baseado em Quaternion</a>&nbsp;que é uma abordagem mais simples que o <a href="http://en.wikipedia.org/wiki/Extended_Kalman_filter" target="_blank">filtro de Kalman extendido (EKF)</a>.<br/>
<br/>
Post sobre os algoritmos do FreeIMU<br/>
<a href="http://dronespersonalizados.blogspot.com.br/2014/07/freeimu-com-gy-86-e-arduino-no-ubuntu.html">http://dronespersonalizados.blogspot.com.br/2014/07/freeimu-com-gy-86-e-arduino-no-ubuntu.html</a><br/>
<div>
<br/></div>
</div>
<div style="text-align: justify;">
Post testando GY86 com FreeIMU<br/>
<a href="http://dronespersonalizados.blogspot.com.br/2014/03/unidade-de-medicao-inercial-gy-86-10dof.html">http://dronespersonalizados.blogspot.com.br/2014/03/unidade-de-medicao-inercial-gy-86-10dof.html</a><br/>
<br/>
Referência de mais implementações MARG para uso em AHRS.<br/>
<a href="http://projectproto.blogspot.de/2011/02/marg-sensors-bluetooth.html">http://projectproto.blogspot.de/2011/02/marg-sensors-bluetooth.html</a><br/>
<br/>
<br/></div>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>
</div>