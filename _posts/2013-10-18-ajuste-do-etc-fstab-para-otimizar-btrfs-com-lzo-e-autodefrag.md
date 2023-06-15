---
layout: post
title: Ajuste do /etc/fstab para otimizar BTRFS com LZO e autodefrag
categories:
 - post
date: 2013-10-18 15:08:00 +0100
---

Editar /etc/fstab assim:  

<blockquote class="tr_bq">
/dev/sdxx / btrfs rw,relatime,compress=lzo,space_cache,autodefrag 0 0</blockquote>

Com compress=lzo a velocidade média fica cerca de 3x maior.  

  

Com autodefrag, toda vez que um pasta ou arquivo estiver causando muitos seeks e lerdeza o defrag é disparado.