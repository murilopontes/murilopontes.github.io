---
layout: post
title: Bitlash- scriptando na Stellaris e salvando na EEPROM
categories:
 - ARM
date: 2014-02-04 02:35:00 +0000
---

O Bitlash é uma versão reduzida de um prompt de comandos e controle de tarefas para microcontroladores. Originalmente foi desenvolvido para Arduino / AVR, mas já conta com suporte para alguns kits ARM.   

<a name="more"></a>Adicionei o suporte de EEPROM e Software reset para o kit Stellaris Launchpad rodar o bitlash com todos as features disponíveis.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-SQXyxx1MTcQ/UvBQLe7nOEI/AAAAAAAAotY/xxjLhdWZWo0/s1600/bitlash-demo.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-SQXyxx1MTcQ/UvBQLe7nOEI/AAAAAAAAotY/xxjLhdWZWo0/s1600/bitlash-demo.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Para instalar o bitlash, basta clonar o repositório dele, em uma pasta sem caracteres especiais dentro da pasta abaixo:<br/>
C:\energia-0101E0011\hardware\lm4f\libraries<br/>
Feito isso, é só procurar no menu de exemplos da Energia IDE os templates para o bitlash</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-iu0egCcmHI0/UvBRHVit-7I/AAAAAAAAotg/hsozl1L0AW4/s1600/bitlash-eeprom-stellaris-startup.JPG" imageanchor="1" style="display: inline !important; margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="390" src="http://1.bp.blogspot.com/-iu0egCcmHI0/UvBRHVit-7I/AAAAAAAAotg/hsozl1L0AW4/s1600/bitlash-eeprom-stellaris-startup.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Dump da eeprom feito pelo comando "peep"<br/>
A função "startup" quando definida pelo usuário é chamada sempre a placa é reiniciada.</td></tr>
</tbody></table>

  

* Página do projeto energia  

http://www.energia.nu/