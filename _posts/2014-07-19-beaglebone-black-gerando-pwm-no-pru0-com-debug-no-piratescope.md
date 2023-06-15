---
layout: post
title: Beaglebone Black gerando PWM no PRU0 com debug no Piratescope
categories:
 - post
date: 2014-07-19 06:06:00 +0100
---

<div class="separator" style="clear: both; text-align: justify;">
A Beaglebone Black além do ARM Cortex-A8 de 1GHz, contém 2 processadores de tempo real (PRU).</div>

<div class="separator" style="clear: both; text-align: justify;">
As duas PRUs rodam a 200 MHz, executam uma instrução por ciclo de clock. Portanto executam uma instrução a cada 5 nanosegundos de maneira determinística.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
</div>

<a name="more"></a>Cada PRU pode ter até 16 pinos de entrada e 16 pinos de saída. A comunicação entre as PRUs e o ARM Cortex-A8 é feita por uma janela de memória compartilhada. É possível usar os GPIOs e ADCs a uma frequência de 192 MHz. E implementar software UART com velocidade de 24 Megabytes por segundo.  

<div class="separator" style="clear: both; text-align: justify;">
Também dá para implementar PWM com precisão de 5 ns, o que é ótimo para controlar motores e servos com extrema precisão. &nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
Seguindo o código de:</div>

<div class="separator" style="clear: both; text-align: justify;">
<a href="http://www.embedded-things.com/bbb/wireless-servo-control-part-3-pwm-servo-control-with-the-bbb-pru/">http://www.embedded-things.com/bbb/wireless-servo-control-part-3-pwm-servo-control-with-the-bbb-pru/</a></div>

<div class="separator" style="clear: both; text-align: justify;">
Com mais alguns ajustes é possível gerar o PWM de 490Hz para controlar os motores do UAV.</div>

<div class="separator" style="clear: both; text-align: justify;">
Também foi preciso mexer na placa mãe do UAV para direcionar os PWMs para o pinos de saída da PRU0. Com a nova configuração 4 motores pode ser acionados pelo PWM do PRU ou do ARM, &nbsp;e mais 4 motores são somente ativados pelo PWM do ARM.</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
Usando o Buspirate (<a href="http://dangerousprototypes.com/docs/Bus_Pirate">http://dangerousprototypes.com/docs/Bus_Pirate</a>) com o Piratescope é fácil verificar que a geração do PWM pelo PRU0 está funcionando como deveria.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
Os próximos testes serão verificar se todos os motores estão sincronizados e testar os efeitos do ajuste fino do PWM na escala de 5ns na velocidade do motor. Como o motor aceita comandos entre 1000 e 2000 milisegundos, o intervalo de 1ms por ser dividido em 200 mil pedaços, é como se fosse um carro de 200 mil marchas ou praticamente marchas infinitas.</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-VTA-xk56tMY/U8n2o4UYQmI/AAAAAAAAscA/YcTqUUWji0I/s1600/piratescope-beagleboneblack-pru-pwm.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="250" src="http://1.bp.blogspot.com/-VTA-xk56tMY/U8n2o4UYQmI/AAAAAAAAscA/YcTqUUWji0I/s1600/piratescope-beagleboneblack-pru-pwm.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Piratescope: PWM gerado pelo PRU0</td></tr>
</tbody></table>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-i6iRAKhVu30/U8n2j-WeI_I/AAAAAAAAsb4/b8h7iHMWyPc/s1600/IMG_20140719_013620.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-i6iRAKhVu30/U8n2j-WeI_I/AAAAAAAAsb4/b8h7iHMWyPc/s1600/IMG_20140719_013620.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Buspirate conectado na placa mãe do UAV</td></tr>
</tbody></table>

  

Com o novo PWM também foi preciso recalibrar os ESCs para reconhecer os novos níveis de PWM para armar os motores, rotação mínima e máxima. Após a calibragem os motores ficaram sincronizados com um precisão de 1 microsegundo.  

  

Tentando subir com hélices 6x4  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/l_URMXIcVFA" width="560"></iframe>

  

  

Tentando subir com hélices 10x6, mas estavam trocadas CW com CCW.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/4Lf4Qh88v3Q" width="560"></iframe>

  

Subindo com hélices 10x6, mas a bateria já estava descarregando.  

Mesmo assim dá para perceber que o desempenho é agressivo.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/YVDpuiX7dB0" width="560"></iframe>