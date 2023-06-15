---
layout: post
title: Estabilizador de voo
categories:
 - controle PID
date: 2013-11-17 18:36:00 +0000
---

Estabilizador de voo / controle PID  

  

<a name="more"></a>  
  

Em multi-rotores a implementação é feita usando um acelerômetro.  

  

O acelerômetro mede a aceleração em um determinado eixo.  

O&nbsp;<span style="font-size: 13px; text-align: center;">Giroscópio mede a velocidade angular em um determinado eixo.</span>  

  

A inclinação em graus do UAV nos eixos X e Y é dada pelo arco tangente em relação ao eixo Z.  

Os valores usado para calcular o arco tangente são as acelerações nos eixos X e Y.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-yaAHCxJEAqg/UliORbfM4yI/AAAAAAAAmfo/_E2caDu_8lk/s1600/giro-sku_154602_1.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-yaAHCxJEAqg/UliORbfM4yI/AAAAAAAAmfo/_E2caDu_8lk/s320/giro-sku_154602_1.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GY-512 MPU6050 - Giroscópio&nbsp;+ acelerômetro.</td></tr>
</tbody></table>

<div style="text-align: justify;">
<span style="font-family: inherit;"><br/></span>
<span style="font-family: inherit;">MPU6050 - Sensor da Invense 6 DOF</span></div>

<h3 class="r" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: medium; font-weight: normal; margin: 0px; overflow: hidden; padding: 0px; text-align: justify; text-overflow: ellipsis; white-space: nowrap;">
<a href="http://dx.com/p/gy-521-mpu6050-3-axis-acceleration-gyroscope-6dof-module-blue-154602" style="background-color: transparent;">http://dx.com/p/gy-521-mpu6050-3-axis-acceleration-gyroscope-6dof-module-blue-154602</a></h3>

<div>
<div style="text-align: justify;">
(cerca $7)<br/>
<span style="background-color: white; color: #333333; font-family: Arial; font-size: 13px; text-align: start;"><br/></span>
<span style="background-color: white; color: #333333; font-family: Arial; font-size: 13px; text-align: start;">L3G4200D</span></div>
<div>
<div style="text-align: justify;">
<a href="http://dx.com/p/gy-50-l3g4200d-3-axis-digital-gyro-sensor-module-for-arduino-148731">http://dx.com/p/gy-50-l3g4200d-3-axis-digital-gyro-sensor-module-for-arduino-148731</a><br/>
(cerca $12)<br/>
<div>
<br/></div>
<div>
<br/></div>
<div>
<br/></div>
</div>
</div>
</div>

Tendo em mãos os valores da aceleração nos 3 eixos a estabilização do UAV é feita através da aplicação de um&nbsp;<b style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">proportional-integral-derivative controller</b><span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">&nbsp;(</span><b style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">PID controller</b><span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">) para cada eixo</span>  

<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">\[</span>[http://en.wikipedia.org/wiki/PID\_controller](http://en.wikipedia.org/wiki/PID_controller)<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">\]</span>  

<span style="background-color: white; font-family: sans-serif;"><span style="font-size: x-small;"><span style="line-height: 19.1875px;">O PID vai regular automaticamente a potência dos motores que seja minimizado o erro de&nbsp;estabilização.</span></span></span>  

<span style="background-color: white; font-family: sans-serif;"><span style="font-size: x-small;"><span style="line-height: 19.1875px;">Quando o erro de&nbsp;</span></span></span><span style="background-color: white; font-family: sans-serif; font-size: x-small; line-height: 19.1875px;">estabilização é próximo a zero, dizemos que o UAV foi estabilizado e está a espera de comandos do piloto.</span>  

<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-6j0MkqdJqF8/UliQIcRjfFI/AAAAAAAAmf0/wppLzYRcHXA/s1600/PID_en_updated_feedback.svg.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="http://1.bp.blogspot.com/-6j0MkqdJqF8/UliQIcRjfFI/AAAAAAAAmf0/wppLzYRcHXA/s1600/PID_en_updated_feedback.svg.png"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Controlador PID</td></tr>
</tbody></table>

<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;">  
</span>
  

  