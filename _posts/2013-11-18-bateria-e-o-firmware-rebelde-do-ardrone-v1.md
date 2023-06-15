---
layout: post
title: Bateria e o firmware rebelde do Ardrone v1
categories:
 - DirectX
date: 2013-11-18 16:43:00 +0000
---

Testando bateria e controle do ardrone com software alternativo  

  

<a name="more"></a>  
  

  

Parte 1 - Antes de começar o teste  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-0rIr286gajk/Uoo3RQ-iJ1I/AAAAAAAAnOs/YbqU_O6OkR8/s1600/IMG_20131117_170620.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-0rIr286gajk/Uoo3RQ-iJ1I/AAAAAAAAnOs/YbqU_O6OkR8/s320/IMG_20131117_170620.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Antes de dar a partida, a bateria que ficou 2 dias carregada e sem uso já perdeu 0,25V<br/>
Pelo aplicativo do Android isso corresponde a 80% da bateria</td></tr>
</tbody></table>

  

Parte 2 - Depois de 1 minuto voando  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-M1zQCm5RNhg/Uoo34ELbrfI/AAAAAAAAnO8/0K89eXO_mi8/s1600/IMG_20131117_171226.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-M1zQCm5RNhg/Uoo34ELbrfI/AAAAAAAAnO8/0K89eXO_mi8/s320/IMG_20131117_171226.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ligou, subiu e menos de 2 minutos saiu de 80% para 0%.<br/>
Ok, desligado. Como dá para ver de praticamente não consumiu nada.<br/>
Colocando a bateria denovo dá 60% pelo aplicativo do Android.</td></tr>
</tbody></table>

Parte 3 - Testando com o cliente em C#/WPF, o monitorando de voltagem está ok 11,xx V. Então resolvi entrar no Drone via telnet, e para minha surpresa, a memória flash estava 100% usada. O problema eram videos gravados na flash interna. Depois de excluir todos ficou assim.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-DOd4X4YQXKw/Uoo7HMmIBiI/AAAAAAAAnPI/EZvxvnwIxc4/s1600/drone-telnet.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="403" src="http://3.bp.blogspot.com/-DOd4X4YQXKw/Uoo7HMmIBiI/AAAAAAAAnPI/EZvxvnwIxc4/s640/drone-telnet.PNG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pelo jeito a flash do ardrone usa o UBIFS, tem 128M de RAM e 128MB.<br/>
(Micron MT29F1G08AAC)</td></tr>
</tbody></table>

Creating 5 MTD partitions on "nand0":  

0x00000000-0x00040000 : "Pbootloader" -&gt; 256kbytes  

0x00040000-0x00840000 : "Pmain_boot" -&gt; 8 mbytes  

0x00840000-0x01040000 : "Pfactory" -&gt; 8 mbytes  

0x01040000-0x02040000 : "Psystem" -&gt; 16 mbytes  

0x02040000-0x08000000 : "Pupdate" -&gt; 95 mbytes&nbsp;+ 768kbytes  

<div>
<br/></div>

<div>
<div>
# cat /proc/mounts</div>
<div>
rootfs / rootfs rw 0 0</div>
<div>
ubi1:system / ubifs rw 0 0</div>
<div>
tmp /tmp tmpfs rw 0 0</div>
<div>
proc /proc proc rw 0 0</div>
<div>
dev /dev tmpfs rw 0 0</div>
<div>
devpts /dev/pts devpts rw,mode=600 0 0</div>
<div>
sys /sys sysfs rw 0 0</div>
<div>
ubi0:factory /factory ubifs ro 0 0</div>
<div>
ubi2:update /update ubifs rw,sync 0 0</div>
<div>
ubi2:data /data ubifs rw 0 0</div>
<div>
#</div>
</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-NBjohHmRBwA/Uoo_V9zA9fI/AAAAAAAAnPU/F0wRH0Xbi7E/s1600/drone-vbat_min.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://4.bp.blogspot.com/-NBjohHmRBwA/Uoo_V9zA9fI/AAAAAAAAnPU/F0wRH0Xbi7E/s400/drone-vbat_min.png" width="323"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O vbat_min está configurado para 9V.... mas parece que não está sendo usado como deveria</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-ySPFRpImI-Q/UopBwAP9cgI/AAAAAAAAnPs/BfgRAJxqQ3c/s1600/IMG_20131118_133401.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://2.bp.blogspot.com/-ySPFRpImI-Q/UopBwAP9cgI/AAAAAAAAnPs/BfgRAJxqQ3c/s320/IMG_20131118_133401.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esse bug tá de sacanagem a bateria em 11,25V envia para aplicação 4%</td></tr>
</tbody></table>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-K226Uk0OcJs/UopCFobsrFI/AAAAAAAAnP0/S3RL7InU_F8/s1600/drone.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="288" src="http://1.bp.blogspot.com/-K226Uk0OcJs/UopCFobsrFI/AAAAAAAAnP0/S3RL7InU_F8/s400/drone.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Bug 38% é 11,38V</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-3Wu1y2-UAMk/UopCGNvcQKI/AAAAAAAAnP4/sbGwARPAzZI/s1600/drone_4_porcento.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="288" src="http://3.bp.blogspot.com/-3Wu1y2-UAMk/UopCGNvcQKI/AAAAAAAAnP4/sbGwARPAzZI/s400/drone_4_porcento.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Bug 4% é 11,25V</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;">&nbsp;<a href="http://2.bp.blogspot.com/-S8cADal1AXA/UopDTqHtPdI/AAAAAAAAnQM/XmAsN3L8JHY/s1600/drone-versao-bugada.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="355" src="http://2.bp.blogspot.com/-S8cADal1AXA/UopDTqHtPdI/AAAAAAAAnQM/XmAsN3L8JHY/s400/drone-versao-bugada.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A versão de SW bugada é a 1.11.5</td></tr>
</tbody></table>

  

__Update 12/03/2014:__  

  

[ Software de controle do Ardrone em C# com suporte a controle do Xbox 360 ]  

https://github.com/shtejv/ARDrone-Control-.NET  

  

Para compilar o ARDrone-Control-.NET é preciso ter:  

* Visual Studio 2010 (ou 2013) &nbsp;;  

* DirectX SDK Jun/2010.  

  

[ DirectX SDK Jun / 2010 ]  

http://www.microsoft.com/en-us/download/details.aspx?id=6812  

  

  

Configuração testada:  

* Windows 8.1 64bits;  

* Visual Studio 2013;  

* DirectX SDK jun/2010;  

* Controle Xbox 360 usb.  

  

  

  

  