---
layout: post
title: Debug Stellaris Lauchpad com OpenOCD
categories:
 - OpenOCD
date: 2013-11-17 15:18:00 +0000
---

Desenvolver sem debug é tenso.  

  

<a name="more"></a>  
  

Depois de encontrar o projeto http://energia.nu que é um port da API do Arduino para Stellaris e MSP430 descobri que existe o mesmo problema do Arduino, não tem debug avançado.  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-jaX-1vCa_K0/UoVUs7-NLAI/AAAAAAAAnMw/WHiObWTb9Ug/s1600/energia-ide.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://4.bp.blogspot.com/-jaX-1vCa_K0/UoVUs7-NLAI/AAAAAAAAnMw/WHiObWTb9Ug/s320/energia-ide.PNG" width="265"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Energia é um clone do Arduino para Stellaris / Tiva C / MSP430</td></tr>
</tbody></table>

  

Estendendo o processo investigativo, descobri o toolchain usado no Energia  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-P2nW9w0YrIE/UoVVKjmWr-I/AAAAAAAAnM4/vPSE3dJ5GZ4/s1600/energia-gcc-yagarto.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="162" src="http://4.bp.blogspot.com/-P2nW9w0YrIE/UoVVKjmWr-I/AAAAAAAAnM4/vPSE3dJ5GZ4/s320/energia-gcc-yagarto.PNG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O Energia usa a toolchain GCC do Yagarto [&nbsp;<a href="http://www.yagarto.org/">http://www.yagarto.org/</a>&nbsp;]</td></tr>
</tbody></table>

Dai que essa toolchain já vem com o &nbsp;"arm-none-eabi-gdb.exe" e "arm-none-eabi-gcc.exe".  

Isso é um bom sinal, já tem o GDB pronto para rodar, só não tem contato dele com a IDE.  

  

É ai que entra em cena o OpenOCD (Open On-Chip-Debugger) que é uma ferramenta ao estilo Linux, que faz interface com praticamente todos os hardware de debug existentes na Terra!  

Para minha alegria a partir da versão 0.7.0 do OpenOCD, a interface ICDI da Stellaris e Tiva C, já são suportadas automagicamente.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-C0MrtlBqoGc/UoVS-wqcAyI/AAAAAAAAnMk/U1y1TvDhayg/s1600/openocd-stellaris.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="163" src="http://4.bp.blogspot.com/-C0MrtlBqoGc/UoVS-wqcAyI/AAAAAAAAnMk/U1y1TvDhayg/s640/openocd-stellaris.PNG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">É só extrair e executar com a linha de comando acima que já tomou posso do debug da Stellaris.<br/>
No caso do windows 8.1 64 bit, só funciona com os binários da pasta bin-x64, tentei com a bin no windows 8.1 64 bit, mas só deu problema.</td></tr>
</tbody></table>

Uma vez aberto o OpenOCD, agora entra a parte de compilar uma aplicação com flags de Debug do GCC e usar o GDB para depurar.  

  

  

  

  

Outra toolchain GCC muito boa é a do Linaro.  

<http://www.linaro.org/downloads/>  

http://launchpad.net/gcc-arm-embedded/4.7/4.7-2013-q1-update/+download/gcc-arm-none-eabi-4_7-2013q1-20130313-win32.exe