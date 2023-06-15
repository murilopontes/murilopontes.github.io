---
layout: post
title: Deadzones em controles analógicos e remoção de ruído
categories:
 - ruído
date: 2013-11-21 14:58:00 +0000
---

  

Encontrei um ótimo post sobre o assunto, que vai direto ao ponto e compara as abordagens existentes.  

http://www.third-helix.com/2013/04/doing-thumbstick-dead-zones-right/  

  

<a name="more"></a>  
  

## Deadzones

<div>
Para quem ainda não conhecem, permita-me uma simples introdução.</div>

<div>
Deadzone é a área que deve ser ignorada por conta do ruído que existe naturalmente nos controles e sensores analógicos. &nbsp;</div>

## abordagem simplista&nbsp;

<pre class="brush:c#">float deadzone = 0.25f;
</pre>

<pre class="brush:c#">Vector2 stickInput = new Vector2(Input.GetAxis(“Horizontal”), Input.GetAxis(“Vertical”));</pre>

<pre class="brush:c#">if(Mathf.Abs(stickInput.x) &lt; deadzone)
    stickInput.x = 0.0f;
if(Mathf.Abs(stickInput.y) &lt; deadzone)
    stickInput.y = 0.0f;

</pre>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-2VFeBpUYQQM/Uo4Zh8psMkI/AAAAAAAAnYQ/tWwPXbJ45Q4/s1600/axial-deadzone.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="200" src="http://4.bp.blogspot.com/-2VFeBpUYQQM/Uo4Zh8psMkI/AAAAAAAAnYQ/tWwPXbJ45Q4/s200/axial-deadzone.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O controle/sensor fica como se estive frouxo / falhando.<br/>
Essa é a solução natural que a maioria dá quando vê o problema pela primeira vez.</td></tr>
</tbody></table>

## 

## abordagem radial

<pre class="brush:c#">float deadzone = 0.25f;
Vector2 stickInput = new Vector2(Input.GetAxis(“Horizontal”), Input.GetAxis(“Vertical”));
if(stickInput.magnitude &lt; deadzone)
    stickInput = Vector2.zero;

</pre>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-ABHs6_nzLlU/Uo4bgnhvJdI/AAAAAAAAnYc/2qh7ir1wl8Y/s1600/radial-deadzone.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="200" src="http://4.bp.blogspot.com/-ABHs6_nzLlU/Uo4bgnhvJdI/AAAAAAAAnYc/2qh7ir1wl8Y/s200/radial-deadzone.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Essa solução já é visivelmente melhor que a primeira,<br/>
no caso de um joystick com manche analógico (com os 2 do xbox360) somente<br/>
a área circular central &nbsp;vai ser ignorada como ruído.<br/>
Só que ainda existe um problema, o ruído não existe apenas na posição central do controle/sensor.</td></tr>
</tbody></table>

<pre class="brush:c#"></pre>

## abordagem radial escalar normalizada

<pre class="brush:c#">float deadzone = 0.25f;
Vector2 stickInput = new Vector2(Input.GetAxis(“Horizontal”), Input.GetAxis(“Vertical”));</pre>

<pre class="brush:c#">if(stickInput.magnitude &lt; deadzone)
    stickInput = Vector2.zero;
else
    stickInput = stickInput.normalized * ((stickInput.magnitude - deadzone) / (1 - deadzone));

</pre>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-w7s1w_0C4tU/Uo4dTqYGK9I/AAAAAAAAnYo/rRDTtBf4fHE/s1600/scaled-radial-deadzone.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="200" src="http://1.bp.blogspot.com/-w7s1w_0C4tU/Uo4dTqYGK9I/AAAAAAAAnYo/rRDTtBf4fHE/s200/scaled-radial-deadzone.jpg" width="200"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Essa solução resolve o problema que restava, da solução anterior.<br/>
O ruído é filtrado de maneira proporcional ao afastamento do centro.</td></tr>
</tbody></table>

  

  

<div>
Tudo isso se aplica tanto a controles (manches do xbox360), bem como, sensores (praticamente todos do drone).</div>

<div>
<br/></div>