---
layout: post
title: tutorial- cross compile libboost 1.49/1.55 for ARM Linux (ardrone)
categories:
 - ARM
date: 2014-03-29 03:01:00 +0000
---

Tutorial completo para compilar a lib Boost para ardrone v1.  

  

<a name="more"></a>  
  

  

__1) Download boost 1.49 / 1.55&nbsp;__  

  

<span style="background-color: #cfe2f3;">http://www.boost.org/</span>  

<span style="background-color: #cfe2f3;">http://www.boost.org/users/history/version\_1\_55\_0.html</span>  

<span style="background-color: #cfe2f3;">http://sourceforge.net/projects/boost/files/boost/1.55.0/boost\_1\_55\_0.7z/download</span>  

  

__2) Bootstrap build system - 1.55__  

* Visual Studio 2013 must be installed before.  

* Sourcery G++ Lite for ARM GNU Linux 2009q1-203 must be installed before.  

  

<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_55\_0&gt;bootstrap.bat</span>  

<span style="background-color: #cfe2f3;">Building Boost.Build engine</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">Bootstrapping is done. To build, run:</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; .\\b2</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">To adjust configuration, edit 'project-config.jam'.</span>  

<span style="background-color: #cfe2f3;">Further information:</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Command line help:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; .\\b2 --help</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Getting started guide:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; http://boost.org/more/getting\_started/windows.html</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Boost.Build documentation:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; http://www.boost.org/boost-build2/doc/html/index.html</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_55\_0&gt;</span>  

  

__3) Bootstrap build system - 1.49__  

  

<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_49\_0&gt;bootstrap.bat</span>  

<span style="background-color: #cfe2f3;">Building Boost.Build engine</span>  

<span style="background-color: #cfe2f3;">cl : Command line warning D9035 : option 'GZ' has been deprecated and will be re</span>  

<span style="background-color: #cfe2f3;">moved in a future release</span>  

<span style="background-color: #cfe2f3;">cl : Command line warning D9036 : use 'RTC1' instead of 'GZ'</span>  

<span style="background-color: #cfe2f3;">cl : Command line warning D9002 : ignoring unknown option '/MLd'</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">Bootstrapping is done. To build, run:</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; .\\b2</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">To adjust configuration, edit 'project-config.jam'.</span>  

<span style="background-color: #cfe2f3;">Further information:</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Command line help:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; .\\b2 --help</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Getting started guide:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; http://boost.org/more/getting\_started/windows.html</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; - Boost.Build documentation:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; http://www.boost.org/boost-build2/doc/html/index.html</span>  

<span style="background-color: #cfe2f3;">  
</span>
<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_49\_0&gt;</span>  

  

  

__4) Configuração do build system__  

O arquivo user-config.jam deve ser criado antes de iniciar o build com a ferramenta bjam  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-V0N72x4PSu0/UzYVR_kE0eI/AAAAAAAApw8/g-EszxPaMEo/s1600/user-config-jam.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="162" src="http://4.bp.blogspot.com/-V0N72x4PSu0/UzYVR_kE0eI/AAAAAAAApw8/g-EszxPaMEo/s1600/user-config-jam.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">user-config.jam<br/>
deve ser salvo do diretório home do usuário,<br/>
e as barras sempre devem ser assim /, não use barras assim \&nbsp;</td></tr>
</tbody></table>

  

__5) bjam Boost 1.49&nbsp;__  

<span style="background-color: #cfe2f3;"></span>  

<span style="background-color: #cfe2f3;">bjam toolset=gcc-arm target-os=linux link=static --without-python threadapi=pthread</span>  

<div>
<span style="background-color: #cfe2f3;"><br/></span></div>

<span style="background-color: #cfe2f3;">...updated 363 targets...</span>  

<span style="background-color: #cfe2f3;">The Boost C++ Libraries were successfully built!</span>  

<span style="background-color: #cfe2f3;">The following directory should be added to compiler include paths:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; C:/ARM-murix/boost\_1\_49\_0</span>  

<span style="background-color: #cfe2f3;">The following directory should be added to linker library paths:</span>  

<span style="background-color: #cfe2f3;">&nbsp; &nbsp; C:\\ARM-murix\\boost\_1\_49\_0\\stage\\lib</span>  

<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_49\_0&gt;</span>  

  

__6) bjam Boost 1.55&nbsp;__  

__  
__
<span style="background-color: #cfe2f3;">bjam toolset=gcc-arm target-os=linux link=static --without-python --without-context &nbsp;--without-log threadapi=pthread</span>  

__  
__
<span style="background-color: #cfe2f3;">...failed updating 2 targets...</span>  

  

<span style="background-color: #cfe2f3;">...skipped 3 targets...</span>  

<span style="background-color: #cfe2f3;">C:\\ARM-murix\\boost\_1\_55\_0&gt;</span>  

  

__7) Considerações finais__  

  

Se for utilizada alguma biblioteca que faça uso do 

<cfenv> é necessário, incluir no projeto o caminho:&nbsp;</cfenv>

  

<span style="background-color: #cfe2f3;">C:\\ARM-murix\\armgcc-2009q1-ardrone\\arm-none-linux-gnueabi\\libc\\usr\\include</span>  

pois a implementação do GCC 4.3.3 não possui a implementação completa deste arquivo,  

mas a libc incluída do no Sourcery G++ Lite for ARM possui a versão completa que vai eliminar todos os erros de compilação.  

  

  

  

  

  

  

  