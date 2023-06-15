---
layout: post
title: Tiva C + Stellaris- pinout
categories:
 - EK-LM4F120XL
date: 2015-04-20 11:51:00 +0100
---

As placas Tiva C e Stellaris possuem alguns "problemas".  

<div>
O primeiro são os resistores R9 e R10 que precisam ser removidos para não dar curto entre os GPIOs.</div>

<div>
O segundo é o pinmux da USART1 e USART4 que iniciam em conflito, então é preciso remapear a USART1 para o conector J1, para que a USART4 funcione no conector J4.</div>

<div>
O terceiro é o U4 presente somente nas Stellaris (na Tiva C já vem de fabrica sem ele), que precisa ser removido para permitir a placa ligar tensões abaixo de 5V (ex: bateria).<br/>
Resolvidos esses "problemas" é só partir para desenvolvimento.<br/>
Estão disponíveis:<br/>
8x UART - Serial<br/>
4x I2C - Wire<br/>
3x SPI</div>

<div>
12x ADC - analogRead<br/>
44x GPIO - digitalRead/Write<br/>
23x PWM - analogWrite<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Iv0iEGENpLc/VTTX0IbZDdI/AAAAAAABIAc/kedUjg-is-A/s1600/tiva%2Bstellaris.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="285" src="http://4.bp.blogspot.com/-Iv0iEGENpLc/VTTX0IbZDdI/AAAAAAABIAc/kedUjg-is-A/s1600/tiva%2Bstellaris.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tiva C + Stellaris: pinout</td></tr>
</tbody></table>
<br/></div>