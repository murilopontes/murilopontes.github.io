---
layout: post
title: Programando PIC18F24J50 com MPLABX e XC8, debug com Pickit2 e Buspirate
categories:
 - post
date: 2014-06-13 03:32:00 +0100
---

<div class="separator" style="clear: both; text-align: center;">
</div>

Template de código para&nbsp;PIC18F24J50 usando compilador XC8.  

  

<a name="more"></a>  

A compilação pode ser feita na IDE MPLABX ou MPLAB 9.82 no entanto somente o MPLAB 9.82 tem suporte para o Pickit 2.  

Um detalhe é que quando o código é gravado como debug, só ira funcionar junto com a ferramenta de debug. Para ter um sistema que ligue junto com a energia é preciso ter gravado usando o modo "programmer" do Pickit 2.  

  

O código de exemplo que preparei fica piscando o LED no pino RA0 e então uma string de contador pela USART com baudrate de 115200 bps.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-tgDGtyJ2zig/U5pkiyFTObI/AAAAAAAArr8/DnIGJxO54-Y/s1600/IMG_20140612_233949.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-tgDGtyJ2zig/U5pkiyFTObI/AAAAAAAArr8/DnIGJxO54-Y/s1600/IMG_20140612_233949.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Debugger Pickit2<br/>
PIC18F24J50 na protoboard com cristal de 20 Mhz capacitores de 22pF, LED, e diodo 1N4148 no MCLR<br/>
Buspirate v3.6 conectado na serial do PIC18F24J50 para fazer o teste de baudrate</td></tr>
</tbody></table>

  

  

  

  

<script src="https://gist.github.com/murix/00488d2e99c52ac59a01.js"></script>