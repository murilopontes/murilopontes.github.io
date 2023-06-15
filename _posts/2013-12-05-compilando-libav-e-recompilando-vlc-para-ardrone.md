---
layout: post
title: Compilando libav e recompilando VLC para ardrone
categories:
 - post
date: 2013-12-05 19:09:00 +0000
---

<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif;"><span style="background-color: white; font-size: 13px; line-height: 18px;">tutorial: adicionando o VLC ao ardrone</span></span>  

<a name="more"></a>  

<span style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px;">Esse post presume que você já tenha feito todo o setup para compilar o VLC para ardrone.</span>  

<a href="http://dronespersonalizados.blogspot.com.br/2013/11/cross-compile-vlc-para-ardrone-usando-o.html" style="background-color: white; color: #888888; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px; text-decoration: none;">http://dronespersonalizados.blogspot.com.br/2013/11/cross-compile-vlc-para-ardrone-usando-o.html</a>  

  

O libav é uma das mais completas bibliotecas para codificação e decodificação de audio e vídeo.  

  

&gt; Ambiente de compila ARM  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# su -</span>  

  

&gt; Baixar libav do git   

<span style="background-color: #cfe2f3;">root@ubuntu:~\# git clone git://git.libav.org/libav.git</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# cd libav/</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/libav\#</span>  

  

&gt; configuração não muito livre  

root@ubuntu:~/libav# ./configure --cross-prefix=arm-none-linux-gnueabi- --enable-cross-compile --target-os=linux --arch=arm --cpu=arm926ej-s --disable-debug --disable-altivec --disable-sse --disable-armv6 --disable-armv6t2 &nbsp;--disable-mmx --disable-neon --disable-amd3dnow --enable-shared --enable-static --prefix=/data/video/vlc &nbsp;--enable-gpl --enable-nonfree --enable-version3  

  

&gt; configuração livre  

<span style="background-color: #cfe2f3;">root@ubuntu:~/libav\# ./configure --cross-prefix=arm-none-linux-gnueabi- --enable-cross-compile --target-os=linux --arch=arm --cpu=arm926ej-s --disable-debug --disable-altivec --disable-sse --disable-armv6 --disable-armv6t2 &nbsp;--disable-mmx --disable-neon --disable-amd3dnow --enable-shared --enable-static --prefix=/data/video/vlc</span>  

  

&gt; Compilar e instalar libav  

<span style="background-color: #cfe2f3;">root@ubuntu:~/libav\# make</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/libav\# make install</span>  

  

  

&gt; Baixar, extrair, configurar, compilar e instalar o pkg-config para ardrone  

<span style="background-color: #cfe2f3;">root@ubuntu:~/libav\# cd ~/Downloads</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\# wget http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\#&nbsp; tar xfvz pkg-config-0.28.tar.gz</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads\# cd pkg-config-0.28</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/pkg-config-0.28\# ./configure --prefix=/data/video/vlc --build=arm-none-linux-gnueabi</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/pkg-config-0.28\# make</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/pkg-config-0.28\# make install</span><span style="background-color: #cfe2f3;"></span>  

<span style="background-color: #cfe2f3;"></span>  

  

&gt; Colocar o pkg-config no PATH para o build do VLC encontrar   

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/pkg-config-0.28\# export PATH=/data/video/vlc/bin:$PATH</span>  

  

&gt; Recompilar o VLC com LIBAV  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/pkg-config-0.28\# cd ../vlc-2.1.1</span>  

<span style="background-color: #cfe2f3;">root@ubuntu:~/Downloads/vlc-2.1.1\#&nbsp;</span><span style="background-color: #cfe2f3;">./configure --host=arm-none-linux-gnueabi --disable-lua --disable-mad --disable-swscale --disable-a52 --disable-xcb --disable-libgcrypt --disable-dbus --disable-alsa --disable-pulse --disable-libxml2 --disable-udev --disable-freetype --disable-sdl --disable-caca --disable-bonjour --enable-run-as-root --prefix=/data/video/vlc &amp;&amp; make &amp;&amp; make install</span>  

  

  