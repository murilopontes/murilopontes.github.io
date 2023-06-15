---
layout: post
title: Método agressivo de instalar todos os pacotes do archlinux em uma linha
categories:
 - Instalar todos pacotes
date: 2013-10-16 12:40:00 +0100
---

for x in $(pacman -Sg &amp;&amp; pacman -Ssq); do pacman --noconfirm --needed --force -S $x ; done