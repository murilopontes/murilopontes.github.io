---
layout: post
title: Configurando Fedora 19
categories:
 - post
date: 2013-11-17 15:30:00 +0000
---

Usando Fedora 19 como ponto de partida

<div>
<a name="more"></a><br/><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-A_MZwnShKCY/UltPOU6SViI/AAAAAAAAmiw/LIhgDQkB4oE/s1600/Captura+de+tela+-+13-10-2013+-+22:54:42.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="225" src="http://3.bp.blogspot.com/-A_MZwnShKCY/UltPOU6SViI/AAAAAAAAmiw/LIhgDQkB4oE/s400/Captura+de+tela+-+13-10-2013+-+22:54:42.png" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Meu desktop atual no Fedora</td></tr>
</tbody></table>
<br/>
<br/>
#instalar o Live CD do Fedora com XFCE<br/>
<br/>
#conectar na internet e......<br/>
<br/>
#logar de root<br/>
<br/>
#atualizar tudo para última versão<br/>
yum -y update<br/>
<br/>
#instalar o google chrome , clique em download,&nbsp;<span style="background-color: white; color: #333333; font-family: 'Open Sans', arial, sans-serif; font-size: 13px; line-height: 18px;">&nbsp;</span><span style="background-color: white; color: #333333; font-family: 'Open Sans', arial, sans-serif; font-size: 13px; line-height: 18px;">64 bit .rpm (Para Fedora/openSUSE)</span><br/>
<a href="http://www.google.com/intl/pt-BR/chrome/">http://www.google.com/intl/pt-BR/chrome/</a><br/>
<br/>
# para os apressados vai de wget<br/>
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm<br/>
<br/>
#instalar o rpm do google chrome<br/>
yum install google-chrome-stable_current_x86_64.rpm<br/>
<br/>
#instalar o java para o banco do brasil e caixa econômica<br/>
yum -y install icedtea-web<br/>
<br/>
#instalar o firefox<br/>
yum -y install firefox<br/>
<br/>
#baixar e instalar o flashplugin<br/>
wget http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm<br/>
yum -y install adobe-release-x86_64-1.0-1.noarch.rpm<br/>
<br/>
#baixar e instalar o acrobat<br/>
<br/>
wget http://ardownload.adobe.com/pub/adobe/reader/unix/8.x/8.1.7/ptb/AdobeReader_ptb-8.1.7-1.i486.rpm<br/>
<br/>
wget http://ardownload.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/enu/AdbeRdr9.5.5-1_i486linux_enu.rpm<br/>
<br/>
yum -y install AdbeRdr9.5.5-1_i486linux_enu.rpm<br/>
<br/>
#instalar o "mc" e "gkrellm"<br/>
yum -y install mc gkrellm<br/>
<br/>
#ativar ssh<br/>
systemctl enable sshd<br/>
systemctl start sshd<br/>
<br/>
#configurar fuso-horário<br/>
timedatectl set-timezone America/Recife<br/>
<br/>
#configurar nuvem privada<br/>
yum -y install owncloud<br/>
<br/>
#o apache do fedora vem bloqueado para acesso externo, tem de liberar no firewall<br/>
systemctl enable httpd<br/>
systemctl start httpd<br/>
<br/>
#remove por completo o firewall do fedora<br/>
systemctl stop firewalld.service<br/>
systemctl disable firewalld.service<br/>
<br/>
#ferramentas para mariadb<br/>
yum -y install phpmyadmin<br/>
<br/>
<br/>
#compiladores<br/>
yum -y install gcc kernel-devel<br/>
<br/>
#vmware player<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>