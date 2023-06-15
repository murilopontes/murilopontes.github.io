---
layout: post
title: Controlando ESC do motor brushless com Arduino Nano V3
categories:
 - post
date: 2013-10-25 16:44:00 +0100
---

Para testar o motor é preciso gerar um sinal PWM na entrada do ESC.  

Mas tem um pequeno detalhe, o ESC não aceita qualquer PWM, os pulsos ativos precisam estar em 1ms (velocidade mínima) e 2ms (velocidade máxima).  

<a name="more"></a>  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-hrNS-LQHdKA/Ump7La4x4uI/AAAAAAAAmuA/QtN_B4LEyho/s1600/IMG_20131024_214708.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-hrNS-LQHdKA/Ump7La4x4uI/AAAAAAAAmuA/QtN_B4LEyho/s320/IMG_20131024_214708.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Motor&nbsp;+ ESC montados</td></tr>
</tbody></table>

Para deixar o teste mais interessante, é possível utilizar a leitura analógica do Arduino para ler um potenciômetro. O ADC do Arduino tem 10 bits, portanto vai gerar valores entre 0 e 1023. A frequência padrão do PWM do Arduino é 500Hz, o que está ok, pois com um duty cycle de 100% terá tempo ativo de 2ms. E com 50% de duty cycle terá 1ms. Então é só mapear os valores do ADC em valor de duty cycle do PWM. No caso do Arduino os valores de duty cycle variam de 0 (0%) a 255 (100%), logo pode-se concluir que 128 &nbsp;é 50% de duty cycle. A próprio API do Arduino já tem a funcão "map" que fará o mapeamento de 0 a 1023 do ADC em 128 a 255 do PWM. O resultado pode ser visto no video.  

Não deu para colocar a fonte no video, &nbsp;mas estava configurada para 11.1V e 1A &nbsp;o motor está na rotação máximo o consumo de corrente é de 700mA até menos de 800mA.  

  

<div class="separator" style="clear: both; text-align: center;">
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/3EIzSX5HSMc" width="420"></iframe>
</div>

  

Antes desse teste usei o Bus Pirate como osciloscópio para verificar se a forma de onde do PWM estava como esperado. Depois post sobre como isso pode ser feito.