---
layout: page
title: Drone- ESC, Motors, Propellers
categories:
 - page
date: 2016-07-31 20:00:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-Dda_gvmz0_o/VFN_iH65bJI/AAAAAAAAthQ/CDkYxgEPHHI/s1600/kit-esc-motor-helice.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="196" src="https://3.bp.blogspot.com/-Dda_gvmz0_o/VFN_iH65bJI/AAAAAAAAthQ/CDkYxgEPHHI/s1600/kit-esc-motor-helice.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Kit ESC+Motor+hélice<br/>
<br/>
<span style="font-size: small; text-align: left;"><a href="http://www.aliexpress.com/item/A2212-1000KV-Brushless-Outrunner-Motor-30A-ESC-1045-Propeller-1-pair-Quad-Rotor-Set-for-RC/1934298152.html">http://www.aliexpress.com/item/A2212-1000KV-Brushless-Outrunner-Motor-30A-ESC-1045-Propeller-1-pair-Quad-Rotor-Set-for-RC/1934298152.html</a></span></td></tr>
</tbody></table>
ESC: o controlador de velocidade eletrônica para motores Brushless geralmente tem como entrada um sinal PWM de até 490Hz, o duty-cycle do PWM determina a velocidade do motor.<br/>
Praticamente todos os ESC precisam ser calibrados para funciona corretamente.<br/>
Geralmente se liga o ESC com o PWM no máximo e depois de 3 segundos é mínimo para o PWM mínimo. E a corrente suportada pelo ESC deve ser sempre maior do que a corrente máxima suportada pelo motor, uma margem de folga de 20% já fica bom.<br/>
<br/>
Motores Brushless: Geralmente são motores trifásicos sem escovas que precisam de um ESC para regular a sua velocidade. Existem modelos inrunner (onde só o miolo gira com baixo torque e alta velocidade) e outrunner (onde a carcaça gira com alto torque e baixa velocidade). Os motores inrunner consome menos corrente mas precisam de uma completa mecânica (gearbox) para fixar a hélice, como exemplo temos o Ardrone v1 e v2 onde os 4 motores juntos no máximo consomem 3A. Os motores outrunner não precisam de nenhum mecânica especial para fixar as hélices, o que reduz bastante a complexidade dos projetos, porém o consumo de corrente é muito alto, como exemplo temos os motores A2212/13T 1000kv que consome no máximo 12A cada, 48A se forem quatro.<br/>
<br/>
Motores Brushed: Geralmente são motores bifásicos com escovas e podem tem a velocidade controlada diretamente por um transistor FET, alto torque e boa velocidade, o problema maior é a vida útil das escovas relativamente pequena e o alto ruido irritante.<br/>
<br/>
Hélices: Precisam ser escolhida para maximizar o empuxo e minimizar o consumo de corrente. Mas também precisa observar o tamanho máximo pois uma hélice muito grande em rotação máximo pode queimar o motor com excesso de corrente por conta do esforço provocado pelo resistência do ar. A hélice também não pode ser pequena demais sem o empuxo não será suficiente para subir. Um critério bom de escolha é usar a hélice que permita a eficiência máxima do motor.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-wPsxz_S8yGs/VFNj2oKw0-I/AAAAAAAAthA/cH-sgE1kqSc/s1600/a2212-13t-eficiencia.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="230" src="https://1.bp.blogspot.com/-wPsxz_S8yGs/VFNj2oKw0-I/AAAAAAAAthA/cH-sgE1kqSc/s1600/a2212-13t-eficiencia.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Gráfico da eficiência do motor a2212/13</td></tr>
</tbody></table>
<br/>
O site Flybrushless tem um banco de dados muito bom sobre a combinação de motores e hélices.<br/>
Um exemplo é o motor a2212/13 que tem sua eficiência máxima atingida por volta dos 4A, após os 6A é possível notar a perda de eficiência, de forma que injetar mais corrente só vai fazer aquecer o motor invés de gerar mais rotações, pois o motor já está saturado.<br/>
<br/>
Com hélices 8x6, 9x5, 10x4.5 um motor a2212/13 funciona bem e gera um empuxo de 600 a 800 gramas. Com quatro daria um empuxo de 3.2kg no máximo. O empuxo tem de ser maior do que o peso total do UAV. Empiricamente se usa um empuxo de pelo menos 2 vezes o peso do UAV para voar calmamente em 2d. Para voar em 3d com manobras radicais é preciso de um empuxo de pelo menos 3 vezes o peso do UAV.<br/>
<br/>
<br/>
Referências::<br/>
<a href="http://www.flybrushless.com/motor/view/206">http://www.flybrushless.com/motor/view/206</a><br/>
<br/>
<br/>
<br/>
<br/></div>