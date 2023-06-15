---
layout: post
title: Testando motores, ESCs, hélices, consumo de corrente  
categories:
 - motores
date: 2013-11-13 23:40:00 +0000
---

<div class="separator" style="clear: both; text-align: center;">
</div>

<div class="separator" style="clear: both; text-align: center;">
</div>

<div class="separator" style="clear: both; text-align: center;">
</div>

<div class="separator" style="clear: both; text-align: justify;">
Chegou a hora de testar quase tudo funcionando junto.</div>

<div class="separator" style="clear: both; text-align: justify;">
O Frame ainda não chegou, mas improvisei um aqui de papelão de caixa de leite.</div>

<div class="separator" style="clear: both; text-align: justify;">
Cortei em 2 tirinhas de 4 cm de largura e tá novo!</div>

<a name="more"></a>  

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-iHKDXVmz5eY/UoQEeq_9tCI/AAAAAAAAnI8/og7sCiBF9mw/s1600/IMG_20131113_180015.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-iHKDXVmz5eY/UoQEeq_9tCI/AAAAAAAAnI8/og7sCiBF9mw/s320/IMG_20131113_180015.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Finalmente acabei de soldar os ESCs que faltavam, <br/>
depois que o jeito dá para soldar cada ESC em menos de 10 minutos.<br/>
<br/></td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-KFZEW_3R8Co/UoQFi28L1rI/AAAAAAAAnJI/fvMKtBwQrNU/s1600/IMG_20131113_182733.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-KFZEW_3R8Co/UoQFi28L1rI/AAAAAAAAnJI/fvMKtBwQrNU/s320/IMG_20131113_182733.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Frame feito com papelão de caixa de leite.<br/>
Enquanto não chega o plástico, alumínio e fibra de carbono,<br/>
o jeito é se virar como pode.</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-zTjsU02o3-Y/UoQGErtnHII/AAAAAAAAnJQ/_ty08VCAhGk/s1600/IMG_20131113_195318.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-zTjsU02o3-Y/UoQGErtnHII/AAAAAAAAnJQ/_ty08VCAhGk/s320/IMG_20131113_195318.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tudo ligado. Multímetro ligado em série com a saída de 12V da fonte de PC.<br/>
Com os motores parados, os ESCs consomem de grátis 0,18A ou 180mA.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-mHqcX5G9LQw/UoQHYoFjDaI/AAAAAAAAnJo/zRAH_BPKvcM/s1600/2013-11-13+20.09.37.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-mHqcX5G9LQw/UoQHYoFjDaI/AAAAAAAAnJo/zRAH_BPKvcM/s320/2013-11-13+20.09.37.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A minha poderosa fonte de PC dá no máximo 8A no 12V.<br/>
Fabricada em 2008, se diz capaz de suportar até 230W.<br/>
Nem precisa dizer que isso é uma lenda.<br/>
É preciso monitorar o uso de concorrente para a fonte não explodir.<br/>
Como o multímetro só mede até 10A e a fonte só dá 8A não haverá problema, <br/>
caso contrário o multímetro também&nbsp;poderia explodir.<br/>
Para medir uma corrente maior que 10A é preciso <br/>
usar um resistor de shunt ligado no ADC do microcontrolador <br/>
e fazer as contas, mas isso fica para outro post.<br/>
Como cada ESC sozinho pode puxar até 30A, a coisa pode ficar tensa e<br/>
uma solução mais elaborada de monitoramento precisa ser desenvolvida.<br/>
<br/>
<br/></td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-NXtz0FE8vJg/UoQKB-qyCKI/AAAAAAAAnKA/-cCV6IDyfS8/s1600/IMG_20131113_195407.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-NXtz0FE8vJg/UoQKB-qyCKI/AAAAAAAAnKA/-cCV6IDyfS8/s320/IMG_20131113_195407.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligado o primeiro motor em rotação minima.<br/>
Liguei usando o prompt de comando (http://bitlash.net) do Arduino, gerando PWM (480Hz)<br/>
com analogWrite em 123 (quase 50% de duty cycle).<br/>
Consumo subiu para 310mA. <br/>
310mA(total)-180(ESCs)=130mA(motor1)</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-De-1UXbyA3Y/UoQK5mgyUQI/AAAAAAAAnKI/Mri1lcRJ7Yg/s1600/IMG_20131113_195437.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-De-1UXbyA3Y/UoQK5mgyUQI/AAAAAAAAnKI/Mri1lcRJ7Yg/s320/IMG_20131113_195437.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligado o segundo motor em rotação mínima.<br/>
Consumo subiu para 440mA.<br/>
440mA(total)-310mA=130mA(motor2)<br/>
<br/>
<br/></td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-JGrXZVCqgkw/UoQLtbWEwvI/AAAAAAAAnKY/8aqdtVp-BqA/s1600/IMG_20131113_195504.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-JGrXZVCqgkw/UoQLtbWEwvI/AAAAAAAAnKY/8aqdtVp-BqA/s320/IMG_20131113_195504.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligado o terceiro motor em rotação mínima.<br/>
Consumo subiu para 670mA.<br/>
670mA(total)-440mA=230mA(motor3)<br/>
<br/></td></tr>
</tbody></table>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-ViDRHV2I2sk/UoQMb4yNmJI/AAAAAAAAnKs/IPDS_g0jQcg/s1600/IMG_20131113_195538.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-ViDRHV2I2sk/UoQMb4yNmJI/AAAAAAAAnKs/IPDS_g0jQcg/s320/IMG_20131113_195538.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligado todos os motores.<br/>
Consumo total de 800mA.<br/>
800mA(total)-670mA=130mA(motor4)<br/>
<br/></td></tr>
</tbody></table>

<div>
Conclusão, tem algo errado no motor 3, está consumindo 100mA a mais que os outros.</div>

<div>
Será o motor?</div>

<div>
Será o ESC? Será a configuraão do ESC, andei testando um emulador de program card que pode ter detonado com a configuração padrão do ESC.</div>

<div>
Será os cabos?</div>

<div>
Será a solda?</div>

<div>
Quando descobrir o que é conto para vocês.</div>

<div>
<br/></div>

<div>
<br/></div>