---
layout: post
title: Estudo comparativo das técnicas de deadzone para controle do Xbox360 usando XInputDotNet
categories:
 - DirectX
date: 2013-11-22 01:38:00 +0000
---

Para completar o post  

<http://dronespersonalizados.blogspot.com.br/2013/11/deadzones-em-controles-analogicos-e.html>  

implementei uma pequena aplicação de teste em C#&nbsp;+ XinputDotNet (wrapper do DirectX input).  

A ideia aqui é validar a teoria usando os sticks analógicos do controle de xbox360.  

  

<a name="more"></a>  
  

No caso do RAW o valor dos sticks está sendo lido e inserido direto no chart sem nenhum pós-processamento adicional.  

No caso do NAIVE o valor usa abordagem de contar os valores abaixo do limiar do deadzone, como pode ser facilmente observado no gráfico, o ruído é reduzido, mas leva junto o sinal útil do outro eixo.  

No caso do RADIAL podemos verificar que o ruído e reduzido, e o sinal de ambos os eixos continuam funcionamento perfeitamente enquanto o ruído foi removido.  

  

Todo o código deste aplicativo está em meu fork do XinputDotNet no Github  

<https://github.com/murix/XInputDotNet>  

Aproveite e faça o fork do meu fork :D  

  

Se não quiser configurar ou montar o ambiente para operar o git, também dá para baixar o repositório em formato zip. Na pasta "binaries" já tem tudo pré-compilado para testar sem precisar &nbsp;ter o Visual Studio instalado.  

https://github.com/murix/XInputDotNet/archive/465e5bc6c9.zip  

  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-GUB7H2AJC5E/Uo6ydNiqBKI/AAAAAAAAnY8/35Jevqoy_t8/s1600/deadzone-comparative.PNG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="616" src="http://1.bp.blogspot.com/-GUB7H2AJC5E/Uo6ydNiqBKI/AAAAAAAAnY8/35Jevqoy_t8/s640/deadzone-comparative.PNG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Estudo comparativo das técnicas de deadzone / remoção de ruído</td></tr>
</tbody></table>

  