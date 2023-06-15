---
layout: post
title: cross-compile VLC para ardrone usando o Sourcery G++ Lite
categories:
 - GLIBC
date: 2013-11-27 01:21:00 +0000
---

Depois de instalado o Sourcery G++ Lite, chegou a hora de compilar o VLC utilizando ele. Com o VLC poderemos faz broadcast do video capturado pelas cameras do ardrone.  

<a name="more"></a>  

  

Instalar o VLC e Mplayer no Ubuntu também para fazer o teste de recebimento do stream em broadcast feito pelo Drone.  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\# apt-get install vlc mplayer </span>  

  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">Baixar e extrair o VLC</span></span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\# wget http://download.videolan.org/pub/videolan/vlc/2.1.1/vlc-2.1.1.tar.xz</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\# tar xfvJ vlc-2.1.1.tar.xz  
root@ubuntu:~/Downloads\# cd vlc-2.1.1</span>  

<span style="background-color: #cfe2f3;"></span>  

  

  

A configuração do VLC é tensa, é preciso remover várias features para compilar sem problemas. E ativar a opção de executar como root, já que no Drone não tem "su".  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/vlc-2.1.1\# ./configure --target=arm-none-linux-gnueabi --host=arm-none-linux-gnueabi --disable-lua --disable-mad --disable-avcodec --disable-swscale --disable-a52 --disable-xcb --disable-libgcrypt --disable-dbus --disable-alsa --disable-pulse --disable-libxml2 --disable-udev --disable-freetype --disable-sdl --disable-caca --disable-bonjour --enable-run-as-root --prefix=/data/video/vlc &amp;&amp; make &amp;&amp; make install</span>  

  

  

  

Agora temos o VLC compilado para Drone instalado no nosso /data/video/vlc.  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# cd /data/video/vlc/  
root@ubuntu:/data/video/vlc\# du -hs  
48M&nbsp;&nbsp;&nbsp; .</span>  

  

Nosso recém compilado VLC tem o singelo tamanho de 48MB.  

  

Primeiro é preciso conectar no Access Point WIFI criado pelo ardrone.  

Uma vez conectado e conseguindo pingar o 192.168.1.1, provavelmente não haverá problemas.  

  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# ping 192.168.1.1  
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.  
64 bytes from 192.168.1.1: icmp\_req=1 ttl=64 time=1.99 ms  
64 bytes from 192.168.1.1: icmp\_req=2 ttl=64 time=1.77 ms  
^C  
--- 192.168.1.1 ping statistics ---  
2 packets transmitted, 2 received, 0% packet loss, time 1002ms  
rtt min/avg/max/mdev = 1.773/1.882/1.992/0.117 ms</span>  

  

  

  

  

  

  

  

&nbsp;Se pingou o Drone segue para o telnet no Drone,  

uma vez na linha de comando do Drone, é bom verificar o espaço livre antes de enviar o VLC para o /data/video via FTP.  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# telnet 192.168.1.1  
Trying 192.168.1.1...  
Connected to 192.168.1.1.  
Escape character is '^\]'.  
  
  
  
BusyBox v1.14.0 (2011-08-30 12:00:29 CEST) built-in shell (ash)  
Enter 'help' for a list of built-in commands.  
  
\# df -ah  
Filesystem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Size&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used Available Use% Mounted on  
ubi1:system&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 12.0M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6.3M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5.1M&nbsp; 55% /  
tmp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 61.6M&nbsp;&nbsp;&nbsp;&nbsp; 32.0K&nbsp;&nbsp;&nbsp;&nbsp; 61.5M&nbsp;&nbsp; 0% /tmp  
proc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 0% /proc  
dev&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 61.6M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp; 61.6M&nbsp;&nbsp; 0% /dev  
devpts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 0% /dev/pts  
sys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 0% /sys  
ubi0:factory&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.8M&nbsp;&nbsp;&nbsp;&nbsp; 44.0K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.5M&nbsp;&nbsp; 1% /factory  
ubi2:update&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 13.2M&nbsp;&nbsp;&nbsp;&nbsp; 32.0K&nbsp;&nbsp;&nbsp;&nbsp; 12.5M&nbsp;&nbsp; 0% /update  
ubi2:data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 67.5M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.4M&nbsp;&nbsp;&nbsp;&nbsp; 62.6M&nbsp;&nbsp; 2% /data  
\# </span>  

  

Segundo o telnet ainda tem livre 62,6MB dos 67,5MB da partição /data, que é onde vamos colocar o VLC ocupando 48MB.   

  

Somente a título de curiosidade, o ardrone é todo feito encima de UBIFS.  

  

