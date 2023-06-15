---
layout: post
title: Taranis Plus com telemetria bluetooth hc-06
categories:
 - Taranis
date: 2015-05-19 03:45:00 +0100
---

Um dos recursos do Taranis Plus é a porta serial RS232 no compartimento da bateria.  

<div>
É possível ativar um mirror da telemetria smart port na página 6 de configurações do rádio.</div>

<div>
O baudrate é 57600. E a polaridade é invertida.&nbsp;</div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-ngeARslrlpY/VVqb17vsbtI/AAAAAAABIpM/qRJPiQmKre0/s1600/IMG_20150517_112134.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-ngeARslrlpY/VVqb17vsbtI/AAAAAAABIpM/qRJPiQmKre0/s320/IMG_20150517_112134.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">HC-06 com regulador 7805 soldado, já que o regulador onboard suporta apenas 6V. <br/>
Bateria carregada fornece mais de 8V, dai a necessidade do 7805.&nbsp;</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-DnmS0_b3DMc/VVqb13Ap38I/AAAAAAABIpM/kvumD57q_-k/s1600/IMG_20150517_112117.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-DnmS0_b3DMc/VVqb13Ap38I/AAAAAAABIpM/kvumD57q_-k/s320/IMG_20150517_112117.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Cabo conversor de 2mm (taranis) para 2.54mm (hc-06)</td></tr>
</tbody></table>

<div>
No entanto, esse setup funcionou parcialmente, pois nenhum dos apps para Android conseguiu se comunicar com o controle. Ligando um cabo usb-ttl no PC, e usando o terminal termite com hex dump, não encontrei nenhum 0x7e do protocolo FrSky. Isso indica que a serial do Taranis também deve ser invertida. Para testar esta hipótese sem modificar o hardware, é só usar uma SoftwareSerial invertida no Arduino.</div>

<div>
<br/></div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-rS8G6YvzcM8/VVqfnydhAoI/AAAAAAABIpY/nkDYQx9Fh1c/s1600/software-serial-arduino.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="53" src="http://1.bp.blogspot.com/-rS8G6YvzcM8/VVqfnydhAoI/AAAAAAABIpY/nkDYQx9Fh1c/s320/software-serial-arduino.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Software Serial invertida nos pinos 3,2&nbsp;</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-zYOPNy7HSxo/VVqgpsShAMI/AAAAAAABIp0/PVWVvCyDwmY/s1600/IMG_20150518_232851.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-zYOPNy7HSxo/VVqgpsShAMI/AAAAAAABIp0/PVWVvCyDwmY/s320/IMG_20150518_232851.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Arduino nano rodando SoftwareSerial invertida</td></tr>
</tbody></table>

<div>
<br/></div>

<div>
A coisa começou a melhorar, o terminal encheu de 0x7e.</div>

<div>
<br/></div>

<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-YuEF5cc9qdw/VVqgdXfjBXI/AAAAAAABIps/AZ-l241mjWw/s1600/termite-frsky.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="204" src="http://2.bp.blogspot.com/-YuEF5cc9qdw/VVqgdXfjBXI/AAAAAAABIps/AZ-l241mjWw/s320/termite-frsky.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Termite 3.1 com hex dump</td></tr>
</tbody></table>
<div>
Agora é só partir para decodificar o protocolo ou deixar para um app de android fazer isso.</div>
<div>
O mestre do barramento smart port, faz polling dos sensores enviando "0x7e" seguido do id do sensor.</div>
<div>
<br/></div>
<div>
----------- inicio do ciclo</div>
<div>
7e 67&nbsp;</div>
<div>
7e 48&nbsp;</div>
<div>
7e e9&nbsp;</div>
<div>
7e 6a&nbsp;</div>
<div>
7e cb&nbsp;</div>
<div>
7e ac&nbsp;</div>
<div>
7e 0d&nbsp;</div>
<div>
7e 98 10 05 f1 01 2d 08 00 c2&nbsp;</div>
<div>
7e 98 10 01 f1 59 93 00 00 10&nbsp;</div>
<div>
7e 98 10 02 f1 58 00 00 00 a3&nbsp;</div>
<div>
7e 98 10 03 f1 06 00 00 00 f4&nbsp;</div>
<div>
7e 8e&nbsp;</div>
<div>
7e 2f&nbsp;</div>
<div>
7e d0&nbsp;</div>
<div>
7e 71&nbsp;</div>
<div>
7e f2&nbsp;</div>
<div>
7e 53&nbsp;</div>
<div>
7e 34&nbsp;</div>
<div>
7e 95&nbsp;</div>
<div>
7e 16&nbsp;</div>
<div>
7e b7&nbsp;</div>
<div>
7e 39&nbsp;</div>
<div>
7e ba&nbsp;</div>
<div>
7e 1b&nbsp;</div>
<div>
7e 00&nbsp;</div>
<div>
7e a1&nbsp;</div>
<div>
7e 22&nbsp;</div>
<div>
7e 83&nbsp;</div>
<div>
7e e4&nbsp;</div>
<div>
7e 45&nbsp;</div>
<div>
7e c6</div>
<div>
--------------- fim do ciclo</div>
</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-9DHhKlmk8aM/VVqjPwJVi7I/AAAAAAABIqA/WPIDTjNmLEU/s1600/inverter.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="246" src="http://2.bp.blogspot.com/-9DHhKlmk8aM/VVqjPwJVi7I/AAAAAAABIqA/WPIDTjNmLEU/s320/inverter.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Inversor para o TX do Taranis (JP1) conectar no RX do HC-06 (JP2)</td></tr>
</tbody></table>

<div>
<br/></div>

<div>
<br/></div>

<div>
<br/></div>