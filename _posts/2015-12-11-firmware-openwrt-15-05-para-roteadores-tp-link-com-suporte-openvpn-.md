---
layout: post
title: Firmware Openwrt-15.05 para roteadores TP-Link com suporte OpenVPN 
categories:
 - Linux
date: 2015-12-11 15:50:00 +0000
---

A imagem padrão disponível no site do Openwrt-15.05 não tem suporte ao OpenVPN, que pode ser instalado pelo gerenciador de pacotes 'opkg', mas devido a limitada memória flash de 4MB de grande maioria dos modelos, a instalação do Openvpn falha por falta de espaço. Mas se a imagem for feita com carinho com o OpenVPN já embutido durante a compilação vai funcionar nos limitados modelos low-cost de 4MB. A quem interessar disponibilizei essas imagens com OpenVPN para modelos de 4MB, veja nos Downloads do blog, essa lista de arquivos:
 
<a href="https://bitbucket.org/murixteam/dronespersonalizados/downloads" target="_blank">DOWNLOAD</a>
  

>  openwrt-15.05-ar71xx-generic-tl-mr3020-v1-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-mr3220-v1-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-mr3220-v2-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-mr3420-v1-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-mr3420-v2-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-wr1043nd-v1-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-wr1043nd-v2-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-wr740n-v1-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-wr740n-v3-squashfs-factory.binopenwrt-15.05-ar71xx-generic-tl-wr740n-v4-squashfs-factory.bin