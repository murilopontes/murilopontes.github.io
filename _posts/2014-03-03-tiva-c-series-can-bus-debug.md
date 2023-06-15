---
layout: post
title: Tiva C Series- CAN Bus debug
categories:
 - CCS
date: 2014-03-03 23:09:00 +0000
---

<div class="separator" style="clear: both; text-align: justify;">
Tiva C Series possui &nbsp;portas CAN e vem com alguns exemplos no TivaWare.</div>

<div class="separator" style="clear: both; text-align: justify;">
Ao testar os exemplos encontrei problemas com interrupções e reset infinito.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
</div>

<a name="more"></a>  

<div class="separator" style="clear: both; text-align: justify;">
Depois de alguns ajustes no vetor de interrupções e melhorias no debug, finalmente estabilizei os dois exemplos que utilizam o barramento CAN.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
A Tiva C Serie possui duas interfaces CAN, mas nenhuma delas está completa.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
Para fazer funcionar as interfaces CAN é preciso adicionar um transceiver CAN, como por exemplo o Microchip MCP2551.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
O setup de hardware do MCP2551 com a Stellaris pode ser feito como está descrito em:</div>

<div class="separator" style="clear: both; text-align: justify;">
<a href="http://www.fischl.de/arm/can_bus_interface_for_stellaris_launchpad/">http://www.fischl.de/arm/can_bus_interface_for_stellaris_launchpad/</a>. &nbsp;</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
Veja os links que seguem para os projetos CAN Bus.</div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://murix.github.io/canbus-stellaris/">http://murix.github.io/canbus-stellaris/</a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="https://github.com/murix/canbus-stellaris">https://github.com/murix/canbus-stellaris</a></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-PSm8A1kFT1U/UxUEWASK_XI/AAAAAAAAo_A/czu-PEI0rMA/s1600/canbus-schematic.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="183" src="http://2.bp.blogspot.com/-PSm8A1kFT1U/UxUEWASK_XI/AAAAAAAAo_A/czu-PEI0rMA/s1600/canbus-schematic.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquemático simplificado e funcional para rede com duas Stellaris&nbsp;+ MCP2551</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-H2V-9FRurjI/UxUEWtJzr8I/AAAAAAAAo_E/dJD1R9L0bNs/s1600/canbus-stellaris-console.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://2.bp.blogspot.com/-H2V-9FRurjI/UxUEWtJzr8I/AAAAAAAAo_E/dJD1R9L0bNs/s1600/canbus-stellaris-console.JPG" width="250"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Saída nas portais seriais dos exemplos</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-rD6nfz3Dhj4/UxUEYbd2UrI/AAAAAAAAo_Q/2mRNKriCrEs/s1600/canbus-stellaris-mcp2551.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="151" src="http://1.bp.blogspot.com/-rD6nfz3Dhj4/UxUEYbd2UrI/AAAAAAAAo_Q/2mRNKriCrEs/s1600/canbus-stellaris-mcp2551.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Montagem completa<br/>
<br/>
<ul style="background-color: #f2f2f2; border: 0px; color: #373737; font-family: 'Myriad Pro', Calibri, Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px; list-style: inside; margin: 0px 0px 15px; padding: 0px 0px 0px 20px; text-align: start; vertical-align: baseline;">
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">2 x Stellaris Launchpad (EK-LM4F120XL)</li>
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">2 x Microchip MCP2551 (<a href="http://www.microchip.com/mcp2551" style="-webkit-transition: text-shadow 0.5s ease; border: 0px; color: #007edf; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; text-decoration: none; text-shadow: none; transition: text-shadow 0.5s ease; vertical-align: baseline;">http://www.microchip.com/mcp2551</a>)</li>
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">2 x 1k ohm resistor</li>
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">2 x 120 ohm resistor</li>
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">10 x Breadboard Jumper Cable Wires Male (<a href="http://dx.com/s/Jumper+wire+male" style="-webkit-transition: text-shadow 0.5s ease; border: 0px; color: #007edf; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; text-decoration: none; text-shadow: none; transition: text-shadow 0.5s ease; vertical-align: baseline;">http://dx.com/s/Jumper+wire+male</a>)</li>
<li style="border: 0px; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; vertical-align: baseline;">1 x Breadboard (<a href="http://dx.com/s/breadboard" style="-webkit-transition: text-shadow 0.5s ease; border: 0px; color: #007edf; font-family: inherit; font-size: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; line-height: inherit; margin: 0px; padding: 0px; text-decoration: none; text-shadow: none; transition: text-shadow 0.5s ease; vertical-align: baseline;">http://dx.com/s/breadboard</a>)</li>
</ul>
</td></tr>
</tbody></table>

  