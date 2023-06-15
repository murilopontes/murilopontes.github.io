---
layout: post
title: Tutorial- Sourcery G++ Lite for ARM GNU/Linux 2009q1 no Ubuntu 14.04
categories:
 - libboost
date: 2014-05-18 02:38:00 +0100
---

Compilador específico para projetos que devem rodar nativamente dentro do Ardrone v1.  

  

<a name="more"></a>  
  

No ubuntu 14.04 instale esses pacotes  

sudo apt-get install libgtk2.0-0:i386 libxtst6:i386 gtk2-engines-murrine:i386 lib32stdc++6 libxt6:i386 libdbus-glib-1-2:i386 libasound2:i386  

<div>
<br/></div>

<div>
Depois rode o instalador do compilador (instale no /opt)</div>

<div>
./arm-2009q1-203-arm-none-linux-gnueabi.bin</div>

<div>
<br/>
Instale também o libboost</div>

<div>
sudo apt-get&nbsp;install libboost-all-dev&nbsp;libbz2-dev<br/>
<br/>
Baixe os fontes boost-1.55 e compile com as seguintes configurações:<br/>
echo "using gcc : arm : /opt/CodeSourcery/Sourcery_G++_Lite/bin/arm-none-linux-gnueabi-g++ ; " &gt; &nbsp;/etc/site-config.jam<br/>
./bootstrap.sh<br/>
./bjam toolset=gcc-arm target-os=linux link=static --without-python --without-iostreams --without-log<br/>
<br/>
Se tudo der certo ao fim do build vai aparecer o seguinte texto:<br/>
<span style="background-color: #cfe2f3;">...found 6737 targets...</span><br/>
<span style="background-color: #cfe2f3;">The Boost C++ Libraries were successfully built!</span><br/>
<span style="background-color: #cfe2f3;">The following directory should be added to compiler include paths:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; /opt/boost_1_55_0-ardrone-ubuntu1404</span><br/>
<span style="background-color: #cfe2f3;">The following directory should be added to linker library paths:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; /opt/boost_1_55_0-ardrone-ubuntu1404/stage/lib</span><br/>
<span style="background-color: #cfe2f3;">root@murix-quad:/opt/boost_1_55_0-ardrone-ubuntu1404#</span><br/>
<br/></div>