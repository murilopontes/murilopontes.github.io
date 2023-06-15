---
layout: post
title: MBED NUCLEO F429ZI com SDCard
categories:
 - post
date: 2018-04-29 11:02:00 +0100
---

Começando pelo exemplo oficial:  

https://github.com/ARMmbed/mbed-os-example-sd-driver  

O código de exemplo oficial, funciona mas precisa de alguns ajustes.  

Tanto na baudrate da porta serial,  

como na ligação do SDcard para os pinos do SDMMC.  

Depois de fazer as correções, o resto do workflow é o normal de qualquer projeto usando mbed.  

  

O código corrigido pode ser encontrado em:  

<https://github.com/murilopontes/mbed-sdcard-nucleo-f429zi>  

  

<div class="separator" style="clear: both; text-align: center;">
<a href="https://2.bp.blogspot.com/-Lz9K1O_BAfk/WuWl2G2iQyI/AAAAAAABicM/KKbhIHyqP5sFY2lxUTyQ0saqssfq6GO1ACLcBGAs/s1600/f429zi-pinout.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="167" data-original-width="441" height="121" src="https://2.bp.blogspot.com/-Lz9K1O_BAfk/WuWl2G2iQyI/AAAAAAABicM/KKbhIHyqP5sFY2lxUTyQ0saqssfq6GO1ACLcBGAs/s320/f429zi-pinout.png" width="320"/></a></div>

  

No conector CN8 vamos usar a interface SPI3 para cuidar do SDCARD.  

PC_9 é o SPI CS&nbsp; /&nbsp; SDCARD D3  

PC_10 é o&nbsp; SPI CLK /&nbsp; SDCARD CLK  

PC_11 é o SPI MISO (DO) / SDCARD D0  

PC_12 é o SPI MOSI (DI ) / SDCARD CMD  

os pinos SDCARD: D2, D1, CD ficam desconectados.  

<div class="separator" style="clear: both; text-align: center;">
<a href="https://2.bp.blogspot.com/-MkCMB_uyLDk/WuWn2p69vvI/AAAAAAABicY/fGSz6o2iw9EyjZH7XEn7sI65rMN-curBACLcBGAs/s1600/sdcard-waveshare.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="220" data-original-width="329" height="213" src="https://2.bp.blogspot.com/-MkCMB_uyLDk/WuWn2p69vvI/AAAAAAABicY/fGSz6o2iw9EyjZH7XEn7sI65rMN-curBACLcBGAs/s320/sdcard-waveshare.png" width="320"/></a></div>

  

  

sudo pip install mbed-cli --upgrade  

  

mbed --version  

1.5.1  

<div>
<br/></div>

mbed import mbed-os-example-sd-driver  

  

cd mbed-os-example-sd-driver  

  

mbed compile -m NUCLEO_F429ZI -t GCC_ARM  

<div class="separator" style="clear: both; text-align: center;">
<a href="https://3.bp.blogspot.com/-0uIAsZ92qog/WuWaGZswz9I/AAAAAAABibk/qFtRMgn9iLo8KpsFM3zWWmZiSXm7OH9cACLcBGAs/s1600/mbed-sdcard.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="673" data-original-width="562" height="320" src="https://3.bp.blogspot.com/-0uIAsZ92qog/WuWaGZswz9I/AAAAAAABibk/qFtRMgn9iLo8KpsFM3zWWmZiSXm7OH9cACLcBGAs/s320/mbed-sdcard.png" width="267"/></a></div>

  

  

st-flash write ./BUILD/NUCLEO_F429ZI/GCC_ARM/mbed-os-example-sd-driver.bin 0x8000000  

<div class="separator" style="clear: both; text-align: center;">
<a href="https://1.bp.blogspot.com/-XaBveMSCzT0/WuWhvNeurlI/AAAAAAABib0/7Vf3BrzBo8wUve8V-9s0gYRJXzuHF9IPwCLcBGAs/s1600/nucleof429zi-flash.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="255" data-original-width="1058" height="76" src="https://1.bp.blogspot.com/-XaBveMSCzT0/WuWhvNeurlI/AAAAAAABib0/7Vf3BrzBo8wUve8V-9s0gYRJXzuHF9IPwCLcBGAs/s320/nucleof429zi-flash.png" width="320"/></a></div>

  

Minicom result  

<div class="separator" style="clear: both; text-align: center;">
<a href="https://2.bp.blogspot.com/-7PGYPLZsnx4/WuWjvkc2ljI/AAAAAAABicA/syauT1o97oAJiS6OsCXaJdXb_3W7Bp_GACLcBGAs/s1600/nucleof429zi-sdcard-minicom.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="1045" data-original-width="627" height="320" src="https://2.bp.blogspot.com/-7PGYPLZsnx4/WuWjvkc2ljI/AAAAAAABicA/syauT1o97oAJiS6OsCXaJdXb_3W7Bp_GACLcBGAs/s320/nucleof429zi-sdcard-minicom.png" width="192"/></a></div>

  

Exportar para Eclipse  

mbed export -m NUCLEO_F429ZI -i eclipse_gcc_arm --source $PWD  

  