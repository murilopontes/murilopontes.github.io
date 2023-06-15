---
layout: post
title: imax b6 battery charger- usb pinout and logview
categories:
 - Taranis
date: 2015-06-06 04:48:00 +0100
---

O carregador imax b6 e seus clones possuem um entrada configurável para o sensor de temperatura LM35 ou para Serial / UART - TX - TTL.  

<div>
<br/>
<div>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-ndJBUDO0LOU/VXJqyS3ZUOI/AAAAAAABJIc/_nDO6_js89Q/s1600/IMAX_B6_LM35_Temp_Sensor_Wiring.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="170" src="http://2.bp.blogspot.com/-ndJBUDO0LOU/VXJqyS3ZUOI/AAAAAAABJIc/_nDO6_js89Q/s400/IMAX_B6_LM35_Temp_Sensor_Wiring.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pinout IMAX B6</td></tr>
</tbody></table>
<br/>
<br/>
<table border="1" style="background-color: #f0f0f0; border-collapse: collapse; color: black; font-family: Tahoma, Arial, sans-serif; font-size: 14.8000001907349px; font-stretch: normal; margin: 0px auto; padding: 0px; text-align: justify; width: 298px;"><tbody style="font-size: 0.85em; font-stretch: normal; margin: 0px; padding: 0px;">
<tr style="font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;"><th align="center" style="background-color: #e6e6e6; border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;">Pin<br/>
Number</th><th align="center" style="background-color: #e6e6e6; border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;">Pin<br/>
Name</th><th align="center" style="background-color: #e6e6e6; border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;">Description</th></tr>
<tr style="font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;"><td align="center" style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">1</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">+5V</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">+5V for LM35 Temperature sensor</td></tr>
<tr style="font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;"><td align="center" style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">2</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">DATA</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">TTL TX for Logging or V-Out of LM35</td></tr>
<tr style="font-size: 1em; font-stretch: normal; margin: 0px; padding: 0px;"><td align="center" style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">3</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">GND</td><td style="border: 1px solid black; font-size: 1em; font-stretch: normal; margin: 0px; padding: 3px 5px;">GND</td></tr>
</tbody></table>
<br/>
<br/>
Quando configurado como Serial é preciso ligar o RX de um cabo USB-TTL no TX do IMAX6.</div>
<div>
Depois é só abrir o <a href="http://logview.info/forum/index.php?resources/logview-v2.1/" target="_blank">logview </a>e acompanhar o progresso de carga e descarga das baterias.<br/>
<br/>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-kKvFJP7OATw/VXJqHgZVJ9I/AAAAAAABJIU/lqJHEHGBXi8/s1600/imax-b6-logview.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="311" src="http://2.bp.blogspot.com/-kKvFJP7OATw/VXJqHgZVJ9I/AAAAAAABJIU/lqJHEHGBXi8/s400/imax-b6-logview.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">logview 2.7.6 monitorando a carga da bateria NiMH de 2000mah do Taranis</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-brt7c_40pWs/VXJtHGU8RbI/AAAAAAABJI8/Tou8HonHFuA/s1600/IMG_20150606_004530.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-brt7c_40pWs/VXJtHGU8RbI/AAAAAAABJI8/Tou8HonHFuA/s320/IMG_20150606_004530.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Essa bateria tem de carregar com 0.1A até chegar em 8.4V são quase 20 horas para carregar completamente.</td></tr>
</tbody></table>
<div>
<br/></div>
</div>
</div>