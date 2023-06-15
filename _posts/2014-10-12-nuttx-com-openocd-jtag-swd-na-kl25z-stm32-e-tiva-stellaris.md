---
layout: post
title: Nuttx com OpenOCD (JTAG/SWD) na KL25Z, STM32 e Tiva/Stellaris
categories:
 - hidapi
date: 2014-10-12 21:21:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Debug step-by-step quase sempre é necessário ou desejável para qualquer projeto.<br/>
Com o Eclipse+CDT+GNU ARM+OpenOCD é possível fazer isso.<br/>
A ideia é executar sistema operacional de tempo real Nuttx passo a passo pelo código fonte.<br/>
<br/>
<a name="more"></a><br/><br/>
<b><u>Instalar o&nbsp;GNU ARM Eclipse</u></b><br/>
<br/>
O guia oficial esta na página do projeto (<a href="http://gnuarmeclipse.livius.net/blog/">http://gnuarmeclipse.livius.net/blog/</a>)<br/>
Mas algumas coisas precisa ser modificadas para funcionar, uma delas é a conexão CMSIS-DAP com a KL25Z que precisa de uma versão recente do OpenOCD com patchs.<br/>
<br/>
<br/>
<b><u>Instalar o hidapi</u></b><br/>
<br/>
O hidapi é uma API para acessar dispositivos USB HID de forma mais fácil que o libUSB.<br/>
<br/>
git clone http://github.com/signal11/hidapi.git<br/>
cd hidapi<br/>
./bootstrap<br/>
./configure<br/>
make<br/>
sudo make install<br/>
<br/>
<u><b>Instalar o openocd com patchs do CMSIS-DAP</b></u><br/>
<br/>
<br/>
git clone http://openocd.zylin.com/openocd<br/>
cd openocd<br/>
./bootstrap<br/>
./configure --enable-maintainer-mode --enable-cmsis-dap --enable-hidapi-libusb<br/>
echo '<br/>
adapter_khz 50<br/>
$_TARGETNAME configure -event gdb-attach {<br/>
&nbsp; &nbsp; halt<br/>
}<br/>
' &gt;&gt; tcl/target/kl25.cfg<br/>
sudo make install<br/>
<br/>
<b><u>Conectar a KL25Z com o OpenSDA da MBED</u></b><br/>
<br/>
Pode conectar assim:<br/>
<br/>
sudo /usr/local/bin/openocd &nbsp;-c "interface cmsis-dap" -f /usr/local/share/openocd/scripts/target/kl25.cfg<br/>
<br/>
Ou assim:<br/>
<br/>
sudo /usr/local/bin/openocd -f /usr/local/share/openocd/scripts/board/frdm-kl25z.cfg<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-XJ9_5twrlWg/VDprkrlyqGI/AAAAAAAAtPQ/DaiY5mFAlwo/s1600/IMG_20141012_085215.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-XJ9_5twrlWg/VDprkrlyqGI/AAAAAAAAtPQ/DaiY5mFAlwo/s1600/IMG_20141012_085215.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">OpenOCD conectado na KL25Z: 2 breakpoints e 2 watchpoints</td></tr>
</tbody></table>
<br/>
<b><u>Conectar a Tiva C / Stellaris</u></b><br/>
<br/>
Pode conectar assim:<br/>
<br/>
sudo /usr/local/bin/openocd -f /usr/local/share/openocd/scripts/board/ek-lm4f120xl.cfg<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-ICG244Fi17g/VDpw8nBdSxI/AAAAAAAAtQA/BPlsKJ2wolo/s1600/IMG_20141012_091426.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://1.bp.blogspot.com/-ICG244Fi17g/VDpw8nBdSxI/AAAAAAAAtQA/BPlsKJ2wolo/s1600/IMG_20141012_091426.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">OpenOCD conectado na Tiva C: 6 breakpoints e 4 watchpoints</td></tr>
</tbody></table>
<b><u>Conectar a STM32 VL Discovery</u></b><br/>
<br/>
Primeiro é preciso desativar as tentativas de usar o stlink como USB storage, senão o stlink vai ficar resetando a porta usb infinitamente.<br/>
<br/>
sudo bash -c 'echo "options usb-storage quirks=483:3744:i" &gt; /etc/modprobe.d/stlink-v1.conf'<br/>
<br/>
Pode conectar assim:<br/>
sudo /usr/local/bin/openocd -f /usr/local/share/openocd/scripts/board/stm32vldiscovery.cfg<br/>
mas houveram problemas.<br/>
<b><br/></b>
<b>UPDATE 14/outubro:</b><br/>
O openocd funcionou com a discovery, o problema era o usb-storage restando em loop infinito. Com o artificio de colocar o id do stlink na blacklist do usb-storage resolveu.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-gZwizA_Tqbs/VD3C0wlNQNI/AAAAAAAAtR0/7AWCL-atnHg/s1600/IMG_20141014_213743.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-gZwizA_Tqbs/VD3C0wlNQNI/AAAAAAAAtR0/7AWCL-atnHg/s1600/IMG_20141014_213743.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">OpenOCD conectado na STM32 VL Discovery: 6 breakpoints e 4 watchpoints</td></tr>
</tbody></table>
<br/>
Se ocorrer um erros de comunicação no openocd com stm32 uma contingência &nbsp;é usar o st-util<br/>
Para conectar faz:<br/>
st-util -s 1 -m<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-KOWZfUqgzls/VDqNM1nLelI/AAAAAAAAtQk/JDEH2Xu42Ac/s1600/IMG_20141012_111526.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-KOWZfUqgzls/VDqNM1nLelI/AAAAAAAAtQk/JDEH2Xu42Ac/s1600/IMG_20141012_111526.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">st-util conectado na STM32VL Discovery e aberto para conexão do GDB na porta 4242.</td></tr>
</tbody></table>
<br/>
<br/>
Depois de colocar todas as placas com OpenOCD ou algum outro tipo de conexão com GDB server, é só rodar o binário como debug no Eclipse, basta passar a porta do GDB server. E ter compilado o binário com os flags de debug do GCC. No caso do Nuttx, é preciso configurar pelo "make menuconfig" o build com símbolos de debug.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-kb35YqV74CY/VD3tzkkvlvI/AAAAAAAAtSI/t_hL-HxOzsw/s1600/eclipse-openocd-nuttx-stm32vldiscovery.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="312" src="http://4.bp.blogspot.com/-kb35YqV74CY/VD3tzkkvlvI/AAAAAAAAtSI/t_hL-HxOzsw/s1600/eclipse-openocd-nuttx-stm32vldiscovery.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Debug do Nuttx linha a linha do código fonte usando o OpenOCD&nbsp;+ GDB,<br/>
primeiro tem de buildar o Nuttx com os símbolos de debug.</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-UCtr6vtzj2k/VD3uR5iSUrI/AAAAAAAAtSQ/jL_5Ka2R8yA/s1600/stm32vldiscovery-pinout-v1.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://4.bp.blogspot.com/-UCtr6vtzj2k/VD3uR5iSUrI/AAAAAAAAtSQ/jL_5Ka2R8yA/s1600/stm32vldiscovery-pinout-v1.png" width="361"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Para facilitar a vida é bom saber a função de cada pino pelo STM32VLDiscovery Pinout<br/>
Lembrando que troquei o STM32F100RB (16k ram 128k flash)<br/>
por um STM32F103RG (96k ram 1024k flash + outros periféricos&nbsp;)&nbsp;</td></tr>
</tbody></table>
<br/>
No datasheet do&nbsp;<a href="http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00161566.pdf" target="_blank">STM32F103CB</a>&nbsp;(20kb RAM 128 kb Flash) no&nbsp;<a href="http://www.hobbyking.com/hobbyking/store/__55819__AfroFlight_Naze32_Acro_AbuseMark_FunFly_Controller.html" target="_blank">AfroFlight Naze32</a> dá para ver até modelos de 36 pinos possuem USB. A IMU usada é o MPU6050. O Multiwii&nbsp;<a href="https://github.com/multiwii/baseflight">Baseflight</a>&nbsp;é o software usado na Naze32, ele não utiliza um RTOS, o que tornar o código mais fácil para iniciantes, mas também perde a garantia que de o código vai executar no tempo certo.<br/>
<br/>
<a href="http://www.hobbyking.com/hobbyking/store/__65885__Openpilot_CC3D_Flight_Controller_With_Cable_Set_Fully_Authorized.html" target="_blank">Openpilot CC3D Flight</a>&nbsp;também usa STM32F103CB (20kb RAM 128 kb Flash), junto com um MPU6050. O sistema do OpenPilot é baseado no <a href="http://www.freertos.org/" target="_blank">FreeRTOS</a>. O código tem no <a href="https://github.com/openpilot/OpenPilot" target="_blank">Github</a>.<br/>
<br/>
<br/>
Um boa opção são os kits do stm32f103vet6 do aliexpress, todos periféricos estão disponíveis, o Nuttx roda macio e também pode rodar o uCLinux se colocar memória externa.<br/>
<br/>
<span style="box-sizing: content-box; color: #333333; font-family: Arial, Helvetica, sans-senif, SimSun, 宋体; font-size: 12px; font-weight: 700; line-height: 18px;">Mini stm32F103VET6 Core Board &nbsp;72MHz/512KFlash/64KRAM with Battery and USB Cable</span><br/>
http://www.aliexpress.com/item/3pcs-lot-Mini-stm32F103VET6-Core-Board-72MHz-512KFlash-64KRAM-with-Battery-and-USB-Cable-FZ0203/1499630831.html<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-qhAm4zdtKe8/VD5UTOzrGUI/AAAAAAAAtSs/fSAWbHwhrUo/s1600/IMG_20141015_080142.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-qhAm4zdtKe8/VD5UTOzrGUI/AAAAAAAAtSs/fSAWbHwhrUo/s1600/IMG_20141015_080142.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">mini stm32f103vet6 com Nuttx rodando macio,<br/>
debug no eclipse com openocd usando SWD com o stlink v1 da stm32vldiscovery,<br/>
outra opção para debug seria uma Jlink v8 que também tem no aliexpress.&nbsp;</td></tr>
</tbody></table>
<br/>
<br/></div>