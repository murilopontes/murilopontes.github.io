---
layout: post
title: Conexão automática e persistente em roteadores WiFi que voam (drones)
categories:
 - post
date: 2014-01-10 21:53:00 +0000
---

Hoje vamos falar sobre conexões automáticas em redes WiFi.  

<div>
E como fazer isso&nbsp;programaticamente em C# / .net</div>

<div>
<div>
<br/>
<a name="more"></a><br/></div>
<div>
Em primeiro lugar é preciso baixar a biblioteca "simplewifi",</div>
<div>
o download por ser feito aqui: https://github.com/DigiExam/simplewifi</div>
<div>
e depois usar esse o snippet abaixo, fazendo as modificações para suas necessidades.<br/>
<br/></div>
<div>
<script src="https://gist.github.com/murix/8363286.js"></script>
</div>
<div>
<br/></div>
<div>
<br/>
<br/>
Como exemplo completo, disponibilizei um projeto de exemplo no <b>Codeplex</b> para fazer a conexão automática com a rede WiFi do ardrone. Assim que o Ardrone é ligado e o WiFi começa a anunciar seu SSID, o programa encontra a rede do ardrone e conecta nela. Além disso, o programa também monitora o tempo de viagem de ida e volta (round trip time - RTT) do ping até ardrone e plota no gráfico.<br/>
<br/>
<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-eXvsEQQ8cXc/UtBmZP7paGI/AAAAAAAAoKk/8puFCCvvmBA/s1600/drone-shot.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="263" src="http://2.bp.blogspot.com/-eXvsEQQ8cXc/UtBmZP7paGI/AAAAAAAAoKk/8puFCCvvmBA/s1600/drone-shot.PNG" width="400"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Projeto completo disponível em<br/>
<span style="font-size: medium; text-align: start;"><b><a href="https://droneconnect.codeplex.com/">https://droneconnect.codeplex.com/</a></b></span></td></tr>
</tbody></table>
<br/>
<br/>
<br/>
<br/>
<br/></div>
</div>