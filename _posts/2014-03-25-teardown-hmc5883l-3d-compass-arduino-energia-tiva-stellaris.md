---
layout: post
title: Teardown HMC5883L 3D compass + Arduino + Energia + Tiva/Stellaris
categories:
 - post
date: 2014-03-25 04:30:00 +0000
---

Testando HMC5883 no Arduino e Energia

<div>
<a name="more"></a><br/><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-KJVE00-OlJs/UzEFEdPadQI/AAAAAAAApkI/gjvsayOTS6o/s1600/IMG_20140325_011950.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-KJVE00-OlJs/UzEFEdPadQI/AAAAAAAApkI/gjvsayOTS6o/s1600/IMG_20140325_011950.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">HMC5883L&nbsp;+ Arduino Nano V3<br/>
HMC5883L&nbsp;+ Stellaris LM4F120</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-pM5UkKraRvo/UzEG7QfOipI/AAAAAAAApkY/n9VIEzHxcAw/s1600/HMC5883-console.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="183" src="http://4.bp.blogspot.com/-pM5UkKraRvo/UzEG7QfOipI/AAAAAAAApkY/n9VIEzHxcAw/s1600/HMC5883-console.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">HMC5583L console</td></tr>
</tbody></table>
<br/>
Arduino Driver<br/>
<br/>
<script src="https://gist.github.com/murix/9755203.js"></script>

Tiva/Stellaris/Energia Driver<br/>
A biblioteca I2C do Energia precisa de alguns ajustes adicionais em relação ao Arduino oficial.<br/>
<br/>
<script src="https://gist.github.com/murix/9755193.js"></script>
</div>