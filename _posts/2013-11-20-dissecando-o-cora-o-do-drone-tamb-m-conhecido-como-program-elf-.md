---
layout: post
title: Dissecando o coração do drone, também conhecido como "program.elf" 
categories:
 - Linux
date: 2013-11-20 14:01:00 +0000
---

Mais um post na série de depuração do ardrone v1, após conectar no access point wifi criado pelo drone, é possível fazer abrir uma conexão telnet no drone (ip=192.168.1.1). Como já sabemos, o ardrone é um Linux embarcado que voa.  

<a name="more"></a> Logo praticamente toda mágica que faz ele voar está implementada em um único programa, que neste caso é o "program.elf" que está rodando com PID 971, segundo a lista de processo abaixo. O "program.elf" é executado durante o boot do Linux pois está no scripts de inicialização do sistema.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-OfLxcF7RAfI/Uoyxiz8Lq9I/AAAAAAAAnXI/cw77NhLdN90/s1600/drone-processos.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://3.bp.blogspot.com/-OfLxcF7RAfI/Uoyxiz8Lq9I/AAAAAAAAnXI/cw77NhLdN90/s640/drone-processos.PNG" width="416"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">"program.elf" em execução no pid 971</td></tr>
</tbody></table>

<div class="separator" style="clear: both; text-align: justify;">
Ok, então como podemos observar tudo gira em torno desse "program.elf". Portanto, vamos dissecá-lo para entender melhor o seu funcionamento. O Linux embarcado é a mesma coisa das versões de desktop, o kernel é exatamente o mesmo de desktop recompilado para ARM, e o "userspace" é o busybox, junto com scripts e drivers específicos da placa. Praticamente todos os sensores podem ser acessados pelos arquivos de dispositivos encontrados dentro do /dev. O que torna o desenvolvimento muito mais fácil, já que basta ficar lendo e escrevendo nos/dos arquivos certos dentro do /dev. Outra boa facilidade são os recursos de threads e concorrência oferecidos pelo Linux / libc / pthread (POSIX threads) &nbsp;que são idênticos aos encontrados no Linux para desktop, permitindo desenvolver e testar tudo no PC, para depois recompilar para ARM e enviar para a placa (na verdade não é tão simples assim, existe detalhes específicos da plataforma ARM como alinhamento de memória e outros que só resolve executando nativamente para depurar). Agora que já foi introduzido o ambiente em que o "program.elf" é executado, vamos ver a execução do mesmo.</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
Antes de executar o "program.elf" novamente é preciso matá-lo antes com o comando "kill -9 971". Caso ele esteja com outro PID no "ps w" é só mudar o 971 pelo PID que estiver aparecendo no seu console de telnet.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
Para executar novamente, basta chamar pelo "program.elf" &nbsp;a qualquer momento, como ele está na pasta /bin e portanto no path de comando do sistema, não haverá problemas e nem linhas de comandos exóticas.</div>

<div class="separator" style="clear: both; text-align: justify;">
Abaixo vemos o "program.elf" inicializando e testando as versões dos motores (que até onde pude verificar, parecem usar comunicação i2c do linux para o atmega8 que é o microcontrolador usado no ESC). Além disso são inicializadas as 2 câmeras (i2c), a placa de navegação (sonar/pic24f e o giroscópio/IDG500), e os ADCs para medir tensão e corrente de diversos pontos do HW e bateria.&nbsp;</div>

<div class="separator" style="clear: both; text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: justify;">
[depois vou colocar o "buspirate 3.6" para investigar o protocolo de comunicação entre o linux e o atmega8 (reprogramável / miniatura do Arduino) do ESC. ]</div>

<div class="separator" style="clear: both; text-align: center;">
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-xKgtApRKXyE/UoyzvHY2-6I/AAAAAAAAnXU/fOY8yaCIdvE/s1600/drone-program.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="572" src="http://2.bp.blogspot.com/-xKgtApRKXyE/UoyzvHY2-6I/AAAAAAAAnXU/fOY8yaCIdvE/s640/drone-program.png" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">"program.elf" verificando os sensores e câmeras do sistema.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-oXzyJH-7hlU/Uoy5jWbWBiI/AAAAAAAAnXk/uoUnGoTlwGM/s1600/drone-bug-vbat.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="556" src="http://3.bp.blogspot.com/-oXzyJH-7hlU/Uoy5jWbWBiI/AAAAAAAAnXk/uoUnGoTlwGM/s640/drone-bug-vbat.PNG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Após alguns segundo de execução o "program.elf" começa a implicar com a bateria,<br/>
mas não só com a bateria, com a fonte de PC também, logo o podemos deduzir que problema não é dá bateria,<br/>
e sim do "program.elf" que está medindo algo do jeito errado, ou seja, um bug.<br/>
A versão desse "program.elf" que está rodando é o 1.11.5.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-83mkbuO-S8g/Uoy6Z9pmPlI/AAAAAAAAnXs/1FLN-OwWTeA/s1600/drone-self-kill-vbat-bug.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="92" src="http://1.bp.blogspot.com/-83mkbuO-S8g/Uoy6Z9pmPlI/AAAAAAAAnXs/1FLN-OwWTeA/s640/drone-self-kill-vbat-bug.PNG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esse bug cabuloso da versão 1.11.5, fica enviando sinal de pouso de emergência mesmo usando a fonte de PC com energia infinita!!! &nbsp;&nbsp;</td></tr>
</tbody></table>

  

