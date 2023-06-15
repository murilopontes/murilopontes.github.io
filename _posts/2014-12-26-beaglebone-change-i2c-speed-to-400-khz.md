---
layout: post
title: Beaglebone change I2C speed to 400 KHz
categories:
 - device tree
date: 2014-12-26 01:22:00 +0000
---

A velocidade padrão das capes no i2c é 100KHz, mas quero mudar para 400KHz  

Testado na Beaglebone Black rev. C com Debian 7.5 e 7.7  

  

  

<a name="more"></a>  

  

#tirar o backup do device tree  

cp /boot/uboot/dtbs/am335x-boneblack.dtb /boot/uboot/dtbs/am335x-boneblack.dtb-backup  

  

#converte device tree binário para texto  

dtc -I dtb -O dts -o /boot/uboot/dtbs/am335x-boneblack.dts /boot/uboot/dtbs/am335x-boneblack.dtb  

  

#editar a clock-frequency para 400000  

nano /boot/uboot/dtbs/am335x-boneblack.dts  

  

&nbsp; &nbsp; &nbsp; i2c@4819c000 {  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; compatible = "ti,omap4-i2c";  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #address-cells = &lt;0x1&gt;;<!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1--><!--0x1-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #size-cells = &lt;0x0&gt;;<!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0--><!--0x0-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ti,hwmods = "i2c3";  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; reg = &lt;0x4819c000 0x1000=""&gt;;<!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000--><!--0x4819c000-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; interrupts = &lt;0x1e&gt;;<!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e--><!--0x1e-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; status = "okay";  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pinctrl-names = "default";  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pinctrl-0 = &lt;0x7&gt;;<!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7--><!--0x7-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #clock-frequency = &lt;0x186a0&gt;; //100KHz<!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0--><!--0x186a0-->  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; clock-frequency = &lt;400000&gt;;<!--400000--><!--400000--><!--400000--><!--400000--><!--400000--><!--400000--><!--400000--><!--400000--><!--400000--><!--400000-->  

  

#converte device tree de texto para binário  

dtc -I dts -O dtb -o /boot/uboot/dtbs/am335x-boneblack.dtb /boot/uboot/dtbs/am335x-boneblack.dts  

  

reiniciar, e procure no log, deve estar em 400KHz agora.  

  

[ &nbsp; &nbsp;0.131766] omap_i2c 44e0b000.i2c: bus 0 rev0.11 at 400 kHz  

[ &nbsp; &nbsp;0.132684] input: tps65217_pwr_but as /devices/ocp.3/44e0b000.i2c/i2c-0/0-0024/input/input0  

[ &nbsp; &nbsp;0.140854] omap_i2c 44e0b000.i2c: unable to select pin group  

__\[ &nbsp; &nbsp;0.141335\] omap\_i2c 4819c000.i2c: bus 1 rev0.11 at 400 kHz__  

  

  

<div class="separator" style="clear: both; text-align: center;">
<a href="http://en.wikipedia.org/wiki/I%C2%B2C" target="_blank"><img border="0" src="http://2.bp.blogspot.com/-56N5cJjXxUo/VLpULjTTrYI/AAAAAAAAukM/5QagGZLTp4U/s1600/i2c_logo2.gif"/></a></div>

  

Desativar o i2c das CAPES  

  

#converte de binário para texto  

dtc -I dtb -O dts -o am335x-boneblack.dts am335x-boneblack.dtb  

  

#mudar de okay para disabled  

&nbsp;status = "okay";  

  

&nbsp;status = "disabled";  

  

#converte de texto para binário  

dtc -I dts -O dtb -o am335x-boneblack.dtb &nbsp;am335x-boneblack.dts  

  

  

  

  