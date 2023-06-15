---
layout: post
title: git server / sparkleshare
categories:
 - post
date: 2013-11-17 15:27:00 +0000
---

tutorial completo  

<a name="more"></a>  

  

__<span style="font-size: large;">Servidor</span>__  

1) nova VM (Vmware, virtualbox ou qemu)  

2) boot pelo Archlinux (o mais recente)  

3) fdisk /dev/sda , o, n,enter,enter,enter,w,enter  

4) mkfs.ext4 /dev/sda1  

5) mount /dev/sda1 /mnt  

6) pacstrap /mnt base grub openssh lxde xorg networkmanager network-manager-applet firefox git net-tools  

7) arch-chroot /mnt  

8) systemctl enable lxdm  

9) systemctl enable sshd  

10) systemctl enable NetworkManager  

<div>
11) password root</div>

<div>
12) ssh-keygen</div>

<div>
13) cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys</div>

<div>
14) grub-mkconfig -o /boot/grub/grub.cfg</div>

<div>
15) grub-install /dev/sda<br/>
16) mkdir /root/backup-git<br/>
17) cd /root/backup-git<br/>
18) git init --bare</div>

<div>
19) control+d</div>

<div>
20) reboot</div>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-F6XyJpa-0As/UnFwhKq1sMI/AAAAAAAAm4Q/n7DDdzxca1o/s1600/git-server.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-F6XyJpa-0As/UnFwhKq1sMI/AAAAAAAAm4Q/n7DDdzxca1o/s320/git-server.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Servidor git rodando no IP 192.168.1.129</td></tr>
</tbody></table>
Cliente - Sparkleshare<br/>
1) instalar WinSCP<br/>
2) instalar Sparkleshare<br/>
3) icone do sparkleshare no systray -&gt; menu sparkleshare -&gt; client id -&gt; copy to clipboard<br/>
4) abrir winscp no 192.168.1.129&nbsp;do servidor git e colar o client id no fim do /root/.ssh/authorized_keys<br/>
5) icone do sparkleshare no systray -&gt; menu sparkleshare -&gt; add host project<br/>
6) "my own server" ssh://root@192.168.1.129 &nbsp;/root/backup-git<br/>
7) fim<br/>
<br/>
<br/></div>