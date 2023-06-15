---
layout: post
title: Consumo de corrente em 15 modelos de hélices diferentes
categories:
 - hélices
date: 2014-12-21 14:01:00 +0000
---

Recebi um algumas de hélices com tamanhos e configurações variadas. A ideia é testar todas para ver qual produz mais empuxo e qual o consumo de corrente de cada uma.  

<div>
<br/>
<br/>
<a name="more"></a><br/><br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Xjo_9Arh96c/VJbFeaPb2PI/AAAAAAAAuXo/zMy_U89RsGg/s1600/IMG_20141221_100409.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-Xjo_9Arh96c/VJbFeaPb2PI/AAAAAAAAuXo/zMy_U89RsGg/s1600/IMG_20141221_100409.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Um monte de hélices diferentes para testar</td></tr>
</tbody></table>
No teste usei um fonte de PC de genérica, um multímetro, a beaglebone com PWM gerado por PRU para controlar os ESCs Flyfun de 30A com motores A2212/13T 1000Kv (pico de corrente&nbsp;12A). Um controle de Xbox com um app em C# com SlimDX para enviar os comandos para a beaglebone via rede WiFi ou Ethernet.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-1VqpfBXDwQ4/VJbI1RkyGHI/AAAAAAAAuYY/ITncxO1ACo8/s1600/IMG_20141221_101309.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-1VqpfBXDwQ4/VJbI1RkyGHI/AAAAAAAAuYY/ITncxO1ACo8/s1600/IMG_20141221_101309.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Fonte de PC - Mymax MPSU/230W versão 1.3 - só vou usar os 12V @&nbsp;8A = 96W</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-I0AoPFgKQf4/VJbJAketRfI/AAAAAAAAuYg/j1YQhge7liU/s1600/IMG_20141221_101355.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://4.bp.blogspot.com/-I0AoPFgKQf4/VJbJAketRfI/AAAAAAAAuYg/j1YQhge7liU/s1600/IMG_20141221_101355.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Multímetro &nbsp;- Minipa ET-1110 - no modo 10A usando a entrada UNFUSED.</td></tr>
</tbody></table>
<br/>
Coloquei um playlist dos testes no Youtube<br/>
<br/>
<div style="text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/VKam2XNsQZs?list=PLB_uIxBF0dCe1DDbgFvizunAutcuvVoQ4" width="560"></iframe>
</div>
<div style="text-align: center;">
<br/></div>
Um breve sumário do que aconteceu:<br/>
5x5e: pico em 2,36A - estável em 2,33A - empuxo fraco<br/>
6x3e: pico em 2,65A - estável em 2,55A&nbsp;- empuxo fraco<br/>
6x4: pico em 2,96A - estável em 2,80A&nbsp;- empuxo fraco<br/>
7x4hy: estável em 4,04A&nbsp;- empuxo fraco<br/>
7x4.5e: pico em 5,78A - estável em 5,06A&nbsp;- empuxo fraco<br/>
7x5: pico 5.02A - estável em 4,74A&nbsp;- empuxo fraco<br/>
8x4 slow: pico em 5,11 - estável em 4,80A&nbsp;- empuxo fraco<br/>
8x4 hy: estável em 4,81A&nbsp;- empuxo fraco<br/>
8x4.5: pico em 6,15A - estável em 4,90A&nbsp;- empuxo fraco<br/>
8x6 gemfan: pico em 5,86A - estável em 5,05A&nbsp;- empuxo fraco<br/>
9x3.8sf: pico em 5,66A - estável em 5,07A&nbsp;- empuxo fraco<br/>
9x5: pico em 5,75A - estável em 4,60A&nbsp;- empuxo fraco<br/>
9x5 gemfan: pico em 6,15A - estável em 5,10A&nbsp;- empuxo fraco<br/>
10x4.5: pico em 7,58A - estável em 5,24A - empuxo suficiente para levantar o drone<br/>
10x6 gemfan: 8,38A - estável em 7,36A - empuxo fraco<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>