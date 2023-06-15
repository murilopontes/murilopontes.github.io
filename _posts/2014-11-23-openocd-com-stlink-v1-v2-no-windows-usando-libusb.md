---
layout: post
title: OpenOCD com STLink v1 / v2 no Windows usando libUSB
categories:
 - GNU ARM Embedded
date: 2014-11-23 10:46:00 +0000
---

Para ativar o debug com o <a href="http://eclipse%20gnu%20arm%20embedded/" target="_blank">Eclipse GNU ARM Embedded</a> além dos plugins instalados.  

<div>
É preciso ter o <a href="http://www.freddiechopin.info/en/download/category/4-openocd" target="_blank">OpenOCD de windows</a>&nbsp;,&nbsp;<a href="http://zadig.akeo.ie/" target="_blank">Zadig</a>&nbsp;,&nbsp;<a href="https://launchpad.net/gcc-arm-embedded" target="_blank">GNU Tools for ARM Embedded Processors</a>&nbsp;</div>

<div>
Depois de baixar e extrair tudo isso, o próximo passo é abrir o Zadig selecionar o STLink e mandar fazer o <i>replace</i> do driver.<br/>
<br/>
<a name="more"></a><br/></div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-oyuAWq8BAN4/VHG6j0MOAeI/AAAAAAAAtvI/47lEZpbSFhg/s1600/zadig-stm32vldiscovery.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="366" src="http://2.bp.blogspot.com/-oyuAWq8BAN4/VHG6j0MOAeI/AAAAAAAAtvI/47lEZpbSFhg/s1600/zadig-stm32vldiscovery.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">STLink com driver libUSB</td></tr>
</tbody></table>

<div>
Com o driver libUSB tomando conta do STLink, o OpenOCD passará a funcionar do mesmo jeito do Linux.</div>

<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-cYwYgEaLcmc/VHG94Leca4I/AAAAAAAAtvU/saIjj0Mh6k4/s1600/eclipse-arm-embedded-openocd-debug.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="290" src="http://4.bp.blogspot.com/-cYwYgEaLcmc/VHG94Leca4I/AAAAAAAAtvU/saIjj0Mh6k4/s1600/eclipse-arm-embedded-openocd-debug.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Eclipse ARM Embedded com debug via OpenOCD e suporte a ARM ITM e Semihosting</td></tr>
</tbody></table>
Como pode ser visto dá para usar o printf com a saída direto pro GDB, também dá para usar arquivos do PC no MCU passando pelo GDB,<br/>
<br/>
<br/></div>

<div>
<br/></div>

<div>
</div>