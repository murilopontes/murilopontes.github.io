---
layout: post
title: ESP8266 ESP-01 esptool.py no Linux
categories:
 - post
date: 2015-04-25 23:21:00 +0100
---

  

A primeira ferramenta para o ESP-01 no Linux é o esptool.py.   

No esptool dá para fazer a manutenção completa do ESP-01  

  

root@murix-System-Product-Name:~/Downloads# wget <https://raw.githubusercontent.com/themadinventor/esptool/master/esptool.py>  

--2015-04-25 17:33:39--&nbsp; <https://raw.githubusercontent.com/themadinventor/esptool/master/esptool.py>  

Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.27.75.133  

Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.27.75.133|:443... connected.  

HTTP request sent, awaiting response... 200 OK  

Length: 23964 (23K) [text/plain]  

Saving to: ‘esptool.py’  

  

100%[===============================================================================================================================&gt;] 23.964&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --.-K/s&nbsp;&nbsp; in 0,006s&nbsp;   

  

2015-04-25 17:33:40 (3,88 MB/s) - ‘esptool.py’ saved [23964/23964]  

  

root@murix-System-Product-Name:~/Downloads# chmod +x esptool.py   

  

  

  

root@murix-System-Product-Name:~/Downloads# ./esptool.py --port /dev/ttyUSB0 read_mac  

Connecting...  

MAC: 18:fe:34:9f:13:f3  

root@murix-System-Product-Name:~/Downloads#   

  

  

[https://github.com/nodemcu/nodemcu-firmware/releases/tag/0.9.6-dev\_20150406](https://github.com/nodemcu/nodemcu-firmware/releases/tag/0.9.6-dev_20150406)  

  

root@murix-System-Product-Name:~/Downloads# ./esptool.py --port /dev/ttyUSB0 write_flash 0x0 nodemcu_integer_0.9.6-dev_20150406.bin   

Connecting...  

Erasing flash...  

Writing at 0x00066400... (100 %)  

  

Leaving...  

root@murix-System-Product-Name:~/Downloads#   

  