---
layout: post
title: Tutorial Internet of things (IOT) com 6LoWPAN
categories:
 - MSP430
date: 2014-03-16 05:53:00 +0000
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<span style="background-color: white;"><span style="font-family: sans-serif; font-size: x-small;"><span style="line-height: 19.200000762939453px;">Tutorial completo.</span></span></span><br/>
<span style="background-color: white;"><span style="font-family: sans-serif; font-size: x-small;"><span style="line-height: 19.200000762939453px;"></span></span></span><br/>
<a name="more"></a><span style="background-color: white;"><span style="font-family: sans-serif; font-size: x-small;"><span style="line-height: 19.200000762939453px;"><br/></span></span></span>
<span style="background-color: white;"><span style="font-family: sans-serif; font-size: x-small;"><span style="line-height: 19.200000762939453px;">O 6LoWPAN significa IPv6 Over Low Power Wireless Personal Network, ou seja, é uma rede IPv6 simplificada para rodar em sistemas&nbsp;microcontrolados.</span></span></span><br/>
<span style="background-color: white;"><span style="font-family: sans-serif; font-size: x-small;"><span style="line-height: 19.200000762939453px;"><br/></span></span></span>
<a href="http://en.wikipedia.org/wiki/6LoWPAN">http://en.wikipedia.org/wiki/6LoWPAN</a><br/>
<a href="http://pt.wikipedia.org/wiki/6LoWPAN">http://pt.wikipedia.org/wiki/6LoWPAN</a><br/>
<br/>
Para testar uma implementação que funcione de 6LoWPAN existem duas opções rápidas.<br/>
Uma totalmente gratuita que é o sistema operacional Contiki, que já possui 6LoWPAN nativo, com roteamento RPL de múltiplos saldos.<br/>
<br/>
Baixe o Contiki<br/>
<a href="http://www.contiki-os.org/">http://www.contiki-os.org/</a><br/>
<br/>
Compre um dos hardwares listados em&nbsp;<a href="http://www.contiki-os.org/hardware.html">http://www.contiki-os.org/hardware.html</a>,<br/>
no caso os únicos disponíveis em larga escala são o stm32w e o cc2530.<br/>
<br/>
O STM32w é um ARM-Cortex M3&nbsp;+ RF 2.4GHz e custa menos $20 a breakout board.<br/>
<a href="http://www.aliexpress.com/wholesale?SearchText=stm32w">http://www.aliexpress.com/wholesale?SearchText=stm32w</a><br/>
<br/>
O CC2530 é um 8051&nbsp;+ RF 2.4GHz e custa menos de $8 a breakout board.<br/>
&nbsp;<a href="http://www.aliexpress.com/wholesale?SearchText=cc2530">http://www.aliexpress.com/wholesale?SearchText=cc2530</a><br/>
<br/>
Ambos tem todo ambiente de desenvolvimento livre, com GCC, GDB, Eclipse-CDT, ....<br/>
É só buildar o contiki e montar sua rede com zilhões de dispositivos com rede IPv6 (internet) para controlar qualquer coisa que você imaginar de qualquer lugar da internet.<br/>
<br/>
Um kit bastante interessante que você pode estar comprando aqui (somente se estiver nos estados unidos),<br/>
é o Texas CC-6LOWPAN-DK, que foi desenvolvimento de uma parceira da Texas com a Sensinode, atualmente a Sensinode foi comprada pela ARM, então podemos esperar que num futuro próximo veremos uma enxurrada de microcontroladores ARM com rede RF prontos para pendurar na internet.<br/>
<br/>
O kit CC-6LOWPAN-DK custa menos de $900 mas ainda acho 'overpriced'<br/>
<a href="http://br.mouser.com/ProductDetail/Texas-Instruments/CC-6LOWPAN-DK-868/?qs=dn9%252bmHMlkg/KYkwM%252bua8Ow==">http://br.mouser.com/ProductDetail/Texas-Instruments/CC-6LOWPAN-DK-868/?qs=dn9%252bmHMlkg/KYkwM%252bua8Ow==</a><br/>
<div>
<br/></div>
<div>
A Wiki do CC-6LOWPAN-DK&nbsp;</div>
<a href="http://processors.wiki.ti.com/index.php/CC-6LoWPAN">http://processors.wiki.ti.com/index.php/CC-6LoWPAN</a><br/>
O kit é funcional, embora a documentação não seja muito extensa, dá para arrumar tudo buscando no Google.<br/>
<br/>
O kit vem com uma placa OMAP-L138 EVM da PDLOGIC, e roda o Arago Linux 2009.11.<br/>
<a href="http://arago-project.org/wiki/index.php/Main_Page">http://arago-project.org/wiki/index.php/Main_Page</a><br/>
<br/>
Todos os binários para regravar o SDCard em caso de destruição acidental do sistema podem ser baixados daqui:<br/>
<a href="http://arago-project.org/files/releases/2009.11/images/da850-omapl138-evm/">http://arago-project.org/files/releases/2009.11/images/da850-omapl138-evm/</a><br/>
<br/>
A sequência é UBL -&gt; uboot -&gt; linux.<br/>
Não encontrei os arquivos do UBL no site do Arago, mas estão disponiveis dentro do SDK do OMAP fornecido pela Texas em:<br/>
<a href="http://software-dl.ti.com/dsps/dsps_public_sw/c6000/web/omapl138_lcdk_sdk/latest/index_FDS.html">http://software-dl.ti.com/dsps/dsps_public_sw/c6000/web/omapl138_lcdk_sdk/latest/index_FDS.html</a><br/>
e que depois foi atualizado para um novo SDK que ativa também o DSP que vem no OMAP.<br/>
<a href="http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/dvsdk/DVSDK_4_00/latest/index_FDS.html">http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/dvsdk/DVSDK_4_00/latest/index_FDS.html</a><br/>
Essas SDK das Texas são um pouco antigos e só são garantidos de rodar sobra o Ubuntu 10.04 LTS.<br/>
Provavelmente você também vai precisar criar uma VM só para isso como é de costume.<br/>
<br/>
Para conectar no console serial do OMAP-L138 EVM é preciso de um cabo RS232 cruzado,<br/>
como de costume, se você não tiver um pronto, é só comprar 2 DB9, soldar assim:<br/>
Lado A | Lado B<br/>
pino 2 &nbsp;--- pino 3<br/>
pino 3 --- pino 2<br/>
pino 5 --- pino 5<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-w8xkgZQRbjk/UySmze8EtLI/AAAAAAAApRM/uDbvRYhK1c4/s1600/IMG_20140315_161210.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-w8xkgZQRbjk/UySmze8EtLI/AAAAAAAApRM/uDbvRYhK1c4/s1600/IMG_20140315_161210.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Cabo serial cruzado para acessar o console serial do OMAP-L138.</td></tr>
</tbody></table>
Feito isso é só abrir o PuTTY, Minicom, termite, advance serial port console, ou qualquer outro software para porta serial de sua preferência. Eu recomendo o PuTTYtray e o minicom.<br/>
<br/>
Putty tray é um fork do Putty com reconexão automática.<br/>
<a href="http://haanstra.eu/putty/">http://haanstra.eu/putty/</a><br/>
<br/>
Vamos dar uma olhada no console serial do OMAP-L138 para ver o que tem de interessante.<br/>
<br/>
<h2>
OMAP-L138 EVM bootloader (UBL)</h2>
<br/>
<pre><span style="background-color: #cfe2f3;">Booting with TI UBL
Device OPP (300MHz, 1.2V)</span>
</pre>
<h2>
</h2>
<h2>
OMAP-L138 Uboot</h2>
<br/>
<pre><span style="background-color: #cfe2f3;">U-Boot 2009.11 (Nov 09 2010 - 18:48:43)

