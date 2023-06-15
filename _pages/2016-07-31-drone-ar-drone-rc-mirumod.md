---
layout: page
title: Drone- AR.Drone RC mirumod
categories:
 - page
date: 2016-07-31 19:55:00 +0100
---

O <a href="http://mirumod.tk/" target="_blank">Mirumod</a> adiciona a possibilidade de controlar o AR.Drone usando um controle RC.  

Isso é feito usando um Arduino para receber o sinal RF e inserir comandos pela UART do Ardrone.  

E um programa adicional, instalado pelo FTP do AR.Drone para receber os comandos gerados pelo Arduino e traduzir para formato de comandos AT do AR.Drone.  

  

  

Para facilitar a montagem, aqui está o pinout da porta de expansão do Ardrone v1.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-FUl8baB-5aY/VWcTRGfC9TI/AAAAAAABI24/VqAFrbwFFG0/s1600/ardrone1-pinout.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="356" src="https://1.bp.blogspot.com/-FUl8baB-5aY/VWcTRGfC9TI/AAAAAAABI24/VqAFrbwFFG0/s400/ardrone1-pinout.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ardrone 1 - pinout</td></tr>
</tbody></table>

  

<div class="separator" style="clear: both; text-align: center;">
</div>

Agora basta conectar o arduino conforme os esquemáticos encontrados nos fóruns.  

  

<http://www.rcgroups.com/forums/showpost.php?p=18859284&amp;postcount=484>  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://4.bp.blogspot.com/-oVWkVSegWwI/VVUxRY_3BPI/AAAAAAABIfI/6S-zRD91Pro/s1600/mirumodnano000.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="https://4.bp.blogspot.com/-oVWkVSegWwI/VVUxRY_3BPI/AAAAAAABIfI/6S-zRD91Pro/s400/mirumodnano000.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">Wiring Arduino Nano to Ardrone</td></tr>
</tbody></table>

<http://www.rcgroups.com/forums/showpost.php?p=17963155&amp;postcount=48>  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://3.bp.blogspot.com/-ZHLk5MiNotQ/VVUyQv_LnAI/AAAAAAABIfQ/sNCekR20hrU/s1600/Miru-Wiring.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="241" src="https://3.bp.blogspot.com/-ZHLk5MiNotQ/VVUyQv_LnAI/AAAAAAABIfQ/sNCekR20hrU/s400/Miru-Wiring.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">Wiring Arduino Pro to Ardrone<br/>
Faltou o resistor de 4.7K na linha do TX<br/>
<div>
<br/></div>
</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-N18PydtKtzo/VWcVQDK1veI/AAAAAAABI3I/MNNtalFa394/s1600/IMG_20150528_095156.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="https://1.bp.blogspot.com/-N18PydtKtzo/VWcVQDK1veI/AAAAAAABI3I/MNNtalFa394/s320/IMG_20150528_095156.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Usei uma cabo flat de 2.00 mm (ardrone) para 2.54 mm (arduino)</td></tr>
</tbody></table>

  

  

  

  