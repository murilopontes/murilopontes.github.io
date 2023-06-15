---
layout: post
title: WR740N e Motores DC- latência do kernel com pthreads
categories:
 - Linux
date: 2014-09-26 05:05:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Experimentado colocar o PWM para funcionar nos Leds do WR740N para controlar os motores do Drone.<br/>
<br/>
<a name="more"></a><br/>
Mas OpenWRT não compila o módulo de PWM nos GPIOs porque não existem timers de hardware livres neste no SOC ar9331.<br/>
<br/>
Uma solução alternativa é implementar o PWM por software usando pthreads. Durante a depuração começam a aparecer problemas. O escalonador de processos com a configuração padrão do Openwrt não é preemptiva, e acaba causando anomalias no PWM que podem ser percebidas olhando o piscado irregular dos leds, e também usando o Buspirate com PirateScope.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-8tdjzwa-Gys/VB-M8iqnHGI/AAAAAAAAtAw/VQAFO8cqv5Q/s1600/wr740-no-preemptive-kernel.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="196" src="http://4.bp.blogspot.com/-8tdjzwa-Gys/VB-M8iqnHGI/AAAAAAAAtAw/VQAFO8cqv5Q/s1600/wr740-no-preemptive-kernel.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O que era para ser um PWM de 50 Hz com 1% de duty cycle se transformou nesta onda defeituosa.<br/>
Mesmo usando todas as configuração de SCHED_RR ou SCHED_FIFO<br/>
para os pthreads anomalias na latência continuam ocorrendo</td></tr>
</tbody></table>
Na configuração do kernel preemptivo de baixa latência existente a promessa de latências menores de que 1 milisegundo. Depois de mais alguns testes e ajustes, foi obtido o resultado esperado.<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-iGfagv9rj7Q/VCTjVYfYWpI/AAAAAAAAtCo/nO1zmByOcBk/s1600/wr740n-soft-pwm-preemptivo.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="163" src="http://3.bp.blogspot.com/-iGfagv9rj7Q/VCTjVYfYWpI/AAAAAAAAtCo/nO1zmByOcBk/s1600/wr740n-soft-pwm-preemptivo.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Soft PWM de 50 Hz via kernel preemptivo de baixa latência.<br/>
Espaçamento sem constante.</td></tr>
</tbody></table>
Quando o PWM desejado é de mais 100 Hz é preciso mudar também a frequência do kernel durante o build. O problema agora é instalar um level shift já que os ESCs do drone não funcionaram com esse sinal que tem pico em 2V.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-bvCZkQu1TmA/VCTkZtZ2N9I/AAAAAAAAtC0/qgcsIcUS6aI/s1600/IMG_20140926_003419.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-bvCZkQu1TmA/VCTkZtZ2N9I/AAAAAAAAtC0/qgcsIcUS6aI/s1600/IMG_20140926_003419.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">BLDC ligados nos Leds do WR740N, <br/>
mas sem o level shift para 3,3v os motores BLDC não reconheceram o WR740N.</td></tr>
</tbody></table>
<b>UPDATE</b>: &nbsp;Durante os testes quando a conexão WiFi do WR740N é muita usada ou ocorre uma desconexão, o PWM por software fica defeituoso mesmo no kernel preemptivo de baixa latência. Portanto, no openwrt / linux não dá para fazer um PWM por software muito confiável. &nbsp;A próxima alternativa é implementar o PWM por HW (arduino) controlado por uma conexão I2C nos leds do WR740N.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-YSPeBfoV9NI/VCiu7ej2MvI/AAAAAAAAtG8/hFELNDr1WZs/s1600/VID_20140928_112633.mp4" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="179" src="http://3.bp.blogspot.com/-YSPeBfoV9NI/VCiu7ej2MvI/AAAAAAAAtG8/hFELNDr1WZs/s1600/VID_20140928_112633.mp4" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">I2C do tplink como master.<br/>
I2C da Tiva como slave.<br/>
tplink envia por I2C os valores de PWM para que a Tiva gere o PWM por HW.<br/>
Funcionou perfeitamente</td></tr>
</tbody></table>
<b>UPDATE 2</b>: Os pinos dos leds são compartilhados com a configuração da CPU, após o boot podem ser usados, mas durante o boot alterar os valores dos gpios pode levar o sistema a estados indeterminados (isso ocorre em alguns pinos &nbsp;das placas Beaglebone também). Sendo assim, vou abandonar o uso do wr740n como placa mãe do drone. alguns outros modelos possuem gpios livres e não compartilhados. No futuro irei testar.<br/>
<br/>
<br/>
<br/></div>