I2C:   ready
DRAM:  64 MB
MMC:   davinci: 0
*** Warning - bad CRC, using default environment

In:    serial
Out:   serial
Err:   serial
ARM Clock : 300000000 Hz
DDR Clock : 132000000 Hz
Net:   Ethernet PHY: GENERIC @ 0x00

Hit any key to stop autoboot:  0
reading boot.scr

** Unable to read "boot.scr" from mmc 0:1 **
reading uImage

1842560 bytes read
## Booting kernel from Legacy Image at c0700000 ...
   Image Name:   Linux-2.6.32-rc6
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    1842496 Bytes =  1.8 MB
   Load Address: c0008000
   Entry Point:  c0008000
   Verifying Checksum ... OK
   Loading Kernel Image ... OK
OK

Starting kernel ...</span>
</pre>
<h2>
kernel do linux iniciando....</h2>
<br/>
<pre><span style="background-color: #cfe2f3;">Uncompressing Linux.......................................................................................................................... done, booting the kernel.
Linux version 2.6.32-rc6 (jars@jars-desktop) (gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203) ) #13 PREEMPT Thu Aug 25 16:46:06 CEST 2011
CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=00053177
CPU: VIVT data cache, VIVT instruction cache
Machine: DaVinci DA850/OMAP-L138 EVM
Memory policy: ECC disabled, Data cache writeback
DaVinci da850/omap-l138/am18x variant 0x1
Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 8128
Kernel command line: mem=32M console=ttyS2,115200n8 root=/dev/mmcblk0p2 rw rootwait ip=off
PID hash table entries: 128 (order: -3, 512 bytes)
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 32MB = 32MB total
Memory: 28540KB available (3484K code, 266K data, 152K init, 0K highmem)
SLUB: Genslabs=11, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
Hierarchical RCU implementation.
NR_IRQS:245
Console: colour dummy device 80x30
Calibrating delay loop... 149.50 BogoMIPS (lpj=747520)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
DaVinci: 144 gpio irqs
regulator: core version 0.5
NET: Registered protocol family 16
MUX: Setting register GPIO4_0
           PINMUX10 (0x00000028) = 0x22222222 -&gt; 0x82222222
MUX: Setting register GPIO4_1
           PINMUX10 (0x00000028) = 0x82222222 -&gt; 0x88222222
MUX: Setting register UART1_RXD
           PINMUX4 (0x00000010) = 0x00222288 -&gt; 0x02222288
MUX: Setting register UART1_TXD
           PINMUX4 (0x00000010) = 0x02222288 -&gt; 0x22222288
MUX: Setting register GPIO1_15
           PINMUX2 (0x00000008) = 0x88888880 -&gt; 0x88888888
MUX: Setting register LCD_D_0
           PINMUX17 (0x00000044) = 0x00000000 -&gt; 0x00000020
MUX: Setting register LCD_D_1
           PINMUX17 (0x00000044) = 0x00000020 -&gt; 0x00000022
MUX: Setting register LCD_D_2
           PINMUX16 (0x00000040) = 0x00000000 -&gt; 0x20000000
MUX: Setting register LCD_D_3
           PINMUX16 (0x00000040) = 0x20000000 -&gt; 0x22000000
MUX: Setting register LCD_D_4
           PINMUX16 (0x00000040) = 0x22000000 -&gt; 0x22200000
MUX: Setting register LCD_D_5
           PINMUX16 (0x00000040) = 0x22200000 -&gt; 0x22220000
MUX: Setting register LCD_D_6
           PINMUX16 (0x00000040) = 0x22220000 -&gt; 0x22222000
MUX: Setting register LCD_D_7
           PINMUX16 (0x00000040) = 0x22222000 -&gt; 0x22222200
MUX: Setting register LCD_D_8
           PINMUX18 (0x00000048) = 0x00000000 -&gt; 0x00000020
MUX: Setting register LCD_D_9
           PINMUX18 (0x00000048) = 0x00000020 -&gt; 0x00000022
MUX: Setting register LCD_D_10
           PINMUX17 (0x00000044) = 0x00000022 -&gt; 0x20000022
MUX: Setting register LCD_D_11
           PINMUX17 (0x00000044) = 0x20000022 -&gt; 0x22000022
MUX: Setting register LCD_D_12
           PINMUX17 (0x00000044) = 0x22000022 -&gt; 0x22200022
MUX: Setting register LCD_D_13
           PINMUX17 (0x00000044) = 0x22200022 -&gt; 0x22220022
MUX: Setting register LCD_D_14
           PINMUX17 (0x00000044) = 0x22220022 -&gt; 0x22222022
MUX: Setting register LCD_D_15
           PINMUX17 (0x00000044) = 0x22222022 -&gt; 0x22222222
MUX: Setting register LCD_PCLK
           PINMUX18 (0x00000048) = 0x00000022 -&gt; 0x02000022
MUX: Setting register LCD_MCLK
           PINMUX18 (0x00000048) = 0x02000022 -&gt; 0x22000022
MUX: Setting register LCD_HSYNC
           PINMUX19 (0x0000004c) = 0x00000000 -&gt; 0x00000002
MUX: Setting register LCD_VSYNC
           PINMUX19 (0x0000004c) = 0x00000002 -&gt; 0x00000022
MUX: Setting register NLCD_AC_ENB_CS
           PINMUX19 (0x0000004c) = 0x00000022 -&gt; 0x02000022
MUX: Setting register GPIO2_8
           PINMUX5 (0x00000014) = 0x00110110 -&gt; 0x80110110
MUX: Setting register GPIO2_15
           PINMUX5 (0x00000014) = 0x80110110 -&gt; 0x80110118
MUX: Setting register GPIO2_4
           PINMUX6 (0x00000018) = 0x00000000 -&gt; 0x00008000
MUX: Setting register GPIO6_13
           PINMUX13 (0x00000034) = 0x00000000 -&gt; 0x00000800
