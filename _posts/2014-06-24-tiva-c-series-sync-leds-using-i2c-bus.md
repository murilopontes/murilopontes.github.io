---
layout: post
title: Tiva C Series- sync leds using I2C Bus
categories:
 - I2C
date: 2014-06-24 01:20:00 +0100
---

I2C bus é um barramento serial multi-master.  

Os barramentos TWI e SMB são similares ao I2C introduzindo pequenas diferenças.  

Na tabela estão as diferenças entre esses barramentos.  

  

<a name="more"></a>  
  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="183"/><col width="100"/><col width="100"/><col width="100"/></colgroup><tbody>
<tr style="height: 21px;"><td style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"I2C"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">I2C</td><td data-sheets-value='[null,2,"TWI"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">TWI</td><td data-sheets-value='[null,2,"SMBus (SMB)"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">SMBus (SMB)</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"SCL line"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">SCL line</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"DAS line"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">SDA line</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Start"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Start</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Stop"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Stop</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"100kbit"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">100kbit</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"400kbit"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">400kbit</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"3.4Mbit"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">3.4Mbit</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"arbitration"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">arbitration</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"collison detection"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">collison detection</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"7bit address"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">7bit address</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"broadcast"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">broadcast</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"10bit address"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">10bit address</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Packet error check (PEC)"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Packet error check (PEC)</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Timeout transfer"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Timeout transfer</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Alert line"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Alert line</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Suspend line"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Suspend line</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Power up/down"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">Power up/down</td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;"></td><td data-sheets-value='[null,2,"x"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; font-size: 110%; padding: 2px 3px 2px 3px; vertical-align: bottom; vertical-align: bottom; white-space: nowrap;">x</td></tr>
</tbody></table>

  

No I2C são especificados somente 4 condições de funcionamento entre Masters e Slaves.  

  

1) O 'master' envia comandos (writes) para os 'slaves'.  

2) Os 'slaves' interpretam os comandos executando ações nos leds.  

  

3) O 'master envia requisições (requests) para os 'slaves'.  

4) Os 'slaves' enviam dados de volta ao 'master'.

  

  

As linhas SDA e SCL precisam de pull-ups usando resistores de 1,8K até 47K.  

Os resistores e tensões mais comuns são:  

  

<table border="1" cellpadding="0" cellspacing="0" dir="ltr" style="border-collapse: collapse; border: 1px solid #ccc; font-family: arial,sans,sans-serif; font-size: 13px; table-layout: fixed;"><colgroup><col width="100"/><col width="100"/></colgroup><tbody>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"Resistor"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">Resistor</td><td data-sheets-value='[null,2,"Tens\u00e3o"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; border-top: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">Tensão</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"1,8k"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">1,8k</td><td data-sheets-value='[null,2,"1,8V"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">1,8V</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"2,2k"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">2,2k</td><td data-sheets-value='[null,2,"3,3V"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">3,3V</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"4,7k"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">4,7k</td><td data-sheets-value='[null,2,"5V"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">5V</td></tr>
<tr style="height: 21px;"><td data-sheets-value='[null,2,"10k"]' style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">10k</td><td data-sheets-value='[null,2,"12V"]' style="border-bottom: 1px solid #000000; border-right: 1px solid #000000; padding: 2px 3px 2px 3px; vertical-align: bottom;">12V</td></tr>
</tbody></table>

  

Quando o resistor do pull-up não está presente as linhas SDA e SCL são lidas como zero, o que significa que o barramento está ocupado. Se o master tentar fazer um 'write' ou 'request' vai ficar travado até que se coloquem os resistores de pull-up nas linhas SDA e SCL.  

  

Referência de implementação de uma rede leds usando barramento I2C.  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><div style="text-align: justify;">
<br/>
<br/>
<br/></div>
<a href="http://1.bp.blogspot.com/-0y9Xfa6Jkn8/U6jB9ufm0rI/AAAAAAAAr2w/wdVT5jxTqPg/s1600/stellaris-tiva-c-i2c-bus.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="172" src="http://1.bp.blogspot.com/-0y9Xfa6Jkn8/U6jB9ufm0rI/AAAAAAAAr2w/wdVT5jxTqPg/s1600/stellaris-tiva-c-i2c-bus.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquemático de barramento I2C para Stellaris / Tiva<br/>
Pino PD_0 é SCL<br/>
Pino PD_1 é SDA</td></tr>
</tbody></table>

  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/UBT_1kWu1vE" width="560"></iframe>

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-DB2Gz96dU2Q/U6jGQ_fDeXI/AAAAAAAAr3E/m6hB-QTLhxM/s1600/tiva-i2c-master-console.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="255" src="http://3.bp.blogspot.com/-DB2Gz96dU2Q/U6jGQ_fDeXI/AAAAAAAAr3E/m6hB-QTLhxM/s1600/tiva-i2c-master-console.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Tiva I2C master serial console</td></tr>
</tbody></table>

  

  

Código do 'master'
  

<script src="https://gist.github.com/murix/0ba6804a51ca00cb7afb.js"></script>

Código dos 'slaves'
  

<script src="https://gist.github.com/murix/c3785580af1e1812f521.js"></script>