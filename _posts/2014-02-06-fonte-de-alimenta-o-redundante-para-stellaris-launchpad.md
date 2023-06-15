---
layout: post
title: Fonte de alimentação redundante para Stellaris Launchpad
categories:
 - fonte
date: 2014-02-06 02:30:00 +0000
---

Tutorial completo de instalação.

<div>
<a name="more"></a><br/><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-nvqoARhn4Cg/UvLwmOWfuNI/AAAAAAAAowU/rJ_er6Uj_S8/s1600/IMG_20140205_211704.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-nvqoARhn4Cg/UvLwmOWfuNI/AAAAAAAAowU/rJ_er6Uj_S8/s1600/IMG_20140205_211704.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Novo ferro de solda Tramontina por R$26</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-OEQM07gjrOg/UvLwmA4RFqI/AAAAAAAAowU/bwdz_hYINI0/s1600/IMG_20140205_193701.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://4.bp.blogspot.com/-OEQM07gjrOg/UvLwmA4RFqI/AAAAAAAAowU/bwdz_hYINI0/s1600/IMG_20140205_193701.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Medindo a tensão depois de instalar um diodo 1N4007 na entrada do VBUS (para permitir alimentação redundante via USB. fonte externa, bateria,...[cada fonte extra precisa de um diodo 1N4007])<br/>
Com 4,22V o reset fica preso, por causa do monitor de tensão U4, que desligar tudo se der menos de 4,83V.<br/>
A solução é remover o monitor de tensão U4 na Stellaris Launchpad.<br/>
No caso da Tiva C Series Launchpad o monitor de tensão U4 não vem instalado, provavelmente durante a revisão da PCB já levaram em consideração a possibilidade de alimentação a placa com LiPo de 1 célula.</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-renVbc9ojQg/UvLwmLfSHjI/AAAAAAAAowU/vDMZpulpY54/s1600/IMG_20140205_193345.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-renVbc9ojQg/UvLwmLfSHjI/AAAAAAAAowU/vDMZpulpY54/s1600/IMG_20140205_193345.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">U4 removido, reset funcionando sem problemas.<br/>
Detalhe: é preciso manter a chave power select na posição device e não nunca ligar um usb na porta device.<br/>
Um outra alternativa é, remover a chave completamente e usar mais um diodo para permitir ligar as duas portas usb sem problemas &nbsp;quando houver alimentação externa no VBUS (bateria, BEC do ESC, ...)</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-hbQ4rlC-fTk/UvLwmAvVncI/AAAAAAAAowU/GF8sfmEr8LQ/s1600/IMG_20140205_164923.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://2.bp.blogspot.com/-hbQ4rlC-fTk/UvLwmAvVncI/AAAAAAAAowU/GF8sfmEr8LQ/s1600/IMG_20140205_164923.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Instalando um diodo 1N4148 na entrada do VBUS, corrente máxima de 300mA.<br/>
Mas não certo, no primeiro curto de GND com VCC, o 1N4148 abriu, parecendo um fusível.<br/>
Se não fosse o curto, acidental funcionaria sem problema já que a placa toda consome cerca de 10mA.&nbsp;</td></tr>
</tbody></table>
<br/>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-R53qzCuaGdA/UvLwmMu-XSI/AAAAAAAAowU/TL0FPQRuIiQ/s1600/IMG_20140205_160021.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="320" src="http://2.bp.blogspot.com/-R53qzCuaGdA/UvLwmMu-XSI/AAAAAAAAowU/TL0FPQRuIiQ/s1600/IMG_20140205_160021.jpg" width="240"/></a></div>
<div class="separator" style="clear: both; text-align: center;">
Medindo o consome da placa. Com tudo ativado ficou estagnado em menos de 10mA.</div>
<br/></div>