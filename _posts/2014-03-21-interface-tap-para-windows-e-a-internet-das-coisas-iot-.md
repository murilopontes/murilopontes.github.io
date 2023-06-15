---
layout: post
title: Interface TAP para Windows e a internet das coisas (IoT)
categories:
 - Linux
date: 2014-03-21 03:37:00 +0000
---

<div class="separator" style="clear: both; text-align: left;">
As interfaces TAP servem com uma placa de rede virtual para injetar pacotes de rede diretamente no kernel do sistema operacional. No caso do Linux isso já é bastante antigo e comum de ser feito. No Windows isso era impossível até pouco tempo atrás. </div>

<a name="more"></a>O projeto OpenVPN, além de implementar VPN para windows, também mantêm o projeto TAP-Windows.  

<div class="separator" style="clear: both; text-align: left;">
<br/></div>

<div class="separator" style="clear: both; text-align: left;">
Você por estar baixando o pacote de instalação:</div>

<div class="separator" style="clear: both; text-align: left;">
http://swupdate.openvpn.org/community/releases/tap-windows-9.9.2_3.exe</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-BHP3hKlhk0M/UyuxVNoHIJI/AAAAAAAApcw/05_IKVQM12g/s1600/tap-interface.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="177" src="http://4.bp.blogspot.com/-BHP3hKlhk0M/UyuxVNoHIJI/AAAAAAAApcw/05_IKVQM12g/s1600/tap-interface.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">TAP em camadas</td></tr>
</tbody></table>

  

Mais detalhes na wiki do OpenWSN Berkeley (internet das coisas / rede de sensores)  

https://openwsn.atlassian.net/wiki/pages/viewpage.action?pageId=5373971  

  

Nesta página tem uma implementação em C# para &nbsp;testar o TAP, mas possui algum problemas com o Windows 8.1, para resolver esses problemas criei um github gist com o código corrigido para Windows 8.1 com Visual Studio 2013.  

http://www.varsanofiev.com/inside/using_tuntap_under_windows.htm  

  

Também existe uma versão em Python 2.7 com python-win32  

https://openwsn.atlassian.net/wiki/download/attachments/5963834/tun-ping-responder.py?api=v2  

  

Código corrigido para Windows 8.1  

  

<div>
<br/></div>

<script src="https://gist.github.com/murix/9678872.js"></script>