Nos próximos posts, irei mostrar como executar uma alternativa open-source para substituir o "program.elf", e que permite controlar cada um dos componentes do drone individualmente, ou seja, tem como testar cada motor individualmente ou em conjunto, placa de navegação e tudo mais. Além de implementar uma nova lógica de controle de estabilização do drone, permitindo até fazer os flips, piruetas e acrobacias 3D. E controlar o drone usando controle de Xbox 360 a partir do PC / Notebook.  

  

Para finalizar, segue abaixo o log completo da saída do "program.elf" em texto plano.  

  

#  

# program.elf  

posix init start build on : Aug 20 2012 14:37:42  

Use ctrl+\ (SIGQUIT) to end the application  

plog drop: thread RT_THRESHOLD=19, SUP_THREAD_MINPRIORITY=31  

plog drop: RR time quantum 0s 10000000ns  

plog drop: thread guard size : default 4096  

plog drop: thread guard size : set to 65536  

plog drop: thread stack size : default 32768, minimal 16384, (system default 8388608)  

plog drop: disable smp  

**  

** Mykonos v1.11.5 &nbsp;built for Hardware 11  

** Build Aug 20 2012 14:52:04  

**  

tid=0x10b5a0, [I] POS: thread starting "Button Monitor" got 0x402bd490 native id  

tid=0x10b350, [I] POS: thread starting "sup log" got 0x40318490 native id  

tid=(nil), [E] POS: register : /dev/input/event0  

tid=(nil), [E] POS: we register 1  

init button  

** ADC hard_version : c0  

0.182339 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp;adc device (soft 0x40046, hard 0xc0) loaded  

0.196621 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 262214 &nbsp;adc device updater status file created  

0.210377 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 772299 &nbsp;adc device updater status file deleted  

0.212195 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 -1098700976 &nbsp;Scanning /data/custom.configs/applis ...  

0.215729 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp; located configuration file   

0.218972 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp; located configuration file   

0.219895 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp;Scanning /data/custom.configs/profiles ...  

0.224305 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp; located configuration file   

0.225156 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp;Scanning /data/custom.configs/sessions ...  

0.231437 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp; located configuration file   

Motors flight anim. callback : &lt;0&gt;<!--0--><!--0--><!--0-->  

Setting WiFi rate to auto  

Owner's MAC address is: 00:00:00:00:00:00  

Clearing pairing rule  

Owner's MAC address is: 00:00:00:00:00:00  

Clearing pairing rule  

Motors leds callback : &lt;0&gt;<!--0--><!--0--><!--0-->  

Userbox state callback : &lt;0&gt;<!--0--><!--0--><!--0-->  

State : 0  

0.542294 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 1668184435 &nbsp;SW VERSION : 00113D68  

0.543821 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 1668184435 &nbsp;Configuring the vertical video pipeline ...  

0.544687 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 543821 &nbsp;Configuring the horizontal video pipeline ...  

0.545791 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 1718513475 &nbsp;Could not open BLC.hex file.  

0.597545 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 0 &nbsp;BLC backup hex available  

0.620289 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC call for motor 1  

0.732537 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC motor 1 soft version 1.43, hard version 3.0, supplier 1.1, lot number 11/10, FVT1 05/01/11  

0.790281 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC call for motor 2  

0.902515 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC motor 2 soft version 1.43, hard version 3.0, supplier 1.1, lot number 11/10, FVT1 05/01/11  

0.960282 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC call for motor 3  

1.072541 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC motor 3 soft version 1.43, hard version 3.0, supplier 1.1, lot number 11/10, FVT1 06/01/11  

1.130467 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC call for motor 4  

1.242518 NULL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 892613943 &nbsp;BLC motor 4 soft version 1.43, hard version 3.0, supplier 1.1, lot number 11/10, FVT1 07/01/11  

Starting thread Master  

tid=0x1480dc, [I] POS: thread starting "Master" got 0x40332490 native id  

Starting thread Acquisition  

tid=0x148138, [I] POS: thread starting "Acquisition" got 0x4034c490 native id  

Starting thread V4Lcamif  

tid=0x148194, [I] POS: thread starting "V4Lcamif" got 0x40362490 native id  

Starting thread V4Lcamif  

tid=0x1481f0, [I] POS: thread starting "V4Lcamif" got 0x40378490 native id  

Starting thread Navdata  

tid=0x14824c, [I] POS: thread starting "Navdata" got 0x40392490 native id  

