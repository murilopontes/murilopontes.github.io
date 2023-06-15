---
layout: post
title: Testando ADC de 12-bits da Stellaris Launchpad
categories:
 - ARM
date: 2013-11-03 00:21:00 +0000
---

<div class="separator" style="clear: both; text-align: justify;">
Depois de terminar o port da API do Arduino do GCC para o IAR e juntar com o FreeRTOS é hora de começar a fazer os testes de HW. Depois dos LEDs, botões e serial, chegou a vez de testar o ADC.</div>

<a name="more"></a>   

<div class="separator" style="clear: both; text-align: center;">
Até agora tudo funcionando perfeito.</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-JoDhUvGOMNI/UnWU6WtHKTI/AAAAAAAAm54/bOj-iaH9qZo/s1600/IMG_20131102_210848.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-JoDhUvGOMNI/UnWU6WtHKTI/AAAAAAAAm54/bOj-iaH9qZo/s320/IMG_20131102_210848.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Setup do&nbsp;&nbsp;potenciômetro na Stellaris Launchpad<br/>
o&nbsp;potenciômetro usado é o Phidgets Slider 60mm p/n 1112<br/>
[&nbsp;<a href="http://www.phidgets.com/products.php?product_id=1112">http://www.phidgets.com/products.php?product_id=1112</a>&nbsp;]</td></tr>
</tbody></table>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-JG-BjsWUvDI/UnWVANq5AHI/AAAAAAAAm6A/lNOTS8cKqro/s1600/tiva-c-series-adc.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="202" src="http://3.bp.blogspot.com/-JG-BjsWUvDI/UnWVANq5AHI/AAAAAAAAm6A/lNOTS8cKqro/s320/tiva-c-series-adc.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Saída serial da Stellaris Launchpad<br/>
ADC no pino PB5 - valores entre 0 e 4095 (0-3.3v)<br/>
&nbsp;gerando o duty cycle do PWM para API do Arduino (analogWrite)</td></tr>
</tbody></table>

  