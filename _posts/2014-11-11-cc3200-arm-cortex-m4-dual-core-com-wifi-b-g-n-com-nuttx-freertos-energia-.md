---
layout: post
title: CC3200 - ARM Cortex M4 (Dual Core) com WiFi b/g/n  com Nuttx , FreeRTOS, Energia  
categories:
 - FTDI
date: 2014-11-11 02:37:00 +0000
---

<div>
A CC3200-launchxl é um kit ARM cortex-m4 +&nbsp;WiFi b/g/n&nbsp;+ sensores.<br/>
É um ponto de entrada para a Internet das coisas (IoT).<br/>
<br/>
<a name="more"></a><br/>
<br/>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-WRqeDY-ElOo/VGFHLw72j9I/AAAAAAAAto0/vqivC4M6BI0/s1600/IMG_20141110_200853.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://1.bp.blogspot.com/-WRqeDY-ElOo/VGFHLw72j9I/AAAAAAAAto0/vqivC4M6BI0/s1600/IMG_20141110_200853.jpg" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC3200&nbsp;: ARM Cortex com WiFi b/g/n&nbsp;</td></tr>
</tbody></table>

Para testar é interessante ter sempre mais de uma placa. Isso vale para qualquer projeto.  

<div>
A CC3200 tem várias revisões de hardware, a que recebi tem na PCB a versão 4.1</div>

