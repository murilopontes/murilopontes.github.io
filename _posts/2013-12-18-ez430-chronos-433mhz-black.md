---
layout: post
title: eZ430-Chronos 433MHz Black
categories:
 - 433MHz
date: 2013-12-18 03:51:00 +0000
---

eZ430-Chronos 433MHz Black, resultado do último black friday.  

<div>
Kit composto do relógio + chave philips&nbsp;+&nbsp;MSP-ez430U&nbsp;+ usb stick cc1111f32.<br/>
<br/>
<a name="more"></a><br/><br/>
Existe uma segunda versão desse kit, que a PCBs do relógio e Access point são brancas, e usam um hardware um pouco diferente. No caso do Access point o CC1111F32 foi substituido por um MSP430&nbsp;+ CC1101.</div>

<div>
</div>

<div>
<br/>
&gt; Hardware do relógio</div>

<div>
O relógio é um SoC CC430F6137 (16-bit 20MHz 4KB-RAM 32KB-FLASH 44-GPIOs).<br/>
O SoC é composto de um MSP430&nbsp;+ CC1101.&nbsp;</div>

<div>
O MSP430 já vem medidor de tensão/bateria e sensor de temperatura.</div>

<div>
Além disso o LCD está ligado no barramento do MSP430,&nbsp;</div>

<div>
junto com um acelerômetro 3d (VTI CMA3000) &nbsp;e um sensor de pressão atmosférica (VTI SCP1000).</div>

<div>
O CC1101 é um rádio sub Giga Hertz com 2 FIFOs de 64 bytes, um para RX e outro para TX.</div>

<div>
O MSP430 é completamente reprogramável usando o&nbsp;MSP-ez430U&nbsp;que vem no kit. E já vem com os conectores.<br/>
<br/></div>

<div>
&gt; Hardware do MSP-ez430U Rev2.0<br/>
MSP430F1612 (16bit 8MHz 5KB-RAM 55KB-FLASH)<br/>
TUSB3410 - Conversor USB / RS232<br/>
É possível atualizar o firmware ez430, mas é necessário possuir um MSP-FET430UIF<br/>
<a href="http://processors.wiki.ti.com/index.php/EZ430_Emulator_Upgrade">http://processors.wiki.ti.com/index.php/EZ430_Emulator_Upgrade</a><br/>
<a href="http://processors.wiki.ti.com/index.php/MSP-FET430UIF">http://processors.wiki.ti.com/index.php/MSP-FET430UIF</a><br/>
<br/>
&gt; Hardware do Access Point<br/>
O access point é um SoC CC1111F32. O SoC é composto de um 8051 (8-bit 4KB-RAM 32KB-FLASH), um rádio CC1101 e uma interface USB.<br/>
O CC1111F32 é completamente reprogramável usando o CC-Debugger, que tem de ser comprado separadamente. &nbsp;Além disso, é preciso soldar o conector nas ilhas de solda na parte de baixo do PCB.</div>

<div>
<br/>
&gt; Notas sobre o Hardware<br/>
A solução como um todo funciona, mas não é auto-contida. Se der problema no firmware do MSP-ez430U é necessário comprar um MSP-FET430UIF para consertar. Se der problema no firmware do CC1111F32 é necessário comprar um CC-DEBUGGER para consertar. Além disso existe uma mistura de processadores, uma parte usa MSP430 e outra parte usa 8051, o que implica na necessidade de ter dois ambientes de desenvolvimento diferentes.<br/>
<br/>
&gt; Notas sobre o software<br/>
1) Chronos: código fonte completo disponível.<br/>
2) MSP-ez430U: código fonte indisponível.<br/>
3) CC1111F32: código fonte completo disponível.<br/>
4) Controle de controle para PC: código fonte parcialmente disponível.<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-SPcdFXx2U3E/UrJllsCPMTI/AAAAAAAAnv8/ZwR4bxQFuBs/s1600/ez430-chronos.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="257" src="http://3.bp.blogspot.com/-SPcdFXx2U3E/UrJllsCPMTI/AAAAAAAAnv8/ZwR4bxQFuBs/s320/ez430-chronos.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Kit ez430-Chronos</td></tr>
</tbody></table>
<br/></div>

