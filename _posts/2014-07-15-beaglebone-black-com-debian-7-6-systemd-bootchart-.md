---
layout: post
title: Beaglebone Black com Debian 7.6 - systemd bootchart 
categories:
 - Debian
date: 2014-07-15 03:01:00 +0100
---

Linux embarcado em menos de 10 segundos.  

O systemd integra todas as ferramentas necessárias para criação do bootchart.  

Para gerar o gráfico em SVG o comando é:  

  

<a name="more"></a>  
  

<span style="background-color: #cfe2f3;">$ systemd-analyze plot &gt; boot.svg</span>  

<span style="background-color: #cfe2f3;">$ firefox boot.svg</span>  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-Z_g-hmWVl2Y/U8SK8WeKXzI/AAAAAAAAsYc/O81tHNVqjMA/s1600/beagleboneblack-systemd.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://2.bp.blogspot.com/-Z_g-hmWVl2Y/U8SK8WeKXzI/AAAAAAAAsYc/O81tHNVqjMA/s1600/beagleboneblack-systemd.png" width="368"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Beaglebone Black bootchart</td></tr>
</tbody></table>

  