<div>
<div>
O software padrão que é baseado no FreeRTOS.<br/>
No SDK tem vários exemplos com FreeRTOS no IAR.</div>
<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><div style="text-align: justify;">
<a href="http://2.bp.blogspot.com/-HW6VrTi6wpQ/VGFISyZbthI/AAAAAAAAtpM/eJYSy9pwUjQ/s1600/IMG_20141110_202007.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" height="240" src="http://2.bp.blogspot.com/-HW6VrTi6wpQ/VGFISyZbthI/AAAAAAAAtpM/eJYSy9pwUjQ/s1600/IMG_20141110_202007.jpg" width="320"/></a></div>
</td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC3200 revisão de hardware 4.1</td></tr>
</tbody></table>
<h2>
Ferramentas e manuais</h2>
<h2>
<div>
<span style="font-family: inherit; font-size: small;"><span style="font-weight: normal;">CC3200 Datasheet</span></span><br/>
<span style="font-size: small; font-weight: normal;"><a href="http://www.ti.com/lit/ds/symlink/cc3200.pdf">http://www.ti.com/lit/ds/symlink/cc3200.pdf</a></span><br/>
<span style="font-family: inherit; font-size: small;"><span style="font-weight: normal;"><br/></span></span>
<span style="font-size: small; font-weight: normal;">CC3200 Launch XL - Esquemático do hardware</span><br/>
<span style="font-size: small; font-weight: normal;"><a href="http://www.ti.com/lit/zip/swrc289">http://www.ti.com/lit/zip/swrc289</a></span><br/>
<span style="font-family: inherit; font-size: small;"><span style="font-weight: normal;"><br/></span></span>
<span style="font-family: inherit; font-size: small;"><span style="font-weight: normal;">SimpleLink Wi-Fi Starter (para Android e IOS) - configurar o CC3200 pelo smartphone<br/><a href="http://www.ti.com/tool/wifistarter">http://www.ti.com/tool/wifistarter</a><br/><br/>CC3200 User guide hardware<br/><a href="http://www.ti.com/lit/ug/swru372a/swru372a.pdf">http://www.ti.com/lit/ug/swru372a/swru372a.pdf</a><br/><br/>CC3200 User guide software<br/><a href="http://www.ti.com/lit/ug/swru376a/swru376a.pdf">http://www.ti.com/lit/ug/swru376a/swru376a.pdf</a><br/><br/>IDE: CCS / IAR<br/><a href="http://www.ti.com/tool/ccstudio-wcs">http://www.ti.com/tool/ccstudio-wcs</a><br/><br/>SDK / examples / Servicepack / OTA<br/><a href="http://www.ti.com/tool/cc3200sdk">http://www.ti.com/tool/cc3200sdk</a><br/><br/>Radio test SW+FW<br/><a href="http://www.ti.com/tool/cc3xxxradiotest">http://www.ti.com/tool/cc3xxxradiotest</a><br/><br/>Uniflash (necessário para gravar na spi flash e instalar o servicepack do radio)<br/><a href="http://www.ti.com/tool/uniflash">http://www.ti.com/tool/uniflash</a><br/><br/>Pinmux utility<br/><a href="http://www.ti.com/tool/pinmuxtool">http://www.ti.com/tool/pinmuxtool</a></span></span></div>
</h2>
<h2>
<div>
</div>
</h2>
<h2>
<span style="font-family: inherit; font-size: large;">Especificação de hardware</span></h2>
<h2>
</h2>
<h2>
<div style="font-size: medium; font-weight: normal;">
MCU: cc3200R1m2 ARM Cortex-m4 (dual core) 80 MHz 256kbytes RAM WiFi b/g/n</div>
<div style="font-size: medium; font-weight: normal;">
Flash: 25PX80 (8 mbits / 1024 kbytes) com opção de 128 mbits / 16 mbytes</div>
<div style="font-size: medium; font-weight: normal;">
Acelerômetro: Bosh BMA222 (I2C addr=0x18)</div>
<div style="font-size: medium; font-weight: normal;">
Termômetro: &nbsp;Texas TMP008 (I2C addr=0x41)</div>
<div style="font-size: medium; font-weight: normal;">
JTAG: FTDI FT2232D (dual port)</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
Recursos do MCU cc3200R1m2</div>
<div style="font-size: medium; font-weight: normal;">
1 x SPI</div>
<div style="font-size: medium; font-weight: normal;">
2 x UART</div>
<div style="font-size: medium; font-weight: normal;">
1 x 8 bit Parallel Camera</div>
<div style="font-size: medium; font-weight: normal;">
1 x McASP (aplicações de audio)</div>
<div style="font-size: medium; font-weight: normal;">
1 x SD / MMC / SD Card</div>
<div style="font-size: medium; font-weight: normal;">
1 x I2C</div>
<div style="font-size: medium; font-weight: normal;">
6 x PWM (16-bit)</div>
<div style="font-size: medium; font-weight: normal;">
8 x Capture and Compare</div>
<div style="font-size: medium; font-weight: normal;">
1 x Watchdog Timer</div>
<div style="font-size: medium; font-weight: normal;">
4 x &nbsp;ADC (12-bit)</div>
<div style="font-size: medium; font-weight: normal;">
27 x GPIO</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
</h2>
<h2>
<span style="font-family: inherit; font-size: large;">Arquitetura de</span><span style="font-size: large;">&nbsp;hardware</span></h2>
<h2>
<div style="font-size: medium; font-weight: normal;">
O CC3200 é um dual core, um núcleo só para aplicação e outro só para rede.</div>
<div style="font-size: medium; font-weight: normal;">
Eles se comunicam via SPI.</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
O CC3200 não contém flash interna, toda a memória flash é externa conectada via SPI.</div>
<div style="font-size: medium; font-weight: normal;">
A memória SPI contém um sistema de arquivos proprietário.</div>
<div style="font-size: medium; font-weight: normal;">
Para gravar na SPI flash é preciso usar o Uniflash,</div>
<div style="font-size: medium; font-weight: normal;">
O projeto energia desenvolveu a ferramenta CC3200prog que também grava na flash, mas não tem todas opções da ferramenta oficial Uniflash.</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
O CC3200 contém uma memória ROM interna com bootloader e a pilha TCP/IP.</div>
<div style="font-size: medium; font-weight: normal;">
O bootloader é serial, e precisa ser ativado através do pino SOP2.</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
O debug via SWD e JTAG é feito na RAM. Dá para desenvolver e testar tudo na RAM, após completar o projeto, é possível gravar o binário na spi flash externa para usar em campo.</div>
<div style="font-size: medium; font-weight: normal;">
Usando a biblioteca de acesso a SPI flash é possível gravar arquivos no formato reconhecido pelo bootloader, portanto um executável pode gravar a si mesmo na spi flash externa, o arquivo lido pelo bootloader é o /sys/mcuimg.bin. O sistema de arquivos da spi flash suporta até 128 arquivos.</div>
<div style="font-size: medium; font-weight: normal;">
Isso permite implementar um upgrade over-the-air (OTA), baixando um novo programa via WiFI e gravando em um arquivo (download.bin) para então chavear o /sys/mcuimg.bin.</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
</h2>
<h2>
<span style="font-family: inherit; font-size: large;">Pinout,&nbsp;</span>Conectores, jumpers, botões e LEDs</h2>
<h2>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
</h2>
<h2>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-iHh7ORzwWnw/VGgVYipmSfI/AAAAAAAAtr0/7ooeDxewbSo/s1600/cc3200launchxl-pinout.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="292" src="http://2.bp.blogspot.com/-iHh7ORzwWnw/VGgVYipmSfI/AAAAAAAAtr0/7ooeDxewbSo/s1600/cc3200launchxl-pinout.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">V1 - pinout inicial</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://2.bp.blogspot.com/-XsH2MB9vedk/VGgeXpP92mI/AAAAAAAAtsE/Bk_p2CiQQMY/s1600/cc3200launchxl-pinout-v2.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="292" src="http://2.bp.blogspot.com/-XsH2MB9vedk/VGgeXpP92mI/AAAAAAAAtsE/Bk_p2CiQQMY/s1600/cc3200launchxl-pinout-v2.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">V2 - adicionando SWD / SWO</td></tr>
</tbody></table>
</h2>
<h2>
</h2>
<h2>
<div style="font-size: medium; font-weight: normal;">
J1: USB / &nbsp;FT2232D JTAG</div>
<div style="font-size: medium; font-weight: normal;">
J2: Sensores I2C SDA</div>
<div style="font-size: medium; font-weight: normal;">
J3: Sensores I2C SCL</div>
<div style="font-size: medium; font-weight: normal;">
J4: Sensores IRQ acelerômetro</div>
<div style="font-size: medium; font-weight: normal;">
J5: Debug de rede</div>
<div style="font-size: medium; font-weight: normal;">
J6: UART 0 RX - fechado&nbsp;FT2232D serial / aberto Boostpack (usado no bootloader com SOP2)</div>
<div style="font-size: medium; font-weight: normal;">
J7: UART 0 TX - fechado&nbsp;FT2232D serial / aberto Boostpack (usado no bootloader com SOP2)</div>
<div style="font-size: medium; font-weight: normal;">
J8: FT2232D JTAG TCK (usado no workaround do CC3200prog junto com SOP2)</div>
<div style="font-size: medium; font-weight: normal;">
J9: FT2232D JTAG TMS</div>
<div style="font-size: medium; font-weight: normal;">
J10: FT2232D JTAG TDI</div>
<div style="font-size: medium; font-weight: normal;">
J11: FT2232D JTAG TDO</div>
<div style="font-size: medium; font-weight: normal;">
J12: medição de corrente</div>
<div style="font-size: medium; font-weight: normal;">
J13: energia por usb do J1</div>
<div style="font-size: medium; font-weight: normal;">
J14: energia por bateria do J20</div>
<div style="font-size: medium; font-weight: normal;">
J15: SOP2 - fechado bootloader via serial (gravação) / aberto bootloader via flash (normal)</div>
<div style="font-size: medium; font-weight: normal;">
J16: SOP1</div>
<div style="font-size: medium; font-weight: normal;">
J17: SOP0 - fechado ativa SWD</div>
<div style="font-size: medium; font-weight: normal;">
J18: antena</div>
<div style="font-size: medium; font-weight: normal;">
J19: usb power output 5v - 0.4v (diodo) = 4,6v</div>
<div style="font-size: medium; font-weight: normal;">
J20: bateria 2xAA funciona até descarrega para 2,3V</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
P1: Boostpack</div>
<div style="font-size: medium; font-weight: normal;">
P2: Boostpack</div>
<div style="font-size: medium; font-weight: normal;">
P3: Boostpack</div>
<div style="font-size: medium; font-weight: normal;">
P4: Boostpack</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
SW2: GPIO 22</div>
<div style="font-size: medium; font-weight: normal;">
SW3: GPIO 13</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
D5 (verde):&nbsp;GPIO&nbsp;11</div>
<div style="font-size: medium; font-weight: normal;">
D6 (amarelo):&nbsp;GPIO&nbsp;10</div>
<div style="font-size: medium; font-weight: normal;">
D7 (vermelho):&nbsp;GPIO&nbsp;9</div>
</h2>
<h2>
<span style="font-size: large;">Configurando CC3200 para funcionar no Windows</span></h2>
<div>
Instalar o SDK oficial, e depois atualizar no painel de controle os drivers usando a pasta do SDK.</div>
<h2>
Configurando CC3200 para funcionar no Linux</h2>
<h2>
<span style="font-size: small; font-weight: normal;">Precisa notificar o driver do ftdi-sio &nbsp;do novo ID do FT2232D que vem na CC3200</span><br/>
<span style="font-size: small; font-weight: normal;">modprobe ftdi_sio</span><br/>
<span style="font-size: small; font-weight: normal;">echo 0451 c32a &gt; /sys/bus/usb-serial/drivers/ftdi_sio/new_id</span><br/>
<span style="font-size: small; font-weight: normal;"><br/></span>
<span style="font-size: small; font-weight: normal;"><br/></span>
<span style="font-size: small; font-weight: normal;">Para deixar as seriais do CC3200 permanente pós reboot, é preciso adicionar uma regra no udev</span><br/>
<span style="font-size: small; font-weight: normal;">nano /etc/udev/rules.d/98-usbftdi.rules</span><br/>
<span style="font-size: small; font-weight: normal;"><br/></span>
<span style="font-size: small; font-weight: normal;">Uma vez aberto o nano, cole essa regra</span><br/>
<span style="font-size: small; font-weight: normal;">SUBSYSTEM=="usb", ATTRS{idVendor}=="0451", ATTRS{idProduct}=="c32a", MODE="0660", GROUP="dialout",</span><br/>
<span style="font-size: small; font-weight: normal;">RUN+="/sbin/modprobe ftdi-sio" RUN+="/bin/sh -c '/bin/echo 0451 c32a &gt; /sys/bus/usb-serial/drivers/ftdi_sio/new_id'"</span><br/>
<div>
<br/></div>
<div>
<div style="font-size: medium; font-weight: normal;">
Depois de salvo, recarregue as regras do udev</div>
<div style="font-size: medium; font-weight: normal;">
sudo udevadm control --reload-rules</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
Se seu usuário não estiver no grupo dialout então adicione</div>
<div style="font-size: medium; font-weight: normal;">
sudo usermod -a -G dialout username</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
<div style="font-size: medium; font-weight: normal;">
Depois isso, vai detectar duas portas USB novas</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.103297] usb 2-1.1: new full-speed USB device number 15 using ehci-pci</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.205927] usb 2-1.1: New USB device found, idVendor=0451, idProduct=c32a</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.205940] usb 2-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.205948] usb 2-1.1: Product: USB &lt;-&gt; JTAG/SWD<!-----><!-----><!-----><!-----><!-----><!-----><!-----></div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.205954] usb 2-1.1: Manufacturer: FTDI</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.205960] usb 2-1.1: SerialNumber: cc3101</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208581] ftdi_sio 2-1.1:1.0: FTDI USB Serial Device converter detected</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208685] usb 2-1.1: Detected FT2232C</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208692] usb 2-1.1: Number of endpoints 2</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208697] usb 2-1.1: Endpoint 1 MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208703] usb 2-1.1: Endpoint 2 MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.208709] usb 2-1.1: Setting MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.210232] usb 2-1.1: FTDI USB Serial Device converter now attached to ttyUSB4</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212552] ftdi_sio 2-1.1:1.1: FTDI USB Serial Device converter detected</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212646] usb 2-1.1: Detected FT2232C</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212652] usb 2-1.1: Number of endpoints 2</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212659] usb 2-1.1: Endpoint 1 MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212665] usb 2-1.1: Endpoint 2 MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.212671] usb 2-1.1: Setting MaxPacketSize 64</div>
<div style="font-size: medium; font-weight: normal;">
[ 4656.214985] usb 2-1.1: FTDI USB Serial Device converter now attached to ttyUSB5</div>
<div style="font-size: medium; font-weight: normal;">
<br/></div>
</div>
</h2>
<h2>
Desenvolvimento usando Energia.nu 0101E0013</h2>
É preciso mexer em jumpers fisicamente para habilitar a gravação dos projetos pelo Energia.<br/>
O SOP2 serve para ativar o bootloader serial do CC3200.<br/>
Quando o SOP2 está fechado o CC3200 sempre vai iniciar o bootloader que vem na ROM.<br/>
Quando o SOP2 está aberto o CC3200 continua usando o bootloader da ROM, mas vai tentar carregar o arquivo /sys/mcuimg.bin da SPI flash para RAM e repassar o controle para ele.<br/>
No projeto Energia a turma faz um workaround para não ficar com essa "frescura" de botar e tirar jumper. O TCK do JTAG é usado para ligar e desligar o bootloader, obviamente o debug por JTAG e SWD não irão funcionar já que perdeu um sinal, mas a gravação por serial agora ficou automática.<br/>
Como o JTAG e SWD vão ficar inutilizados, dá para abrir o J9, J10, J11. E usar os sinais dos J8, J9, J10, J11 para qualquer coisa, no meu caso vou aproveitar eles como PWM.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://2.bp.blogspot.com/-vhUTKGJkeAg/VGc5zLsbVVI/AAAAAAAAtrg/67vS1ehStkE/s1600/cc3200-prog-workaround.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="143" src="http://2.bp.blogspot.com/-vhUTKGJkeAg/VGc5zLsbVVI/AAAAAAAAtrg/67vS1ehStkE/s1600/cc3200-prog-workaround.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">Para grava usando o CC3200prog é preciso fazer um pequeno ajuste na placa,<br/>
ligando o TCK de cima com o SOP2 de baixo</td></tr>
</tbody></table>
<br/>
A revisão de hardwdare 4.1 tem problemas de gravação com o CC3200prog do energia&nbsp;0101E0013.<br/>
Esse bug já foi reportado:&nbsp;<a href="https://github.com/energia/Energia/issues/507">https://github.com/energia/Energia/issues/507</a><br/>
Tem de baixar o cc3200 corrigido e jogar por cima do que vem na versão 0101E0013<br/>
<a href="http://energia.nu/files/cc3200prog_win.zip">http://energia.nu/files/cc3200prog_win.zip</a><br/>
<div>
<a href="http://energia.nu/files/cc3200prog_mac.zip">http://energia.nu/files/cc3200prog_mac.zip</a><br/>
<a href="http://energia.nu/files/cc3200prog_linux64.tar.gz">http://energia.nu/files/cc3200prog_linux64.tar.gz</a><br/>
<a href="http://energia.nu/files/cc3200prog_linux.tar.gz">http://energia.nu/files/cc3200prog_linux.tar.gz</a><br/>
<br/>
Além do cc3200prog precisa dos bootloaders do energia para funcionar, então fiz um pacote das versões windows, mac e linux que roda standalone, o download pode ser feito no meu bitbucket.<br/>
<a href="https://bitbucket.org/murilorebelopontes/dronespersonalizados/downloads/cc3200prog-hw-4.1-windows-mac-linux.zip">https://bitbucket.org/murilorebelopontes/dronespersonalizados/downloads/cc3200prog-hw-4.1-windows-mac-linux.zip</a><br/>
<br/>
Somente 192kb de RAM usável<br/>
<a href="https://github.com/energia/Energia/issues/517">https://github.com/energia/Energia/issues/517</a><br/>
Antes da revisão de hardware 4.1 com CC3200R1M2 com ROM 1.33 somente 192kb podiam ser usados, com a ROM 1,33 todos 256kb de RAM podem ser usados quando resolverem o problema do linker.<br/>
<br/>
Falta de API / Driver para escrever na SPI Flash<br/>
<a href="https://github.com/energia/Energia/issues/494">https://github.com/energia/Energia/issues/494</a><br/>
Um projeto já resolveu isso, mas ainda não foi integrado&nbsp;<a href="https://github.com/spirilis/SLFS">https://github.com/spirilis/SLFS</a><br/>
Com o SLFS dá para implementar OTA, criando um arquivo de download ou escrevendo por cima da /sys/mcuimg.bin<br/>
<br/></div>
<div>
Veja o que acontece no log do Energia com o CC3200prog bugado...</div>
<blockquote class="tr_bq">
Binary sketch size: 2.720 bytes (of a 262.144 byte maximum)<br/>
Open UART /dev/ttyUSB1<br/>
open UART success<br/>
Getting storage list<br/>
Bootloader Version: 4<br/>
Silicon version ES1.32<br/>
Bootloader version is 2, 1, 4, 0<br/>
It's a CC3101 device: PG1.32<br/>
BlockSize is 4096, number of blocks is 64<br/>
erasing 1 blocks starting from &nbsp;4<br/>
Switch to NWP bootloader complete<br/>
Silicon version ES1.32<br/>
Bootloader version is 2, 0, 4, 0<br/>
BlockSize is 4096, number of blocks is 16<br/>
<b>erasing 12 blocks starting from &nbsp;0</b> &nbsp; <span style="color: red;">TRAVOU</span></blockquote>
</div>
</div>