Starting thread vp_com_server  

tid=(nil), [W] POS: vp_com_server : stack size 8192 is too small, setting to 16384  

tid=0x1482a8, [I] POS: thread starting "vp_com_server" got 0x403a8490 native id  

Starting thread ATCmdServer  

tid=0x148304, [I] POS: thread starting "ATCmdServer" got 0x403c2490 native id  

Starting thread FlashMgr  

tid=0x148360, [I] POS: thread starting "FlashMgr" got 0x403dc490 native id  

Starting thread vbat  

tid=0x1483bc, [I] POS: thread starting "vbat" got 0x403f6490 native id  

Starting thread Video  

tid=0x148418, [I] POS: thread starting "Video" got 0x40410490 native id  

Starting thread Video_Hori  

tid=0x148474, [I] POS: thread starting "Video_Hori" got 0x4042a490 native id  

Starting thread Leds  

tid=0x1484d0, [I] POS: thread starting "Leds" got 0x40444490 native id  

Starting thread ImageBox  

tid=0x14852c, [I] POS: thread starting "ImageBox" got 0x4045e490 native id  

tid=(nil), [W] POS: disable smp  

thread start  

Thread AT Commands Server Start  

1.337714 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Mykonos configuration saved.  

tid=0x10b350, [I] log: starting  

1.541467 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Unable to load trims because file /data/fact_trims.bin is missing  

1.554083 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Unable to load trims because file /data/trims.bin is missing  

1.565681 Acquisition &nbsp; &nbsp;6 1482 &nbsp;Calibration request  

1.566619 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Mykonos Accs Infos loaded from /data/fact_accs_infos.bin: val(0) = 31.261818; val(1) = 76.368988; val(2) = -1016.875732  

<starting info="">Version="AR.Drone 1.11.5" WIFI="OK" AddrMAC="00:26:7E:62:DB:A3" Calibration="DEFAULT" PICVersion="4.70" Motor1Version="1.43" Motor2Version="1.43" Motor3Version="1.43" Motor4Version="1.43"</starting>

  

1.569034 Acquisition &nbsp; &nbsp;6 1482 &nbsp;change the ultrasound frequency. 25Hz  

1.570774 Acquisition &nbsp; &nbsp;6 1482 &nbsp;syslog switches to buffer 1 (0x000FBEE8)  

1.570690 Acquisition &nbsp; &nbsp;6 1482 &nbsp;change the ultrasound frequency. 25Hz  

1.581957 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Mykonos Accs Infos loaded from /data/accs_infos.bin: val(0) = 90.915741; val(1) = -18.565979; val(2) = -1016.159668  

1.603352 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Mykonos configuration saved.  

1.617712 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Beginning syslog dump in flash  

1.618710 FlashMgr &nbsp; &nbsp; &nbsp; 6 1488 &nbsp;Syslog dump in flash done  

tid=0x1480dc, [I] POS: thread "Master" stack usage -1%  

tid=0x1480dc, [I] POS: thread "Master" exited  

2.211181 Acquisition &nbsp; &nbsp;6 1482 &nbsp;GAINS AT : pq_kp = 40000, r_kp = 200000, r_ki = 3000, ea_kp = 9000, ea_ki = 8000, alt_kp = 3000, alt_ki = 400, vz_kp = 200, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; vz_ki = 100, hov_kp = 8000, hov_ki = 8000, hov_b_kp = 1200, hov_b_ki = 500  

2.431739 Acquisition &nbsp; &nbsp;6 1482 &nbsp;GAINS AT : pq_kp = 40000, r_kp = 200000, r_ki = 3000, ea_kp = 9000, ea_ki = 8000, alt_kp = 3000, alt_ki = 400, vz_kp = 200, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; vz_ki = 100, hov_kp = 8000, hov_ki = 8000, hov_b_kp = 1200, hov_b_ki = 500  

camera configured  

4.116301 Video &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;6 1490 &nbsp;Opening device Vertical camera (/dev/video1) with resolution 176x144 and pixel format YU12  

TAG_TYPE_COCKPIT 480  

4.155146 Video &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;6 1490 &nbsp;Camera Config : Setting the cresyn camera into default mode  

7.723848 Video_Hori &nbsp; &nbsp; 6 1491 &nbsp;Opening device Horizontal camera (/dev/video0) with resolution 640x480 and pixel format YU12  

video_utils_init unknown codec 0  

TAG_TYPE_COCKPIT 480  

TAG_TYPE_COCKPIT 480  

dct status 0x0  

9.248981 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING *********  

12.265384 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING KILLED *********  

16.287392 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING *********  

20.309354 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING KILLED *********  

33.381706 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING *********  

38.409263 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING KILLED *********  

42.431519 Acquisition &nbsp; &nbsp;6 1482 &nbsp; ********* &nbsp; VBAT LOW WARNING *********  

<div>
<br/></div>

  