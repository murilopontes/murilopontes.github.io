---
layout: post
title: Level shift 3,3V 5V bidirecional
categories:
 - 2N4401
date: 2014-04-04 02:01:00 +0100
---

Para misturar hardware de diferentes tensões é necessário utilizar circuitos de level shift.  

  

<a name="more"></a>  
  

Na página do Arduino existe um esquema para ligar lógica de 3V3 em 5V.  

http://www.hagtech.com/pdf/iic.pdf  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-nqGCXxy6Xfg/Uz4CR-zGo5I/AAAAAAAAp20/VNCyvttLCZs/s1600/i2c-level-shifter-transistors.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="262" src="http://2.bp.blogspot.com/-nqGCXxy6Xfg/Uz4CR-zGo5I/AAAAAAAAp20/VNCyvttLCZs/s1600/i2c-level-shifter-transistors.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Level shift de baixo custo e fácil de encontrar .</td></tr>
</tbody></table>

Os resistores devem ser maiores que 4,7k para manter a conformidade com a especificação I2C.  

Para outras aplicações os resistores mais externos (pull-ups do I2C) não são necessários.  

Os transistores podem ser trocados por qualquer um desses:  

2N2222  

2N3904  

PN100  

2N4401  

BC337  

BC546  

As tensões das lógicas também podem ser modificadas, não precisa ficar preso em 3V3 e 5V.