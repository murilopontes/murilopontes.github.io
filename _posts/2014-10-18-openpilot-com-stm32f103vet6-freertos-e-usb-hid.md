---
layout: post
title: OpenPilot com stm32f103vet6, FreeRTOS e USB HID
categories:
 - bootloader
date: 2014-10-18 22:41:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
O Openpilot é um projeto para criação de UAVs.<br/>
O projeto faz uso de microcontroladores STM32.<br/>
<br/>
<a name="more"></a><br/><br/>
O modelo mais básico usa um stm32f103cb com 20kb de ram e 128kb de flash, um sensor mpu6050 e mais uma memória spi de 8mb para logs de vôo.<br/>
O software é baseado no FreeRTOS que é um RTOS de código aberto que apenas 3 arquivos C provê threads, mutex, queues, e muito mais. Também possui um bootloader que faz isso da porta USB como dispositivo HID.<br/>
<br/>
Em teoria qualquer stm32 com configuração maior ou igual ao stm32f103cb pode rodar o software do Openpilot e sair voando por ai.<br/>
<br/>
Comecei um teste usando o stm32f103vet6 que tem 64kb de ram e 512kb de flash, um sensor mpu6050, e removendo a memória spi de 8mb do projeto inicial.<br/>
Segue os passos do experimento feito no Ubuntu 14.04:<br/>
<br/>
# obter o código fonte<br/>
git clone https://github.com/openpilot/OpenPilot.git<br/>
cd OpenPilot<br/>
<br/>
------------------------------------------------------------------------------<br/>
<div>
<br/></div>
1) No ubuntu<br/>
<br/>
Instalar o GNU ARM embedded que é mantido pela própria ARM.<br/>
(<span style="background-color: white; color: #333333; font-family: Ubuntu, 'Bitstream Vera Sans', 'DejaVu Sans', Tahoma, sans-serif; font-size: 12px; line-height: 18px;">ARM employees are maintaining this project.)</span><br/>
<br/>
https://launchpad.net/gcc-arm-embedded<br/>
<br/>
Step1: Inside Ubuntu, open a terminal and input<br/>
&nbsp; &nbsp; &nbsp; &nbsp;"sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded"<br/>
Step2: Continue to input<br/>
&nbsp; &nbsp; &nbsp; &nbsp;"sudo apt-get update"<br/>
Step3: Continue to input to install toolchain<br/>
&nbsp; &nbsp; &nbsp; &nbsp;"sudo apt-get install gcc-arm-none-eabi"<br/>
<br/>
<br/>
2) No ArchLinux<br/>
<br/>
# instala o toolchain para cross compilar com o GNU ARM embedded<br/>
make arm_sdk_install<br/>
<br/>
&nbsp;no Archlinux é preciso habilitar o repositorio multilib e instalar o skype ou wine para instalar as lib32* que o U ARM Embedded depende.<br/>
<div>
<br/></div>
# muda o path se necessário<br/>
export PATH=$PWD/tools/gcc-arm-none-eabi-4_8-2014q1/bin/:$PATH<br/>
<br/>
------------------------------------------------------------------------------<br/>
<br/>
<div>
#limpar tudo<br/>
21:16:11 murix@localhost:~/workspace/OpenPilot$make all_clean<br/>
&nbsp;CLEAN &nbsp; &nbsp; &nbsp;build<br/>
<br/>
# gerar o firmware completo (bootloader+app)<br/>
<div>
21:17:07 murix@localhost:~/workspace/OpenPilot$make ef_coptercontrol</div>
<div>
<br/></div>
<div>
<br/></div>
Making bootloader for CopterControl, board revision 0x02<br/>
Use BOARD_REVISION=1 for CC, BOARD_REVISION=2 for CC3D (default)<br/>
&nbsp;AS &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/startup_stm32f10x_MD_CC.S<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/CMSIS/Core/CM3/system_stm32f10x.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_adc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_bkp.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_bl_helper.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_debug.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_delay.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_dsm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_eeprom.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_exti.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_flash_internal.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_gpio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_i2c.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_irq.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_ppm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_ppm_out.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_pwm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_rtc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_servo.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_spi.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_sys.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_tim.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usart.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_cdc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid_istr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid_pwr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_rctx.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usbhook.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_wdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/misc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_adc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_bkp.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_can.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_cec.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_crc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dac.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dbgmcu.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dma.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_exti.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_flash.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_fsmc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_gpio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_i2c.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_iwdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_pwr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_rcc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_rtc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_sdio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_spi.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_tim.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_usart.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_wwdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_core.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_init.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_int.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_mem.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_regs.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_sil.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/pios_usb_board_data.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/bootloader/main.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/bootloader/pios_board.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_board_info.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_com_msg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_iap.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_usb_desc_hid_only.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_usb_util.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_led.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/op_dfu.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/printf-stdarg.c<br/>
&nbsp;LD &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/bl_coptercontrol/bl_coptercontrol.elf<br/>
&nbsp;BIN/HEX &nbsp; &nbsp; build/bl_coptercontrol/bl_coptercontrol.bin<br/>
compiling ../../ground/uavobjgenerator/main.cpp<br/>
compiling ../../ground/uavobjgenerator/uavobjectparser.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/generator_io.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/java/uavobjectgeneratorjava.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/flight/uavobjectgeneratorflight.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/gcs/uavobjectgeneratorgcs.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/matlab/uavobjectgeneratormatlab.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/python/uavobjectgeneratorpython.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/wireshark/uavobjectgeneratorwireshark.cpp<br/>
compiling ../../ground/uavobjgenerator/generators/generator_common.cpp<br/>
linking uavobjgenerator<br/>
- OpenPilot UAVObject Generator -<br/>
Done: processed 101 XML files and generated 101 objects with no ID collisions. Total size of the data fields is 3923 bytes.<br/>
generating flight code<br/>
&nbsp;AS &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/startup_stm32f10x_MD_CC.S<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/notification.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/CMSIS/Core/CM3/system_stm32f10x.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/pios_usb_board_data.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/System/systemmod.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/firmware/coptercontrol.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/targets/boards/coptercontrol/firmware/pios_board.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/alarms.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/instrumentation.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/uavtalk/uavtalk.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/uavobjects/uavobjectmanager.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/uavobjects/eventdispatcher.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/accessorydesired.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/objectpersistence.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gcstelemetrystats.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/flighttelemetrystats.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/faultsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/flightstatus.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/systemstats.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/systemalarms.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/systemsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationdesired.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationsettingsbank1.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationsettingsbank2.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationsettingsbank3.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationstatus.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/stabilizationbank.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/actuatorcommand.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/actuatordesired.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/actuatorsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/accelstate.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/accelgyrosettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gyrostate.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/attitudestate.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/manualcontrolcommand.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/i2cstats.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/watchdogstatus.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/manualcontrolsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/flightmodesettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/mixersettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/firmwareiapobj.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/attitudesettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/camerastabsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/cameradesired.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gpspositionsensor.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gpsvelocitysensor.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gpssettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/hwsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/gcsreceiver.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/receiveractivity.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/relaytuningsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/relaytuning.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/taskinfo.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/callbackinfo.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/mixerstatus.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/ratedesired.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/barosensor.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/txpidsettings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/airspeedstate.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/mpu6000settings.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/uavobject-synthetics/flight/perfcounter.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/croutine.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/event_groups.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/list.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/queue.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/tasks.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/timers.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_adc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_bkp.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_bl_helper.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_debug.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_delay.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_dsm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_eeprom.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_exti.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_flash_internal.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_gpio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_i2c.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_irq.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_ppm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_ppm_out.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_pwm.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_rtc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_servo.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_spi.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_sys.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_tim.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usart.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_cdc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid_istr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_hid_pwr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usb_rctx.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_usbhook.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/pios_wdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/misc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_adc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_bkp.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_can.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_cec.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_crc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dac.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dbgmcu.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_dma.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_exti.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_flash.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_fsmc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_gpio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_i2c.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_iwdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_pwr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_rcc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_rtc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_sdio.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_spi.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_tim.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_usart.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32F10x_StdPeriph_Driver/src/stm32f10x_wwdg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_core.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_init.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_int.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_mem.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_regs.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/stm32f10x/libraries/STM32_USB-FS-Device_Driver/src/usb_sil.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/portable/GCC/ARM_CM3/port.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/libraries/FreeRTOS/Source/portable/MemMang/heap_1.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_adxl345.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_bma180.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_bmp085.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_etasv3.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_gcsrcvr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_hcsr04.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_hmc5843.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_hmc5883.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_i2c_esc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_l3gd20.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_mpu6000.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_mpxv.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_ms4525do.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_ms5611.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_oplinkrcvr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_video.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_wavplay.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_iap.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_com.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_com_msg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_crc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_flashfs_logfs.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_flash_jedec.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_debuglog.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_deltatime.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_rcvr.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_rfm22b.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_rfm22b_com.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_sbus.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_sdcard.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_led.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_usb_desc_hid_cdc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_usb_desc_hid_only.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_usb_util.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_task_monitor.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_callbackscheduler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_notify.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_instrumentation.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/pios/common/pios_mem.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/fifo_buffer.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/sanitycheck.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/CoordinateConversions.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/math/sin_lookup.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/math/pid.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/math/mathmisc.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/libraries/printf-stdarg.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Attitude/attitude.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/altitudeloop.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/cruisecontrol.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/innerloop.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/outerloop.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/relay_tuning.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/stabilization.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Stabilization/virtualflybar.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Actuator/actuator.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Receiver/receiver.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/armhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/manualcontrol.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/manualhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/pathfollowerhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/pathplannerhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/stabilizedhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ManualControl/takeofflocationhandler.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/FirmwareIAP/firmwareiap.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Telemetry/telemetry.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/CameraStab/camerastab.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/ComUsbBridge/ComUsbBridge.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/GPS/GPS.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/GPS/NMEA.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/GPS/UBX.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/TxPID/txpid.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;flight/modules/Osd/osdoutput/osdoutput.c<br/>
&nbsp;LD &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/fw_coptercontrol/fw_coptercontrol.elf<br/>
&nbsp;BIN/HEX &nbsp; &nbsp; build/fw_coptercontrol/fw_coptercontrol.bin<br/>
&nbsp;FWINFO &nbsp; &nbsp; &nbsp;build/fw_coptercontrol/fw_coptercontrol.bin.firmware_info.c<br/>
&nbsp;CC &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;build/fw_coptercontrol/fw_coptercontrol.bin.firmware_info.c<br/>
&nbsp;BIN/HEX &nbsp; &nbsp; build/fw_coptercontrol/fw_coptercontrol.bin.firmware_info.bin<br/>
&nbsp;OPFW &nbsp; &nbsp; &nbsp; &nbsp;build/fw_coptercontrol/fw_coptercontrol.opfw<br/>
&nbsp;FLASH_IMG &nbsp; /home/murix/workspace/OpenPilot/build/ef_coptercontrol/ef_coptercontrol.bin<br/>
21:18:16 murix@localhost:~/workspace/OpenPilot$<br/>
<div>
<br/></div>
#gravar por SWD<br/>
st-flash &nbsp;write build/ef_coptercontrol/ef_coptercontrol.bin 0x08000000<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-5F6cx8KVgWk/VELatMCrMcI/AAAAAAAAtUU/hv2o3iM7om0/s1600/openpilot-stm32-boot-loop-hiddev-hidraw.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="115" src="http://3.bp.blogspot.com/-5F6cx8KVgWk/VELatMCrMcI/AAAAAAAAtUU/hv2o3iM7om0/s1600/openpilot-stm32-boot-loop-hiddev-hidraw.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">STM32F103VET6 com Openpilot detectado como USB HID</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-fSbQv0LvpZM/VEM1JXtMaLI/AAAAAAAAtUk/M4k5qK9L1pk/s1600/openpilot-stm32-flash-error.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="271" src="http://4.bp.blogspot.com/-fSbQv0LvpZM/VEM1JXtMaLI/AAAAAAAAtUk/M4k5qK9L1pk/s1600/openpilot-stm32-flash-error.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Openpilot &nbsp;Ground&nbsp;Control station (GCS)<br/>
bootloader reconhecido,<br/>
problema com o firmware que está resetando</td></tr>
</tbody></table>
<br/>
Testando também o fork TauLabs (no Ubuntu 14.04 e no Archlinux)<br/>
<a href="https://github.com/TauLabs/TauLabs">https://github.com/TauLabs/TauLabs</a><br/>
<br/>
# compila tudo<br/>
make package -j4<br/>
# gera imagem inteira da flash (bootloader+dados+app)<br/>
make ef_coptercontrol<br/>
# gravar a imagem no stm32f103vet6 com o stlink via SWD (pinos PA13 e PA14)<br/>
st-flash &nbsp;write build/ef_coptercontrol/ef_coptercontrol.bin 0x08000000<br/>
<div>
# executa a ground control station</div>
./build/ground/gcs/bin/taulabsgcs</div>
<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-sPJ7XUQmSHU/VEPjAy_QQPI/AAAAAAAAtU0/t-Y4OPSmeq4/s1600/taulabs-gps-stm32.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="286" src="http://2.bp.blogspot.com/-sPJ7XUQmSHU/VEPjAy_QQPI/AAAAAAAAtU0/t-Y4OPSmeq4/s1600/taulabs-gps-stm32.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Taulabs Ground Control station (GCS)<br/>
é um fork do Openpilot que tem mais placas e mais plugins.<br/>
O firmware para o stm32f103vet6 já ficou melhor, já está reconhecendo sem reboot,<br/>
porém nem o boot e nem o safeboot funcionaram ainda</td></tr>
</tbody></table>
<br/>
<br/>
Observações finais:<br/>
<br/>
O Openpilot é muito bem estruturado.<br/>
Também é ótimo para quem quiser aprender a programar multi-linguagens (C, C++, Java).<br/>
<br/>
<br/>
A Control Ground Station (GCS) em Qt5 é muito completa e suporta plugins para estender ainda mais.<br/>
<br/>
Também conta com Control Ground Station (GCS) para Android, então dá para pilot usando o telefone ou tablet pelo WiFi.<br/>
<br/>
O firmware para placas STM32F1 (legado) e STM32F4 (atual),<br/>
contam com ajuda do FreeRTOS (que é um sistema operacional de real - RTOS - em apenas 3 arquivos), <br/>
também faz uso das placas USB configuradas como dispositivos HID,<br/>
possuem um bootloader com suporte USB.<br/>
O controle de vôo implementa um filtro estendido de Kalman (EKF) rodando a 500Hz é uma das melhores, senão a melhor solução conhecida.<br/>
<br/>
<br/></div>
</div>