Aqui temos a configuração do MTD que vai ser passada para o UBI.   

<span style="background-color: #cfe2f3;">&nbsp;\# cat /proc/cmdline   
parrotparts=nand0:256K(Pbootloader),8M(Pmain\_boot),8M(Pfactory),16M(Psystem),98048K(Pupdate) console=ttyPA0,115200 loglevel=4 ubi.mtd=Pfactory,2048 ubi.mtd=Psystem,2048 ubi.mtd=Pupdate,2048 root=ubi1:system rootfstype=ubifs parrot5.low\_latency=1  
\#&nbsp;</span>  

  

Olhando o log do kernel, o volume /data tem na verdade 73MB, mas quando tira os espaços reversados fica somente 67,5MB.   

<span style="background-color: #cfe2f3;">\# dmesg | grep UBIFS  
\[&nbsp;&nbsp;&nbsp; 1.361041\] UBIFS: recovery needed  
\[&nbsp;&nbsp;&nbsp; 1.378984\] UBIFS: recovery deferred  
\[&nbsp;&nbsp;&nbsp; 1.379025\] UBIFS: mounted UBI device 1, volume 0, name "system"  
\[&nbsp;&nbsp;&nbsp; 1.379048\] UBIFS: mounted read-only  
\[&nbsp;&nbsp;&nbsp; 1.379071\] UBIFS: file system size:&nbsp;&nbsp; 14348288 bytes (14012 KiB, 13 MiB, 113 LEBs)  
\[&nbsp;&nbsp;&nbsp; 1.379103\] UBIFS: journal size:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1015809 bytes (992 KiB, 0 MiB, 6 LEBs)  
\[&nbsp;&nbsp;&nbsp; 1.379132\] UBIFS: media format:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; w4/r0 (latest is w4/r0)  
\[&nbsp;&nbsp;&nbsp; 1.379155\] UBIFS: default compressor: none  
\[&nbsp;&nbsp;&nbsp; 1.379176\] UBIFS: reserved for root:&nbsp; 677704 bytes (661 KiB)  
\[&nbsp;&nbsp;&nbsp; 1.571892\] UBIFS: completing deferred recovery  
\[&nbsp;&nbsp;&nbsp; 1.578212\] UBIFS: deferred recovery completed  
\[&nbsp;&nbsp;&nbsp; 2.314383\] UBIFS: mounted UBI device 0, volume 0, name "factory"  
\[&nbsp;&nbsp;&nbsp; 2.314416\] UBIFS: mounted read-only  
\[&nbsp;&nbsp;&nbsp; 2.314441\] UBIFS: file system size:&nbsp;&nbsp; 6221824 bytes (6076 KiB, 5 MiB, 49 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.314472\] UBIFS: journal size:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1015809 bytes (992 KiB, 0 MiB, 6 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.314501\] UBIFS: media format:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; w4/r0 (latest is w4/r0)  
\[&nbsp;&nbsp;&nbsp; 2.314524\] UBIFS: default compressor: none  
\[&nbsp;&nbsp;&nbsp; 2.314545\] UBIFS: reserved for root:&nbsp; 293871 bytes (286 KiB)  
\[&nbsp;&nbsp;&nbsp; 2.343121\] UBIFS: recovery needed  
\[&nbsp;&nbsp;&nbsp; 2.369371\] UBIFS: recovery completed  
\[&nbsp;&nbsp;&nbsp; 2.369411\] UBIFS: mounted UBI device 2, volume 0, name "update"  
\[&nbsp;&nbsp;&nbsp; 2.369441\] UBIFS: file system size:&nbsp;&nbsp; 15745024 bytes (15376 KiB, 15 MiB, 124 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.369474\] UBIFS: journal size:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1015809 bytes (992 KiB, 0 MiB, 6 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.369503\] UBIFS: media format:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; w4/r0 (latest is w4/r0)  
\[&nbsp;&nbsp;&nbsp; 2.369527\] UBIFS: default compressor: none  
\[&nbsp;&nbsp;&nbsp; 2.369548\] UBIFS: reserved for root:&nbsp; 743676 bytes (726 KiB)  
\[&nbsp;&nbsp;&nbsp; 2.398642\] UBIFS: recovery needed  
\[&nbsp;&nbsp;&nbsp; 2.450956\] UBIFS: recovery completed  
\[&nbsp;&nbsp;&nbsp; 2.450996\] UBIFS: mounted UBI device 2, volume 1, name "data"  
\[&nbsp;&nbsp;&nbsp; 2.451027\] UBIFS: file system size:&nbsp;&nbsp; 77328384 bytes (75516 KiB, 73 MiB, 609 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.451059\] UBIFS: journal size:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3809280 bytes (3720 KiB, 3 MiB, 30 LEBs)  
\[&nbsp;&nbsp;&nbsp; 2.451089\] UBIFS: media format:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; w4/r0 (latest is w4/r0)  
\[&nbsp;&nbsp;&nbsp; 2.451112\] UBIFS: default compressor: none  
\[&nbsp;&nbsp;&nbsp; 2.451133\] UBIFS: reserved for root:&nbsp; 3652410 bytes (3566 KiB)  
\# </span>  