<div>
Veja o que acontece no log do Energia com o CC3200prog corrigido...</div>

<blockquote class="tr_bq">
Binary sketch size: 2.720 bytes (of a 262.144 byte maximum)<br/>
Opening COM5<br/>
Getting storage list<br/>
Bootloader Version: 4<br/>
Silicon version ES1.32 or higher<br/>
Bootloader version is 2, 1, 4, 0<br/>
It's a CC3200 device: PG1.33 or higher<br/>
Switch UART pinmux to APPS<br/>
Switch to NWP bootloader complete<br/>
Load common boot command for PG1.33 or higher<br/>
Bootloader version is 2, 0, 4, 0<br/>
BlockSize is 4096, number of blocks is 16<br/>
erasing 13 blocks starting from &nbsp;0<br/>
erasing file "/sys/mcuimg.bin"<br/>
deleting file "/sys/mcuimg.bin"<br/>
erase file completed<br/>
Downloading file "/sys/mcuimg.bin" with size 2720<br/>
<b>.Download complete &nbsp; &nbsp;<span style="background-color: white; color: #38761d;">TUDO PERFEITO</span></b></blockquote>

  

## Desenvolvimento com Nuttx

  

Baixar e buildar o Nuttx para CC3200  

git clone git://git.code.sf.net/p/nuttx/git nuttx-git  

