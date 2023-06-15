---
layout: post
title: Rádio CC1101 433MHz @ 10dbm testado alcance de 300 metros com sucesso
categories:
 - post
date: 2014-02-11 13:33:00 +0000
---

<div>
Rádio CC1101 testado em ambiente urbano com todo tipo de obstáculo foi um sucesso.</div>

<div>
Configurado com baudrate de 38.4k o teste consistiu em manter um enlace bidirecional com troca de pacotes com intervalo aleatório entre 100ms a 1000ms. Com perda estimada menor que 1% o rádio recebe pacotes com potência inferior a -100 dbm.</div>

<div>
<br/></div>

<div>
O código fonte está disponível no meu github&nbsp;</div>

<div>
https://github.com/murix/energia-0101E0011</div>

<div>
<br/></div>

<div>
A Stellaris foi descontinuada com a entrada Tiva C Series [Stellaris revisada]&nbsp;</div>

<div>
https://estore.ti.com/Tiva-C-LaunchPad.aspx</div>

<div>
<br/></div>

<div>
As placas de CC1101 usadas no experimento podem ser encontradas no DX, o único problema é que o passo do conector é de 2mm, o que dificulta a instalação em placas com passo de 2.54 mm</div>

<div>
http://dx.com/p/diy-cc1101-433mhz-wireless-transceiver-module-for-arduino-green-2-pcs-149251#.UvojNvldWaw</div>

<div>
<br/></div>

<div>
Outro lote de CC1101 usado em experimentos pode ser encontrado no Aliexpress, que tem diversas opções de tamanho e preços.&nbsp;</div>

<div>
http://www.aliexpress.com/wholesale?SearchText=cc1101</div>

<div>
<div>
<br/></div>
</div>

<div>
Esquemático de ligação no comentário da foto.</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-eYS42aUm5F0/UvhZUU_xmMI/AAAAAAAAo0A/pz91tKyiSwc/s1600/IMG_20140210_014450.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="480" src="http://4.bp.blogspot.com/-eYS42aUm5F0/UvhZUU_xmMI/AAAAAAAAo0A/pz91tKyiSwc/s1600/IMG_20140210_014450.jpg" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC1101 conectado na porta SPI0 da Stellaris Launchpad.<br/>
CC1101 -&gt; Stellaris / Tiva<br/>
GDO0 -&gt; PB6<br/>
CSN -&gt;PA3<br/>
SO -&gt; PA4<br/>
SCK -&gt; PA2<br/>
SI -&gt; PA5</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-ZMYsADg3uhw/UvWnhd38wuI/AAAAAAAAozA/h7QmuVnsXeA/s1600/IMG_20140208_004128.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="480" src="http://3.bp.blogspot.com/-ZMYsADg3uhw/UvWnhd38wuI/AAAAAAAAozA/h7QmuVnsXeA/s1600/IMG_20140208_004128.jpg" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Hardware usado no teste de alcance<br/>
CC1101 + Stellaris Launchpad<br/>
CC1101 + Tiva C Series Launchpad</td></tr>
</tbody></table>

  

<div class="separator" style="clear: both; text-align: center;">
</div>

  

<div class="separator" style="clear: both; text-align: center;">
</div>

  

<img border="0" src="http://maps.google.com/maps/api/staticmap?size=600x500&amp;path=fillcolor:0x00FF00|weight:1|color:0xFFFFFF|enc:na_p@ne_tE?g@JmAHe@XkAb@cATa@p@{@Z[|@o@`@UdAa@hAWd@GlAGf@?lAFd@FhAVdA`@~@l@\V\Zp@z@T`@b@bAXjAHd@HlA@f@Ad@IlAIf@YhAc@dAU^q@z@]Z{@n@a@TeA`@iAVe@FmAFg@?mAGe@GiAWeAa@aAk@]Y[[q@{@U_@c@eAYiAIg@KmA?e@&amp;sensor=true"/>