---
layout: post
title: ArchLinux instalado os 32GB em 6724 pacotes
categories:
 - post
date: 2014-10-18 01:13:00 +0100
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<br/>
# Quantos pacotes tem?<br/>
pacman -Ssq | wc -l<br/>
6724<br/>
<br/>
# Vamos baixar tudo?<br/>
sudo pacman -S $(pacman -Ssq) --needed --force --nodeps -w<br/>
<div>
Vamos ver, .... humm é só 32GB de download</div>
<div>
<br/></div>
<div>
# Vamos instalar tudo?</div>
<div>
sudo pacman -S $(pacman -Ssq)</div>
<div>
<br/></div>
<div>
E o mais incrível ainda não tem tudo que quero, mas já ajudou bastante.</div>
<div>
<br/></div>
<div>
</div>
</div>