---
layout: post
title: Compilando e testando v4l-utils para ardrone
categories:
 - Video4Linux
date: 2013-12-04 21:10:00 +0000
---

Tutorial adicionando v4l-utils no ardrone  

  

<a name="more"></a>  
  

Esse post presume que você já tenha feito todo o setup para compilar o VLC para ardrone.  

<http://dronespersonalizados.blogspot.com.br/2013/11/cross-compile-vlc-para-ardrone-usando-o.html>  

  

  

&gt; Entrar no ambiente do compilação para ARM e testar a versão do compilador.  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# su -</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# arm-none-linux-gnueabi-gcc -v</span>  

<span style="background-color: #cfe2f3;">Using built-in specs.</span>  

<span style="background-color: #cfe2f3;">Target: arm-none-linux-gnueabi</span>  

<span style="background-color: #cfe2f3;">Configured with: /scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/src/gcc-4.3/configure --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu --target=arm-none-linux-gnueabi --enable-threads --disable-libmudflap --disable-libssp --disable-libstdcxx-pch --with-gnu-as --with-gnu-ld --with-specs='%{funwind-tables|fno-unwind-tables|mabi=\*|ffreestanding|nostdlib:;:-funwind-tables}' --enable-languages=c,c++ --enable-shared --enable-symvers=gnu --enable-\_\_cxa\_atexit --with-pkgversion='Sourcery G++ Lite 2009q1-203' --with-bugurl=https://support.codesourcery.com/GNUToolchain/ --disable-nls --prefix=/opt/codesourcery --with-sysroot=/opt/codesourcery/arm-none-linux-gnueabi/libc --with-build-sysroot=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/libc --with-gmp=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/obj/host-libs-2009q1-203-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-mpfr=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/obj/host-libs-2009q1-203-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --disable-libgomp --enable-poison-system-directories --with-build-time-tools=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/bin --with-build-time-tools=/scratch/mitchell/builds/4.3-arm-none-linux-gnueabi-respin/lite/install/arm-none-linux-gnueabi/bin</span>  

<span style="background-color: #cfe2f3;">Thread model: posix</span>  

<span style="background-color: #cfe2f3;">gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203)&nbsp;</span>  

  

&gt; Instalar as ferramentas necessárias  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# apt-get install git</span>  

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# apt-get install autoconf</span></div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# apt-get install libtool</span></div>

<div>
<span style="background-color: #cfe2f3;"><br/></span></div>

<div>
&gt; Clonar v4l-utils do git</div>

<span style="background-color: #cfe2f3;">root@ubuntu:~\# git clone git://linuxtv.org/v4l-utils.git</span>  

<span style="background-color: #cfe2f3;">Cloning into 'v4l-utils'...</span>  

<span style="background-color: #cfe2f3;">remote: Counting objects: 14446, done.</span>  

<span style="background-color: #cfe2f3;">remote: Compressing objects: 100% (3005/3005), done.</span>  

<span style="background-color: #cfe2f3;">remote: Total 14446 (delta 11375), reused 14397 (delta 11344)</span>  

<span style="background-color: #cfe2f3;">Receiving objects: 100% (14446/14446), 2.34 MiB | 329 KiB/s, done.</span>  

<span style="background-color: #cfe2f3;">Resolving deltas: 100% (11375/11375), done.</span>  

  

&gt; entrar na pasta e rodar o autoconf  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# cd v4l-utils/</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils\# autoreconf --force --install</span>  

<span style="background-color: #cfe2f3;">libtoolize: putting auxiliary files in AC\_CONFIG\_AUX\_DIR, \`build-aux'.</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`build-aux/config.guess'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`build-aux/config.sub'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`build-aux/install-sh'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`build-aux/ltmain.sh'</span>  

<span style="background-color: #cfe2f3;">libtoolize: putting macros in AC\_CONFIG\_MACRO\_DIR, \`m4'.</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`m4/libtool.m4'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`m4/ltoptions.m4'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`m4/ltsugar.m4'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`m4/ltversion.m4'</span>  

