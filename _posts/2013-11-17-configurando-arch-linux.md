---
layout: post
title: Configurando Arch Linux
categories:
 - post
date: 2013-11-17 15:21:00 +0000
---

Configurando o ArchLinux para desktop<a name="more"></a>

<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody></tbody></table>

  

  

<a href="http://4.bp.blogspot.com/-OU0yP_jw5ok/Ulu3Xf8lkhI/AAAAAAAAmjA/sh6H-9bIpoc/s1600/snapshot1.png" imageanchor="1" style="margin-left: auto; margin-right: auto;">

<img border="0" height="250" src="http://4.bp.blogspot.com/-OU0yP_jw5ok/Ulu3Xf8lkhI/AAAAAAAAmjA/sh6H-9bIpoc/s400/snapshot1.png" width="400"/>

</a>  

  

  

Meu desktop atual no Archlinux  

  

  

<pre></pre>

Instalação do archlinux  

  

fdisk /dev/sda  

o  

n  

p  

enter  

enter  

mkfs.btrfs /dev/sda1  

mount -o compress=lzo /dev/sda1 /mnt  

pacstrap /mnt base base-devel grub ntfs-3g os-prober net-tools xfce4 xorg hdparm smartmontools reflector  

genfstab /mnt &gt;&gt; /mnt/etc/fstab  

arch-chroot /mnt  

grub-mkconfig -o /boot/grub/grub.cfg  

grub-install /dev/sda  

ctrl+d  

reboot  

#gerar lista de mirrors otimizada  

<pre><pre>#reflector -l 50 -f 50 --verbose -c Brazil --save /etc/pacman.d/mirrorlist</pre>
</pre>

pacman -S net-tools &nbsp;kdebase xorg btrfs-progs  

pacman -S xorg-xinit xterm lxdm mc networkmanager network-manager-applet  

systemctl enable NetworkManager  

systemctl enable lxdm  

hdparm -tT /dev/sda  

partx -a /dev/sda  

reboot  

pacman -S firefox flashplugin icedtea-web-java7  

testar no firefox  

http://www.bb.com.br  

http://www.caixa.gov.br  

pacman -S gedit base-devel gnome-disk-utility gkrellm chromium openssh  

yaourt --noconfirm --needed --force -S aur/mkinitcpio-btrfs  

#remove pacote mazelado  

pacman -R openresolv  

#configura idioma e teclado  

localectl set-locale LANG=pt_BR.utf8  

localectl set-keymap br-abnt  

localectl set-x11-keymap br  

#desligar/remove pacote fcitx ; senão o teclado fica sem inglês  

  