cd nuttx-git/nuttx  

make distclean  

cd tools  

./configure.sh cc3200-launchpad/nsh  

cd ..  

make  

  

  

Preparar para debug com OpenOCD  

  

[root@debian ~/workspace/nuttx-tiva/nuttx/configs/cc3200-launchpad/tools]# openocd -f cc3200.cfg  

Open On-Chip Debugger 0.8.0 (2014-10-20-21:48)  

Licensed under GNU GPL v2  

For bug reports, read  

<span class="Apple-tab-span" style="white-space: pre;"> </span>http://openocd.sourceforge.net/doc/doxygen/bugs.html  

Info : only one transport option; autoselect 'jtag'  

adapter speed: 1000 kHz  

Info : clock speed 1000 kHz  

Info : JTAG tap: cc3200.jrc tap/device found: 0x0b97c02f (mfg: 0x017, part: 0xb97c, ver: 0x0)  

Info : JTAG tap: cc3200.dap enabled  

Info : cc3200.cpu: hardware has 6 breakpoints, 4 watchpoints  

  

Gravando o Nuttx pelo GDB e executar  

  

[root@debian ~/workspace/nuttx-tiva/nuttx]# arm-none-eabi-gdb  

GNU gdb (7.7.1+dfsg-1+6) 7.7.1  

