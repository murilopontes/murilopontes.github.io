---
layout: post
title: Ubuntu and Archlinux - Install MPLAB X + XC8, Code Compose Studio (CCS), Kinetis Design Studio (KDS) 
categories:
 - CCS
date: 2014-05-06 19:31:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Tutorial completo:<br/>
1) Instalar os requisitos comuns a todos<br/>
2) Instalar Texas Code Compose Studio (CCS)<br/>
3) Instalar o Microchip MPLAB X<br/>
4) Instalar o&nbsp;Microchip&nbsp;XC8<br/>
5) Instalar o&nbsp;Kinetis Design Studio<br/>
<br/>
<a name="more"></a><br/>
<h2 style="text-align: left;">
1) Instalar os requisitos comuns a todos</h2>
No Ubuntu primeiro precisamos instalar os pacotes indicados no link de suporte<br/>
<a href="http://processors.wiki.ti.com/index.php/Linux_Host_Support_CCSv6">http://processors.wiki.ti.com/index.php/Linux_Host_Support_CCSv6</a><br/>
<br/>
<span style="color: #274e13;">aptitude install libc6-i386 libx11-6:i386 libasound2:i386 libatk1.0-0:i386 libcairo2:i386 libcups2:i386 libdbus-glib-1-2:i386 libgconf-2-4:i386 libgdk-pixbuf2.0-0:i386 libgtk-3-0:i386 libice6:i386 libncurses5:i386 libsm6:i386 liborbit2:i386 libudev1:i386 libusb-0.1-4:i386 libstdc++6:i386 libxt6:i386 libxtst6:i386 libgnomeui-0:i386 libusb-1.0-0-dev:i386 libcanberra-gtk-module:i386</span><br/>
<strike><br/></strike>
No Archlinux, precisamos ativar o&nbsp;repositório multilib, e instalar o wine e skype parece que sejam instalada todas essas bibliotecas de 32-bits que são usadas no CCS, MPLAB X e XC8&nbsp;.<br/>
<strike><br/></strike>
<span style="color: #274e13;">pacman -S wine skype</span><br/>
<strike><br/></strike>
<br/>
<h2 style="text-align: left;">
2) Instalar Texas Code Compose Studio (CCS)</h2>
Fazer o download do CCS<br/>
<a href="http://processors.wiki.ti.com/index.php/Download_CCS">http://processors.wiki.ti.com/index.php/Download_CCS</a><br/>
Talvez funcione o link direto abaixo (eles vivem mudando)<br/>
<a href="http://downloads.ti.com/downloads/ccs/esd/CCSv6/CCS_6_0_1/CCS6.0.1.00040_linux.tar.gz">http://downloads.ti.com/downloads/ccs/esd/CCSv6/CCS_6_0_1/CCS6.0.1.00040_linux.tar.gz</a><br/>
tar xfvz&nbsp;CCS6.0.1.00040_linux.tar.gz<br/>
./ccs_setup_6.0.1.00040.bin<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-oq-JwXsTu7E/VEVpqZRCNUI/AAAAAAAAtXQ/6V6kuTX5aPw/s1600/ccs6-ubuntu-energia.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="297" src="http://1.bp.blogspot.com/-oq-JwXsTu7E/VEVpqZRCNUI/AAAAAAAAtXQ/6V6kuTX5aPw/s1600/ccs6-ubuntu-energia.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">No CCS 6 também é possivel criar sketchs do Energia e usar toda API do Arduino.<br/>
Tem compilador C/C++ para PRU da beaglebone<br/>
E todas as ferramentas para MSP430</td></tr>
</tbody></table>
<br/>
<h2 style="text-align: left;">
3) Instalar o Microchip MPLAB X</h2>
Fazer o MPLAB X 2.10<br/>
<span style="color: #274e13;">wget -c http://ww1.microchip.com/downloads/en/DeviceDoc/MPLABX-v2.10-linux-installer.run</span><br/>
<span style="color: #274e13;"><br/></span>
Update: novo MPLAB X 2.20<br/>
<span style="color: #274e13;">wget -c&nbsp;http://ww1.microchip.com/downloads/en/DeviceDoc/MPLABX-v2.20-linux-installer.sh</span><br/>
<br/>
<br/>
Dar permissão de executável<br/>
<span style="color: #274e13;">chmod +x MPLABX-v2.10-linux-installer.run</span><br/>
<br/>
Tente instalar no modo gráfico, ser de segfault no instalador tente o modo texto<br/>
<span style="color: #274e13;">root@murix-quad:/tmp# ./MPLABX-v2.10-linux-installer.run&nbsp;</span><br/>
<span style="color: #274e13;">root@murix-quad:/tmp# ./MPLABX-v2.10-linux-installer.run --mode gtk</span><br/>
<span style="color: #274e13;">root@murix-quad:/tmp# ./MPLABX-v2.10-linux-installer.run --mode xwindow</span><br/>
<br/>
<div>
No modo texto o MPLABX instalou sem problemas</div>
<div>
<span style="color: #274e13;">root@murix-quad:/tmp# ./MPLABX-v2.10-linux-installer.run --mode text</span></div>
<div>
<span style="color: #274e13;">root@murix-quad:/tmp# ./MPLABX-v2.10-linux-installer.run --mode unattended</span></div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-jtH7olh8rjQ/VEPx_sIi3iI/AAAAAAAAtVE/-P6hbc5kvM8/s1600/pic16f876a-mplabx-linux.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="286" src="http://4.bp.blogspot.com/-jtH7olh8rjQ/VEPx_sIi3iI/AAAAAAAAtVE/-P6hbc5kvM8/s1600/pic16f876a-mplabx-linux.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">MPLAB X 2.10 + XC8 1.31&nbsp;com PIC16F876A e Pickit2<br/>
funcionando perfeito no Ubuntu 14.04 e Archlinux</td></tr>
</tbody></table>
<h2 style="text-align: left;">
4) Instalar o&nbsp;Microchip&nbsp;XC8</h2>
<br/>
Fazer o download do XC8 1.31<br/>
<span style="color: #274e13;">wget -c http://ww1.microchip.com/downloads/en/DeviceDoc/xc8-v1.31-linux.run.tar</span><br/>
<br/>
Update: novo XC8 1.33<br/>
<span style="color: #274e13;">wget -c&nbsp;http://ww1.microchip.com/downloads/en/DeviceDoc/xc8-v1.33-full-install-linux-installer.run</span><br/>
<br/>
Extrair<br/>
<span style="color: #274e13;">tar xfv xc8-v1.31-linux.run.tar</span><br/>
<br/>
Dar permissão de executável<br/>
<span style="color: #274e13;">chmod&nbsp;+x xc8-v1.31-linux.run</span><br/>
<br/>
Tente instalar no modo gráfico, ser de segfault no instalador tente o modo texto<br/>
<span style="background-color: white; color: #274e13;">root@murix-quad:/tmp#&nbsp;./xc8-v1.31-linux.run</span><br/>
<span style="background-color: white; color: #274e13;">root@murix-quad:/tmp#&nbsp;./xc8-v1.31-linux.run --mode gtk</span><br/>
<span style="background-color: white; color: #274e13;">root@murix-quad:/tmp#&nbsp;./xc8-v1.31-linux.run --mode xwindow</span><br/>
<br/>
Instalação do XC8 sem problemas no instalador<br/>
<span style="color: #274e13;">root@murix-quad:/tmp# ./xc8-v1.31-linux.run --mode text</span><br/>
<span style="color: #274e13;">root@murix-quad:/tmp# ./xc8-v1.31-linux.run --mode unattended --netservername localhost</span><br/>
<div>
<br/></div>
<br/>
<h2 style="text-align: left;">
5) Instalar o&nbsp;Kinetis Design Studio</h2>
Fazer download do instalador<br/>
<span style="color: #274e13;">wget -c https://cache.freescale.com/secured/KDS/kinetis-design-studio-1.1.1-1_i386.deb.bin</span><br/>
<br/>
Instalar<br/>
<span style="color: #274e13;">sudo dpkg -i kinetis-design-studio-1.1.1-1_i386.deb.bin</span><br/>
<br/>
Como o KDS é 32bits precisa do jdk de 32bits<br/>
<span style="color: #274e13;">sudo aptitude install openjdk-6-jdk:i386</span><br/>
<br/>
Executa o KDS com jdk de 32bits como root para instalar os SDKs<br/>
<span style="color: #274e13;">sudo PATH=/usr/lib/jvm/java-6-openjdk-i386/bin:$PATH /opt/Freescale/KDS_1.1.1/eclipse/eclipse</span><br/>
Quando o eclipse KDS abrir, help-&gt;install new software-&gt;instalar os SDKs: KDS e PEMICRO.<br/>
<div>
<br/></div>
<div>
Depois que instalar os SDK do KDS por iniciar com usuário normal</div>
<span style="color: #274e13;">PATH=/usr/lib/jvm/java-6-openjdk-i386/bin:$PATH /opt/Freescale/KDS_1.1.1/eclipse/eclipse</span><br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-CNqRKBfHma8/VEYsOkeGvvI/AAAAAAAAtYE/CmbeBgLjlQs/s1600/eclipse-kds.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="257" src="http://4.bp.blogspot.com/-CNqRKBfHma8/VEYsOkeGvvI/AAAAAAAAtYE/CmbeBgLjlQs/s1600/eclipse-kds.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Eclipse Kinetis Design Studio com Processor Expert&nbsp;</td></tr>
</tbody></table>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>