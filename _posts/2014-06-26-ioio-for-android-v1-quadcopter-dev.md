---
layout: post
title: IOIO for Android v1 - Quadcopter Dev
categories:
 - post
date: 2014-06-26 23:56:00 +0100
---

<div class="separator" style="clear: both; text-align: left;">
Construir drones usando Android com IOIO pode ser uma opção.</div>

<a name="more"></a>  

<div class="separator" style="clear: both; text-align: left;">
<br/></div>

<div class="separator" style="clear: both; text-align: left;">
Funcionalidades do IOIO for Android</div>

<div class="separator" style="clear: both;">
</div>

*   48 total I/O pins - qualquer um pode ser entrada/saída.
*   16 analog inputs (10-bit).
*   9 PWM outputs.
*   4 UART channels.
*   3 SPI channels.
*   3 TWI (I²C-compatible).
*   On-board switch-mode regulator provendo 1.5A @&nbsp;5V.&nbsp;

  

<div>
Existem dois modelos da placa IOIO, o mais antigo conhecido como v1 é facilmente encontrado no Aliexpress por menos de R$50 (<a href="http://www.aliexpress.com/w/wholesale-ioio.html?SearchText=ioio">http://www.aliexpress.com/w/wholesale-ioio.html?SearchText=ioio</a>)</div>

<div>
A versão v1 tem 6 revisões de hardware e a versão OTG só tem uma revisão de hardware.&nbsp;</div>

Na sparkfun é a v1 não é mais vendida.  

  

<span style="background-color: white; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.1;">IOIO for Android (v1)</span>  

<https://www.sparkfun.com/products/retired/10748>  

  

<span style="background-color: white; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.1;">IOIO-OTG (micro-usb onboard)</span>  

<https://www.sparkfun.com/products/11343>  

  

Antes de conectar no telefone é preciso alimentar a placa com um tensão de 5-15V pelo pino de Vin.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-SaPrUjGGfdE/U6yaD8F_usI/AAAAAAAAr8Q/5kctRp2zRX0/s1600/IMG_20140626_190821.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="240" src="http://3.bp.blogspot.com/-SaPrUjGGfdE/U6yaD8F_usI/AAAAAAAAr8Q/5kctRp2zRX0/s1600/IMG_20140626_190821.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Alimentando o IOIO for android v1 com um os&nbsp;+5V do um conversor USB-Serial-TTL</td></tr>
</tbody></table>

  

No android é preciso baixar o pacote de firmwares  

<https://github.com/ytai/ioio/raw/master/release/software/App-IOIO0504.zip>  

Extrair o pacote e instalar o helloIOIO.apk  

Quando o IOIO for plugado no telefone vai aparece a seguinte tela.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-KGDMzx_FSGs/U6yZJqxu1TI/AAAAAAAAr74/dUANePa3Cyw/s1600/ioio.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://3.bp.blogspot.com/-KGDMzx_FSGs/U6yZJqxu1TI/AAAAAAAAr74/dUANePa3Cyw/s1600/ioio.png" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">helloIOIO.apk<br/>
A versão de hardware do meu IOIO é a SPRK0016</td></tr>
</tbody></table>

Pelo que parece a versão 0500 do software só funciona com o IOIO-OTG que já tem o firmware atualizado com a versão 0500.  

<https://github.com/ytai/ioio/raw/master/release/firmware/device-bootloader/DevBoot-IOIO0401-App-IOIO0500.zip>  

  

O firmware detectado pelo aplicativo na minha placa foi a versão 0400 e bootloader 0311:  

<https://github.com/ytai/ioio/raw/master/release/firmware/bootloader/Boot-IOIO0311-App-IOIO0400.zip>  

Então a versão 0400 do helloIOIO.apk deve funcionar com &nbsp;firmware 0400 e bootloader 0311:  

<https://github.com/ytai/ioio/raw/master/release/software/App-IOIO0400.zip>  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-DLs_zM17gPc/U6yjmgmn6kI/AAAAAAAAr9M/EuPr7WTCfns/s1600/ioio-working.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-DLs_zM17gPc/U6yjmgmn6kI/AAAAAAAAr9M/EuPr7WTCfns/s1600/ioio-working.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">IOIO for Android v1<br/>
hardware revision:&nbsp;&nbsp;SPRK0016<br/>
bootloader firmware: 0311<br/>
application firmware: 0400<br/>
IOIO library: 0400<br/>
helloIOIO.apk : 0400<br/>
Com todas as versões casadas o controle do led 'stat' pelo telefone funcionou perfeitamente</td></tr>
</tbody></table>

  

Agora é só fazer uma aplicação Android para pilotar o Quadcopter usando os sensores do celular e as saídas PWM do IOIO.  

  

  