Copyright (C) 2014 Free Software Foundation, Inc.  

License GPLv3+: GNU GPL version 3 or later 

<http: gnu.org="" gpl.html="" licenses=""></http:>

  

This is free software: you are free to change and redistribute it.  

There is NO WARRANTY, to the extent permitted by law. &nbsp;Type "show copying"  

and "show warranty" for details.  

This GDB was configured as "--host=x86_64-linux-gnu --target=arm-none-eabi".  

Type "show configuration" for configuration details.  

For bug reporting instructions, please see:  

<http: bugs="" gdb="" software="" www.gnu.org="">.</http:>

  

Find the GDB manual and other documentation resources online at:  

<http: documentation="" gdb="" software="" www.gnu.org="">.</http:>

  

For help, type "help".  

Type "apropos word" to search for commands related to "word".  

__(gdb) file nuttx__  

Reading symbols from nuttx...done.  

__(gdb) target extended :3333__  

Remote debugging using :3333  

0x00001f5e in ?? ()  

__(gdb) monitor reset halt__  

adapter speed: 1000 kHz  

JTAG tap: cc3200.jrc tap/device found: 0x0b97c02f (mfg: 0x017, part: 0xb97c, ver: 0x0)  

JTAG tap: cc3200.dap enabled  

target state: halted  

