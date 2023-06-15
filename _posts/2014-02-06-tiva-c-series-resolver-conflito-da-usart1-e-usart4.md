---
layout: post
title: Tiva C series- resolver conflito da USART1 e USART4
categories:
 - post
date: 2014-02-06 14:49:00 +0000
---

Usando a Energia IDE (https://github.com/energia/Energia) é super simples.  

O truque é remapear a USART1, para remover o conflito com os pinos da USART4.  

  

<a name="more"></a>  
  

Sem remapear os pinos, uma tentativa de ativar a USART1 e USART4 com configuração padrão resulta em: USART4 (PC4 e PC5) &nbsp;ok e &nbsp;USART1 morta.  

Para que isso não ocorra é só remapear os pinos da USART1 para PB0 e PB1.  

O código para fazer isso está no snippet a seguir.  

  

  

<script src="https://gist.github.com/murix/8845413.js"></script>

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-E_aEvL1_F8U/UvOfapkoKsI/AAAAAAAAoxE/9YPHbvkAAqM/s1600/IMG_20140206_113318.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://1.bp.blogspot.com/-E_aEvL1_F8U/UvOfapkoKsI/AAAAAAAAoxE/9YPHbvkAAqM/s1600/IMG_20140206_113318.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Depois de compilado e instalado, <br/>
é só passar com o Buspirate no TX de cada uma das oito portas seriais para verificar a mensagem de teste.</td></tr>
</tbody></table>

  