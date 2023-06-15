---
layout: post
title: Debug eZ430-Chronos Access point 
categories:
 - ez430
date: 2014-05-07 00:27:00 +0100
---

Como depurar o Access point do Kit do&nbsp;eZ430-Chronos se conector do USB não dá para ligar o ez430 e o Access point ao mesmo tempo?  

<div>
<br/>
<a name="more"></a><br/>
<br/>
MSP430 F5509 - 24k Flash - 4k RAM - 2k USB RAM<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><div style="text-align: justify;">
<br/></div>
<a href="http://4.bp.blogspot.com/-JLlFzQirsvA/U2lqOUto24I/AAAAAAAArKE/eYm6hACpgrM/s1600/msp430f5509-cc1101-ez430-usb-emulator.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="395" src="http://4.bp.blogspot.com/-JLlFzQirsvA/U2lqOUto24I/AAAAAAAArKE/eYm6hACpgrM/s1600/msp430f5509-cc1101-ez430-usb-emulator.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><span style="font-size: xx-small; text-align: start;">Access point ( msp430f5509 CC1101 )&nbsp;+&nbsp;ez430-usb (emulator msp430f1612)</span></td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: left;">
A solução passa por arrancar fora as portas USB, e deixar tudo mais conveniente.</div>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-8N-ItqbZYLo/U2lqvPVxDCI/AAAAAAAArKM/NvgNvMrrBg4/s1600/IMG_20140506_195807.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-8N-ItqbZYLo/U2lqvPVxDCI/AAAAAAAArKM/NvgNvMrrBg4/s1600/IMG_20140506_195807.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">ez430-USB e Access point ligados ao mesmo tempo</td></tr>
</tbody></table>
Agora é só depurar com o Code Compose Studio ou IAR.<br/>
<br/>
<br/></div>