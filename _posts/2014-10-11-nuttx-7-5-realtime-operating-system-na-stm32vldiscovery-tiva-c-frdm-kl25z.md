---
layout: post
title: Nuttx 7.5 Realtime Operating System na STM32VLDiscovery, Tiva C, FRDM-KL25Z
categories:
 - CZ ministm32f103v_-ek
date: 2014-10-11 21:49:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
O Nuttx (<a href="http://www.nuttx.org/">http://www.nuttx.org/</a>) &nbsp;é um sistema operacional de tempo real que tem praticamente tudo que tem no Linux.<br/>
A grande vantagem é que cabe em microcontroladores de 8-bits até 32-bits, consumo de energia ultra-low-power.<br/>
<br/>
<a name="more"></a><br/><br/>
Com o Nuttx instalado é possível usar a biblioteca pthread do praticamente do mesmo jeito do Linux, também dá para fazer scripts e gravar na própria flash do microcontrolador, tem Ramdisk, sistema de arquivos em rede (NFS), e drivers para zilhões de sensores, rádios e adaptadores de rede, ... é praticamente um PC com Linux só que ultra-low-power.<br/>
<br/>
<b>UPDATE</b>: &nbsp;<a class="g-profile" href="https://plus.google.com/105828292850714221005" target="_blank">+Jeronimo Avelar Filho</a>&nbsp;me reportou bugs no build pelo MacOSX. Faltou colocar neste post uma coisa em relação ao processo de compilação. Quando o Nuttx é configurado para uma placa cria vários links dentro do sistema de build, se mudar de configuração e tentar buildar denovo vai dar vários erros, antes de reconfigurar para outra placa é preciso fazer um "make distclean" para limpar completamente os resíduos da configuração anterior. Outra opção é fazer um git checkout para cada placa em diretórios diferentes.<br/>
<br/>
<br/>
<b><u>Instalando na stm32vldiscovery</u></b><br/>
<br/>
#baixar os fontes<br/>
git clone http://git.code.sf.net/p/nuttx/git<br/>
#entrar na pasta<br/>
cd git<br/>
#mudar para o código da tag 7.5<br/>
git checkout nuttx-7.5<br/>
#ir para pasta de ferramentas<br/>
cd nuttx/tools<br/>
#configurar para stm32vldiscovery<br/>
./configure.sh stm32f100rc_generic/nsh<br/>
# voltar para raiz do nuttx<br/>
cd ..<br/>
#para compilar o projeto da shell nsh para stm32vldiscovery<br/>
make<br/>
#para gravar o projeto na stm32vldiscovery (instale antes https://github.com/texane/stlink)<br/>
st-flash write nuttx.bin 0x8000000<br/>
#conecte um cabo usb-ttl (pl2303, ftdi, cp2301, ...) nos pinos PA2 e PA3<br/>
para ter acesso a console ao prompt do NSH, comandos de Linux como free, ps, df e vários outros estão disponíveis.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-eNiAfhwP828/VDl4Q2Ao1AI/AAAAAAAAtMc/XQy4aYojjp8/s1600/IMG_20141011_153135.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-eNiAfhwP828/VDl4Q2Ao1AI/AAAAAAAAtMc/XQy4aYojjp8/s1600/IMG_20141011_153135.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">STM32VLDiscovery com ARM Cortex-M3 STM32F103RG <br/>
(configurado para usar somente 24 Kbytes de RAM)<br/>
RAM 96 Kbytes<br/>
Flash 1 MByte<br/>
Espaço da RAM usado pelo Nuttx.bin é 11KBytes fica 85KBytes livres para aplicativos<br/>
Espaço da flash usado pelo Nuttx.bin é 67Kbytes fica 957Kbytes livres para aplicativos</td></tr>
</tbody></table>
No caso a minha STM32VLDiscovery foi modificada para substituir o STM32F100RB (8KB RAM 128KB flash) por um STM32F103RG (96KB RAM 1MB flash).<br/>
<br/>
Foi necessário mudar algumas coisas no código para ajustar o tamanho da RAM.<br/>
<br/>
Também dá para usar a STM32VLDiscovery para gravar outras placas STM32 por SWD, que faz o mesmo serviço de uma JTAG usando apenas 2 fios.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Vp8_rFEr2Kc/VDm2GZLKmCI/AAAAAAAAtOQ/BbGjq4z9klE/s1600/stm32-swd.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://4.bp.blogspot.com/-Vp8_rFEr2Kc/VDm2GZLKmCI/AAAAAAAAtOQ/BbGjq4z9klE/s1600/stm32-swd.png" width="316"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Para ativar o SWD para um STM32 externo basta abrir os jumpers do CN3.<br/>
E conectar o SWCLK e SWDIO no STM32 externo,<br/>
o GND é mandatório sempre ligar,<br/>
o VCC liga se precisa alimentar a placa externa.</td></tr>
</tbody></table>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-endOFVWTeIo/VDm_CWhqHiI/AAAAAAAAtOs/Yjv2M8x6H4c/s1600/IMG_20141011_203518.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-endOFVWTeIo/VDm_CWhqHiI/AAAAAAAAtOs/Yjv2M8x6H4c/s1600/IMG_20141011_203518.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">STM32VL gravando o Nuttx.bin em uma CZ miniSTM32F103V_-EK<br/>
Esse é um STM32F103VET6 - ARM Cortex-M3 64KB RAM e 512KB Flash<br/>
<br/>
STM32VL pin 2 --&gt; externo PA14 (SWCLK)<br/>
STM32VL pin 3 --&gt; externo GND<br/>
STM32VL pin 4 --&gt; externo PA13 (SWDIO)</td></tr>
</tbody></table>
<br/>
<br/>
<b><u>Instalando na FRDM-KL25Z</u></b><br/>
<br/>
#baixar os fontes<br/>
git clone http://git.code.sf.net/p/nuttx/git<br/>
#entrar na pasta<br/>
cd git<br/>
#mudar para o código da tag 7.5<br/>
git checkout nuttx-7.5<br/>
#ir para pasta de ferramentas<br/>
cd nuttx/tools<br/>
#configurar para FRDM-KL25Z<br/>
./configure.sh freedom-kl25z/nsh<br/>
# voltar para raiz do nuttx<br/>
cd ..<br/>
#para compilar o projeto da shell nsh para FRDM-KL25Z<br/>
make<br/>
#instalar o firmware da OpenSDA da MBED<br/>
http://developer.mbed.org/handbook/Firmware-FRDM-KL25Z<br/>
Agora que a FRDM-KL25Z virou um pendrive MBED gravador de firmware basta arrastar o nuttx.bin para dentro.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-4cDUaCWCMGE/VDmDWud0oEI/AAAAAAAAtNA/UYk5twlJky0/s1600/IMG_20141011_162104.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-4cDUaCWCMGE/VDmDWud0oEI/AAAAAAAAtNA/UYk5twlJky0/s1600/IMG_20141011_162104.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Freescale FRDM KL25Z com ARM Cortex-M0 16KBytes RAM 128KBytes<br/>
Usado de RAM pelo Nuttx.bin 6 KB e livre 10 KB para apps<br/>
Usado de Flash pelo Nuttx.bin 38KB e livre 90KB para apps</td></tr>
</tbody></table>
Um outra vantagem do OpenSDA da MBED é que dá para acessar o NSH do Nuttx pela porta serial USB virtual da MBED, no caso do Linux é só abrir o minicom na /dev/ttyACM0<br/>
<br/>
Não foi necessário modificar nada no código para funcionar de primeira.<br/>
<br/>
<b><u>Instalando na Tiva EK-TM4C123GXL e Stellaris EK-LM4F120XL</u></b><br/>
<br/>
#baixar os fontes<br/>
git clone http://git.code.sf.net/p/nuttx/git<br/>
#entrar na pasta<br/>
cd git<br/>
#mudar para o código da tag 7.5<br/>
git checkout nuttx-7.5<br/>
#ir para pasta de ferramentas<br/>
cd nuttx/tools<br/>
#configurar para Tiva/Stellaris<br/>
./configure.sh tm4c123g-launchpad/nsh<br/>
# voltar para raiz do nuttx<br/>
cd ..<br/>
#para compilar o projeto da shell nsh para Tiva/Stellaris<br/>
make<br/>
#instale o lm4flash (https://github.com/utzig/lm4tools)<br/>
#programe a Tiva/Stellaris com o nuttx.bin<br/>
<div>
lm4flash nuttx.bin&nbsp;</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-pXX_WOwGCq4/VDmVg6HanzI/AAAAAAAAtNk/G72wTglOW1M/s1600/IMG_20141011_173845.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-pXX_WOwGCq4/VDmVg6HanzI/AAAAAAAAtNk/G72wTglOW1M/s1600/IMG_20141011_173845.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tiva C com ARM Cortex-M4F 32KB RAM 256KB Flash<br/>
Usado de RAM pelo Nuttx.bin 10 KB e livre 22 KB para apps<br/>
Usado de Flash pelo Nuttx.bin 52KB e livre 204 KB para apps</td></tr>
</tbody></table>
<div>
No caso da Tiva/Stellaris já existe um conversor serial usb na placa, basta abrir o minicom na /dev/ttyACM0</div>
<br/>
Foi necessários modificar o toolchain para compilar com o&nbsp;GNU Tools for ARM Embedded Processors (https://launchpad.net/gcc-arm-embedded), o STM32 e o FRDM-KL25 também usam esse mesmo toolchain. Também dá para usar outros toolchains ou criar o seu próprio.<br/>
<br/>
<br/>
Como considerações finais deste post, pode se dizer que instalando o Nuttx, não importa mais qual o microcontrolador usado, sempre haverá uma interface de programação praticamente igual ao Linux, e dezenas de drivers e bibliotecas prontas para uso.<br/>
<br/></div>