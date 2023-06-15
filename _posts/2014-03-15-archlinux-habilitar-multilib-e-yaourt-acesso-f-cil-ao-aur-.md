---
layout: post
title: archlinux habilitar multilib e yaourt (acesso fácil ao AUR)
categories:
 - post
date: 2014-03-15 15:18:00 +0000
---

Abrir o arquivo /etc/pacman.conf  

Descomentar essas linhas (remove o #)  

  

<a name="more"></a>  
  

[multilib]  

Include = /etc/pacman.d/mirrorlist  

<div>
<br/></div>

<div>
Adicionar esses linhas abaixo do trecho descomentado do multilib<br/>
<br/>
<br/></div>

<div>
<span style="background-color: #cfe2f3;">[archlinuxfr]</span><br/>
<span style="background-color: #cfe2f3;">SigLevel = Never</span><br/>
<span style="background-color: #cfe2f3;">Server = http://repo.archlinux.fr/$arch</span></div>

<div>
<br/></div>

  
Atualizar a lista de pacotes  

<div>
<br/></div>

<div>
pacman -Sy</div>

<div>
<br/></div>

<div>
Instalar o yaourt</div>

<div>
<br/></div>

<div>
pacman -S yaourt</div>

<div>
<br/></div>

<div>
Agora você tem acesso fácil a instalar pacotes do AUR com o yaourt do mesmo jeito que faz com o pacman.</div>

<div>
<br/>
<div>
<br/></div>
</div>