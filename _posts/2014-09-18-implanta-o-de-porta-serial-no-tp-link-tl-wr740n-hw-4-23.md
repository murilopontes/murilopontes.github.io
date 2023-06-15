---
layout: post
title: Implantação de porta serial no TP-Link TL-WR740N HW 4.23
categories:
 - TP-Link
date: 2014-09-18 05:07:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
o TP-Link WR740N é um SOC Atheros AR9331 com 32MB de RAM e 4MB de flash, dá para montar um drone com ele. Para começar vou soldar a porta serial de debug.<br/>
<br/>
<a name="more"></a><br/><br/>
(datasheet:&nbsp;<a href="http://www.openhacks.com/uploadsproductos/ar9331_datasheet.pdf">http://www.openhacks.com/uploadsproductos/ar9331_datasheet.pdf</a>):<br/>
<ul style="text-align: left;">
<li>CPU MIPS 32-bit 400MHz</li>
<li>32MB RAM</li>
<li>4MB FLASH via SPI</li>
<li>WiFi b/g/n 150 mbit/s</li>
<li>5 portas ethernet 100 mbit/s</li>
<li>29 GPIOs - pelo menos 10 de fácil acesso nos leds e botões</li>
<li>USB com raspadinha (<a href="https://forum.openwrt.org/viewtopic.php?id=37368">https://forum.openwrt.org/viewtopic.php?id=37368</a>)</li>
<li>Interfaces I2C de 83KHz via software GPIO</li>
<li>SPI dedicado para flash</li>
<li>UART via J1</li>
<li>8 Leds de usuário via GPIO - sendo 2 com lógica invertida</li>
<li>2 botões de usuário via GPIO</li>
</ul>
Ótima placa mãe para Drone já com WiFi por cerca de R$44, ou seja, menos de 2 hamburguês em fast-food.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-_zH3ZfLAq2A/VBpTDRaOfHI/AAAAAAAAs9o/JpRlPF1rO7g/s1600/wrt740%2B-%2B6" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="213" src="http://1.bp.blogspot.com/-_zH3ZfLAq2A/VBpTDRaOfHI/AAAAAAAAs9o/JpRlPF1rO7g/s1600/wrt740%2B-%2B6" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N ainda virgem</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-_QOz9wWdTHc/VBpTDVDBNYI/AAAAAAAAs90/SVcGUmbY_Mc/s1600/wrt740%2B-%2B7" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="213" src="http://4.bp.blogspot.com/-_QOz9wWdTHc/VBpTDVDBNYI/AAAAAAAAs90/SVcGUmbY_Mc/s1600/wrt740%2B-%2B7" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">TP-Link TL-WR740N &nbsp;Aberto,<br/>
só 2 parafusos embaixo das borrachas dos pés traseiros.</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-SefcTs8Jw8k/VBpTDU5bWqI/AAAAAAAAs_U/hmVIRupd5nw/s1600/wrt740%2B-%2B15" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="213" src="http://4.bp.blogspot.com/-SefcTs8Jw8k/VBpTDU5bWqI/AAAAAAAAs_U/hmVIRupd5nw/s1600/wrt740%2B-%2B15" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N peso total de 188 gramas</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-dLZh6DVnoiQ/VBpTDTDE69I/AAAAAAAAs-A/u5deA5r8py8/s1600/wrt740%2B-%2B8" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="213" src="http://3.bp.blogspot.com/-dLZh6DVnoiQ/VBpTDTDE69I/AAAAAAAAs-A/u5deA5r8py8/s1600/wrt740%2B-%2B8" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N sem a tampa de cima fica só 133 gramas</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-KIoyN5D49bs/VBpTDZeXgEI/AAAAAAAAs-k/kjWT1OrgIIE/s1600/wrt740%2B-%2B11" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="213" src="http://1.bp.blogspot.com/-KIoyN5D49bs/VBpTDZeXgEI/AAAAAAAAs-k/kjWT1OrgIIE/s1600/wrt740%2B-%2B11" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N incríveis 70 gramas sem a carcaça branca, <br/>
está ficando interessante para voar</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-7oOXlB1qIVY/VBpTDRXEI6I/AAAAAAAAs8s/BYtbPK0jI3o/s1600/wrt740%2B-%2B1" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="320" src="http://4.bp.blogspot.com/-7oOXlB1qIVY/VBpTDRXEI6I/AAAAAAAAs8s/BYtbPK0jI3o/s1600/wrt740%2B-%2B1" width="213"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N removida a solda do J1 (porta serial)</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-p4dFaKA7bN0/VBpTDcOAD1I/AAAAAAAAs-w/LoPqlvHkTpk/s1600/wrt740%2B-%2B12" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="320" src="http://1.bp.blogspot.com/-p4dFaKA7bN0/VBpTDcOAD1I/AAAAAAAAs-w/LoPqlvHkTpk/s1600/wrt740%2B-%2B12" width="213"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N &nbsp;barra de pino soldada, é de 2,54mm.<br/>
<br/></td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://1.bp.blogspot.com/-Yjxz3dXEzNM/VBpTDdClueI/AAAAAAAAs-Y/tsLHH8-56HQ/s1600/wrt740%2B-%2B10" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="213" src="http://1.bp.blogspot.com/-Yjxz3dXEzNM/VBpTDdClueI/AAAAAAAAs-Y/tsLHH8-56HQ/s1600/wrt740%2B-%2B10" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">TP-Link TL-WR740N &nbsp;face inferior da PCB</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-8rDs4Bzm_jA/VBpTDZa8IhI/AAAAAAAAs-M/6_VK6Tr0tbU/s1600/wrt740%2B-%2B9" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="320" src="http://2.bp.blogspot.com/-8rDs4Bzm_jA/VBpTDZa8IhI/AAAAAAAAs-M/6_VK6Tr0tbU/s1600/wrt740%2B-%2B9" width="213"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N &nbsp;- O testpoint TP18 é o TX da USART, fácil de conferir usando Buspirate.</td></tr>
</tbody></table>
<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-kV4xlMUdlq0/VBpTDf2k9rI/AAAAAAAAs84/8lJyTq1xbHY/s1600/wrt740%2B-%2B2" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="213" src="http://4.bp.blogspot.com/-kV4xlMUdlq0/VBpTDf2k9rI/AAAAAAAAs84/8lJyTq1xbHY/s1600/wrt740%2B-%2B2" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N - Solda TX no J1</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-jlbqxvBErD0/VBpTDSjs1qI/AAAAAAAAs9c/yCJ8NJFyzeE/s1600/wrt740%2B-%2B5" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="213" src="http://2.bp.blogspot.com/-jlbqxvBErD0/VBpTDSjs1qI/AAAAAAAAs9c/yCJ8NJFyzeE/s1600/wrt740%2B-%2B5" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N &nbsp;- Solda TX no TP18</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-TuHJPcuIK5s/VBpTDYzb7yI/AAAAAAAAs9E/2GQurc5Ktn4/s1600/wrt740%2B-%2B3" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="213" src="http://2.bp.blogspot.com/-TuHJPcuIK5s/VBpTDYzb7yI/AAAAAAAAs9E/2GQurc5Ktn4/s1600/wrt740%2B-%2B3" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TP-Link TL-WR740N - Porta serial implantada com sucesso!<br/>
Agora é só usar um PL2303, FTDI232, Buspirate, ou qualquer outra USB-Serial de 3,3v<br/>
com minicom, putty, teraterm, .....<br/>
para entrar no terminal do Linux&nbsp;</td></tr>
</tbody></table>
Pinout:<br/>
J1-1 TX<br/>
J1-2 RX<br/>
J1-3 GND<br/>
J1-4 3.3V<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-i-mZYMby_kA/VB68IJJg9jI/AAAAAAAAs_0/hM5Xh7UB6EI/s1600/wr740n-openwrt-serial.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="189" src="http://1.bp.blogspot.com/-i-mZYMby_kA/VB68IJJg9jI/AAAAAAAAs_0/hM5Xh7UB6EI/s1600/wr740n-openwrt-serial.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Minicom conectado no TP-Link TL-WR740N usando um PL2303 na porta serial implantada</td></tr>
</tbody></table>
<br/>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
</div>