bio: create slab </span><bio-0><span style="background-color: #cfe2f3;"> at 0
SCSI subsystem initialized
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
regulator: VDCDC1: 3200 &lt;--&gt; 3300 mV
regulator: VDCDC2: 1750 &lt;--&gt; 3300 mV
regulator: VDCDC3: 950 &lt;--&gt; 1300 mV
regulator: LDO1: 1800 mV
regulator: LDO2: 1150 &lt;--&gt; 1300 mV
pca953x 1-0020: failed reading register
pca953x: probe of 1-0020 failed with error -121
Switching to clocksource timer0_1
musb_hdrc: version 6.0, cppi4.1-dma, (host+peripheral), debug=0
Waiting for USB PHY clock good...
musb_hdrc: USB OTG mode controller at fee00000 using DMA, IRQ 58
musb_hdrc musb_hdrc: MUSB HDRC host driver
musb_hdrc musb_hdrc: new USB bus registered, assigned bus number 1
usb usb1: configuration #1 chosen from 1 choice
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 1 port detected
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 1024 (order: 1, 8192 bytes)
TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
TCP: Hash tables configured (established 1024 bind 1024)
TCP reno registered
NET: Registered protocol family 1
RPC: Registered udp transport module.
RPC: Registered tcp transport module.
RPC: Registered tcp NFSv4.1 backchannel transport module.
EMAC: MII PHY configured, RMII PHY will not be functional
MUX: Setting register GPIO2_6
           PINMUX6 (0x00000018) = 0x00008000 -&gt; 0x00008080
JFFS2 version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
msgmni has been set to 55
io scheduler noop registered
io scheduler anticipatory registered (default)
da8xx_lcdc da8xx_lcdc.0: GLCD: Found Sharp_LK043T1DG01 panel
Console: switching to colour frame buffer device 60x34
Serial: 8250/16550 driver, 3 ports, IRQ sharing disabled
serial8250.0: ttyS0 at MMIO 0x1c42000 (irq = 25) is a 16550A
serial8250.0: ttyS1 at MMIO 0x1d0c000 (irq = 53) is a 16550A
serial8250.0: ttyS2 at MMIO 0x1d0d000 (irq = 61) is a 16550A
console [ttyS2] enabled
brd: module loaded
ahci ahci: forcing PORTS_IMPL to 0x1
ahci ahci: AHCI 0001.0100 32 slots 1 ports 3 Gbps 0x1 impl SATA mode
ahci ahci: flags: ncq sntf pm led clo only pmp pio slum part ccc
scsi0 : ahci
ata1: SATA max UDMA/133 irq 67
m25p80 spi1.0: m25p64 (8192 Kbytes)
Creating 4 MTD partitions on "m25p80":
0x000000000000-0x000000040000 : "U-Boot"
0x000000040000-0x000000050000 : "U-Boot Environment"
0x000000050000-0x0000007f0000 : "Linux"
0x0000007f0000-0x000000800000 : "MAC Address"
Read MAC addr from EEPROM: 00:08:ee:05:0d:66
davinci SPI Controller driver at 0xfef0e000 (irq = 56) use_dma=1
tun: Universal TUN/TAP device driver, 1.6
tun: (C) 1999-2004 Max Krasnyansky <!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------></span><maxk qualcomm.com=""><span style="background-color: #cfe2f3;">
console [netcon0] enabled
netconsole: network logging started
ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
ohci ohci.0: DA8xx OHCI
ohci ohci.0: new USB bus registered, assigned bus number 2
ohci ohci.0: irq 59, io mem 0x01e25000
usb usb2: configuration #1 chosen from 1 choice
hub 2-0:1.0: USB hub found
hub 2-0:1.0: 1 port detected
Initializing USB Mass Storage driver...
usbcore: registered new interface driver usb-storage
USB Mass Storage support registered.
g_ether gadget: using random self ethernet address
g_ether gadget: using random host ethernet address
usb0: MAC 3e:7a:01:62:bf:e2
usb0: HOST MAC 06:8c:ae:fe:d5:0b
g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
g_ether gadget: g_ether ready
omap_rtc omap_rtc: rtc core: registered omap_rtc as rtc0
omap_rtc: RTC power up reset detected
i2c /dev entries driver
watchdog watchdog: heartbeat 60 sec
cpuidle: using governor ladder
cpuidle: using governor menu
davinci_mmc davinci_mmc.0: Using DMA, 4-bit mode
usbcore: registered new interface driver usbhid
usbhid: v2.6:USB HID core driver
TCP cubic registered
NET: Registered protocol family 17
Clocks: disable unused emac
regulator_init_complete: incomplete constraints, leaving LDO2 on
regulator_init_complete: incomplete constraints, leaving LDO1 on
regulator_init_complete: incomplete constraints, leaving VDCDC3 on
regulator_init_complete: incomplete constraints, leaving VDCDC2 on
regulator_init_complete: incomplete constraints, leaving VDCDC1 on
emac-mii: probed
omap_rtc omap_rtc: setting system clock to 2000-01-01 00:00:00 UTC (946684800)
ata1: SATA link down (SStatus 0 SControl 300)
mmc0: new high speed SDHC card at address 1234
mmcblk0: mmc0:1234 SA04G 3.68 GiB
Waiting for root device /dev/mmcblk0p2...
 mmcblk0: p1 p2
g_ether gadget: high speed config #2: RNDIS
EXT3-fs warning: maximal mount count reached, running e2fsck is recommended
kjournald starting.  Commit interval 5 seconds
EXT3 FS on mmcblk0p2, internal journal
EXT3-fs: recovery complete.
EXT3-fs: mounted filesystem with writeback data mode.
VFS: Mounted root (ext3 filesystem) on device 179:2.
Freeing init memory: 152K
serial_link_irq_chain
ttyS2: request irq 61
serial_link_irq_chain
ttyS2: request irq 61
serial_link_irq_chain
ttyS2: request irq 61
INIT: serial_link_irq_chain
ttyS2: request irq 61
version 2.86 bootingserial_link_irq_chain
ttyS2: request irq 61

serial_link_irq_chain
ttyS2: request irq 61
Please wait: booting...
Starting udev
udev: starting version 141
udevd[458]: inotify_add_watch(3, (null), 10) failed: Bad address

udevd[458]: inotify_add_watch(3, (null), 10) failed: Bad address

udevd[458]: inotify_add_watch(3, (null), 10) failed: Bad address

udevd[458]: inotify_add_watch(3, (null), 10) failed: Bad address

Remounting root file system...
NET: Registered protocol family 10
root: mount: mounting rootfs on / failed: No such file or directory
root: mount: mounting usbfs on /proc/bus/usb failed: No such file or directory
Setting up IP spoofing protection: rp_filter.
Configuring network interfaces... eth0: attached PHY driver [Generic PHY] (mii_bus:phy_addr=1:00, id=7c0f1)
ADDRCONF(NETDEV_UP): eth0: link is not ready
ifconfig: SIOCGIFFLAGS: No such device
ifconfig: SIOCSIFADDR: No such device
route: SIOCADDRT: No such device
done.
Sat Dec 12 04:23:00 UTC 2009
serial_link_irq_chain
ttyS2: request irq 61
INIT: serial_link_irq_chain
ttyS2: request irq 61
Entering runlevel: 5serial_link_irq_chain
ttyS2: request irq 61

