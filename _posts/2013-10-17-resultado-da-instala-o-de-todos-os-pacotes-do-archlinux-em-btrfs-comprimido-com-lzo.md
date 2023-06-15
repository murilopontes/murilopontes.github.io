---
layout: post
title: Resultado da instalação de todos os pacotes do ArchLinux em BTRFS comprimido com LZO
categories:
 - Instalar todos pacotes
date: 2013-10-17 12:22:00 +0100
---

<div>
<span style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px;">Depois de instalar todos os pacotes com a linha a abaixo</span><br/>
<span style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px;"></span><br/>
<a name="more"></a><br/></div>

<span style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px;"></span>  

<blockquote class="tr_bq">
<span style="background-color: white; color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: 13px; line-height: 18px;">for x in $(pacman -Sg &amp;&amp; pacman -Ssq); do pacman --noconfirm --needed --force -S $x ; done</span></blockquote>

<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">O resultado é que nem todos os 6182 pacotes podem ser instalados juntos, cerca de 100 pacotes possuem problemas / conflitos / mazelas. De qualquer modo, a maioria dos pacotes pode ser instalada sem problemas.</span></span></div>

<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">Para fazer isso sem ter problemas de espaço em disco é bom que a partição raiz tenha pelo menos 150GB a 200GB. Com o BTRFS usando a compressão LZO transparente este requisito fica entre 100GB a 120GB. O download em cache ocupa de 25GB a 30GB, e os pacotes instalados ocupam cerca de 65GB a 70GB.</span></span></div>

<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">Depois da instalação recomendo fazer um defrag dos metadados do BTRFS, que pode ficar um pouco lento depois de instalar zilhões de arquivos.&nbsp;</span></span></div>

<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;"><br/></span></span></div>

<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">Para desfragmentar somente a raiz faça (leva uns 5 minutos):</span></span></div>

<div>
<blockquote class="tr_bq">
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">btrfs filesystem defrag /</span></span></blockquote>
<div>
<div>
<span style="color: #666666; font-family: Trebuchet MS, Trebuchet, Verdana, sans-serif; font-size: x-small;"><span style="line-height: 18px;">Se quiser desfragmentar o sistema inteiro faça&nbsp;</span></span><span style="color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: x-small; line-height: 18px;">(leva uns 240 minutos - mas pode continuar usando normal)</span><span style="color: #666666; font-family: 'Trebuchet MS', Trebuchet, Verdana, sans-serif; font-size: x-small; line-height: 18px;">:</span></div>
<div>
</div>
</div>
<div>
<blockquote class="tr_bq">
&nbsp; find &nbsp;/ -xdev -type f -print -exec btrfs filesystem defrag '{}' \;</blockquote>
</div>
<div>
<br/></div>
<div>
No mais é isso ai, provavelmente nunca mais vai precisa instalar nada. Para desenvolvedores é muito bom que todas as bibliotecas e todos os compiladores mais exóticos estão todos disponíveis.&nbsp;</div>
<div>
Tem mais uma vantagem no Arch Linux todos os pacotes são versões&nbsp;<span style="background-color: white; font-family: sans-serif; font-size: 13px; line-height: 19.1875px;"><b style="font-style: italic;">cutting edge, </b>o que facilita bastante se manter informado<b style="font-style: italic;">&nbsp;</b>um passo a frente de todos da concorrência.</span></div>
<div>
<br/></div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-wcHXAqwzlZE/Ul_CJjYBeFI/AAAAAAAAmkc/822a5yx93TI/s1600/todos-pacotes.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="252" src="http://1.bp.blogspot.com/-wcHXAqwzlZE/Ul_CJjYBeFI/AAAAAAAAmkc/822a5yx93TI/s400/todos-pacotes.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Archlinux com todos os pacotes de todos os repositórios instalados.</td></tr>
</tbody></table>
<br/></div>