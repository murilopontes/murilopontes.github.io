---
layout: post
title: pipe view - usando dd com barra de progresso
categories:
 - post
date: 2015-04-19 19:00:00 +0100
---

Para ver o progresso de ferramentas como `dd`, apresento o `pv`.  

O pv (pipe view) mostra a quantidade e velocidade dos bytes que passam em um pipe.  

  

Muito simples de usar, basta passar o pv entre os pipes dos comandos.  

  

Exemplo com dd:   

root@murix:~/Downloads# dd if=archlinux-2015.04.01-dual.iso | pv | dd of=/dev/sdd bs=4M  

  

&nbsp;37MB 0:00:08 [17.1MB/s] [ &nbsp; &nbsp; &nbsp; &nbsp; &lt;=&gt; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;]  

  

  