&nbsp;   

O próximo passo é copiar o diretório vlc para o FTP do Drone.  

Lembrando que o modo de transferência deve ser sempre o binário, senão os executáveis serão destruidos durante a cópia.   

Para facilitar a cópia recomendo usar o Filezilla (lembre de mudar para modo binário, isto é fundamental)   

  

<span style="background-color: #cfe2f3;">&nbsp;root@ubuntu:~\# apt-get install filezilla</span>  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-v_Q1y-rmSJY/UpUcgsly6bI/AAAAAAAAnc8/_q8qLfYhbjs/s1600/filezilla-drone-transfer.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="274" src="http://2.bp.blogspot.com/-v_Q1y-rmSJY/UpUcgsly6bI/AAAAAAAAnc8/_q8qLfYhbjs/s1600/filezilla-drone-transfer.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O Host é o IP do Drone, 192.168.1.1</td><td class="tr-caption" style="text-align: center;"></td><td class="tr-caption" style="text-align: center;"><br/></td><td class="tr-caption" style="text-align: center;"><br/></td></tr>
</tbody></table>

No mais é só entrar em /data/video e arrastar para dentro do drone.  

Quando terminar de transferir tudo, vamos testar via telnet no drone.  

  

  

  

<span style="background-color: #cfe2f3;">&nbsp;root@ubuntu:~\# telnet 192.168.1.1  
Trying 192.168.1.1...  
Connected to 192.168.1.1.  
Escape character is '^\]'.  
  
  
  
BusyBox v1.14.0 (2011-08-30 12:00:29 CEST) built-in shell (ash)  
Enter 'help' for a list of built-in commands.</span>  

  

  

  

De volta ao drone, é hora de colocar as permissões de execução no VLC   

  

<span style="background-color: #cfe2f3;">\# chmod -R +x /data/video/vlc</span>  

  

E por fim testar o VLC  

  

<span style="background-color: #cfe2f3;">\# /data/video/vlc/bin/vlc  
/data/video/vlc/bin/vlc: error while loading shared libraries: libvlc.so.5: cannot open shared object file: No such file or directory</span>  

  

  

  

Problema de .so faltando, é normal quando não se tem o ldconfig,  

para resolver o jeito é linkar na mão e testar denovo  

  

<span style="background-color: #cfe2f3;">\# ln -s /data/video/vlc/lib/libvlc.so.5.4.0 /data/video/vlc/lib/libvlc.so.5</span>  

<span style="background-color: #cfe2f3;">\# /data/video/vlc/bin/vlc</span><span style="background-color: #cfe2f3;">/data/video/vlc/bin/vlc: error while loading shared libraries: libvlccore.so.7: cannot open shared object file: No such file or directory</span>  

  

Outra lib faltando, ok. Linkar na mão e testar.  

  

<span style="background-color: #cfe2f3;">\# ln -s /data/video/vlc/lib/libvlccore.so.7.0.0 /data/video/vlc/lib/libvlccore.so.7</span>  

