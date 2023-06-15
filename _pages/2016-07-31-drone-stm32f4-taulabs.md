---
layout: page
title: Drone- STM32F4 Taulabs
categories:
 - page
date: 2016-07-31 19:52:00 +0100
---

Baseado no autopilot Taulabs  

<https://github.com/TauLabs/TauLabs/wiki/Creating-a-FlyingF4-from-scratch>  

  

PCB dupla face montada com placa de expansão da STM32F4 Discovery  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://2.bp.blogspot.com/-J5qqsLADHVA/VWstHKto_bI/AAAAAAABI-k/O7C0nj9xAlM/s1600/IMG_20150531_124606.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="https://2.bp.blogspot.com/-J5qqsLADHVA/VWstHKto_bI/AAAAAAABI-k/O7C0nj9xAlM/s320/IMG_20150531_124606.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 12.8000001907349px;">STM32F4 almost ready<br/>
I2C: GY-86 10DOF (MPU6050, HMC5883, MS5611)<br/>
UART2: GY-GPS6MV1 (Ublox Neo-6M)<br/>
UART3: ESP8266 / ESP-01 (WiFi AP with transparent serial over TCP for Ground Station)<br/>
Receiver is Frsky D8R-II Plus<br/>
Transmitter is Frsky Taranis Plus<br/>
Two turnigy MX-M80l servos for camera stabization</td></tr>
</tbody></table>

### 

### 

### Pinout para montagem do Flying F4

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-Kz1FhGvOTew/VXQftSJl_XI/AAAAAAABJO0/uw-f7BqcKHI/s1600/flyingf4-pinout-x8r-apm.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="248" src="https://4.bp.blogspot.com/-Kz1FhGvOTew/VXQftSJl_XI/AAAAAAABJO0/uw-f7BqcKHI/s400/flyingf4-pinout-x8r-apm.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;"><span style="font-size: 12.8000001907349px;">STM32F4 Discovery pinout for Taulabs Flying F4</span></td></tr>
</tbody></table>

  

### 

### FPV

O kit FPV é composto pelo:  

- Transmissor Boscam TS351 de 5.8 GHz&nbsp;+ Camera CDD Sony&nbsp;cxd3172ar  

- Receptor Boscam RC305 de 5.8 GHz&nbsp;+ TV Sony  

- Dois servos Turnigy MX-M801  

### 

### 

### Flying F4 ADC &nbsp;/ battery monitor

Conectar a saida V do APM PM no pino PC1  

Conectar a saida I do APM PM no pino PC2  

Ativar o "Battery monitor" pelo GCS  

Reiniciar o FlyingF4  

Calibrar o monitor com ajuda de um multímetro.  

  

O monitor pode ser acessado usando:  

- na telemetria do GCS se uma Uart estiver configurar como "Telemetry"&nbsp;+ ESP01 WiFi Serial.  

- na telemetria do Taranis com D8RII se uma Uart estiver configurada como FrSky Sensor Hub  

- na telemetria do Taranis com X8R se uma Uart estiver configurada como FrSky SPort Telemetry  

### 

### Usando as portas analógicas do D8R-II-Plus

  

A telemetria da bateria também pode ser feita usando as entradas analógicas do D8R-II.  

O "APM Power Module" deve ser conectado nas portas A0 e A1 do receptor D8R para medir corrente e tensão.  

<div>
<br/></div>

### 

### Usando o CPPM do D8R-II-Plus

- Conectar os canais 7 e 8 para entrada no modo de programação  

- Conectar um cabo USB FDTI com RX e TX invertidos na port UART do D8R-II-Plus  

- Gravar o <a href="http://www.frsky-rc.com/download/view.php?sort=&amp;down=10&amp;file=D8R-XP_CPPM_27ms" target="_blank">firmware CPPM 27ms do D8R-XP</a>  

- Depois de gravado remover o conexão entra os canais 7 e 8, e fazer uma entre os canais 3,4  

- Agora o canal 1 é o CPPM de 27ms e o canal 2 é o RSSI.  

  

### 

### Usando a Telemetria UART do D8R-II-Plus

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-FICFOC3AwCo/VW6BhgeLwoI/AAAAAAABJD0/gvHqbeHiJyg/s1600/flyingf4-frsky-sensor-hub-inverter.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="307" src="https://3.bp.blogspot.com/-FICFOC3AwCo/VW6BhgeLwoI/AAAAAAABJD0/gvHqbeHiJyg/s400/flyingf4-frsky-sensor-hub-inverter.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Required inverter to emulate FrSky Sensor Hub<br/>
Telemetry is working perfectly in my tests</td></tr>
</tbody></table>

0) inverter o sinal do TX gerado pela FlyingF4 para conectar no RX do D8R.  

1) configurar a porta como Frsky Sensor Hub  

2) em Modules ativar o Frsky Sensor Hub  

3) fazer o reboot para começar a receber a telemetria no Taranis  

  

Dados que são recebidos pelo Taranis:  

1) altitude (variable 'Alt')  

2) temperatures (from baro and from accelerometer, variables 'T1' and 'T2')  

3) x, y and z acceleration (variables 'AccX', 'AccY' and 'AccZ')  

4) current, voltage and cell voltages (if battery module is enabled, variables 'Curr' and 'Cels')  

5) gps data (if gps module has a fix, variable 'GPS Alt' latitude, longitude)  

  

  

### Usando o SBUS do X8R

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-1-B-MJb7Vq0/VW5rRs5uF8I/AAAAAAABJDk/7Da6GpOz9O4/s1600/flyingf4-sbus-inverter.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="307" src="https://2.bp.blogspot.com/-1-B-MJb7Vq0/VW5rRs5uF8I/AAAAAAABJDk/7Da6GpOz9O4/s400/flyingf4-sbus-inverter.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Required Sbus inverter to use UART1 as Sbus input.<br/>
Set Taranis to D16 mode and channel to 1-16.<br/>
All 16 channels from X8R sbus work perfectly in my tests.</td></tr>
</tbody></table>

  

### 

### Usando a&nbsp;Telemetria&nbsp;&nbsp;Smart Port do X8R

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-nxLq2qQjY5Q/VXQx7mXd68I/AAAAAAABJPE/7I1K35pRT0A/s1600/smart-port-inverter.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="186" src="https://1.bp.blogspot.com/-nxLq2qQjY5Q/VXQx7mXd68I/AAAAAAABJPE/7I1K35pRT0A/s400/smart-port-inverter.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">FrSky Smart Port inverter</td></tr>
</tbody></table>

  

  

  

  