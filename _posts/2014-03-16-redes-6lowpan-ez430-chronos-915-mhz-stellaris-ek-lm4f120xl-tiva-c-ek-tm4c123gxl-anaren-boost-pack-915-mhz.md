---
layout: post
title: Redes 6LoWPAN- ez430-Chronos 915 Mhz, Stellaris EK-LM4F120XL / Tiva C EK-TM4C123GXL  + Anaren Boost Pack 915 MHz
categories:
 - EK-LM4F120XL
date: 2014-03-16 06:55:00 +0000
---

<div>
Chegaram os módulos Anaren 915MHz para montar a rede de teste RF.</div>

<div>
<a name="more"></a><br/></div>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-AqqwPXv4Ydg/UyVHjCYDWEI/AAAAAAAApXE/J8Q9sy7P308/s1600/IMG_20140316_033549.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://3.bp.blogspot.com/-AqqwPXv4Ydg/UyVHjCYDWEI/AAAAAAAApXE/J8Q9sy7P308/s1600/IMG_20140316_033549.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Border router: PC com Linux usando o Access Point RF do ez430-Chronos 915 MHz<br/>
O Access Point é um MSP430F5509 - 4k RAM 24k FLASH&nbsp;+ CC1101.<br/>
Módulos de rede: Stellaris e/ou Tiva com Contiki-OS usando o Anaren Boost Pack 915 MHz<br/>
ez430 Chronos (CC430F6137 - 4k RAM e 32k FLASH) &nbsp;- funcionando como controle remoto.</td></tr>
</tbody></table>

Em breve resultados desta rede funcionando no controle de várias tarefas de automação.  

  

O chip do boost pack anaren ($19 um par) é o CC110L que é uma versão "pelada" do CC1101.  

Aqui está a lista do que foi removido do CC1101 ($1,65) para criar o CC110L ($1,45)  

1) Forward error correction (FEC) and interleaving  

2) Wake-on-Radio (WOR) and RCOSC (no RX timeout possible)  

3) Data Whitening  

4) Preamble quality threshold (PQT) indication (used to gate sync word detection)  

5) Link quality (LQI) indication (received signal strength (RSSI) is supported in Value Line parts)  

6) Temp sensor  

7) PA ramping and shaping  

8) MSK and ASK modulation (OOK modulation is supported in Value Line parts)  

9) No pin control for strobe commands (SPI strobe commands need to be used)  

10) ATEST removed  

<div>
<br/></div>

A antena embutida do boost pack da Anaren funciona&nbsp;868-870MHz e 902-928MHz.  

Ou seja, dá para fazer um sniffer ou analisador de espectro na faixa de 868MHz até 928 MHz.  

  

Teste de alcance em 868 MHz / 915 MHz com 10 dbm (10mW):  

* Com baudrate mínimo  

260 yards = 238 metros  

* Com baudrate máximo  

194 yards = 178 metros (perdeu 60 metros com o aumento do baudrate)  

  

No mercado chinês, o boost pack que custa $19 o par, ou $9,5 a unidade,  

tem seu equivalente vendido por $3,17 com CC110L.  

E a versão com CC1101 sai por $3,19.  

Muito mais barato e ainda dá para escolher a frequência 315/433/868/915 MHz.  

  

  

  

  

  