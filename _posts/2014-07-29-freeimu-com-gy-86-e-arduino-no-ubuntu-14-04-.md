---
layout: post
title: FreeIMU com GY-86 e Arduino no Ubuntu 14.04 
categories:
 - Spherical
date: 2014-07-29 05:50:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Para ter uma IMU funcional não basta ler todos os sensores, é preciso remover o ruido das leituras, e fazer a fusão dos valores para ter uma estimativa mais precisa da orientação do sensores.<br/>
<br/>
<a name="more"></a><br/>
O projeto FreeIMU (<a href="http://www.varesano.net/projects/hardware/FreeIMU">http://www.varesano.net/projects/hardware/FreeIMU</a>) estava em pleno desenvolvimento até o final de 2012, quando o seu autor morreu. Os amigos do desenvolver prometeram continuar o projeto, mas isto não aconteceu ainda. Então resolvi criar um fork para dar continuidade ao projeto. Minha ideal inicial é colocar a biblioteca para funcionar no Ubuntu 14.04 com as versão atuais de todas as bibliotecas atualizadas.<br/>
O código corrigido pode ser encontrado no meu github (<a href="https://github.com/murix/open-inertial-measurement-unit">https://github.com/murix/open-inertial-measurement-unit</a>).<br/>
<br/>
Pretendo também portar para rodar na:<br/>
Stellaris LaunchPad&nbsp;com&nbsp;<a href="http://energia.nu/">Energia</a><br/>
Tiva C Series 123 LaunchPad&nbsp;com <a href="http://energia.nu/">Energia</a><br/>
STM32F103 com <a href="https://mbed.org/">MBED</a><br/>
FRDM-KL25Z&nbsp;com <a href="https://mbed.org/">MBED</a><br/>
<br/>
Na <a href="http://beagleboard.org/black">Beaglebone Black</a> criei uma camada de compatibilidade com a API do Arduino, isso já permite compilar o projeto como biblioteca estática.<br/>
<br/>
# pacotes necessários no Ubuntu 14.04<br/>
apt-get -y install&nbsp;python-qt4&nbsp;python-qt4-gl&nbsp;python-opengl arduino<br/>
<br/>
# baixar o código do FreeIMU com as correções necessárias para rodar no Ubuntu 14.04<br/>
<a href="https://github.com/murix/open-inertial-measurement-unit">https://github.com/murix/open-inertial-measurement-unit</a><br/>
<br/>
Para compilar o código para arduino nano v3, usei o próprio arduino que vem no Ubuntu 14.04 que é a versão 1.0.1, deve ser gravada na placa o sketch do FreeIMU-serial.<br/>
<br/>
O próximo passa é calibrar os sensores usando uma ferramenta feita em Python com Qt4 e OpenGL.<br/>
A ferramenta vai usar a conexão serial com o Arduino para capturar diversos samples dos sensores, e calcular com um método de calibração de "elipsoides na esfera" os valores que precisam ser gravados na EEPROM do arduino ou num arquivo ,h para pode ser embarcado no código. Um vez gravados os valores da calibração, é preciso resetar o Arduino.<br/>
<br/>
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/rlGxA3Hqn4Q" width="560"></iframe><br/>
<br/>
O teste do FreeIMU calibrado é feito usado a ferramenta Processing (<a href="https://www.processing.org/">https://www.processing.org/</a>) que também funciona com sketchs de Arduino e cria interfaces 3D para simulação. No video a seguir demonstro a biblioteca FreeIMU já calibrada rodar na placa de uma UAV que é composto por um Arduino Nano v3 junto com um Breakout board GY-86 (quase é 100% compatível com a versão de hardware 0.4.3 do FreeIMU).<br/>
<br/>
<br/>
<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/zizJOUMH_vE" width="560"></iframe>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-BpHGgQ9KRjo/U9g53EyAxRI/AAAAAAAAsk8/qmUr_-PMrT0/s1600/freeimu-sampling.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="279" src="http://1.bp.blogspot.com/-BpHGgQ9KRjo/U9g53EyAxRI/AAAAAAAAsk8/qmUr_-PMrT0/s1600/freeimu-sampling.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">FreeIMU : Capturando os valores descalibrados<br/>
Deve sem ser feitos giros completos de 360 nos eixos X,Y,Z para que o<br/>
algoritmo de otimização de aproximação de elipsoide em esfera calcule a calibração ótima.</td></tr>
</tbody></table>
<br/>
O algoritmo utilizado no cálculo da calibração ótima está no artigo:<br/>
Approximation of n-Dimensional Data Using Spherical and Ellipsoidal Primitives<br/>
<a href="http://staff.polito.it/giuseppe.calafiore/Documenti/Papers/Ellipsoidal%20Approximation_TSMC-02.pdf">http://staff.polito.it/giuseppe.calafiore/Documenti/Papers/Ellipsoidal%20Approximation_TSMC-02.pdf</a><br/>
<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://3.bp.blogspot.com/-WuIvN-wCQqE/U9g53Bp_MBI/AAAAAAAAsk4/jrgZ-FaxjSk/s1600/freeimu-calibrated.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="279" src="http://3.bp.blogspot.com/-WuIvN-wCQqE/U9g53Bp_MBI/AAAAAAAAsk4/jrgZ-FaxjSk/s1600/freeimu-calibrated.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">FreeIMU :&nbsp;Gerando os valores para calibrar o deslocamento e escala do sensores</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-eVFhyNXkc70/U9g53DI0-1I/AAAAAAAAsk0/dD4LK7NA5Ik/s1600/freeimu-cube.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="248" src="http://2.bp.blogspot.com/-eVFhyNXkc70/U9g53DI0-1I/AAAAAAAAsk0/dD4LK7NA5Ik/s1600/freeimu-cube.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">FreeIMU :&nbsp;Testando a placa calibrada com o cubo 3D</td></tr>
</tbody></table>
<br/>
<br/>
<br/></div>