---
layout: post
title: Criando uma imagem do Ubuntu 14.04 para BeagleBone Black
categories:
 - emmc
date: 2014-07-10 04:34:00 +0100
---

Instalando o Ubuntu 14.04 na beaglebone black pode trazer algumas facilidades para o desenvolvimento em geral.   

<a name="more"></a>São mais de 50 mil pacotes prontos para serem instalados via apt-get.  

Outra facilidade é que as versões das bibliotecas são as mesmas do Ubuntu Desktop, para o desenvolvedor testar diferentes builds de um mesmo software em hardwares sem precisar compilar também as bibliotecas do sistema é uma verdadeira mão roda, economia de tempo e dinheiro.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-NEP_mLBqKmQ/U74Ge2-KzBI/AAAAAAAAsVg/tCqGBwpxJ2k/s1600/IMG_20140710_001958.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-NEP_mLBqKmQ/U74Ge2-KzBI/AAAAAAAAsVg/tCqGBwpxJ2k/s1600/IMG_20140710_001958.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">BeagleBone Black com Ubuntu, debug na UART0 usando Buspirate</td></tr>
</tbody></table>

  

__Comandos no Ubuntu PC__  

  

# No ubuntu desktop instalar os pacotes para desenvolvimento  

<span style="background-color: #cfe2f3;">$ apt-get install dosfstools git-core kpartx u-boot-tools wget parte</span>  

  

# baixar do git os scripts para geração da imagem  

<span style="background-color: #cfe2f3;">$ git clone https://github.com/RobertCNelson/omap-image-builder</span>  

  

# criar o rootfs do Ubuntu Console usando os scripts  

<span style="background-color: #cfe2f3;">$ cd&nbsp;omap-image-builder</span>  

<span style="background-color: #cfe2f3;">$ ./RootStock-NG.sh -c rcn-ee\_console\_ubuntu\_stable\_armhf</span>  

  

# criar a imagem do cartão SD para gravar do eMMC  

<span style="background-color: #cfe2f3;">$ cd&nbsp;deploy/ubuntu-14.04-console-armhf-2014-07-09</span>  

<span style="background-color: #cfe2f3;">$ ./setup\_sdcard.sh --img-1gb sdcard-ubuntu --dtb beaglebone --beagleboard.org-production --bbb-flasher --boot\_label BBB\_BONE --rootfs\_label BBB\_FLASHER --offline</span>  

<div>
<br/></div>

<div>
# copiar a imagem gerada para o cartão SD físico (tempo médio de 3 minutos)</div>

<div>
<span style="background-color: #cfe2f3;">$ cat sdcard-ubuntu-1gb.img &gt; /dev/sdx</span><br/>
<br/>
# No Ubuntu Desktop habilite o roteamento da internet via USB, assim a Beablebone Black poderá instalar pacotes remoto diretamente via apt-get.<br/>
<span style="background-color: #cfe2f3;">$ sysctl -w net.ipv4.ip_forward=1</span><br/>
<span style="background-color: #cfe2f3;">$ iptables -t nat -A POSTROUTING -j MASQUERADE</span><br/>
<span style="background-color: #cfe2f3;"><br/></span>
# Ligar a beaglebone com o botão S2 pressionado junto com o SD preparado. Durante a cópia dos arquivos os leds D1,2,3,4 ficaram piscando como um barra de progresso. Ao fim do processo ficaram os quatro leds acessos. Então é só reiniciar sem o cartão SD e esperar na média 2 minutos para fazer login pelo ssh em 192.168.7.2 login=ubuntu senha=temppwd.<br/>
<span style="background-color: #cfe2f3;">$ ssh ubuntu@192.168.7.2</span><br/>
<br/>
<b>Comandos no SSH da BeagleBone Black</b><br/>
<br/>
# &nbsp;editar a configuração da rede usb</div>

<div>
<span style="background-color: #cfe2f3;">$ sudo nano /opt/scripts/boot/am335x_evm.sh&nbsp;</span></div>

<div>
# adicionar abaixo da linha ifconfig usb0 .... 192.168.7.2<br/>
route add default gw 192.168.7.1<br/>
<br/>
<span style="background-color: #cfe2f3;">$ sudo nano /etc/rc.local</span><br/>
# adicionar configuração do dns ao final do boot.<br/>
echo "nameserver 8.8.8.8" &gt; /etc/resolv.conf<br/>
<br/>
# reiniciar a beaglebone para entrar com a nova configuração de rede, que agora tem gateway e DNS.<br/>
<br/>
# atualizar a lista de pacotes<br/>
<span style="background-color: #cfe2f3;">$ apt-get update</span><br/>
<span style="background-color: #cfe2f3;">$ apt-get dist-upgrade</span><br/>
<br/>
# Até esse ponto estão usados 451mb e livres 1.2gb<br/>
<br/>
# instalar outros pacotes<br/>
<span style="background-color: #cfe2f3;">$ apt-get install -y aptitude mc ipython device-tree-compiler</span><br/>
<br/>
# talvez instalar os pacotes para transformar a Beaglebone Black em desktop<br/>
<span style="background-color: #cfe2f3;">$ apt-get install network-manager xrdp lxde strace firefox</span><br/>
<br/>
# pacotes de suporte para Adafruit BBIO<br/>
<span style="background-color: #cfe2f3;">$ apt-get install -y build-essential python-dev python-setuptools python-pip python-smbus</span><br/>
<br/>
# instalar Adafruit BBIO<br/>
<span style="background-color: #cfe2f3;">$pip install Adafruit_BBIO</span><br/>
<br/>
# desligar HDMI para liberar mais pinos de I/O<br/>
<span style="background-color: #cfe2f3;">echo optargs=quiet capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN &gt;&gt; /boot/uEnv.txt</span><br/>
<br/>
# depois de tudo pronto é fácil criar um instalador / replicador do sistema usando:<br/>
<span style="background-color: #cfe2f3;">$ /opt/scripts/tools/eMMC/beaglebone-black-make-microSD-flasher-from-eMMC.sh</span><br/>
<br/>
<br/>
<br/>
<br/>
<br/></div>