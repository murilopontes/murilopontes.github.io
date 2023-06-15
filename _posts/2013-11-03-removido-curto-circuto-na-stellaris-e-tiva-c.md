---
layout: post
title: Removido curto-circuto na Stellaris e Tiva C
categories:
 - post
date: 2013-11-03 15:19:00 +0000
---

Para solucionar o curto, é preciso remover os resistores R9 e R10.

<div>
<a name="more"></a><br/><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-USANo2XSIFM/UnZoZpXwqlI/AAAAAAAAm7k/gc6fnhq7RSU/s1600/IMG_20131103_120921.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-USANo2XSIFM/UnZoZpXwqlI/AAAAAAAAm7k/gc6fnhq7RSU/s320/IMG_20131103_120921.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Removido R9 e R10, eliminado o curto-circuito dos pinos&nbsp;<span style="background-color: white; color: #333333; font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 15px; line-height: 25px; text-align: start;">PD0/</span><span style="background-color: white; color: #333333; font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 15px; line-height: 25px; text-align: start;">PB6</span><span style="background-color: white; color: #333333; font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 15px; line-height: 25px; text-align: start;">&nbsp;e PD1/PB7.<br/>R9 e R10 eram resistores de 0 ohm, para manter a compatibilidade com os Boostpacks dos kits MSP430 Launchpad.</span></td></tr>
</tbody></table>
<br/></div>