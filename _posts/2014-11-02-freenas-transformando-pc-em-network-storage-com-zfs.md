---
layout: post
title: FreeNAS transformando PC em network storage com ZFS
categories:
 - post
date: 2014-11-02 19:15:00 +0000
---

Com o <a href="http://www.freenas.org/" target="_blank">FreeNAS </a>&nbsp;dá para transformar qualquer PC em&nbsp;network storage com ZFS.  

  

<a name="more"></a>  

A única coisa que precisa é um pendrive de 4gb/8gb para instalar o sistema de gerenciamento.  

Primeiro é preciso baixa a versão downloads para 32 e 64 bits, dependendo do PC.  

<http://download.freenas.org/9.2.1.8/RELEASE/x86/FreeNAS-9.2.1.8-RELEASE-x86.img.xz>  

<http://download.freenas.org/9.2.1.8/RELEASE/x64/FreeNAS-9.2.1.8-RELEASE-x64.img.xz>  

Para instalar no pendrive  

xzcat FreeNAS-9.2.1.8-RELEASE-x86.img.xz &gt; /dev/sdx  

Configura na bios para o PC ficar sempre ligado e com boot pelo usb.  

Dá primeira vez que liga demora uns 10 minutos para completar o boot, depois é rápido.  

Abrir o navegador em http://freenas.lan, configurar a senha, e fazer as outras configurações no painel administrativo.  

  

Dá para compartilhar os arquivos com CIFS (para windows), NFS (para linux) e APF (para macos).  

Tem também uma shell web, ssh e muito mais coisa.  

  

Tem como testar a velocidade dos discos.  

Se o disco for muito lento é melhor trocar.  

  

Testando um HD de 1,5TB SATA2  

[root@freenas] ~# diskinfo -t /dev/ada0  

/dev/ada0  

&nbsp; &nbsp; &nbsp; &nbsp; 512 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # sectorsize  

&nbsp; &nbsp; &nbsp; &nbsp; 1500301910016 &nbsp; # mediasize in bytes (1.4T)  

&nbsp; &nbsp; &nbsp; &nbsp; 2930277168 &nbsp; &nbsp; &nbsp;# mediasize in sectors  

&nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # stripesize  

&nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # stripeoffset  

&nbsp; &nbsp; &nbsp; &nbsp; 2907021 &nbsp; &nbsp; &nbsp; &nbsp; # Cylinders according to firmware.  

&nbsp; &nbsp; &nbsp; &nbsp; 16 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Heads according to firmware.  

&nbsp; &nbsp; &nbsp; &nbsp; 63 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Sectors according to firmware.  

&nbsp; &nbsp; &nbsp; &nbsp; S240J50Z507260 &nbsp;# Disk ident.  

  

Seek times:  

&nbsp; &nbsp; &nbsp; &nbsp; Full stroke: &nbsp; &nbsp; &nbsp;250 iter in &nbsp; 5.906169 sec = &nbsp; 23.625 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Half stroke: &nbsp; &nbsp; &nbsp;250 iter in &nbsp; 4.522182 sec = &nbsp; 18.089 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Quarter stroke: &nbsp; 500 iter in &nbsp; 7.660322 sec = &nbsp; 15.321 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Short forward: &nbsp; &nbsp;400 iter in &nbsp; 3.741322 sec = &nbsp; &nbsp;9.353 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Short backward: &nbsp; 400 iter in &nbsp; 3.068722 sec = &nbsp; &nbsp;7.672 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Seq outer: &nbsp; &nbsp; &nbsp; 2048 iter in &nbsp; 0.241615 sec = &nbsp; &nbsp;0.118 msec  

&nbsp; &nbsp; &nbsp; &nbsp; Seq inner: &nbsp; &nbsp; &nbsp; 2048 iter in &nbsp; 0.241997 sec = &nbsp; &nbsp;0.118 msec  

Transfer rates:  

&nbsp; &nbsp; &nbsp; &nbsp; outside: &nbsp; &nbsp; &nbsp; 102400 kbytes in &nbsp; 0.937724 sec = &nbsp; 109201 kbytes/sec  

&nbsp; &nbsp; &nbsp; &nbsp; middle: &nbsp; &nbsp; &nbsp; &nbsp;102400 kbytes in &nbsp; 1.089443 sec = &nbsp; &nbsp;93993 kbytes/sec  

&nbsp; &nbsp; &nbsp; &nbsp; inside: &nbsp; &nbsp; &nbsp; &nbsp;102400 kbytes in &nbsp; 1.977842 sec = &nbsp; &nbsp;51774 kbytes/sec  

  

[root@freenas] ~#  

<div>
<br/>
Testando um pendrive de 4GB USB2<br/>
[root@freenas] ~# diskinfo -t /dev/da0<br/>
/dev/da0<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 512 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # sectorsize<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 4047503360 &nbsp; &nbsp; &nbsp;# mediasize in bytes (3.8G)<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 7905280 &nbsp; &nbsp; &nbsp; &nbsp; # mediasize in sectors<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # stripesize<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # stripeoffset<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 492 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Cylinders according to firmware.<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 255 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Heads according to firmware.<br/>
&nbsp; &nbsp; &nbsp; &nbsp; 63 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Sectors according to firmware.<br/>
&nbsp; &nbsp; &nbsp; &nbsp; B04F5FBB52AFDC44 &nbsp; &nbsp; &nbsp; &nbsp;# Disk ident.<br/>
<br/>
Seek times:<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Full stroke: &nbsp; &nbsp; &nbsp;250 iter in &nbsp; 0.527853 sec = &nbsp; &nbsp;2.111 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Half stroke: &nbsp; &nbsp; &nbsp;250 iter in &nbsp; 0.929037 sec = &nbsp; &nbsp;3.716 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Quarter stroke: &nbsp; 500 iter in &nbsp; 1.760160 sec = &nbsp; &nbsp;3.520 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Short forward: &nbsp; &nbsp;400 iter in &nbsp; 0.222976 sec = &nbsp; &nbsp;0.557 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Short backward: &nbsp; 400 iter in &nbsp; 0.220846 sec = &nbsp; &nbsp;0.552 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Seq outer: &nbsp; &nbsp; &nbsp; 2048 iter in &nbsp; 1.151830 sec = &nbsp; &nbsp;0.562 msec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; Seq inner: &nbsp; &nbsp; &nbsp; 2048 iter in &nbsp; 1.216756 sec = &nbsp; &nbsp;0.594 msec<br/>
Transfer rates:<br/>
&nbsp; &nbsp; &nbsp; &nbsp; outside: &nbsp; &nbsp; &nbsp; 102400 kbytes in &nbsp; 6.249961 sec = &nbsp; &nbsp;16384 kbytes/sec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; middle: &nbsp; &nbsp; &nbsp; &nbsp;102400 kbytes in &nbsp; 6.009538 sec = &nbsp; &nbsp;17040 kbytes/sec<br/>
&nbsp; &nbsp; &nbsp; &nbsp; inside: &nbsp; &nbsp; &nbsp; &nbsp;102400 kbytes in &nbsp; 6.047922 sec = &nbsp; &nbsp;16931 kbytes/sec<br/>
<br/>
O pendrive tem seek time um pouco maior que um SSD, mesmo assim ainda é muito melhor que os 23 ms do HD, O problema do pendrive é a taxa de taxa transferência que fica em torno dos 16mb/s.<br/>
Em USB 2.0 o máximo seria 480mbit ou 60mbytes/s. Eficiência de 26% apenas.<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>