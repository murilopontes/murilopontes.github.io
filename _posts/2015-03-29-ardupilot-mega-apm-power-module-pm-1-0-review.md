---
layout: post
title: ArduPilot Mega (APM) Power module (PM) 1.0 review
categories:
 - ArduPilot Mega
date: 2015-03-29 16:58:00 +0100
---

Antes de ligar qualquer hardware é bom verificar se componentes são os que deveriam ser.  

<div>
E também verificar as tensões de entrada e saída, se estão dentro do esperado.</div>

<div>
<br/></div>

<div>
Especificação do APM PM 1.0</div>

<div>
<div>
Max input voltage: 18V</div>
<div>
Min input voltage: 4.5 V</div>
<div>
Max current sensing: 90A with APM, 60A with Pixhawk</div>
<div>
Voltage and current measurement configured for 5V ADC</div>
<div>
Switching regulator outputs 5.3V and 2.25A max</div>
<div>
6-pos DF13 cable plugs directly to APM 2.5's 'PM' connector</div>
</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-FLicvas_xl8/VRgPbh0X0aI/AAAAAAABHbA/NFyTIPms5aY/s1600/IMG_20150329_114154.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-FLicvas_xl8/VRgPbh0X0aI/AAAAAAABHbA/NFyTIPms5aY/s1600/IMG_20150329_114154.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Face superior do APM PM</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-2pJiRjkjUBw/VRgPdzcsp4I/AAAAAAABHbI/5vO_TL3Cw-o/s1600/IMG_20150329_114209.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-2pJiRjkjUBw/VRgPdzcsp4I/AAAAAAABHbI/5vO_TL3Cw-o/s1600/IMG_20150329_114209.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Face inferior do APM PM</td></tr>
</tbody></table>

<div>
Soldei os headers de 2.54mm para facilitar os testes.&nbsp;</div>

<div>
<br/></div>

<div>
O regulador usado neste versão da placa, é o MP1583DN<br/>
<div>
<div>
- 3A Output Current</div>
<div>
- Programmable Soft-Start</div>
<div>
- 100mΩ Internal Power MOSFET Switch</div>
<div>
- Stable with Low ESR Output Ceramic Capacitors</div>
<div>
- Up to 95% Efficiency</div>
<div>
- 20μA Shutdown Mode</div>
<div>
- Fixed 385KHz Frequency</div>
<div>
- Thermal Shutdown</div>
<div>
- Cycle-by-Cycle Over Current Protection</div>
<div>
- Wide 4.75V to 23V Operating Input Range</div>
<div>
- Output Adjustable from 1.22V to 21V</div>
<div>
- Under-Voltage Lockout</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://1.bp.blogspot.com/-A_QOedc3OZg/VRgMOlA5jpI/AAAAAAABHaI/QXLTD-GugFM/s1600/IMG_20150329_112638.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-A_QOedc3OZg/VRgMOlA5jpI/AAAAAAABHaI/QXLTD-GugFM/s1600/IMG_20150329_112638.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">O APM power module usa um Regulador chaveado MP1583DN<br/>
Monolithic Power Systems (MPS) - 3A 385kHz 23V Buck</td></tr>
</tbody></table>
No multímetro a saída do MP1583DN ficou em 5,3V como indicado no projeto.&nbsp;</div>
<div>
Essa saída não serve para alimentar os Servos porque é chaveada, o recomendo para os servos é usar os BEC lineares (7805 e similares) dos ESCs.</div>
<div>
<br/></div>
<div>
A medição do tensão é feita por um divisor resistivo de 1,5k 0.1% e 13,7k 0.1%.</div>
<div>
Medindo com o multímetro os valores foram próximos: R1=1,49k e R2=13,69k.</div>
</div>

<div>
http://www.raltron.com/cust/tools/voltage_divider.asp</div>

<div>
Para entrada de 18V a saída ficou em 1,77V</div>

<div>
Para entrada de 12V a saída ficou em 1,18V</div>

<div>
Com esses valores dá para ligar direto no ADC da beaglebone black, que aceita até 1,8V<br/>
<br/></div>

<div>
No arduino com ADC de 10bits, o analogRead na média móvel de 100 valores deu 250 para 11,50V<br/>
A referência analógica 4,62V deu no multímetro.<br/>
Então 4,62 / 1024 = 0,00451171875V.<br/>
Vo=1,1279296875<br/>
Vin = Vo * (R1+R2) / R2 =&nbsp;11,491256816275167785234899328859<br/>
<br/></div>

<div>
<br/></div>

<div>
A medição de corrente é feita usando o INA169 com resistor shunt RS=0.0005ohm 1% 4W e resistor de saída de RL=110k 0.1%.<br/>
No multímetro o resistor de saída RL deu 108.3k. RS=0,2ohm (por falta de resolução).<br/>
Segundo o datasheet com Is = Vo * 1000 / (RL*RS)<br/>
Na fonte o consumo de 0.8A gerou 0,044V no Vo,<br/>
Então Is=(0.044*1000)/(0.0005*110000)=44/55=0.8A<br/>
Para Is=60A =&gt; 60*55/1000 = 3.3V<br/>
Para Is=90A =&gt; 90*55/1000 = 4,95V<br/>
<br/>
<br/></div>