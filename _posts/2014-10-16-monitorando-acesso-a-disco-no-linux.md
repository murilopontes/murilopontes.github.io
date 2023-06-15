---
layout: post
title: Monitorando acesso a disco no Linux
categories:
 - block_dump
date: 2014-10-16 16:53:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
No&nbsp;<a href="http://acassis.wordpress.com/2007/10/15/quem-est-usando-meu-hd/" target="_blank">blog do Alan</a>&nbsp;encontrei uma dica interessante para monitorar o acesso ao disco<br/>
<br/>
Para ativar<br/>
echo 1 &gt; /proc/sys/vm/block_dump<br/>
<br/>
para visualizar:<br/>
dmesg<br/>
[18761.145648] BrowserBlocking(4512): WRITE block 1536032 on sda5 (32 sectors)<br/>
[18761.145654] BrowserBlocking(4512): WRITE block 3633184 on sda5 (32 sectors)<br/>
[18761.180958] BrowserBlocking(4512): WRITE block 128 on sda5 (8 sectors)<br/>
[18761.200588] btrfs-delalloc-(8064): WRITE block 781894752 on sda5 (8 sectors)<br/>
[18761.200826] BrowserBlocking(4512): WRITE block 1536128 on sda5 (32 sectors)<br/>
[18761.200833] BrowserBlocking(4512): WRITE block 3633280 on sda5 (32 sectors)<br/>
[18761.200889] BrowserBlocking(4512): WRITE block 1536160 on sda5 (32 sectors)<br/>
<div>
<br/></div>
<div>
<br/></div>
</div>