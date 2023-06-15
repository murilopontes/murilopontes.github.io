---
layout: post
title: MWC com tubos PVC
categories:
 - Mini Deans-T
date: 2013-11-23 03:16:00 +0000
---

Enquanto não chega o frame de fibra de carbono, uma alternativa barata (entenda-se menos de R$30) é fazer um frame totalmente de PVC usando tubulação para água.  

<a name="more"></a>  

Depois de rodar um bocado descobri que o nome do "PVC cross" aqui é "cruzeta".  

Juntando com cano e presilhas tem o resultado do vídeo abaixo onde testo o protótipo.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/iC1NVoL_PfE" width="420"></iframe>

  

  

  

  

Dependendo da orientação da placa do Arduíno, a lógica de controle apresentam 2 modelos básicos. principais. São eles configuração em "+" e "x". Abaixo estão as fotos de como ligar os motores no Arduino.  

No caso do Drone PVC foi usado o Arduino Nano V3.0.   

Os motores 3 e 9, giram no sentido horário com hélices 10x4.5 e motores ligados nas fases A B C do ESC. Os motores 10 e 11, giram no sentido anti-horário, com hélices 10x4.5R (reversa) e os motores ligado nas fases C B A (para girar ao contrário é só inverte 2 fases) do ESC.  

  

Para facilitar a montagem, coloquei conectores banana (bullet) macho de 3,5 mm nos motores.  

Por padrão da comunidade RC, os conectores dos motores sempre serão machos, e  

os conectores das fases A B C do ESC serão sempre fêmeas.  

No caso do Drone PVC tem um facilitador extra que é a capa plástica dos conectores em trio, que já fazer a isolação e organiza.  

Outro material muito usado no lugar da capa plástica é termo retrátil, que é fácil de instalar e de baixo custo.  

  

Na entrada de alimentação do ESC também instalei conectores banana macho de 3,5 mm. E faço a distribuição usado cabo XT60 macho para 4 pares de banana fêmea de 3,5 mm.  

  

Para ligar na fonte de PC é usado um conector XT60 fêmea (para simular uma bateria LiPo).  

É preciso ter cuidado com a fonte de PC pois se ligar todos os motores na velocidade máxima, a corrente drenada é muito alta (cerca de 12A por motor, então 4 x 12A = 48A [é a corrente de uma bateria de carro médio]). Se a fonte não tiver proteção ou for de qualidade muito ruim, pode explodir ou queimar.  

Portanto instale um amperímetro e não use um PWM nos motores que produza um consumo de corrente maior do que o especificado pela fonte de PC para a saída de +12V.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-G6X5hMifFEg/UpAbo9c7eyI/AAAAAAAAnZs/bW-hMKNaMoo/s1600/QUADX_328-291x300.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" src="http://4.bp.blogspot.com/-G6X5hMifFEg/UpAbo9c7eyI/AAAAAAAAnZs/bW-hMKNaMoo/s1600/QUADX_328-291x300.jpg"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">QUAD X</td></tr>
</tbody></table>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-PL7ZJCmP_-U/UpAbld0LPBI/AAAAAAAAnZk/YBpw1Am3_88/s1600/QUADP_328-300x285.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto; text-align: center;"><img border="0" src="http://2.bp.blogspot.com/-PL7ZJCmP_-U/UpAbld0LPBI/AAAAAAAAnZk/YBpw1Am3_88/s1600/QUADP_328-300x285.jpg"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">QUAD&nbsp;+</td></tr>
</tbody></table>

  

Várias outras configurações de quantidade e distribuição de motores podem ser encontradas no site do MultiWii.  

<http://www.multiwii.com/connecting-elements>  

  

Abaixo o comparativo dos conectores que foram eleitos para o drone em PVC.  

  

<iframe frameborder="0" height="400" src="https://docs.google.com/spreadsheet/pub?key=0As_hnNFIRrivdDh5OFYzNV9jNHRuTC1VVklsaFNxQkE&amp;output=html&amp;widget=true" width="650"></iframe>