<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-8mCwMHbQGVs/UrJigKUBM5I/AAAAAAAAnu0/_xhXo4SiZTM/s1600/IMG_20131219_000323.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-8mCwMHbQGVs/UrJigKUBM5I/AAAAAAAAnu0/_xhXo4SiZTM/s320/IMG_20131219_000323.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">eZ430-Chronos 433MHz Black PCB.<br/>
Com bateria nova.</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-_AymadO8yMo/UrEYPTDEJSI/AAAAAAAAns0/MlFZ482lhRY/s1600/IMG_20131218_002311.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://1.bp.blogspot.com/-_AymadO8yMo/UrEYPTDEJSI/AAAAAAAAns0/MlFZ482lhRY/s400/IMG_20131218_002311.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">eZ430-Chronos desmontado para gravação</td></tr>
</tbody></table>
<br/>
<br/>
<br/>
<br/>
root@ubuntu:~# dmesg<br/>
<span style="background-color: #cfe2f3;">&nbsp;generic-usb 0003:0451:F432.0002: hiddev0,hidraw1: USB HID v1.01 Device [Texas Instruments Texas Instruments MSP-FET430UIF]</span><br/>
<br/>
<br/>
root@ubuntu:~# lsusb<br/>
<span style="background-color: #cfe2f3;">Bus 002 Device 014: ID 0451:16a6 Texas Instruments, Inc. BM-USBD1 BlueRobin RF heart rate sensor receiver</span><br/>
<span style="background-color: #cfe2f3;">Bus 002 Device 015: ID 0451:f432 Texas Instruments, Inc. eZ430 Development Tool</span></div>

<div>
<br/></div>

<div>
<br/></div>

<div>
root@ubuntu:~# <b>aptitude install gcc-msp430 binutils-msp430 gdb-msp430 msp430-libc msp430mcu mspdebug</b></div>

<div>
<br/>
<br/>
root@ubuntu:~# mspdebug --usb-list<br/>
<span style="background-color: #cfe2f3;">Devices on bus 002:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 002:017 0451:f432 eZ430-RF2500 [serial: 54FF41E50F942A19]</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 002:013 0e0f:0008 &nbsp;[serial: 000650268328]</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 002:003 0e0f:0002 &nbsp;[serial: ?]</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 002:002 0e0f:0003 &nbsp;[serial: ?]</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 002:001 1d6b:0001 &nbsp;[serial: 0000:02:00.0]</span><br/>
<span style="background-color: #cfe2f3;">Devices on bus 001:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; 001:001 1d6b:0002 &nbsp;[serial: 0000:02:03.0]</span></div>

<div>
<br/>
&gt;Compilar o projeto do relógio<br/>
root@ubuntu:~# <b>git clone https://github.com/murix/openchronos-ubuntu_12.04.git</b></div>

<div>
root@ubuntu:~# cd openchronos-ubuntu_12.04</div>

<div>
root@ubuntu:~/openchronos-ubuntu_12.04# make</div>

<div>
<br/></div>

