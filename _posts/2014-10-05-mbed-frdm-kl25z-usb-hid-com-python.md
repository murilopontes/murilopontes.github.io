---
layout: post
title: MBED FRDM-KL25Z USB HID com Python
categories:
 - usb hid
date: 2014-10-05 04:40:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Tutorial de como usar a KL25Z como um dispositivo USB HID usando a plataforma da MBED.<br/>
E a comunicação usando Python com USB lib.<br/>
<br/>
<a name="more"></a><br/><br/>
<br/>
Importar, compilar e arrastar para a FRDM-KL25Z<br/>
https://developer.mbed.org/compiler/#import:/users/samux/code/USBHID_TestCase/<br/>
<br/>
Este programa vai receber e enviar dados pela interface USB do KL25Z configurada como um dispositivo HID, e também irá usar a porta USB do OpenSDA para mostrar as mensagens enviadas e recebidas pelo dispositivo HID.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-or4TsveSG5c/VDC6-koR76I/AAAAAAAAtHo/CVl66RJz9g4/s1600/IMG_20141005_002640.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-or4TsveSG5c/VDC6-koR76I/AAAAAAAAtHo/CVl66RJz9g4/s1600/IMG_20141005_002640.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A FRDM-KL25Z precisa estar com as duas interfaces conectadas para realizar o teste do USB HID completo&nbsp;</td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<br/>
<br/>
<br/>
Python USB library<br/>
https://github.com/walac/pyusb<br/>
<br/>
Clone Python USB library<br/>
git clone&nbsp;https://github.com/walac/pyusb.git<br/>
<br/>
Install &nbsp;Python USB library<br/>
python setup.py install<br/>
<br/>
Código de teste em python<br/>
------------
<br/>
<script src="https://gist.github.com/murix/f6effc4468cca6f4e8f0.js"></script>

------------

<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-lPzGrzoceck/VDC89wSxrZI/AAAAAAAAtH8/judxCB3Ur5s/s1600/mbed-kl25z-linux-hid.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="133" src="http://4.bp.blogspot.com/-lPzGrzoceck/VDC89wSxrZI/AAAAAAAAtH8/judxCB3Ur5s/s1600/mbed-kl25z-linux-hid.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">MBED detectada pelo Linux sem problemas</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-6mczup071tA/VDC89cyda3I/AAAAAAAAtH4/oNosRAk4QuA/s1600/mbed-kl25z-hid-python-test.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="174" src="http://1.bp.blogspot.com/-6mczup071tA/VDC89cyda3I/AAAAAAAAtH4/oNosRAk4QuA/s1600/mbed-kl25z-hid-python-test.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Script python enviando dados para o USB HID</td></tr>
</tbody></table>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-Os9F8ySOHQY/VDC89sfRRfI/AAAAAAAAtIA/T4f_-xBFZDs/s1600/mbed-kl25z-sda-output.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="205" src="http://1.bp.blogspot.com/-Os9F8ySOHQY/VDC89sfRRfI/AAAAAAAAtIA/T4f_-xBFZDs/s1600/mbed-kl25z-sda-output.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Console OpenSDA da MBED mostrando tudo que foi recebido.</td></tr>
</tbody></table>
<div>
<br/></div>
</div>