<span style="background-color: #cfe2f3;">\# /data/video/vlc/bin/vlc  
/data/video/vlc/bin/vlc: /lib/libc.so.6: version \`GLIBC\_2.10' not found (required by /data/video/vlc/lib/libvlccore.so.7)  
/data/video/vlc/bin/vlc: /lib/libc.so.6: version \`GLIBC\_2.9' not found (required by /data/video/vlc/lib/libvlccore.so.7)</span>  

Agora a coisa ficou feita, provavelmente por causa da versão da GLIBC que tem no   

gcc version 4.5.2 (Sourcery G++ Lite 2011.03-41)  

  

  

<span style="background-color: #cfe2f3;">\# cat /firmware/version.txt   
1.7.6  
\# cat /update/version.txt   
1.7.6</span>  

<span style="background-color: #cfe2f3;">\# cat /proc/version </span>  

<span style="background-color: #cfe2f3;">Linux version 2.6.27.47-parrot (aferran@FR-B-800-0053) (gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203) ) \#1 PREEMPT Tue Aug 30 12:05:09 CEST 2011  
\#</span>  

  

problema é descobrir qual a versão do GCC que buildou o resto do sistema.  

Depois pensar, resolvido matar o inetd e subir com um config nova export a raiz do sistema, dai pude copiar o sistema todo do drone para minha máquina pelo Filezilla.  

&nbsp;Agora com as ferramentas todas fica mais fácil.  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/drone/lib\# strings -a \* | grep GLIBC | sort | uniq  
GLIBC\_2.0  
GLIBC\_2.4  
GLIBC\_2.5  
GLIBC\_2.6  
GLIBC\_2.7  
GLIBC\_2.8  
GLIBC\_PRIVATE</span>  

  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/drone/lib\# strings -a \* | grep GCC | sort | uniq  
GCC\_3.0  
GCC\_3.3  
GCC\_3.3.1  
GCC\_3.3.4  
GCC\_3.4  
GCC\_3.4.2  
GCC\_3.5  
GCC\_4.0.0  
GCC\_4.2.0  
GCC\_4.3.0</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">Realmente lascou, a versão </span></span><span style="background-color: #cfe2f3;"><span style="background-color: white;">Sourcery G++ Lite 2011.03-41 não vai servir para buildar o VLC para o firmware 1.7.6, já que a lista de símbolos é diferente.</span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">Vai ser preciso refazer todo o processo provavelmente com a versão&nbsp; </span></span>  

<span style="background-color: #cfe2f3;">gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203) </span>  

  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">&nbsp;Removido a versão 2011 e instalado o 2009.</span></span>  

  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">  
</span></span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">&nbsp;<span style="background-color: #cfe2f3;">root@ubuntu:~\# arm-none-linux-gnueabi-gcc -v  
Using built-in specs.  
Target: arm-none-linux-gnueabi  
Configured with: /scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/src/gcc-4.3/configure --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu --target=arm-none-linux-gnueabi --enable-threads --disable-libmudflap --disable-libssp --disable-libstdcxx-pch --with-gnu-as --with-gnu-ld --with-specs='%{funwind-tables|fno-unwind-tables|mabi=\*|ffreestanding|nostdlib:;:-funwind-tables}' --enable-languages=c,c++ --enable-shared --enable-symvers=gnu --enable-\_\_cxa\_atexit --with-pkgversion='Sourcery G++ Lite 2009q1-203' --with-bugurl=https://support.codesourcery.com/GNUToolchain/ --disable-nls --prefix=/opt/codesourcery --with-sysroot=/opt/codesourcery/arm-none-linux-gnueabi/libc --with-build-sysroot=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/libc --with-gmp=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/obj/host-libs-2009q1-203-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-mpfr=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/obj/host-libs-2009q1-203-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --disable-libgomp --enable-poison-system-directories --with-build-time-tools=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/bin --with-build-time-tools=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/bin  
Thread model: posix  
gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203)   
root@ubuntu:~\# </span></span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">  
</span></span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">Build do VLC com a versão 2009, foi de primeira sem nenhum problema.</span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">Agora é copiar pelo FTP e testar no telnet como já tinha feito antes.</span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;"></span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;"><span style="background-color: #cfe2f3;"></span>  
</span></span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">  
</span></span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;"><span style="background-color: #cfe2f3;">\# /data/video/vlc/bin/vlc --version  
VLC media player 2.1.1 Rincewind (revision 2.1.0-207-g89c9520)  
VLC version 2.1.1 Rincewind (2.1.0-207-g89c9520)  
Compiled by root on ubuntu (Nov 26 2013 16:26:14)  
Compiler: gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203)  
This program comes with NO WARRANTY, to the extent permitted by law.  
You may redistribute it under the terms of the GNU General Public License;  
see the file named COPYING for details.  
Written by the VideoLAN team; see the AUTHORS file.  
\# </span></span></span>  

<span style="background-color: #cfe2f3;"><span style="background-color: white;">  
</span></span>
<span style="background-color: #cfe2f3;"><span style="background-color: white;">Agora sim, funcionou como esperado!!!</span></span>  

  

Comandos para fazer o stream das câmeras do drone.  

<span style="background-color: #cfe2f3; font-size: xx-small;">\# /data/video/vlc/bin/vlc v4l2:///dev/video0:width=640:height=480 -I dummy -v --noaudio --sout '\#std{access=mmsh,dst=:8080}'  
\# /data/video/vlc/bin/vlc v4l2:///dev/video1:width=176:height=144 -I dummy -v --noaudio --sout '\#std{access=mmsh,dst=:8080}'</span>  

<div>
<br/></div>

<div>
Agora existe algum problema com as câmeras que ficaram rebeldes e sem funcionar.</div>

<div>
<br/></div>

  

  

<span style="background-color: #cfe2f3;">  
</span>