<div>
root@ubuntu:~/openchronos-ubuntu_12.04# <b>mspdebug rf2500 'prog build/eZChronos.elf'</b><br/>
<span style="background-color: #cfe2f3;">MSPDebug version 0.18 - debugging tool for MSP430 MCUs</span><br/>
<span style="background-color: #cfe2f3;">Copyright (C) 2009-2011 Daniel Beer <dlbeer gmail.com=""></dlbeer></span><br/>
<span style="background-color: #cfe2f3;">This is free software; see the source for copying conditions. &nbsp;There is NO</span><br/>
<span style="background-color: #cfe2f3;">warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Trying to open interface 1 on 017</span><br/>
<span style="background-color: #cfe2f3;">Initializing FET...</span><br/>
<span style="background-color: #cfe2f3;">FET protocol version is 30001000</span><br/>
<span style="background-color: #cfe2f3;">Configured for Spy-Bi-Wire</span><br/>
<span style="background-color: #cfe2f3;">Set Vcc: 3000 mV</span><br/>
<span style="background-color: #cfe2f3;">Device ID: 0x6137</span><br/>
<span style="background-color: #cfe2f3;">Device: CC430F6137</span><br/>
<span style="background-color: #cfe2f3;">Code memory starts at 0x8000</span><br/>
<span style="background-color: #cfe2f3;">Number of breakpoints: 3</span><br/>
<span style="background-color: #cfe2f3;">fet: FET returned NAK</span><br/>
<span style="background-color: #cfe2f3;">fet: warning: message 0x30 failed</span><br/>
<span style="background-color: #cfe2f3;">Erasing...</span><br/>
<span style="background-color: #cfe2f3;">Programming...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to 8000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to 9000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to a000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to b000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to c000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing 3904 bytes to d000 [section: .text]...</span><br/>
<span style="background-color: #cfe2f3;">Writing &nbsp;144 bytes to df40 [section: .data]...</span><br/>
<span style="background-color: #cfe2f3;">Writing &nbsp;128 bytes to ff80 [section: .vectors]...</span><br/>
root@ubuntu:~/openchronos-ubuntu_12.04#&nbsp;</div>

<div class="separator" style="clear: both; text-align: center;">
</div>

