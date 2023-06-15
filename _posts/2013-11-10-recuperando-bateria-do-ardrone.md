---
layout: post
title: Recuperando bateria do ardrone
categories:
 - bateria
date: 2013-11-10 02:33:00 +0000
---

<div style="text-align: justify;">
Passos para o sucesso:<br/>
1) descarregar a bateria entre 9,53V (3,2V por célula) e 10,3V (3,43V por célula)&nbsp;</div>

<div style="text-align: justify;">
2) deixar carregar até 12,5V (4,16V por célula)</div>

<div>
<br/>
<a name="more"></a><br/></div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-X9CD7tL_H8g/Un-Lr0CEI6I/AAAAAAAAnDo/N93DKUbY34o/s1600/2013-11-10+10.15.17.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-X9CD7tL_H8g/Un-Lr0CEI6I/AAAAAAAAnDo/N93DKUbY34o/s320/2013-11-10+10.15.17.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Com 9,58V o ar.drone liga com LEDs vermelhos (ok, durante o boot do Linux),<br/>
depois fica verde (Linux ok), ainda dá para conectar e ver o 0% de bateria.<br/>
Porém em menos de 10 segundos todos os LEDs apagam.<br/>
Sinal que o sistema de sobre-descarga da bateria está funcionando ok.<br/>
<br/></td></tr>
</tbody></table>

<div>
Durante o processo de recuperação os leds do carregador podem piscar aleatoriamente, e depois de algum tempo quando a bateria estabilizar nos 11V, geralmente somente o LED de status ficaram vermelho sem piscar. Ignore esse LED e monitore pelo multimetro. Quando chegar em 12,5V já está pronto usar novamente.</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-mRxbf8rSgug/Un7vxn7-bQI/AAAAAAAAnDY/znA8i5NJ1aM/s1600/IMG_20131109_163508.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-mRxbf8rSgug/Un7vxn7-bQI/AAAAAAAAnDY/znA8i5NJ1aM/s320/IMG_20131109_163508.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Carregador do AR.Drone V1 fica piscando verde e vermelho.<br/>
O LED de status parece que não sabe o que está fazendo.</td></tr>
</tbody></table>

Lembre-se de carregar a bateria longe de qualquer material inflamável. E se a bateria estiver estufada ou buxuda é melhor não carregar mais, que a chance de exploir é maior. Se após duas horas a bateria não atingir os 12,5V é sinal que o degaste interno atingiu um nível próximo do máximo.  

  

  

  