<span style="background-color: #cfe2f3;">libtoolize: copying file \`m4/lt~obsolete.m4'</span>  

<span style="background-color: #cfe2f3;">configure.ac:48: installing \`build-aux/missing'</span>  

<span style="background-color: #cfe2f3;">contrib/test/Makefile.am: installing \`build-aux/depcomp'</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils\#&nbsp;</span>  

<div>
<br/></div>

<div>
&gt; Configurar, compilar e instalar</div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils# ./configure --prefix=/data/video/v4l-utils-nojpeg --host=arm-none-linux-gnueabi &nbsp;--without-jpeg</span></div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils# make -i</span><br/>
<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils# make -i install</span><br/>
<br/>
O -i é para ignorar alguns erros na compilação de uma ferramenta que depende do Xorg, como o ardrone não tem Xorg (ainda não), pode compilar ignorando esse erro.<br/>
<br/>
Próximo passo é copiar a pasta /data/video/v4l-utils-nojpeg para o ardrone usando o filezilla do mesmo jeito que foi feito com o VLC, e entrar no TELNET do ardrone e criar os links para as bibliotecas que foram copiadas pelo FTP / Filezilla<br/>
<br/>
<span style="background-color: #cfe2f3;">root@ubuntu:~/v4l-utils# telnet 192.168.1.1</span><br/>
<span style="background-color: #cfe2f3;">BusyBox v1.14.0 (2012-08-20 14:37:54 CEST) built-in shell (ash)</span><br/>
<span style="background-color: #cfe2f3;">Enter 'help' for a list of built-in commands.</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">#</span><br/>
<div>
<span style="background-color: #cfe2f3;"># ln -s&nbsp;/data/video/v4l-utils-nojpeg/lib/libv4l2.so.0.0.0 /data/video/v4l-utils-nojpeg/lib/libv4l2.so.0</span></div>
<span style="background-color: #cfe2f3;"># ln -s&nbsp;/data/video/v4l-utils-nojpeg/lib/libv4lconvert.so.0.0.0 /data/video/v4l-utils-nojpeg/lib/libv4lconvert.so.0</span><br/>
<br/>
&gt; Testando na camera horizontal<br/>
<span style="background-color: #cfe2f3;"># /data/video/v4l-utils-nojpeg/bin/v4l2-ctl --all -d /dev/video0</span><br/>
<span style="background-color: #cfe2f3;">Driver Info (not using libv4l2):</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Driver name &nbsp; : p6_camif.0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Card type &nbsp; &nbsp; : p6_camif</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bus info &nbsp; &nbsp; &nbsp;:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Driver version: 0.0.5</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Capabilities &nbsp;: 0x04000001</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Video Capture</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Streaming</span><br/>
<span style="background-color: #cfe2f3;">Video input : 0 (Camera: ok)</span><br/>
<span style="background-color: #cfe2f3;">Video Standard = 0x00000000</span><br/>
<span style="background-color: #cfe2f3;">Format Video Capture:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Width/Height &nbsp;: 640/480</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Format &nbsp;: 'YU12'</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Field &nbsp; &nbsp; &nbsp; &nbsp; : None</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bytes per Line: 960</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Size Image &nbsp; &nbsp;: 460800</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Colorspace &nbsp; &nbsp;: Unknown (00000000)</span><br/>
<span style="background-color: #cfe2f3;">Crop Capability Video Capture:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bounds &nbsp; &nbsp; &nbsp;: Left 0, Top 0, Width 0, Height 0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Default &nbsp; &nbsp; : Left 0, Top 0, Width 640, Height 480</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Aspect: 1/1</span><br/>
<span style="background-color: #cfe2f3;">Crop Capability Video Capture:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bounds &nbsp; &nbsp; &nbsp;: Left 0, Top 0, Width 0, Height 0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Default &nbsp; &nbsp; : Left 0, Top 0, Width 640, Height 480</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Aspect: 1/1</span><br/>
<span style="background-color: #cfe2f3;">Crop: Left 0, Top 0, Width 640, Height 480</span><br/>
<span style="background-color: #cfe2f3;">Streaming Parameters Video Capture:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Frames per second: 25.000 (25/1)</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Read buffers &nbsp; &nbsp; : 0</span><br/>
<span style="background-color: #cfe2f3;">#</span><br/>
<div>
<br/></div>
<div>
&gt; Testando na camera vertical</div>
<div>
<div>
<span style="background-color: #cfe2f3;"># /data/video/v4l-utils-nojpeg/bin/v4l2-ctl --all -d /dev/video1</span></div>
<div>
<span style="background-color: #cfe2f3;">Driver Info (not using libv4l2):</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Driver name &nbsp; : p6_camif.1</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Card type &nbsp; &nbsp; : p6_camif</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bus info &nbsp; &nbsp; &nbsp;:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Driver version: 0.0.5</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Capabilities &nbsp;: 0x04000001</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Video Capture</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Streaming</span></div>
<div>
<span style="background-color: #cfe2f3;">Video input : 0 (Camera: ok)</span></div>
<div>
<span style="background-color: #cfe2f3;">Video Standard = 0x00000000</span></div>
<div>
<span style="background-color: #cfe2f3;">Format Video Capture:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Width/Height &nbsp;: 176/144</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Format &nbsp;: 'YU12'</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Field &nbsp; &nbsp; &nbsp; &nbsp; : None</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bytes per Line: 264</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Size Image &nbsp; &nbsp;: 38016</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Colorspace &nbsp; &nbsp;: Unknown (00000000)</span></div>
<div>
<span style="background-color: #cfe2f3;">Crop Capability Video Capture:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bounds &nbsp; &nbsp; &nbsp;: Left 0, Top 0, Width 0, Height 0</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Default &nbsp; &nbsp; : Left 0, Top 0, Width 640, Height 480</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Aspect: 1/1</span></div>
<div>
<span style="background-color: #cfe2f3;">Crop Capability Video Capture:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Bounds &nbsp; &nbsp; &nbsp;: Left 0, Top 0, Width 0, Height 0</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Default &nbsp; &nbsp; : Left 0, Top 0, Width 640, Height 480</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Pixel Aspect: 1/1</span></div>
<div>
<span style="background-color: #cfe2f3;">Crop: Left 0, Top 0, Width 176, Height 144</span></div>
<div>
<span style="background-color: #cfe2f3;">Streaming Parameters Video Capture:</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Frames per second: 25.000 (25/1)</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; Read buffers &nbsp; &nbsp; : 0</span></div>
<div>
<span style="background-color: #cfe2f3;">#</span></div>
</div>
<div>
<br/></div>
<div>
<br/></div>
<div>
<br/></div>
<div>
<br/></div>
<br/></div>

<div>
<br/></div>