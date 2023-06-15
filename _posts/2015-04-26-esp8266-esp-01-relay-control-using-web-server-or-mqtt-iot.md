---
layout: post
title: ESP8266 ESP-01 relay control using Web server or MQTT / IOT
categories:
 - MQTT
date: 2015-04-26 14:05:00 +0100
---

Build with ESP8266 ESP-01 Arduino IDE (<https://github.com/esp8266/Arduino>)  

  

# turn off relay  

curl -X PUT http://eclipse.mqttbridge.com/murilo/esp/rele/off  

  

# turn on relay  

curl -X PUT&nbsp;http://eclipse.mqttbridge.com/murilo/esp/rele/on  

  

# control relay from Android  

https://play.google.com/store/apps/details?id=at.tripwire.mqtt.client&amp;hl=en  

publish murilo/esp/rele/on &nbsp; - turn on relay  

publish murilo/esp/rele/off &nbsp;- turn off relay  

<div>
<br/></div>

<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/u3nateL1Ar8" width="420"></iframe>

  

  

See source code...  

<a name="more"></a>  

<script src="https://gist.github.com/murix/992fd558180e56173105.js"></script>