target halted due to debug-request, current mode: Thread  

xPSR: 0x41000000 pc: 0x00001f5e msp: 0x20003fe0  

__(gdb) load__  

Loading section .text, size 0xd43b lma 0x20004000  

Loading section .ARM.exidx, size 0x8 lma 0x2001143c  

Loading section .data, size 0x54 lma 0x20011444  

Start address 0x20004484, load size 54423  

Transfer rate: 64 KB/sec, 3401 bytes/write.  

__(gdb) monitor reset init__  

adapter speed: 1000 kHz  

JTAG tap: cc3200.jrc tap/device found: 0x0b97c02f (mfg: 0x017, part: 0xb97c, ver: 0x0)  

JTAG tap: cc3200.dap enabled  

target state: halted  

target halted due to debug-request, current mode: Thread  

xPSR: 0x41000000 pc: 0x00001f5e msp: 0x20003fe0  

__(gdb) continue__  

Continuing.  

  

  

Com a última revisão do git, o Nuttx não funcionou na CC3200R1M2 PCB v4.1.  

  

No lugar do NSH só aparece isso e trava.  

<blockquote class="tr_bq">
Airq_unexpected_isr: irq: 15<br/>
up_assert: Assertion failed at file:irq/irq_unexpectedisr.c line: 85</blockquote>

  

  

