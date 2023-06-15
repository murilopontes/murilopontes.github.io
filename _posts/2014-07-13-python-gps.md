---
layout: post
title: Python GPS
categories:
 - GYGPS6MV1
date: 2014-07-13 14:56:00 +0100
---

GPS com Python é jogo rápido  

  

<a name="more"></a>  

  

# instalar os pacotes  

apt-get -y install gpsd python-gps  

  

# adicionar a porta serial do GPS ao daemon  

gpsdctl add /dev/ttyUSB0  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-k-O0UQ2pNqk/U8KPmQTn6PI/AAAAAAAAsWY/ccUdK1bCK4A/s1600/python-gps.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="209" src="http://1.bp.blogspot.com/-k-O0UQ2pNqk/U8KPmQTn6PI/AAAAAAAAsWY/ccUdK1bCK4A/s1600/python-gps.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Saída do Python GPS</td></tr>
</tbody></table>

  

  

<script src="https://gist.github.com/murix/8a7684ea599bf0703665.js"></script>