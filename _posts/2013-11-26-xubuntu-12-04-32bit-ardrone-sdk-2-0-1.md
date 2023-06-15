---
layout: post
title: xubuntu 12.04 32bit + ardrone sdk 2.0.1
categories:
 - post
date: 2013-11-26 17:39:00 +0000
---

tutorial completo  

<a name="more"></a>  

  

1) instale o xubuntu 12.04 32bit no PC ou VM  

  

2) torne-se root  

  

3) copie o SDK para PC ou VM  

  

4) extrair o SDK  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# tar xfvz ARDrone\_SDK\_2\_0\_1.tar.gz</span>  

  

5) ir para os exemplos  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# cd ARDrone\_SDK\_2\_0\_1/Examples/Linux</span>  

  

6) compilar tudo  

<span style="background-color: #cfe2f3;">root@ubuntu:~/ARDrone\_SDK\_2\_0\_1/Examples/Linux\# make</span>  

<div>
<br/></div>

<div>
<div>
<span style="background-color: #cfe2f3;">Checking required Ubuntu packages ...</span></div>
<div>
<span style="background-color: #cfe2f3;">You should install the following packages to compile the AR.Drone SDK with Ubuntu:</span></div>
<div>
</div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; daemontools : Mandatory to build the AR.Drone project on Ubuntu</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; libsdl1.2-dev</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; libgtk2.0-dev</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; libxml2-dev</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; libudev-dev</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; libiw-dev&nbsp;</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;">Do you want to install them now [y/n] ?</span></div>
</div>

<div>
Resposta "y" e depois "y" denovo</div>

<div>
Aguarde o download e instalação, que o build continua.</div>

<div>
<br/></div>

<div>
7) Ok, tudo pronto.</div>

<div>
<div>
<span style="background-color: #cfe2f3;">ld ardrone_testing_tool</span></div>
<div>
<span style="background-color: #cfe2f3;">make[1]: Leaving directory `/root/ARDrone_SDK_2_0_1/Examples/Linux/Testbenches/ftp_test/Build'</span></div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/ARDrone_SDK_2_0_1/Examples/Linux#</span>&nbsp;</div>
</div>

<div>
Usando a versão 12.04 é o build do ardrone SDK é expresso e sem problema.</div>

<div>
Testei usando a versão 13.10 mas vários problemas ocorreram, alguns com soluções bem rápidas, outros bastantes cabulosos. Como no mundo virtualizado é mais fácil criar uma VM com as versões já homologadas para cada tarefa especifica. Não resta dúvida, o 13.10 foi descartado para esta tarefa e recomendo a todos usar o 12.04 que funciona perfeito.</div>

<div>
<br/></div>

<div>
8) Mudar para pasta dos binários recém compilados</div>

<div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/ARDrone_SDK_2_0_1/Examples/Linux# cd ../Linux/Build/Release/</span></div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release#</span></div>
</div>

<div>
<br/></div>

<div>
9) Rodar a ferramenta de navegação (já vem com suporte a controle Xbox 360)</div>

<div>
<br/></div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~/ARDrone_SDK_2_0_1/Examples/Linux/Build/Release# ./ardrone_navigation&nbsp;</span></div>

<div>
<div>
<span style="background-color: #cfe2f3;">AR.Drone Navigation - build Nov 26 2013 09:13:28</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;">Setting locale to en_GB.UTF-8</span></div>
<div>
<span style="background-color: #cfe2f3;">===================+&gt; 192.168.1.1</span></div>
<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-yW6_m_6UK1w/UpTcI6d89SI/AAAAAAAAncM/O1l3mQAzFg4/s1600/Screenshot+-+11262013+-+09:31:21+AM.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="256" src="http://1.bp.blogspot.com/-yW6_m_6UK1w/UpTcI6d89SI/AAAAAAAAncM/O1l3mQAzFg4/s1600/Screenshot+-+11262013+-+09:31:21+AM.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Este é o ardrone_navigation com as 2 câmeras funcionando e controle de Xbox 360 configurado.</td></tr>
</tbody></table>
<br/></div>
</div>

<div>
<br/></div>

<div>
<br/></div>