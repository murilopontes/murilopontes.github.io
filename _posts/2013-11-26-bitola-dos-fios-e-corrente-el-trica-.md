---
layout: post
title: Bitola dos fios e corrente elétrica 
categories:
 - bitola
date: 2013-11-26 16:00:00 +0000
---

Antes que seu Drone exploda por causa de conexões elétricas subdimensionadas, verifique a tabela deste post e veja se algum fio ficou dimensionado abaixo da corrente máxima esperada.  

  

<a name="more"></a>  
  

AWG - é o padrão americano para padronização de cabos e fios.  

  

Resumindo o artigo da Wikipedia para os cabos que podem ser comprados na hobbyking e no comercio local de Recife-PE, ficamos com as seguintes opções.  

  

AWG - mm - fusível em 10s - isolado temperatura 60~90C  

26 AWG - 0,40mm - 10A - (servos)  

20 AWG - 0,81mm - 58A -  

<span style="color: #38761d;">__18 AWG - 1,02mm - 83A - 14A - (usado nos cabos breakout pós-bifurcação)__</span>  

__<span style="color: #38761d;">16 AWG - 1,29mm - 117A - 18A (saída&nbsp;do ESC para o motor / entrada do ESC)</span>__  

<span style="color: #38761d;">__14 AWG - 1,62mm - 166A - 20~25A (usado nos adaptadores, e cabos breakout pré-bifurcação)__</span>  

<span style="color: #38761d;">__12 AWG - 2,05mm - 235A - 25~30A (usado na maioria dos cabos de 10 cm para adaptadores)__</span>  

10 AWG - 2,58mm - 333A - 30~40A -  

8 AWG &nbsp;- 3,2mm - 472A - 40~55A  

[&nbsp;[http://en.wikipedia.org/wiki/American\_wire\_gauge](http://en.wikipedia.org/wiki/American_wire_gauge)]  

<div>
<br/></div>

<div>
Observe que todo fio é um fusível se você insistir em passar uma corrente maior do que ele suporta.</div>

<div>
O fluxo máximo de elétrons no fio é proporcional a área de seção transversal do fio.</div>

<div>
Portanto lembre-se que tudo tem um limite!&nbsp;</div>

<div>
Também é importante lembrar praticamente tudo sofre efeito da temperatura.</div>

<div>
<br/></div>

<div>
Vamos a um exemplo, prático:</div>

<div>
37 AWG - 0,11mm - corrente de fusão de 3A em 10s.</div>

<div>
Quem lembra do fusível que achamos nas réguas e estabilizadores de PC?</div>

<div>
Pois bem, eles são feito com fio 37 AWG ou semelhante.</div>

<div>
Geralmente pode ser mais fino ou mais fácil de derreter do que cobre, pois se for esperar os 10 segundos a 3A para derreter o cobre, já tem queimado tudo. Acredito que já deu para pegar o espírito da coisa.</div>

<div>
<br/></div>

<div>
No caso dos motores A2212/13T a corrente máxima é de 12A,</div>

a fonte vai precisa enviar 12A x 4 = 48A, portanto o fio mais adequado para o cabo de distribuição  

é o 8 AWG ou 3,2 mm. No entanto o mais próximo de 3,2 mm encontrado em Recife-PE é 2,5 mm.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-EzudjteyDIU/UpjzmDCDl1I/AAAAAAAAnfA/ORH4KPfGRq0/s1600/IMG_20131129_170534.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-EzudjteyDIU/UpjzmDCDl1I/AAAAAAAAnfA/ORH4KPfGRq0/s320/IMG_20131129_170534.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">10 metros 2,5 mm2 2,91Kg/100m -&gt; 10m 291gramas.<br/>
Para voar fica 291 x 2 = 582 gramas.<br/>
classe térmica 70º, isolação de PVC.<br/>
corrente máxima de 21~25A.<br/>
Em teoria é o equivalente ao 10 AWG.<br/>
Talvez o cabo de 1,5 mm2 / 14 AWG pode ser uma alternativa também.</td></tr>
</tbody></table>

  

  

Obviamente que todo curioso não vai resistir a tentar passar mais do que pode pelo fio para testar se a teoria está certa. Meu conselho é não desistir de tentar pelo bem da ciência, mas lembre-se de fazer forma segura e esteja preparado para qualquer explosão ou pipoco ou conversão em plasma ou sublimação!!!!!  

Esse é o espírito do DIY, só aprende fazendo.  

  

  

  