serial_link_irq_chain
ttyS2: request irq 61
Starting telnet daemon.
Starting syslogd/klogd: done
Starting thttpd.
net.ipv6.conf.all.proxy_ndp = 1
net.ipv6.conf.all.forwarding = 1
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.proxy_ndp = 1
net.ipv6.conf.default.forwarding = 1
net.ipv6.conf.default.autoconf = 0
net.ipv6.conf.eth0.proxy_ndp = 1
net.ipv6.conf.eth0.forwarding = 1
net.ipv6.conf.eth0.autoconf = 0
cp: cannot stat 'default.txt': No such file or directory
Starting NanoRouter:
serial_link_irq_chain
ttyS2: request irq 61
serial_link_irq_chain
ttyS2: request irq 61

 _____                    _____           _         _
|  _  |___ ___ ___ ___   |  _  |___ ___  |_|___ ___| |_
|     |  _| .'| . | . |  |   __|  _| . | | | -_|  _|  _|
|__|__|_| |__,|_  |___|  |__|  |_| |___|_| |___|___|_|
              |___|                    |___|

Arago Project http://arago-project.org da850-omapl138-evm ttyS2

Arago 2009.11 da850-omapl138-evm ttyS2

da850-omapl138-evm login:</span>
</maxk><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------><!------></bio-0></pre>
<br/>
<h2>
Detalhes do OMAP</h2>
A placa tem de 64MB de RAM, 32MB para o Linux e 32MB para o DSP.<br/>
<br/>
O ARM926EJ é v5 de 300MHz<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# uname -a</span><br/>
<span style="background-color: #cfe2f3;">Linux da850-omapl138-evm 2.6.32-rc6 #13 PREEMPT Thu Aug 25 16:46:06 CEST 2011 armv5tejl unknown</span><br/>
<span style="background-color: #cfe2f3;">r</span><br/>
<br/>
Com esses bogomips é equivalente a um Pentium 100 Mhz<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# cat /proc/cpuinfo</span><br/>
<span style="background-color: #cfe2f3;">Processor &nbsp; &nbsp; &nbsp; : ARM926EJ-S rev 5 (v5l)</span><br/>
<span style="background-color: #cfe2f3;">BogoMIPS &nbsp; &nbsp; &nbsp; &nbsp;: 149.50</span><br/>
<span style="background-color: #cfe2f3;">Features &nbsp; &nbsp; &nbsp; &nbsp;: swp half thumb fastmult edsp java</span><br/>
<span style="background-color: #cfe2f3;">CPU implementer : 0x41</span><br/>
<span style="background-color: #cfe2f3;">CPU architecture: 5TEJ</span><br/>
<span style="background-color: #cfe2f3;">CPU variant &nbsp; &nbsp; : 0x0</span><br/>
<span style="background-color: #cfe2f3;">CPU part &nbsp; &nbsp; &nbsp; &nbsp;: 0x926</span><br/>
<span style="background-color: #cfe2f3;">CPU revision &nbsp; &nbsp;: 5</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Hardware &nbsp; &nbsp; &nbsp; &nbsp;: DaVinci DA850/OMAP-L138 EVM</span><br/>
<span style="background-color: #cfe2f3;">Revision &nbsp; &nbsp; &nbsp; &nbsp;: 0000</span><br/>
<span style="background-color: #cfe2f3;">Serial &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: 0000000000000000</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# free</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; total &nbsp; &nbsp; &nbsp; &nbsp; used &nbsp; &nbsp; &nbsp; &nbsp; free &nbsp; &nbsp; &nbsp; shared &nbsp; &nbsp; &nbsp;buffers</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; Mem: &nbsp; &nbsp; &nbsp; &nbsp;28692 &nbsp; &nbsp; &nbsp; &nbsp;15208 &nbsp; &nbsp; &nbsp; &nbsp;13484 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0 &nbsp; &nbsp; &nbsp; &nbsp; 1500</span><br/>
<span style="background-color: #cfe2f3;">&nbsp;Swap: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;0</span><br/>
<span style="background-color: #cfe2f3;">Total: &nbsp; &nbsp; &nbsp; &nbsp;28692 &nbsp; &nbsp; &nbsp; &nbsp;15208 &nbsp; &nbsp; &nbsp; &nbsp;13484</span><br/>
<br/>
<b>O IPv6 padrão do kit é configurado estaticamente para 2001::11/64</b><br/>
<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# ifconfig</span><br/>
<span style="background-color: #cfe2f3;">eth0 &nbsp; &nbsp; &nbsp;Link encap:Ethernet &nbsp;HWaddr 00:08:EE:05:0D:66</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inet addr:192.168.1.10 &nbsp;Bcast:192.168.1.255 &nbsp;Mask:255.255.255.0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inet6 addr: 2001::11/64 Scope:Global</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; UP BROADCAST MULTICAST &nbsp;MTU:1500 &nbsp;Metric:1</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; RX packets:0 errors:0 dropped:0 overruns:0 frame:0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; TX packets:0 errors:0 dropped:0 overruns:0 carrier:0</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; collisions:0 txqueuelen:1000</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; RX bytes:0 (0.0 B) &nbsp;TX bytes:0 (0.0 B)</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Interrupt:33</span><br/>
<div>
<br/></div>
Agora é só faz um ssh de máquina qualquer no esteja na rede 2001::xx/64,<br/>
no caso configurei meu windows para ficar com o IPv6 2001::69/64.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-8Yr7_1rAaJ8/UySso2kH4HI/AAAAAAAApRk/uPH9nRtiiHk/s1600/windows-ipv6-6lowpan.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="290" src="http://1.bp.blogspot.com/-8Yr7_1rAaJ8/UySso2kH4HI/AAAAAAAApRk/uPH9nRtiiHk/s1600/windows-ipv6-6lowpan.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Configurando o windows com IPv6 2001::69/64</td></tr>
</tbody></table>
Feito isso é testar com o ping para ver se deu cerco.<br/>
<span style="background-color: #cfe2f3;">C:\Users\mpontes&gt;ping 2001::11</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Disparando 2001::11 com 32 bytes de dados:</span><br/>
<span style="background-color: #cfe2f3;">Resposta de 2001::11: tempo=4ms</span><br/>
<span style="background-color: #cfe2f3;">Resposta de 2001::11: tempo=1ms</span><br/>
<span style="background-color: #cfe2f3;">Resposta de 2001::11: tempo=17ms</span><br/>
<span style="background-color: #cfe2f3;">Resposta de 2001::11: tempo=2ms</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Estatísticas do Ping para 2001::11:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; Pacotes: Enviados = 4, Recebidos = 4, Perdidos = 0 (0% de</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;perda),</span><br/>
<span style="background-color: #cfe2f3;">Aproximar um número redondo de vezes em milissegundos:</span><br/>
<span style="background-color: #cfe2f3;">&nbsp; &nbsp; Mínimo = 1ms, Máximo = 17ms, Média = 6ms</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">C:\Users\mpontes&gt;</span><br/>
<br/>
Ok, conectar pelo telnet, já que o OMAP não vem SSH.<br/>
Agora é a uma boa hora de usar o puttytray com reconexão automática.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-rIjwO4sYa-w/UySt3DHy9KI/AAAAAAAApRw/3PMNqVkviH8/s1600/omap-l138-telnet-ipv6.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="202" src="http://4.bp.blogspot.com/-rIjwO4sYa-w/UySt3DHy9KI/AAAAAAAApRw/3PMNqVkviH8/s1600/omap-l138-telnet-ipv6.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">putty conectado no telnet IPv6 do OMAP</td></tr>
</tbody></table>
Agora é hora de depurar o programas da sensinode que vem junto com o kit.<br/>
Dentro da pasta /home/root do omap você vai encontrar esses arquivos ai:<br/>
<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# find last tools</span><br/>
<span style="background-color: #cfe2f3;">last</span><br/>
<span style="background-color: #cfe2f3;">last/NAPSocketServer</span><br/>
<span style="background-color: #cfe2f3;">last/NAPSocketServer/NAPSocketServer</span><br/>
<span style="background-color: #cfe2f3;">last/NAPSocketServer/Version.txt</span><br/>
<span style="background-color: #cfe2f3;">last/configFiles</span><br/>
<span style="background-color: #cfe2f3;">last/configFiles/rf_configuration_ttyS1.conf</span><br/>
<span style="background-color: #cfe2f3;">last/configFiles/if_full.txt</span><br/>
<span style="background-color: #cfe2f3;">last/ConfSv</span><br/>
<span style="background-color: #cfe2f3;">last/ConfSv/Version.txt</span><br/>
<span style="background-color: #cfe2f3;">last/ConfSv/ConfSv</span><br/>
<span style="background-color: #cfe2f3;">last/nanorouter</span><br/>
<span style="background-color: #cfe2f3;">last/6routed</span><br/>
<span style="background-color: #cfe2f3;">last/6routed/Version.txt</span><br/>
<span style="background-color: #cfe2f3;">last/6routed/6routed</span><br/>
<span style="background-color: #cfe2f3;">tools</span><br/>
<span style="background-color: #cfe2f3;">tools/NanoBoot_host_10_8552</span><br/>
<span style="background-color: #cfe2f3;">tools/ENCRYPTED_CC1180_AP_FW.hex</span><br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~#</span><br/>
<div>
<br/></div>
<div>
Todos esses arquivos podem ser baixados daqui:</div>
<div>
<a href="http://e2e.ti.com/members/1492871/files/beaglebone_5f00_nanorouter_5f00_files.zip.aspx">http://e2e.ti.com/members/1492871/files/beaglebone_5f00_nanorouter_5f00_files.zip.aspx</a></div>
<div>
Para instalar no OMAP ou BeagleBone, ou qualquer outro Linux para ARM.</div>
<div>
<br/></div>
<div>
O nanoboot_host e o firmware do CC1180 podem ser baixados direto da página da sensinode.</div>
<div>
<a href="http://www.sensinode.com/EN/products/software/ti-cc-6lowpan-kit.html">http://www.sensinode.com/EN/products/software/ti-cc-6lowpan-kit.html</a></div>
<div>
<br/></div>
<div>
O nanorouter é o daemon pai de todos os processos da rede 6lowpan. Quando executado ele vai subir os outros daemons filhos: NAPSocketServer, ConfSv e 6routed.&nbsp;</div>
<div>
O nanorouter vai criar uma subnet baseado no IPv6 da interface eth0 para alocar os IPv6 de todos dispositivos da rede 6LowPAN.</div>
<div>
<br/></div>
<div>
Quando for rodar pela primeira vez, é provável que o kit trave por algum ruido no conector do CC1180 que é muito frágil. Quando isto ocorre, os leds do CC1180 ficam acessos por toda eternidade.</div>
<div>
Para resolver esse problema é necessário mexer no GPIO do OMAP até que o travamento suma.</div>
<div>
Talvez seja necessário atualizar ou gravar o firmware do CC1180 se ele estiver zerado de fábrica.</div>
<div>
<br/></div>
<div>
Hora de matar todos os processos do nanorouter, para fazer o debug do GPIO e do firmware do CC1180</div>
<div>
<span style="background-color: #cfe2f3;">killall -9 6routed ConfSv NAPSocketServer nanorouter</span>&nbsp;</div>
<div>
<br/></div>
<div>
Crie também dois scripts para mudar o nivel do GPIO do OMAP que está ligado no CC1180.</div>
<div>
<br/></div>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# cat um.sh</span><br/>
<span style="background-color: #cfe2f3;">echo 31 &gt;/sys/class/gpio/export</span><br/>
<span style="background-color: #cfe2f3;">echo out &gt; /sys/class/gpio/gpio31/direction</span><br/>
<span style="background-color: #cfe2f3;">echo 1 &gt; /sys/class/gpio/gpio31/value</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~# cat zero.sh</span><br/>
<span style="background-color: #cfe2f3;">echo 31 &gt;/sys/class/gpio/export</span><br/>
<span style="background-color: #cfe2f3;">echo out &gt; /sys/class/gpio/gpio31/direction</span><br/>
<span style="background-color: #cfe2f3;">echo 0 &gt; /sys/class/gpio/gpio31/value</span><br/>
<br/>
Segundo o datasheet do CC1180 se os 2 leds estiverem acessos continuamente sem piscar, é porque o CC1180 encontra-se em modo de bootloader.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-uZEHr_RasWo/UyS-XLcANbI/AAAAAAAApSU/hoxlWDXRTtE/s1600/IMG_20140315_170154.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-uZEHr_RasWo/UyS-XLcANbI/AAAAAAAApSU/hoxlWDXRTtE/s1600/IMG_20140315_170154.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC1180 com leds acessos sem piscar = modo bootloader</td></tr>
</tbody></table>
MODE=0 -&gt; modo bootloader<br/>
MODE=1 -&gt; modo aplicativo<br/>
<br/>
Com o CC1180 em modo bootloader é possivel usar o nanoboot_host para gravar o firmware de Access Point (AP) da rede 6lowpan.<br/>
<br/>
O CC1180 na verdade é o CC1110F32 pre gravado com o bootloader da sensinode, que é proprietário e na está disponível para download. &nbsp;Este bootloader ocupa 5k dos 32k do CC1110F32.<br/>
A parte atualizável do firmware são os 27K que estão disponíveis no link:<br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/encrypted_cc1180_ap_fw.zip">http://www.sensinode.com/media/ti-cc-6lowpan/encrypted_cc1180_ap_fw.zip</a><br/>
<br/>
Neste outro link tem o nanoboot_host para ARM e PC<br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/nanoboot-host-1.0.zip">http://www.sensinode.com/media/ti-cc-6lowpan/nanoboot-host-1.0.zip</a><br/>
<br/>
Para atualizar o kit do OMAP-L138, é só extrair o encrypted_cc1180_ap_fw.zip e o nanoboot-host-1.0.zip para ARM, colocar no SDCard do OMAP e executar os comandos que seguem...<br/>
<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~/tools# ./NanoBoot_host_10_8552 /dev/ttyS1 ENCRYPTED_CC1180_AP_FW.hex</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<br/>
<div>
<div>
<span style="background-color: #cfe2f3;">NanoBoot HOST application 1.0</span></div>
<div>
<span style="background-color: #cfe2f3;">Pserial_link_irq_chain</span></div>
<div>
<span style="background-color: #cfe2f3;">ress 1 and enterttyS1: request irq 53</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp;to open menu.</span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<span style="background-color: #cfe2f3;"><serial_port: ...ok="" dev="" opening="" port="" serial="" to="" ttys1=""></serial_port:></span></div>
<div>
<span style="background-color: #cfe2f3;">Requesting version...</span></div>
<div>
<span style="background-color: #cfe2f3;">NanoBoot 1.1</span></div>
<div>
<span style="background-color: #cfe2f3;">Firmware version info: &nbsp;ff ff ff ff ff ff</span></div>
</div>
<div>
<div>
<span style="background-color: #cfe2f3;">1</span></div>
<div>
<span style="background-color: #cfe2f3;">Select packet type:</span></div>
<div>
<span style="background-color: #cfe2f3;">0. Check mac address (sanity check)</span></div>
<div>
<span style="background-color: #cfe2f3;">1. Write binary ENCRYPTED_CC1180_AP_FW.hex</span></div>
<div>
<span style="background-color: #cfe2f3;">2. Set MAC address.</span></div>
<div>
<span style="background-color: #cfe2f3;">3. Switch to application mode</span></div>
<div>
<span style="background-color: #cfe2f3;">4. Firmware versions</span></div>
<div>
<span style="background-color: #cfe2f3;">6. Toggle GPIO line (For mode change).</span></div>
</div>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<div>
<span style="background-color: #cfe2f3;">Select packet type:</span></div>
<div>
<span style="background-color: #cfe2f3;">0. Check mac address (sanity check)</span></div>
<div>
<span style="background-color: #cfe2f3;">1. Write binary ENCRYPTED_CC1180_AP_FW.hex</span></div>
<div>
<span style="background-color: #cfe2f3;">2. Set MAC address.</span></div>
<div>
<span style="background-color: #cfe2f3;">3. Switch to application mode</span></div>
<div>
<span style="background-color: #cfe2f3;">4. Firmware versions</span></div>
<div>
<span style="background-color: #cfe2f3;">6. Toggle GPIO line (For mode change).</span></div>
<div>
<span style="background-color: #cfe2f3;">1</span></div>
<div>
<span style="background-color: #cfe2f3;">File ok</span></div>
<div>
<span style="background-color: #cfe2f3;"><start firmware="" update=""></start></span></div>
<div>
<span style="background-color: #cfe2f3;">...............1 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............2 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............3 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............4 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............5 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............6 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............7 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............8 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............9 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............10 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............11 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............12 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............13 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............14 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............15 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............16 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............17 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............18 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............19 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............20 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............21 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............22 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............23 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............24 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............25 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............26 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">...............27 Page Done OK!</span></div>
<div>
<span style="background-color: #cfe2f3;">Firmware update completed.</span></div>
<div>
<br/></div>
</div>
<div>
Prontinho, firmware do CC1180 gravado com sucesso!</div>
<div>
<br/></div>
Usando o opção 4 do menu do nanoboot temos o seguinte<br/>
<span style="background-color: #cfe2f3;">Select packet type:</span><br/>
<span style="background-color: #cfe2f3;">0. Check mac address (sanity check)</span><br/>
<span style="background-color: #cfe2f3;">1. Write binary ENCRYPTED_CC1180_AP_FW.hex</span><br/>
<span style="background-color: #cfe2f3;">2. Set MAC address.</span><br/>
<span style="background-color: #cfe2f3;">3. Switch to application mode</span><br/>
<span style="background-color: #cfe2f3;">4. Firmware versions</span><br/>
<span style="background-color: #cfe2f3;">6. Toggle GPIO line (For mode change).</span><br/>
<span style="background-color: #cfe2f3;">4</span><br/>
<span style="background-color: #cfe2f3;">NanoBoot 1.1</span><br/>
<b style="background-color: #cfe2f3;">Firmware version info: &nbsp;01 10 01 00 23 93</b><br/>
<br/>
Testando o endereço MAC de 64-bit do CC1180<br/>
<br/>
<span style="background-color: #cfe2f3;">Select packet type:</span><br/>
<span style="background-color: #cfe2f3;">0. Check mac address (sanity check)</span><br/>
<span style="background-color: #cfe2f3;">1. Write binary ENCRYPTED_CC1180_AP_FW.hex</span><br/>
<span style="background-color: #cfe2f3;">2. Set MAC address.</span><br/>
<span style="background-color: #cfe2f3;">3. Switch to application mode</span><br/>
<span style="background-color: #cfe2f3;">4. Firmware versions</span><br/>
<span style="background-color: #cfe2f3;">6. Toggle GPIO line (For mode change).</span><br/>
<span style="background-color: #cfe2f3;">0</span><br/>
<span style="background-color: #cfe2f3;">HW address bytes: ff:ff:ff:ff:ff:ff:ff:ff</span><br/>
<br/>
Endereço ff:ff:ff:ff:ff:ff:ff:ff é inválido / broadcast / reversado, vamos criar um com o tradicional 1,2,3,4,5,6,7,8<br/>
<br/>
<span style="background-color: #cfe2f3;">Select packet type:</span><br/>
<span style="background-color: #cfe2f3;">0. Check mac address (sanity check)</span><br/>
<span style="background-color: #cfe2f3;">1. Write binary ENCRYPTED_CC1180_AP_FW.hex</span><br/>
<span style="background-color: #cfe2f3;">2. Set MAC address.</span><br/>
<span style="background-color: #cfe2f3;">3. Switch to application mode</span><br/>
<span style="background-color: #cfe2f3;">4. Firmware versions</span><br/>
<span style="background-color: #cfe2f3;">6. Toggle GPIO line (For mode change).</span><br/>
<span style="background-color: #cfe2f3;">2</span><br/>
<span style="background-color: #cfe2f3;">MAC address in hex format (8 bytes):</span><br/>
<span style="background-color: #cfe2f3;">byte 1: 1</span><br/>
<span style="background-color: #cfe2f3;">byte 2: 2</span><br/>
<span style="background-color: #cfe2f3;">byte 3: 3</span><br/>
<span style="background-color: #cfe2f3;">byte 4: 4</span><br/>
<span style="background-color: #cfe2f3;">byte 5: 5</span><br/>
<span style="background-color: #cfe2f3;">byte 6: 6</span><br/>
<span style="background-color: #cfe2f3;">byte 7: 7</span><br/>
<span style="background-color: #cfe2f3;">byte 8: 8</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">given MAC address:</span><br/>
<span style="background-color: #cfe2f3;">01:02:03:04:05:06:07:08:</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">HW address bytes: 01:02:03:04:05:06:07:08</span><br/>
<div>
<br/></div>
Pronto agora o CC1180, já tem firmware e MAC válidos para montar um rede 6lowpan.<br/>
Então vamos dar outro pipoco (rode o script um.sh que foi criado anteriormente) no GPIO do OMAP para que o CC1180 entre em modo aplicativo,<br/>
ou seja, os leds agora devem ficar piscando.<br/>
<br/>
Apos rodar o script um.sh, os leds do CC1180 vão começar a piscar juntos, de 5 em 5 segundos.<br/>
É sinal que o CC1180 está em modo aplicativo, mas que ninguém está comandando ele.<br/>
Na verdade esse pisca pisca, segundo a documentação da sensinode é o tempo que o watchdog leva para resetar o CC1180 se nenhum comando de controle for recebido.<br/>
<br/>
Hora de finalmente rodar o nanorouter para começar a formar a rede 6lowpan.<br/>
<br/>
<br/>
<span style="background-color: #cfe2f3;">root@da850-omapl138-evm:~/last# ./nanorouter</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">NanoRouter 2.0 - 6routed v2.0</span><br/>
<span style="background-color: #cfe2f3;">------------STARTING CONFIGURATION SERVER Version: 2.0------------</span><br/>
<span style="background-color: #cfe2f3;">------------STARTING 6ROUTED Version: 2.0------------</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: cannot bind port number 50005</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: binding port number 50006</span><br/>
<span style="background-color: #cfe2f3;">ConfSv::handshake - trying a new port: 50005</span><br/>
<span style="background-color: #cfe2f3;">ConfSv::handshake - trying a new port: 50006</span><br/>
<span style="background-color: #cfe2f3;">ConfSv::handshake - trying a new port: 50007</span><br/>
<span style="background-color: #cfe2f3;">Configuration::constructor- handshake done!</span><br/>
<span style="background-color: #cfe2f3;">New get address got: 2001:0000:0000:0000:0000:0000:0000:0011</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
<span style="background-color: #cfe2f3;">Core::read_config - create Ethernet interface by default</span><br/>
<span style="background-color: #cfe2f3;">Ethernet::Device /dev/net/tun opened successfully</span><br/>
<span style="background-color: #cfe2f3;">Ethernet::Failed an ioctl() call on virtual interface fd</span><br/>
<span style="background-color: #cfe2f3;">Ethernet::Could not open virtual network interface to communicate with the kernel</span><br/>
<span style="background-color: #cfe2f3;">Bailing out</span><br/>
<span style="background-color: #cfe2f3;">ConfSv::handshake - done!</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: cannot bind port number 50004</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: cannot bind port number 50005</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: cannot bind port number 50006</span><br/>
<span style="background-color: #cfe2f3;">Server::socket_server_set_params: binding port number 50007</span><br/>
<div>
<br/></div>
Agora, nanorouter está pronto para ser configurado e controlador pelo nodeview<br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/nodeview-2.0.zip">http://www.sensinode.com/media/ti-cc-6lowpan/nodeview-2.0.zip</a><br/>
<br/>
Extrai e execute o nodeview, e adicione o IPv6 do OMAP.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-pa6SSFmWikE/UyTGTv5gOTI/AAAAAAAApSk/3yU0lZwz7HI/s1600/nodeview-add-nanorouter.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="247" src="http://3.bp.blogspot.com/-pa6SSFmWikE/UyTGTv5gOTI/AAAAAAAApSk/3yU0lZwz7HI/s1600/nodeview-add-nanorouter.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Adicionando IPv6 do OMAP ao NodeView</td></tr>
</tbody></table>
<br/>
Depois de adicionado, é hora de criar uma interface, configurar a rede, frequência,....<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-Fd9rlj3Np1E/UyTHFwOgq0I/AAAAAAAApSs/cxtxwJQPenE/s1600/nodeview-show-interfaces.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="227" src="http://2.bp.blogspot.com/-Fd9rlj3Np1E/UyTHFwOgq0I/AAAAAAAApSs/cxtxwJQPenE/s1600/nodeview-show-interfaces.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">NodeView -&gt; show interfaces para listar as interfaces configuradas do roteador</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-SrXI1mltgA4/UyTJtGIZwII/AAAAAAAApS4/sOPx0ieS8pc/s1600/nodeview-create-interface.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="395" src="http://4.bp.blogspot.com/-SrXI1mltgA4/UyTJtGIZwII/AAAAAAAApS4/sOPx0ieS8pc/s1600/nodeview-create-interface.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Configurando a interface para 915MHz,<br/>
26MHz o cristal do CC1101 que fica dentro do CC1180,<br/>
Date rate 50Kbs<br/>
Channel space 200KHz,<br/>
PATABLE do CC1101 = C2 (1mW)<br/>
<br/></td></tr>
</tbody></table>
Depois de configurada a interface o CC1180 do OMAP vai ficar com o led verde acesso direto, o led vermelho vai piscar quando houver dados trafegando na rede.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-dF3HI8FOv_8/UyTUEJHB_3I/AAAAAAAApTs/Ao8ESaIi7Es/s1600/IMG_20140315_192755.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-dF3HI8FOv_8/UyTUEJHB_3I/AAAAAAAApTs/Ao8ESaIi7Es/s1600/IMG_20140315_192755.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC1180 do OMAP depois de configurada a interface de rede pelo NodeView</td></tr>
</tbody></table>
<br/>
Agora precisamos adicionar os dispositivos de rede,<br/>
os módulos são de dois tipos:<br/>
1) CC430 (soc de msp430&nbsp;+ CC1101),<br/>
2) MSP430 com cc1180 (cc1110f32).<br/>
<br/>
O código para o CC430 (F5137) pode ser baixado da página da sensinode<br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/cc430f5137-library-model.zip">http://www.sensinode.com/media/ti-cc-6lowpan/cc430f5137-library-model.zip</a><br/>
<br/>
Depois de extraído as únicas modificações necessárias são ajustas o MAC e a frequência e potência<br/>
<br/>
<span style="background-color: #cfe2f3;">//MAC</span><br/>
<span style="background-color: #cfe2f3;">__root __code const uint8_t hard_coded_mac[8] @ 0xff70 = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x42, 0x25};</span><br/>
<div>
<span style="background-color: #cfe2f3;"><br/></span></div>
<div>
<div>
<span style="background-color: #cfe2f3;">//default settings for RF interface</span></div>
<div>
<span style="background-color: #cfe2f3;">static rf_conf_settings_t rf_configurations = {</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; DATA_RATE_200,&nbsp;</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; CHANNEL_SPACING_200,&nbsp;</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; MODULATION_INDEX_10,&nbsp;</span></div>
<div>
<span style="background-color: #cfe2f3;">// &nbsp;0x21,0x65,0x6A, //868mhz smartrf freq2,freq1,freq0</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; 0x23,0x31,0x3b, //915mhz smartrf studio freq2,freq1,freq0</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; 0xc3, //smart studio rf PATABLE 10dbm cc430</span></div>
<div>
<span style="background-color: #cfe2f3;">&nbsp; RX_ATTENUATION_0dbm};</span></div>
</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-x0GwzSlzNPI/UyUDYsRfNWI/AAAAAAAApUY/XUBNGEBEOyo/s1600/cc430-smart-studio-rf-915mhz.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="317" src="http://1.bp.blogspot.com/-x0GwzSlzNPI/UyUDYsRfNWI/AAAAAAAApUY/XUBNGEBEOyo/s1600/cc430-smart-studio-rf-915mhz.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">SmartRF Studio - janela do CC430 configurado para 915MHz</td></tr>
</tbody></table>
<div>
Depois é só compilar com o IAR para MSP430, e gravar com o MSP430 Debug-interface.</div>
<div>
<br/></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-VW7Q3XT285g/UyTS7iTWS_I/AAAAAAAApTU/g78wM8wDWbw/s1600/IMG_20140315_192221.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-VW7Q3XT285g/UyTS7iTWS_I/AAAAAAAApTU/g78wM8wDWbw/s1600/IMG_20140315_192221.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Gravando o CC430 com o MSP430 Debug Interface</td></tr>
</tbody></table>
O Led do CC430 fica piscando vermelho quando está procurando o access point da rede 6LowPAN.<br/>
Quando conecta fica verde.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-NjGffLu4Cyo/UyUqIu5nSVI/AAAAAAAApVY/6OWKMSHzgS4/s1600/IMG_20140316_003734.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-NjGffLu4Cyo/UyUqIu5nSVI/AAAAAAAApVY/6OWKMSHzgS4/s1600/IMG_20140316_003734.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">CC430 conectado ao OMAP&nbsp;+ CC1180 com sucesso!</td></tr>
</tbody></table>
<br/>
<div class="separator" style="clear: both; text-align: center;">
</div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-XBVfpA4XTZ8/UyUqSY2KP_I/AAAAAAAApVg/PxiWiNmm_Hg/s1600/IMG_20140316_005431.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-XBVfpA4XTZ8/UyUqSY2KP_I/AAAAAAAApVg/PxiWiNmm_Hg/s1600/IMG_20140316_005431.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Cada placa deve ter um endereço MAC diferente,<br/>
que é justamente a configuração feita no main.C<br/>
<span style="background-color: #cfe2f3; font-size: xx-small; text-align: start;">__root __code const uint8_t hard_coded_mac[8] @ 0xff70 = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x42, 0x25}</span></td></tr>
</tbody></table>
Ainda resta os módulos MSP430 (F5438A - 16K RAM 256K FLASH)&nbsp;+ CC1180, para entrar na rede 6lowpan.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-CXJt7Bo-FnI/UyU3b2JZqwI/AAAAAAAApWI/-OsAnB4rNAE/s1600/IMG_20140316_023125.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-CXJt7Bo-FnI/UyU3b2JZqwI/AAAAAAAApWI/-OsAnB4rNAE/s1600/IMG_20140316_023125.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Módulos MSP430F5438A&nbsp;+ CC1180 915 MHz</td></tr>
</tbody></table>
<br/>
No caso desses módulos é preciso fazer a mesma coisa que foi feita com o CC1180 do OMAP, mas desta vez usando o firmware CC1180-NWP, que pode ser baixado daqui:<br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/encrypted_cc1180_nwp.zip">http://www.sensinode.com/media/ti-cc-6lowpan/encrypted_cc1180_nwp.zip</a><br/>
<div>
Para estes módulos o código fonte do exemplo para entrar na rede 6LowPAN é baixado daqui:</div>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/nanohost-example-1.0.zip">http://www.sensinode.com/media/ti-cc-6lowpan/nanohost-example-1.0.zip</a><br/>
<a href="http://www.sensinode.com/media/ti-cc-6lowpan/napsocket-library-1.0.zip">http://www.sensinode.com/media/ti-cc-6lowpan/napsocket-library-1.0.zip</a><br/>
É preciso fazer o merge dos arquivos e configurações desses 2 exemplos,<br/>
como é muito coisa para explicar, já disponibilizei o código pronto no meu github,<br/>
<a href="https://github.com/murix/6lowpan-MSP430F5138A-CC1180">https://github.com/murix/6lowpan-MSP430F5138A-CC1180</a><br/>
No caso os endereços MAC desses módulos são gravados do mesmo jeito do OMAP, usando o nanoboot_host como foi feito anteriormente.<br/>
<br/>
Depois de alguns experimentos, os módulos MSP430F5138A-CC1180 não entraram na &nbsp;rede, provavelmente pode ser a antena na PCB que é para 868 MHz, depois com mais tempo verifico melhor.<br/>
<br/>
Vamos olhar no nodeview como ficou a rede depois de todo o trabalho.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-QsBlBmuo36E/UyU63Zyv_-I/AAAAAAAApWY/JrzfUj09nYg/s1600/nodeview-4-cc430-list.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="181" src="http://2.bp.blogspot.com/-QsBlBmuo36E/UyU63Zyv_-I/AAAAAAAApWY/JrzfUj09nYg/s1600/nodeview-4-cc430-list.JPG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Quando o nodeview é aberto / detecta um módulo pela primeira vez,<br/>
é enviado o pacote de configuração para ajustar a velocidade de atualização do nodeview.</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-UWp_eDYLiGg/UyU7SC4I6rI/AAAAAAAApWg/s4EYQvdtGQ4/s1600/nodeview-4-cc430-map.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="204" src="http://3.bp.blogspot.com/-UWp_eDYLiGg/UyU7SC4I6rI/AAAAAAAApWg/s4EYQvdtGQ4/s1600/nodeview-4-cc430-map.JPG" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A melhor coisa do 6lowpan é que o roteamento em mesh funciona, <br/>
ou seja, pacotes de dados podem dar vários saltos.</td></tr>
</tbody></table>
Também é possível copiar o IPv6 de qualquer módulo do nodeview, e pingar direto do windows ou linux.<br/>
Se houver mais serviço de rede nos módulos, todos poderão ser acessos diretamente no IPv6 do módulo de destino.<br/>
<br/>
Toda a rede roda encima do CC1180 (CC1110F32), um 8051 com 4K de RAM e 32K de FLASH junto com o CC1101 / CC110L. Ou CC430F5137, um MSP430 com 4K de RAM e 32K de FLASH.<br/>
Ou seja, o footprint de uma rede 6lowpan otimizada, é de 4K de RAM e 32K de FLASH.<br/>
Sendo assim, qualquer coisa com especificação parecida como PIC18F, PIC16, AVR, ARM Cortex-M0,.... junto com um rádio pode fazer o mesmo, é só instalar o Contiki-OS.<br/>
<br/>
<br/>
<br/></div>