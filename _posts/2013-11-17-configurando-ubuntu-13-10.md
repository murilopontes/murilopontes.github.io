---
layout: post
title: Configurando Ubuntu 13.10
categories:
 - post
date: 2013-11-17 15:31:00 +0000
---

Usando o kubuntu 13.10 como ponto de partida  

<a href="http://kubuntu.org/" target="_blank">http://kubuntu.org/</a>  

  

<a name="more"></a>  
  

Ubuntu  

*ativar o canal de software partner pelo "software-properties-gtk" na aba "outros programas"  

Kubuntu  

*ativar o canal de software partner pelo "software-properties-kde" na aba "outros programas"  

<div>
<br/></div>

#instalar o aptitude, que a interface de comando é tudo em um.  

sudo apt-get -y install aptitude  

  

#atualizar lista de pacotes  

sudo aptitude -y update  

  

#atualizar os pacotes  

sudo aptitude -y upgrade  

  

# gerenciadores de arquivos em console  

sudo aptitude -y install mc  

  

# monitores do sistema  

sudo aptitude -y&nbsp;gkrellm  

  

# nuvens privadas  

sudo aptitude -y&nbsp;owncloud owncloud-client  

  

# navegadores  

sudo aptitude -y&nbsp;chromium-browser  

  

# conferência / voip  

sudo aptitude -y&nbsp;skype  

  

# java  

sudo aptitude -y&nbsp;icedtea-7-plugin  

  

  

  

  

  

  

  

  