<div>
<br/>
<br/>
<br/>
<a href="http://processors.wiki.ti.com/index.php/EZ430-Chronos">http://processors.wiki.ti.com/index.php/EZ430-Chronos</a><br/>
<br/>
root@ubuntu:~#&nbsp;wget http://www.ti.com/lit/sw/slac388c/slac388c.zip<br/>
<br/>
&gt; instalar mais alguns pacotes rodar o centro de controle<br/>
root@ubuntu:~# aptitude install tcl tk xdotool<br/>
<br/>
O pacote <b>xdotool </b>é usado para simular teclado e mouse.<br/>
<br/>
<br/>
&gt;Regravando o firmware oficial versão 2.1 (contido no slac388c.zip)<br/>
<br/>
root@ubuntu:~/ez430/Recovery/Chronos Watch/Applications# <b>mspdebug rf2500 'prog Recovery_ez430_chronos_433MHz_2_1.txt'</b><br/>
<span style="background-color: #cfe2f3;">MSPDebug version 0.18 - debugging tool for MSP430 MCUs</span><br/>
<span style="background-color: #cfe2f3;">Copyright (C) 2009-2011 Daniel Beer <dlbeer gmail.com=""></dlbeer></span><br/>
<span style="background-color: #cfe2f3;">This is free software; see the source for copying conditions. &nbsp;There is NO</span><br/>
<span style="background-color: #cfe2f3;">warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Trying to open interface 1 on 020</span><br/>
<span style="background-color: #cfe2f3;">Initializing FET...</span><br/>
<span style="background-color: #cfe2f3;">FET protocol version is 30001000</span><br/>
<span style="background-color: #cfe2f3;">Configured for Spy-Bi-Wire</span><br/>
<span style="background-color: #cfe2f3;">Set Vcc: 3000 mV</span><br/>
<span style="background-color: #cfe2f3;">Device ID: 0x6137</span><br/>
<span style="background-color: #cfe2f3;">Device: CC430F6137</span><br/>
<span style="background-color: #cfe2f3;">Code memory starts at 0x8000</span><br/>
<span style="background-color: #cfe2f3;">Number of breakpoints: 3</span><br/>
<span style="background-color: #cfe2f3;">fet: FET returned NAK</span><br/>
<span style="background-color: #cfe2f3;">fet: warning: message 0x30 failed</span><br/>
<span style="background-color: #cfe2f3;">Erasing...</span><br/>
<span style="background-color: #cfe2f3;">Programming...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to 8000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to 9000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to a000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to b000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to c000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to d000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 4096 bytes to e000...</span><br/>
<span style="background-color: #cfe2f3;">Writing 2221 bytes to f000...</span><br/>
<span style="background-color: #cfe2f3;">Writing &nbsp;386 bytes to f8ae...</span><br/>
<span style="background-color: #cfe2f3;">Writing &nbsp; 38 bytes to ffda...</span><br/>
root@ubuntu:~/ez430/Recovery/Chronos Watch/Applications#<br/>
<div>
<br/>
&gt; Manual do usuário</div>
<a href="http://www.ti.com/lit/ug/slau292f/slau292f.pdf">http://www.ti.com/lit/ug/slau292f/slau292f.pdf</a><br/>
<br/>
&gt; Esquema de navegação nos menus<br/>
<br/>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-BFyYSdG6abA/UrHbbJKqLmI/AAAAAAAAntI/2cPraQYVv_g/s1600/ez430menu.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="295" src="http://3.bp.blogspot.com/-BFyYSdG6abA/UrHbbJKqLmI/AAAAAAAAntI/2cPraQYVv_g/s400/ez430menu.PNG" width="400"/></a></div>
<br/>
<br/>
<br/>
&gt; Depois de algumas tentativas, o RF finalmente funcionou.<br/>
O problema era que estava dando era o reset do Chronos em todas as tentativas de TX do RF.<br/>
Para fazer TX todo e qualquer rádio consome uma corrente maior do que a usada no RX.<br/>
A bateria com 2,90V ainda funciona direito para todas as funções que não envolve o TX do RF.<br/>
<br/>
Com todos os firmwares testados (oficiais e abertos) a bateria de 2,90V provoca reset, e algumas vezes os botões param de funcionar.<br/>
Com a bateria nova (3,01V a 3,12V) todos os firmware funcionaram perfeitamente o TX do RF.<br/>
Com o kit conectado no MSP-FET/Debugger também funciona tudo sem problemas, já que alimentação vem direto do USB.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-J4zMcHBxrD0/UrJBkE1xUzI/AAAAAAAAntY/95hybrkxbtg/s1600/CCS+chronos.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://2.bp.blogspot.com/-J4zMcHBxrD0/UrJBkE1xUzI/AAAAAAAAntY/95hybrkxbtg/s400/CCS+chronos.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Code Composer Studio (CCStudio) Integrated Development Environment (IDE) v5,<br/>
com projeto do ez430-Chronos que vem no slac388c.zip.<br/>
O centro de controle vem no pacote slac341d.zip</td></tr>
</tbody></table>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-picYGSnUDjg/UrJjHKChtjI/AAAAAAAAnu8/Vlr7ypwpOdc/s1600/IMG_20131218_232925.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-picYGSnUDjg/UrJjHKChtjI/AAAAAAAAnu8/Vlr7ypwpOdc/s320/IMG_20131218_232925.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Bateria com apenas 2.9V provoca reset se rodar qualquer função que use RF</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-j3PCcLWB9YM/UrJjXGbYKsI/AAAAAAAAnvE/8MnwsRQ1etA/s1600/IMG_20131218_232902.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-j3PCcLWB9YM/UrJjXGbYKsI/AAAAAAAAnvE/8MnwsRQ1etA/s320/IMG_20131218_232902.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tela em que fica travado após usar RF com bateria fraca.</td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: center;">
</div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-_PR8BqatLf4/UrJZt4HHCzI/AAAAAAAAnvY/P8DfRca7bbA/s1600/IMG_20131218_232807.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-_PR8BqatLf4/UrJZt4HHCzI/AAAAAAAAnvY/P8DfRca7bbA/s320/IMG_20131218_232807.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Com a bateria nova deu 3,01V<br/>
<br/></td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-1Ane4mZHG7w/UrJkOXsxnYI/AAAAAAAAnvw/Lzcd7s8Xejg/s1600/IMG_20131218_233036.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-1Ane4mZHG7w/UrJkOXsxnYI/AAAAAAAAnvw/Lzcd7s8Xejg/s320/IMG_20131218_233036.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Bateria nova fazendo broadcast RF do acelerômetro sem problemas.</td></tr>
</tbody></table>
<br/>
<br/></div>

<div>
<br/>
<br/>
<br/></div>

<div>
<br/></div>