## <span style="font-size: large;">Debug com FT2232D para usar SWD com SWO</span>

<h2><span style="font-size: small;"><span style="font-weight: normal;">Dá para usar o SWD para fazer debug com o SWO, usando uma JTAG externa, o FT2232D não tem suporte para SWO.</span></span><br/><span style="font-family: inherit; font-size: small; font-weight: normal;"><a href="http://searchingforbit.blogspot.com.br/2014/07/cc3200-launchpad-with-external-debugger.html">http://searchingforbit.blogspot.com.br/2014/07/cc3200-launchpad-with-external-debugger.html</a></span><br/><span style="font-size: small; font-weight: normal;"><a href="http://e2e.ti.com/support/wireless_connectivity/f/968/p/360927/1276370.aspx#1276370">http://e2e.ti.com/support/wireless_connectivity/f/968/p/360927/1276370.aspx#1276370</a></span><br/><div>
<br/></div></h2>

<div>
<h2>
CC3200prog gravando o Nuttx na flash</h2>
Bootloaders do cc3200 fica na pasta DLL, tem um bootloader para cada versão do silício.<br/>
Quando tentei rodar fora da pasta do cc3200prog, estouro o erro abaixo:<br/>
<br/>
[root@debian ~/workspace/nuttx-tiva/nuttx]# /opt/energia-0101E0013/hardware/tools/lm4f/bin/cc3200prog /dev/ttyUSB1 nuttx.bin<br/>
Open UART /dev/ttyUSB1<br/>
open UART success<br/>
Getting storage list<br/>
Bootloader Version: 4<br/>
Unable to open file dll/rbtl3101_132.dll<br/>
Silicon version ES1.32 or higher<br/>
Unable to open file dll/rbtl3100s.dll<br/>
Load common boot command for PG1.33 or higher<br/>
erasing file "/sys/mcuimg.bin"<br/>
deleting file "/sys/mcuimg.bin"<br/>
erase file completed<br/>
Downloading file "/sys/mcuimg.bin" with size 61428<br/>
Open operation failed<br/>
<div>
<br/></div>
<div>
Quando roda na pasta junto com os bootloaders, a gravação é perfeita</div>
<div>
<br/></div>
[root@debian /opt/energia-0101E0013/hardware/tools/lm4f/bin]# ./cc3200prog /dev/ttyUSB1 /root/workspace/nuttx-tiva/nuttx/nuttx.bin<br/>
Open UART /dev/ttyUSB1<br/>
open UART success<br/>
Getting storage list<br/>
Bootloader Version: 4<br/>
Silicon version ES1.32 or higher<br/>
Bootloader version is 2, 1, 4, 0<br/>
It's a CC3200 device: PG1.33 or higher<br/>
Switch UART pinmux to APPS<br/>
Switch to NWP bootloader complete<br/>
Load common boot command for PG1.33 or higher<br/>
Bootloader version is 2, 0, 4, 0<br/>
BlockSize is 4096, number of blocks is 16<br/>
erasing 13 blocks starting from &nbsp;0<br/>
erasing file "/sys/mcuimg.bin"<br/>
deleting file "/sys/mcuimg.bin"<br/>
erase file completed<br/>
Downloading file "/sys/mcuimg.bin" with size 61428<br/>
...............<br/>
Download complete<br/>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-xeCupneTt28/VGymJKzteNI/AAAAAAAAtss/wvPzEd6R_Kg/s1600/IMG_20141119_111452.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-xeCupneTt28/VGymJKzteNI/AAAAAAAAtss/wvPzEd6R_Kg/s1600/IMG_20141119_111452.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Nuttx rodando na CC3200 após ser gravado na flash pelo CC3200prog do Energia.nu<br/>
Até agora só tem a UART funcionando, falta ainda:<br/>
wifi,&nbsp;i2c, spi, camera, ccp, pwm,&nbsp;i2s, adc, sdcard</td></tr>
</tbody></table>
<br/></div>