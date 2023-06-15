---
layout: post
title: Controle de PS3 no Windows, Linux e Beaglebone
categories:
 - sixad
date: 2014-12-24 01:58:00 +0000
---

<div>
O SCP é um driver para controles do PS2, PS3, PS4 no Windows.&nbsp;</div>

<div>
É opensource e muito melhor que o Motionjoy.</div>

<div>
Os controles podem ser conectados por USB ou Bluetooth.</div>

<div>
Preparei um pacote com os fontes e os binários.<br/>
<div>
<br/>
<br/>
<a name="more"></a><br/><br/>
<br/></div>
<div>
Para instalar é só executar o&nbsp;ScpDriver.exe,</div>
<div>
Os controles irão aparece como controles nativos do Xbox.&nbsp;</div>
<div>
<br/></div>
<div>
<br/></div>
<div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-MMTq5-wsivU/VJjJOKGtyaI/AAAAAAAAuc0/vQbu_DnAYQA/s1600/scp-install.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="181" src="http://4.bp.blogspot.com/-MMTq5-wsivU/VJjJOKGtyaI/AAAAAAAAuc0/vQbu_DnAYQA/s1600/scp-install.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Instalador dos drivers e serviços SCP DS3</td></tr>
</tbody></table>
<br/>
Referências:<br/>
http://emulation-general.wikia.com/wiki/SCP_Driver_Package<br/>
http://forums.pcsx2.net/Thread-XInput-Wrapper-for-DS3-and-Play-com-USB-Dual-DS2-Controller<br/>
http://www.motioninjoy.com/<br/>
<br/>
<br/>
Na beaglebone com Debian 7.7, o caminho é usar um dongle USB Bluetooth,<br/>
existem vários genéricos de menos de 2 dólares com chip da CSR (Cambridge Silicon Radio)<br/>
<br/>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse# lsusb<br/>
Bus 001 Device 002: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)<br/>
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub<br/>
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub<br/>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse#<br/>
<br/>
Então é só pegar o endereço MAC do Dongle USB com hciconfig para configurar o controle usando o sixpair.<br/>
<div>
<br/></div>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse# hciconfig<br/>
hci0: &nbsp; Type: BR/EDR &nbsp;Bus: USB<br/>
&nbsp; &nbsp; &nbsp; &nbsp; BD Address: 00:15:83:07:D4:EF &nbsp;ACL MTU: 310:10 &nbsp;SCO MTU: 64:8<br/>
&nbsp; &nbsp; &nbsp; &nbsp; UP RUNNING PSCAN<br/>
&nbsp; &nbsp; &nbsp; &nbsp; RX bytes:1269 acl:0 sco:0 events:45 errors:0<br/>
&nbsp; &nbsp; &nbsp; &nbsp; TX bytes:446 acl:0 sco:0 commands:43 errors:0<br/>
<br/>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse#<br/>
<div>
<br/></div>
<div>
Usando o sixpair com o &nbsp;MAC do bluetooth</div>
<div>
<br/></div>
<div>
<div>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse# ./sixpair 00:15:83:07:D4:EF</div>
<div>
Current Bluetooth master: f8:2f:a8:42:53:39</div>
<div>
Setting master bd_addr to 00:15:83:07:d4:ef</div>
<div>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse#</div>
</div>
<div>
<br/></div>
<div>
Verificando se o sixpair configurou o MAC corretamente</div>
<div>
<br/></div>
<div>
<div>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse# ./sixpair</div>
<div>
Current Bluetooth master: 00:15:83:07:d4:ef</div>
<div>
Unable to retrieve local bd_addr from `hcitool dev`.</div>
<div>
Please enable Bluetooth or specify an address manually.</div>
<div>
root@beaglebone:~/beaglebonequadcopter/quad-eclipse#</div>
</div>
<div>
<br/></div>
<div>
apt-get install bluez-utils bluez-compat bluez-hcidump checkinstall libusb-dev libbluetooth-dev joystick</div>
<div>
<br/>
wget http://colocrossing.dl.sourceforge.net/project/qtsixa/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz<br/>
<br/></div>
<div>
root@beaglebone:~/QtSixA-1.5.1/sixad# make<br/>
mkdir -p bins<br/>
g++ -O2 -Wall -Wl,-Bsymbolic-functions sixad-bin.cpp bluetooth.cpp shared.cpp textfile.cpp -o bins/sixad-bin `pkg-config --cflags --libs bluez` -lpthread -fpermissive<br/>
sixad-bin.cpp: In function 'int main(int, char**)':<br/>
sixad-bin.cpp:84:20: warning: taking address of temporary [-fpermissive]<br/>
g++ -O2 -Wall -Wl,-Bsymbolic-functions sixad-sixaxis.cpp sixaxis.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-sixaxis -lpthread -lrt<br/>
g++ -O2 -Wall -Wl,-Bsymbolic-functions sixad-remote.cpp remote.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-remote -lrt<br/>
g++ -O2 -Wall -Wl,-Bsymbolic-functions sixad-raw.cpp sixaxis.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-raw<br/>
g++ -O2 -Wall -Wl,-Bsymbolic-functions sixad-3in1.cpp sixaxis.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-3in1</div>
<div>
<br/></div>
<div>
<br/></div>
<div>
mkdir -pv /var/lib/sixad/profiles<br/>
<br/>
root@beaglebone:~/QtSixA-1.5.1/sixad# checkinstall<br/>
<br/>
checkinstall 1.6.2, Copyright 2009 Felipe Eduardo Sanchez Diaz Duran<br/>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;This software is released under the GNU GPL.<br/>
<br/>
<br/>
The package documentation directory ./doc-pak does not exist.<br/>
Should I create a default set of package docs? &nbsp;[y]: n<br/>
<br/>
*****************************************<br/>
**** Debian package creation selected ***<br/>
*****************************************<br/>
<br/>
This package will be built according to these values:<br/>
<br/>
0 - &nbsp;Maintainer: [ root@beaglebone ]<br/>
1 - &nbsp;Summary: [ sixad ]<br/>
2 - &nbsp;Name: &nbsp; &nbsp;[ sixad ]<br/>
3 - &nbsp;Version: [ 20141224 ]<br/>
4 - &nbsp;Release: [ 1 ]<br/>
5 - &nbsp;License: [ GPL ]<br/>
6 - &nbsp;Group: &nbsp; [ checkinstall ]<br/>
7 - &nbsp;Architecture: [ armhf ]<br/>
8 - &nbsp;Source location: [ sixad ]<br/>
9 - &nbsp;Alternate source location: [ &nbsp;]<br/>
10 - Requires: [ &nbsp;]<br/>
11 - Provides: [ sixad ]<br/>
12 - Conflicts: [ &nbsp;]<br/>
13 - Replaces: [ &nbsp;]<br/>
<br/>
Enter a number to change any of them or press ENTER to continue:<br/>
<br/>
Installing with make install...<br/>
<br/>
========================= Installation results ===========================<br/>
install -d /etc/default/<br/>
install -d /etc/init.d/<br/>
install -d /etc/logrotate.d/<br/>
install -d /usr/bin/<br/>
install -d /usr/sbin/<br/>
install -d /var/lib/sixad/<br/>
install -d /var/lib/sixad/profiles/<br/>
install -m 644 sixad.default /etc/default/sixad<br/>
install -m 755 sixad.init /etc/init.d/sixad<br/>
install -m 644 sixad.log /etc/logrotate.d/sixad<br/>
install -m 755 sixad /usr/bin/<br/>
install -m 755 bins/sixad-bin /usr/sbin/<br/>
install -m 755 bins/sixad-sixaxis /usr/sbin/<br/>
install -m 755 bins/sixad-remote /usr/sbin/<br/>
install -m 755 bins/sixad-3in1 /usr/sbin/<br/>
install -m 755 bins/sixad-raw /usr/sbin/<br/>
install -m 755 sixad-dbus-blocker /usr/sbin/<br/>
Installation is Complete!<br/>
<br/>
======================== Installation successful ==========================<br/>
<br/>
Copying files to the temporary directory...OK<br/>
<br/>
Stripping ELF binaries and libraries...OK<br/>
<br/>
Compressing man pages...OK<br/>
<br/>
Building file list...OK<br/>
<br/>
Building Debian package...OK<br/>
<br/>
Installing Debian package...OK<br/>
<br/>
Erasing temporary files...OK<br/>
<br/>
Writing backup package...OK<br/>
OK<br/>
<br/>
Deleting temp dir...OK<br/>
<br/>
<br/>
**********************************************************************<br/>
<br/>
&nbsp;Done. The new package has been installed and saved to<br/>
<br/>
&nbsp;/root/QtSixA-1.5.1/sixad/sixad_20141224-1_armhf.deb<br/>
<br/>
&nbsp;You can remove it from your system anytime using:<br/>
<br/>
&nbsp; &nbsp; &nbsp; dpkg -r sixad<br/>
<br/>
**********************************************************************<br/>
<br/></div>
<div>
root@beaglebone:~/QtSixA-1.5.1/sixad# dpkg -L sixad<br/>
/.<br/>
/etc<br/>
/etc/default<br/>
/etc/default/sixad<br/>
/etc/init.d<br/>
/etc/init.d/sixad<br/>
/etc/logrotate.d<br/>
/etc/logrotate.d/sixad<br/>
/usr<br/>
/usr/sbin<br/>
/usr/sbin/sixad-dbus-blocker<br/>
/usr/sbin/sixad-remote<br/>
/usr/sbin/sixad-3in1<br/>
/usr/sbin/sixad-bin<br/>
/usr/sbin/sixad-raw<br/>
/usr/sbin/sixad-sixaxis<br/>
/usr/bin<br/>
/usr/bin/sixad</div>
<div>
<br/></div>
<div>
<br/></div>
<div>
<div>
root@beaglebone:~/QtSixA-1.5.1/sixad# sixad --start</div>
<div>
sixad-bin[1972]: started</div>
<div>
sixad-bin[1972]: sixad started, press the PS button now</div>
<div>
sixad-bin[1972]: unable to connect to sdp session</div>
<div>
sixad-bin[1972]: Connected Sony Computer Entertainment Wireless Controller (38:C0:96:5E:8C:74)</div>
</div>
<div>
<br/></div>
<div>
update-rc.d sixad defaults</div>
<div>
<br/></div>
<div>
<div>
root@beaglebone:~/QtSixA-1.5.1/sixad# /etc/init.d/sixad start</div>
<div>
[ ok ] Starting sixad (via systemctl): sixad.service.</div>
<div>
root@beaglebone:~/QtSixA-1.5.1/sixad#</div>
</div>
<div>
<br/></div>
<div>
<div>
[ &nbsp;907.328485] Bluetooth: HIDP (Human Interface Emulation) ver 1.2</div>
<div>
[ &nbsp;907.335550] Bluetooth: HIDP socket layer initialized</div>
<div>
[ &nbsp;917.768067] sony 0005:054C:0268.0001: Fixing up Sony Sixaxis report descriptor</div>
<div>
[ &nbsp;917.793477] sony 0005:054C:0268.0001: unknown main item tag 0x0</div>
<div>
[ &nbsp;917.814176] input: Sony Computer Entertainment Wireless Controller as /devices/ocp.3/47400000.usb/musb-hdrc.1.auto/usb1/1-1/1-1:1.0/bluetooth/hci0/hci0:42/input1</div>
<div>
[ &nbsp;917.852215] sony 0005:054C:0268.0001: input,hidraw0: BLUETOOTH HID v1.00 Joystick [Sony Computer Entertainment Wireless Controller] on 00:15:83:07:d4:ef</div>
<div>
root@beaglebone:~#</div>
</div>
<div>
<br/></div>
<div>
<div>
root@beaglebone:~# jstest /dev/input/js0</div>
<div>
Driver version is 2.1.0.</div>
<div>
Joystick (Sony Computer Entertainment Wireless Controller) has 27 axes (X, Y, Z, Rz, (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null), (null))</div>
<div>
and 19 buttons (Trigger, ThumbBtn, ThumbBtn2, TopBtn, TopBtn2, PinkieBtn, BaseBtn, BaseBtn2, BaseBtn3, BaseBtn4, BaseBtn5, BaseBtn6, BtnDead, BtnA, BtnB, BtnC, (null), (null), (null)).</div>
<div>
Testing ... (interrupt to exit)</div>
<div>
Axes: &nbsp;0: &nbsp; &nbsp; 0 &nbsp;1: &nbsp; &nbsp; 0 &nbsp;2: &nbsp; &nbsp; 0 &nbsp;3: &nbsp; &nbsp; 0 &nbsp;4: &nbsp; &nbsp; 0 &nbsp;5: &nbsp; &nbsp; 0 &nbsp;6: &nbsp; &nbsp; 0 &nbsp;7: &nbsp; &nbsp; 0 &nbsp;8: &nbsp; &nbsp; 0 &nbsp;9: &nbsp; &nbsp; 0 10: &nbsp; &nbsp; 0 11: &nbsp; &nbsp; 0 12: &nbsp; &nbsp; 0 13: &nbsp; &nbsp; 0 14: &nbsp; &nbsp; 0 15: &nbsp; &nbsp; 0 16: &nbsp; &nbsp; 0 17: &nbsp; &nbsp; 0 18: &nbsp; &nbsp; 0 19: &nbsp; &nbsp; 0 20: &nbsp; &nbsp; 0 21: &nbsp; &nbsp; 0&nbsp;&nbsp;22:-32767 23: &nbsp; &nbsp; 0 24: &nbsp; &nbsp; 0 25: -4256 26: &nbsp; &nbsp; 0 Buttons: &nbsp;0:off &nbsp;1:off &nbsp;2:off &nbsp;3:off &nbsp;4:off &nbsp;5:off &nbsp;6:off &nbsp;7:off &nbsp;8:off &nbsp;9:off 10:off 11:off 12:off 13:off 14:off 15:off 16:off 17:off 18:off&nbsp;</div>
</div>
<br/>
Muito interessante, praticamente todos os botões são analógicos, dá para pegar a pressão de cada um deles. Também tem um acelerômetro e os 2 motores de feedback.<br/>
<br/></div>
</div>