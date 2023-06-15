---
layout: post
title: Drones no estilo faça você mesmo
categories:
 - super capacitor
date: 2013-09-17 12:53:00 +0100
---

<div style="text-align: justify;">
Este post está sempre sendo atualizado e é dedicado a elaborar um roteiro para montar um veiculo aéreo não tripulado (VANT) ou drone do tipo quad-rotor ou multi-rotor. Incluindo o projeto do hardware e software/firmware. E que seja facilmente personalizável.</div>

<div style="text-align: justify;">
<br/>
Demonstração do drone semelhante ao que está sendo montado neste post</div>

<div style="text-align: justify;">
<a href="http://vimeo.com/28427063">http://vimeo.com/28427063</a><br/>
<br/>
<iframe allowfullscreen="" frameborder="0" height="281" mozallowfullscreen="" src="//player.vimeo.com/video/28427063" webkitallowfullscreen="" width="500"></iframe> <br/>
<a href="http://vimeo.com/28427063">mwc quad // suppo 2212/13</a> from <a href="http://vimeo.com/warthox">warthox</a> on <a href="https://vimeo.com/">Vimeo</a>.<br/>
<br/>
<iframe allowfullscreen="" frameborder="0" height="281" mozallowfullscreen="" src="//player.vimeo.com/video/72441236" webkitallowfullscreen="" width="500"></iframe> <br/>
<a href="http://vimeo.com/72441236">mwc quad // learning to fly inverted [uncut]</a> from <a href="http://vimeo.com/warthox">warthox</a> on <a href="https://vimeo.com/">Vimeo</a>.<br/>
<br/>
Ferramenta para cálculo do motor e hélices.<br/>
<a href="http://www.drivecalc.de/">http://www.drivecalc.de/</a></div>

<div style="text-align: justify;">
<br/>
<br/></div>

<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-iJPkPb92Z9o/UjkX5kSg1oI/AAAAAAAAliQ/8EOCOI-lHa8/s1600/drone.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="194" src="http://1.bp.blogspot.com/-iJPkPb92Z9o/UjkX5kSg1oI/AAAAAAAAliQ/8EOCOI-lHa8/s320/drone.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Modelo de Drone simplificado</td></tr>
</tbody></table>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<span style="font-size: large;"><b>Requisitos:</b></span></div>

<div style="text-align: justify;">
- Baixo custo (praticamente tudo chinês)</div>

<div style="text-align: justify;">
- Anticolisão</div>

<div style="text-align: justify;">
- Automatizado por GPS</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Vamos a lista de peças necessárias e revisão.</div>

<div style="text-align: justify;">
Além disso, vou colocar um acompanhamento dos prazo que leva para chegar as peças.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b><span style="color: #93c47d;">Comprados:</span></b></div>

<div style="text-align: justify;">
frame - Turnigy Talon v1 Carbon Fiber (R$110)<br/>
<div>
4 x ESC HobbyWing Pentium - 30A - (R$100)</div>
4 x motores Suppo A2212/13T &nbsp;12A 1000kv - (R$100)<br/>
<br/>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
</div>
<br/>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
<div>
4 x hélices 9x5 de nylon - sendo 2 CW e 2 CCW</div>
<div>
<div style="margin: 0px;">
</div>
</div>
<div style="margin: 0px;">
4 x hélices 8x4 de nylon - sendo 2 CW e 2 CCW</div>
</div>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
<div style="margin: 0px;">
6 x sensor ultrasom (distância até 5 metros em +-x,+-y,+-z) - HC-SR04<br/>
<br/>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
</div>
<br/>
<div style="-webkit-text-stroke-width: 0px; color: black; font-family: 'Times New Roman'; font-size: medium; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;">
<div style="margin: 0px;">
sensor de pressão (altitude além dos 5 metros) - bmp085</div>
</div>
</div>
</div>
</div>

<div style="text-align: justify;">
2 x comunicação rádio 433mhz - cc1101</div>

<div style="text-align: justify;">
navegador bússola 3d - hmc5883l</div>

<div style="text-align: justify;">
giroscópio 3d - MPU6050</div>

<div style="text-align: justify;">
acelerômetro 3d - MPU6050</div>

<div style="text-align: justify;">
kit microcontrolador - Texas EK-ML4F120XL (ARM Cortex-m4)</div>

<div style="text-align: justify;">
kit microcontrolador - ST Discovery-VL (ARM Cortex-m3)</div>

<div style="text-align: justify;">
kit&nbsp;microcontrolador&nbsp;- FreeScale FRDM-KL25Z (ARM Cortex-m0)</div>

<div style="text-align: justify;">
kit&nbsp;microcontrolador&nbsp;-&nbsp;rl78/g13 (Renesas)</div>

<div style="text-align: justify;">
kit&nbsp;microcontrolador&nbsp;- Arduino Nano v3 (Atmel-AVR)</div>

<div style="text-align: justify;">
conversor USB/TTL - Prolific 2303HX</div>

<div>
<div style="text-align: justify;">
<br/>
<div>
<span style="color: red;"><b>Falta comprar:</b></span></div>
<div>
navegador&nbsp;gps -</div>
<div>
comunicação gsm quadband - sim900</div>
<div>
comunicação&nbsp;wifi - cc3000</div>
<div>
bateria LiPo -</div>
<div>
Carregador LiPo -</div>
</div>
</div>

<div>
<div style="text-align: justify;">
<br/>
<br/></div>
</div>

<div style="text-align: justify;">
<span style="font-size: x-large;"><b>Frame / Esqueleto / Armação</b></span></div>

<div style="text-align: justify;">
As opções no mercado são de alumínio, fibra de carbono, fibra de vidro e plástico.</div>

<div style="text-align: justify;">
fibra de vidro e plástico são muito moles e quebram com extrema facilidade.</div>

<div style="text-align: justify;">
A de alumínio é leve e bem resistente, mas é fácil de arranhar.</div>

<div style="text-align: justify;">
A solução ideal seria de fibra de carbono que é mais leve que alumínio e mais forte que do aço.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Plástico</div>

<div style="text-align: justify;">
<a href="http://dx.com/p/4-axis-hj600-plastic-multi-copter-quadcopter-xcopter-frame-kit-white-black-146827">http://dx.com/p/4-axis-hj600-plastic-multi-copter-quadcopter-xcopter-frame-kit-white-black-146827</a></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/4-axis-hj600-plastic-multi-copter-quadcopter-xcopter-frame-kit-red-black-146828">http://dx.com/p/4-axis-hj600-plastic-multi-copter-quadcopter-xcopter-frame-kit-red-black-146828</a></div>

<div>
<div style="text-align: justify;">
<br/></div>
</div>

<div>
<div style="text-align: justify;">
Fibra de vidro</div>
</div>

<div>
<div style="text-align: justify;">
<a href="http://dx.com/p/600mm-4-axis-kk-mk-x525-v3-quad-rotor-multi-hc-helicopter-fiber-glass-folded-form-kit-123219">http://dx.com/p/600mm-4-axis-kk-mk-x525-v3-quad-rotor-multi-hc-helicopter-fiber-glass-folded-form-kit-123219</a></div>
</div>

<div>
<div style="text-align: justify;">
<br/></div>
</div>

<div>
<div style="text-align: justify;">
Alumínio</div>
</div>

<div style="text-align: justify;">
<a href="http://dx.com/p/st450-folding-frame-quad-rotor-aluminum-aircraft-129364">http://dx.com/p/st450-folding-frame-quad-rotor-aluminum-aircraft-129364</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Fibra de carbono</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
(este me parece a melhor opção custo / benefício)</div>

<div style="text-align: justify;">
<a href="http://www.hobbyking.com/hobbyking/store/__22397__Turnigy_Talon_Carbon_Fiber_Quadcopter_Frame.html">http://www.hobbyking.com/hobbyking/store/__22397__Turnigy_Talon_Carbon_Fiber_Quadcopter_Frame.html</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
[a versão 2.0 da primeira]</div>

<div style="text-align: justify;">
<a href="http://www.hobbyking.com/hobbyking/store/__22781__Turnigy_Talon_Quadcopter_V2_0_Carbon_Fiber_Frame_550mm.html">http://www.hobbyking.com/hobbyking/store/__22781__Turnigy_Talon_Quadcopter_V2_0_Carbon_Fiber_Frame_550mm.html</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
[uma opção com pés de helicóptero]</div>

<div style="text-align: justify;">
<a href="http://www.hobbyking.com/hobbyking/store/__25557__AQ_600_Carbon_Fiber_Quadcopter_Frame_550mm.html">http://www.hobbyking.com/hobbyking/store/__25557__AQ_600_Carbon_Fiber_Quadcopter_Frame_550mm.html</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Se estiver a fim de fazer seu próprio frame em fibra de carbono, tem um cidadão explicando como faz para montar uma bicicleta, mas o processo é o mesmo.</div>

<div style="text-align: justify;">
<a href="http://theprojectjunkie.com/composite-bicycles/homemade-carbon-fiber-bike-project.html">http://theprojectjunkie.com/composite-bicycles/homemade-carbon-fiber-bike-project.html</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b><span style="font-size: x-large;">Eletronic Speed Control (ESC)</span></b></div>

<div style="text-align: justify;">
O controle eletrônico de velocidade é aplicado a motores brushless trifásicos para controlar a velocidade com extrema precisão. Os motores compostos por 3 bobinas separadas de 120 graus, precisam ser acionadas sequencialmente para que o motor gire. O ESC geralmente é composto de uma fonte chaveada que é alimentada pela bateria do sistema (geralmente polímero de lítio [Lipo] de 3 células), e fornece um saída estabilizada de 5V (battery eliminator circuit [BEC]) para alimentar o microcontrolador do ESC e o resto do sistema, além da saída que vai para os transistor de efeito de campo (FET) que vai alimentar cada bobina do motor no momento certo. O FET funciona como uma chave de liga e desliga eletrônica que muda de aberto para fechado dependendo do que é injetado na base. O que o programa do ESC faz é controlar os FET usando GPIO do MCU. O MCU recebe como entrada o sinal de controle, a frequência de chaveamento do sinal de controle é usada para ajustar a velocidade do PWM que auxila no chaveamento dos FET obedecendo a sequência de disparo de 120 graus. Além disso, o MCU também recebe como entrada sinais de força contra eletromotriz (back EMF) para detectar onde está o miolo central do motor. À primeira vista parece um programa muito simples, mas existe muito mais detalhes para construir um ESC com HW e SW / FW otimizados. Como o objetivo é construir um Drone e não um ESC, vamos usar um solução já pronta e disponível comercialmente.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<br/></div>

<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-tE9T1asRXXQ/UjkAueW-ACI/AAAAAAAAlhw/SlL6VenzFsE/s1600/ESC-design.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="196" src="http://2.bp.blogspot.com/-tE9T1asRXXQ/UjkAueW-ACI/AAAAAAAAlhw/SlL6VenzFsE/s320/ESC-design.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema simplificado de um ESC com BEC</td></tr>
</tbody></table>

<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-hASxsFGn4QU/UjkSqYfqSiI/AAAAAAAAliA/MPfF4Xrc5WE/s1600/TowerPro25aEscSchematic.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="221" src="http://3.bp.blogspot.com/-hASxsFGn4QU/UjkSqYfqSiI/AAAAAAAAliA/MPfF4Xrc5WE/s320/TowerPro25aEscSchematic.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Esquema elétrico de um ESC [s1]</td></tr>
</tbody></table>

<div style="text-align: justify;">
[s1]&nbsp;<a href="http://www.rcgroups.com/forums/attachment.php?attachmentid=3794669">http://www.rcgroups.com/forums/attachment.php?attachmentid=3794669</a></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<br/></div>

<div class="separator" style="clear: both; text-align: center;">
</div>

<div style="text-align: justify;">
<b>Importante:</b> a corrente máxima suportada pelo ESC deve ser sempre maior (pelo menos 10% de folga) em relação a corrente máxima especificada pelo motor. O erro mais comum é usar um ESC com corrente menor do que a especificada pelo motor. A consequência deste erro é ver o ESC (em especial os FETs) virar carvão em menos de 1 segundo.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Corrente máxima 30A</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/hobbywing-pentium-30a-brushless-speed-controller-esc-for-r-c-helicopter-quadcopter-black-184272">http://dx.com/p/hobbywing-pentium-30a-brushless-speed-controller-esc-for-r-c-helicopter-quadcopter-black-184272</a>&nbsp;(cerca de $9,20)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/flying-30a-bec-electronic-speed-controller-for-brushless-motors-esc-11981">http://dx.com/p/flying-30a-bec-electronic-speed-controller-for-brushless-motors-esc-11981</a>&nbsp;(cerca de&nbsp;$11,20)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Corrente máxima 40A</div>

<div style="text-align: justify;">
<br/></div>

<div>
<div style="text-align: justify;">
<a href="http://dx.com/p/thunder-40a-m-sw-40a-esc-w-bec-switching-mode-for-brushless-motors-on-r-c-helicopters-red-198564">http://dx.com/p/thunder-40a-m-sw-40a-esc-w-bec-switching-mode-for-brushless-motors-on-r-c-helicopters-red-198564</a>&nbsp; (cerca de&nbsp;$17.40)</div>
</div>

<div>
<div style="text-align: justify;">
<br/></div>
</div>

<div style="text-align: justify;">
Corrente máxima 70A</div>

<div style="text-align: justify;">
<br/></div>

<div>
<div style="text-align: justify;">
<a href="http://dx.com/p/flying-70a-bec-electronic-speed-controller-for-brushless-motors-esc-11983">http://dx.com/p/flying-70a-bec-electronic-speed-controller-for-brushless-motors-esc-11983</a>&nbsp;(cerca de&nbsp;$22.84)</div>
</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<span style="font-size: x-large;"><b>Hélices / Propellers</b></span></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
As hélices possuem dois tipos CW e CCW. As CW cortam o ar em sentido horário e as CCW cortam o ar em sentido anti-horário. Para voar os drones quadrotor precisam ter 2 hélices de cada tipo.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
A hélices possuem dois parâmetros: tamanho e ângulo de ataque.</div>

<div style="text-align: justify;">
Uma hélice 9 x 5 que dizer que o diâmetro da hélice é 9 polegadas e 5 é o ângulo de ataque do ar, ou seja, a inclinação da hélice é de 5 graus.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b>Relação tamanho vs ângulo de ataque vs empuxo gerado vs corrente necessária vs bateria</b></div>

<div style="text-align: justify;">
Quanto maior a hélice e o ângulo de ataque, maior será a força de empuxo gerada (Thrust).</div>

<div style="text-align: justify;">
A resistência do ar é proporcional a área da pá e ângulo de ataque.</div>

<div style="text-align: justify;">
Isso implica que uma maior resistência do ar causa um maior esforço do motor, e quanto maior o esforço do motor maior será a corrente necessária. E se a corrente necessária for próxima da máxima especificada pelo motor, provavelmente a eficiência energética do motor não será otimizada. E motor não otimizado implica consumir mais energia da bateria e como consequência menor autonomia de voo, pois a quantidade de energia da bateria é limitada. Aumentar o tamanho de bateria para ter mais energia implica em aumentar o peso, e aumentar o peso também causa mais esforço do motor.</div>

<div style="text-align: justify;">
Portanto não é um problema trivial dimensionar as configurações de hélice / motor / bateria / autonomia de voo desejada / peso extra para bagagens.</div>

<div style="text-align: justify;">
Parece mais um problema recursivo que só faz crescer de si mesmo.</div>

<div style="text-align: justify;">
O desafio é encontrar uma configuração de hélice que gere o empuxo desejado sem comprometer a eficiência energética do motor.<br/>
<br/>
Além disso tudo, ainda tem de escolher o material do qual é feito a hélice. As hélices de plástico são baratas, mas costumam vibrar mais do que as hélices de fibra de carbono. A hélices de fibra de carbono são 100 vezes mais forte que as hélices de alumínio.<br/>
<br/></div>

<iframe allowfullscreen="" frameborder="0" height="344" src="//www.youtube.com/embed/dkQqD96AEd4" width="459"></iframe>

  

No caso das hélices de fibra de caborno é altamente recomendado realizar o balanceamento manual da hélice.
É um processo simples de tentativa e erro, até deixar os dois lados da hélice com o mesmo peso.

<iframe allowfullscreen="" frameborder="0" height="344" src="//www.youtube.com/embed/IrPcqL2OHb8" width="459"></iframe>

  

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<br/>
<br/>
<br/>
<br/></div>

<div style="text-align: justify;">
<b><span style="font-size: x-large;">Motores (Brushless Outrunner)</span></b><br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-oa0l4zVXh8g/Uj2ksLRVztI/AAAAAAAAlkc/M3O71Ji5H-U/s1600/a2212-13t.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" src="http://2.bp.blogspot.com/-oa0l4zVXh8g/Uj2ksLRVztI/AAAAAAAAlkc/M3O71Ji5H-U/s1600/a2212-13t.jpg"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Motor Mistery / Suppo A2212/13T 1000Kv</td></tr>
</tbody></table>
<b><span style="font-size: x-large;"><br/></span></b></div>

<div style="text-align: justify;">
Existem basicamente 2 tipos de motores os outrunner (que a carcaça gira junto, tem alto torque e baixa rotação) e os motores inrunner (que somente o eixo gira, tem baixo torque e alta rotação).</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
A corrente máxima do ESC deve sempre ser maior que a corrente máxima exigida pelo motor.</div>

<div style="text-align: justify;">
Se o ESC tiver corrente máxima menor que a de exigência do motor, o ESC virará "plasma" em 1 segundo.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Cada motor foi projetado para um determinado esforço máximo, portanto sempre se deve utilizar uma hélice do tamanho adequado. Se a hélices exigirem mais esforço do que o máximo suportado pelo motor, quem virará "plasma" é o motor.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
O desafio é usar a maior hélice possível (quanto maior a hélice e o ângulo de ataque, maior será o empuxo gerado) que o motor suporta. Uma vez achada tal hélice, é preciso usar um ESC que forneça uma corrente maior do que a corrente exigida pelo motor equipado com a hélice.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Mas aqui existe outro problema, quando o motor está trabalhando com esforço máximo em 99,99% dos casos boa parte da energia está sendo gasta em calor, pois o núcleo do motor já está saturado magneticamente faltando. Dai é necessário descobrir qual é o esforço máximo do motor que maximiza a eficiência na relação corrente consumida x torque produzido.</div>

<div style="text-align: justify;">
<br/>
Opção de motor da EMAX<br/>
<a href="http://dx.com/p/emax-cf2822-1200kv-diy-brushless-external-rotor-electric-machine-motor-for-apc-8x3-8-more-218180">http://dx.com/p/emax-cf2822-1200kv-diy-brushless-external-rotor-electric-machine-motor-for-apc-8x3-8-more-218180</a><br/>
<br/>
O fabricante é "SUPPO" modelo A2212/13T<br/>
<a href="http://dx.com/p/a2212-13t-1000kv-outrunner-brushless-motor-set-yellow-gold-silver-219554">http://dx.com/p/a2212-13t-1000kv-outrunner-brushless-motor-set-yellow-gold-silver-219554</a><br/>
(cerca de $12)<br/>
<br/>
O mesmo motor SUPPO modelo A2212/13T com desconto<br/>
<a href="http://dx.com/p/kv1000-brushless-exterior-rotor-motor-outrunner-motor-yellow-154904">http://dx.com/p/kv1000-brushless-exterior-rotor-motor-outrunner-motor-yellow-154904</a><br/>
<div>
(cerca de $10)</div>
<br/>
[ref]&nbsp;<a href="http://www.rctimer.com/product_118.html">http://www.rctimer.com/product_118.html</a><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Model:&nbsp; 2212-13</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Motor size: Ф28*26mm</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Shaft size: Ф3.175*37mm</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Weight: 50g</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">KV(rpm/v): 1000</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Max Power: 150W</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Battery: 2-3Li-Po</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Test Prop: 11x7/10x5</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">Ri(M Ω): 0.127</span><br/>
<span style="font-family: arial; font-size: x-small; line-height: 20px; text-align: left;">ESC(A): 30A</span><br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-ktNiLX-_itA/Uj2jBgz_SkI/AAAAAAAAlkQ/Lee8FewwPh4/s1600/1305451092.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="117" src="http://2.bp.blogspot.com/-ktNiLX-_itA/Uj2jBgz_SkI/AAAAAAAAlkQ/Lee8FewwPh4/s320/1305451092.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Mecânica do motor A2212/13T</td></tr>
</tbody></table>
<br/>
<table border="0" cellpadding="2" cellspacing="1" style="color: black; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; margin: 0px; outline: none; padding: 0px;"><tbody style="margin: 0px; outline: none; padding: 0px;">
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;"><span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">No. of Cells:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 2 - 3 Li-Poly ( 7.2V até 11.1V)<br style="margin: 0px; outline: none; padding: 0px;"/>&nbsp;&nbsp;6 - 10 NiCd/NiMH &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Kv:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 1000 RPM/V &nbsp;(até 11mil rpm sem hélice, com hélice é menos por causa da resistência do ar)</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Max Efficiency:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 80% &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Max Efficiency Current:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 4 - 10A (&gt;75%) &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">No Load Current:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 0.5A @10V &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Resistance:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 0.090 ohms &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Max Current:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 13A for 60S &nbsp;(</span><span class="text10" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">derrete </span>se passar mais de um minuto com essa corrente)</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Max Watts:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 150W &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Weight:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 52.7 g / 1.86 oz &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Size:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 28 mm dia x 28 mm bell length &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Shaft Diameter:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 3.2 mm &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Poles:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#dddddd" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 14 &nbsp;</span></td></tr>
<tr style="margin: 0px; outline: none; padding: 0px;"><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp;&nbsp;<span class="Apple-style-span" style="margin: 0px; outline: none; padding: 0px;">Model Weight:</span>&nbsp;&nbsp;</span></td><td align="left" bgcolor="#cccccc" style="margin: 0px; outline: none; padding: 0px;"><span class="text10" style="margin: 0px; outline: none; padding: 0px;">&nbsp; 300 - 800g / 10.5 - 28.2 oz &nbsp;</span></td></tr>
</tbody></table>
</div>

<div style="text-align: justify;">
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;">[ref]&nbsp;<a href="http://www.batteryheatedclothing.com/pages/a2212-13t-technical-data.html">http://www.batteryheatedclothing.com/pages/a2212-13t-technical-data.html</a><br/>
<br/>
<a href="http://4.bp.blogspot.com/-Teb1dW8XFDk/Uj0f0S6cjkI/AAAAAAAAljw/RSJFZTN8BxQ/s1600/a2212-13-efficiency.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="154" src="http://4.bp.blogspot.com/-Teb1dW8XFDk/Uj0f0S6cjkI/AAAAAAAAljw/RSJFZTN8BxQ/s320/a2212-13-efficiency.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Gráfico da eficiência enérgica do motor. Pelo que pode ser visto no gráfico a maior (próxima a 80%) fica na faixa de 4 a 8 amperes.</td></tr>
</tbody></table>
<div style="font-size: 13px; text-align: left;">
<span style="font-size: small;">[ref]&nbsp;</span><a href="http://www.batteryheatedclothing.com/pages/a2212-13t-technical-data.html" style="font-size: medium;">http://www.batteryheatedclothing.com/pages/a2212-13t-technical-data.html</a></div>
<div style="font-size: 13px; text-align: center;">
<br/></div>
<div style="font-size: 13px; text-align: center;">
<br/></div>
<div style="font-size: 13px; text-align: left;">
<span style="font-size: small;">Testando sem hélice, as velocidades são essas abaixo</span></div>
<div style="font-size: 13px; text-align: left;">
<span style="font-size: small;">[ref]&nbsp;<a href="http://www.flybrushless.com/motor/view/206">http://www.flybrushless.com/motor/view/206</a></span></div>
<br/>
<br/>
<br/>
<table style="background-color: white; border-collapse: collapse; border: 1px solid black; color: black; font-family: 'Trebuchet MS', Tahoma, Arial; font-size: 13px; margin: 0px; padding: 0px; width: 100%px;"><tbody style="margin: 0px; padding: 0px;">
<tr style="margin: 0px; padding: 0px;"><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;">Volts</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;">Amps</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;">RPM</th></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">0.6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7380</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">8</td><td style="border: 1px solid; margin: 0px; padding: 2px;">0.65</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8460</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">10</td><td style="border: 1px solid; margin: 0px; padding: 2px;">0.75</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10500</td></tr>
</tbody></table>
<br/>
Testando com hélices<br/>
[ref]&nbsp;<a href="http://www.flybrushless.com/motor/view/206">http://www.flybrushless.com/motor/view/206</a><br/>
<b><span style="font-size: x-large;"><br/></span></b>
<br/>
<table id="testData14" style="background-color: white; border-collapse: collapse; border: 1px solid black; color: black; font-family: 'Trebuchet MS', Tahoma, Arial; font-size: 13px; margin: 0px; padding: 0px; width: 100%px;"><thead style="margin: 0px; padding: 0px;">
<tr style="margin: 0px; padding: 0px;"><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="24%">Propeller</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="9%">Gear Ratio</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="7%">Volts</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="7%">Amps</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="7%">Watts</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="7%">RPM</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="10%">Speed (mph)</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="10%">Thrust (g)</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="10%">Thrust (oz)</th><th style="background-color: darkseagreen; border: 1px solid; margin: 0px; padding: 2px; text-align: center; vertical-align: top;" width="9%">RPM as % of Kv*V</th></tr>
</thead><tbody style="margin: 0px; padding: 0px;">
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 8x4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">3.35</td><td style="border: 1px solid; margin: 0px; padding: 2px;">23</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6630</td><td style="border: 1px solid; margin: 0px; padding: 2px;">25.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">226<br/>
(4x= 900g)<br/>
mínimo</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.97</td><td style="border: 1px solid; margin: 0px; padding: 2px;">88%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 8x4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">4.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">32</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7410</td><td style="border: 1px solid; margin: 0px; padding: 2px;">28.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">287</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.12</td><td style="border: 1px solid; margin: 0px; padding: 2px;">87%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 8x4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">4.85</td><td style="border: 1px solid; margin: 0px; padding: 2px;">43</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8220</td><td style="border: 1px solid; margin: 0px; padding: 2px;">31.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">347</td><td style="border: 1px solid; margin: 0px; padding: 2px;">12.24</td><td style="border: 1px solid; margin: 0px; padding: 2px;">86%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 8x4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">5.65</td><td style="border: 1px solid; margin: 0px; padding: 2px;">55</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8940</td><td style="border: 1px solid; margin: 0px; padding: 2px;">33.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">420</td><td style="border: 1px solid; margin: 0px; padding: 2px;">14.82</td><td style="border: 1px solid; margin: 0px; padding: 2px;">84%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 8x4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6.5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">70</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9660</td><td style="border: 1px solid; margin: 0px; padding: 2px;">36.6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">495<br/>
(4x= 1980g)<br/>
máximo</td><td style="border: 1px solid; margin: 0px; padding: 2px;">17.46</td><td style="border: 1px solid; margin: 0px; padding: 2px;">82%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 9x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">5.5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">37</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6000</td><td style="border: 1px solid; margin: 0px; padding: 2px;">28.4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">348<br/>
(4x= 1392g)<br/>
mínimo</td><td style="border: 1px solid; margin: 0px; padding: 2px;">12.28</td><td style="border: 1px solid; margin: 0px; padding: 2px;">81%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 9x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6.7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">52</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6660</td><td style="border: 1px solid; margin: 0px; padding: 2px;">31.5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">436</td><td style="border: 1px solid; margin: 0px; padding: 2px;">15.38</td><td style="border: 1px solid; margin: 0px; padding: 2px;">78%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 9x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.85</td><td style="border: 1px solid; margin: 0px; padding: 2px;">69</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7290</td><td style="border: 1px solid; margin: 0px; padding: 2px;">34.5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">526</td><td style="border: 1px solid; margin: 0px; padding: 2px;">18.55</td><td style="border: 1px solid; margin: 0px; padding: 2px;">76%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 9x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.25</td><td style="border: 1px solid; margin: 0px; padding: 2px;">91</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7920</td><td style="border: 1px solid; margin: 0px; padding: 2px;">37.5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">627<br/>
(4x= 2508g)<br/>
máximo</td><td style="border: 1px solid; margin: 0px; padding: 2px;">22.12</td><td style="border: 1px solid; margin: 0px; padding: 2px;">74%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">APC E 10x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">48</td><td style="border: 1px solid; margin: 0px; padding: 2px;">5610</td><td style="border: 1px solid; margin: 0px; padding: 2px;">26.6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">406</td><td style="border: 1px solid; margin: 0px; padding: 2px;">14.32</td><td style="border: 1px solid; margin: 0px; padding: 2px;">75%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">APC E 10x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.45</td><td style="border: 1px solid; margin: 0px; padding: 2px;">66</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6120</td><td style="border: 1px solid; margin: 0px; padding: 2px;">29.0</td><td style="border: 1px solid; margin: 0px; padding: 2px;">505</td><td style="border: 1px solid; margin: 0px; padding: 2px;">17.81</td><td style="border: 1px solid; margin: 0px; padding: 2px;">72%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">APC E 10x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">88</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6690</td><td style="border: 1px solid; margin: 0px; padding: 2px;">31.7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">604</td><td style="border: 1px solid; margin: 0px; padding: 2px;">21.31</td><td style="border: 1px solid; margin: 0px; padding: 2px;">70%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">APC E 10x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">11.45</td><td style="border: 1px solid; margin: 0px; padding: 2px;">113</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7170</td><td style="border: 1px solid; margin: 0px; padding: 2px;">34.0</td><td style="border: 1px solid; margin: 0px; padding: 2px;">702</td><td style="border: 1px solid; margin: 0px; padding: 2px;">24.76</td><td style="border: 1px solid; margin: 0px; padding: 2px;">67%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">APC E 10x5</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;"><span style="color: red;"><b>13 (perigo)</b></span></td><td style="border: 1px solid; margin: 0px; padding: 2px;">141</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7650</td><td style="border: 1px solid; margin: 0px; padding: 2px;">36.2</td><td style="border: 1px solid; margin: 0px; padding: 2px;">802</td><td style="border: 1px solid; margin: 0px; padding: 2px;">28.29</td><td style="border: 1px solid; margin: 0px; padding: 2px;">65%&nbsp;</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.2</td><td style="border: 1px solid; margin: 0px; padding: 2px;">49</td><td style="border: 1px solid; margin: 0px; padding: 2px;">5610</td><td style="border: 1px solid; margin: 0px; padding: 2px;">31.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">424</td><td style="border: 1px solid; margin: 0px; padding: 2px;">14.96</td><td style="border: 1px solid; margin: 0px; padding: 2px;">75%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">68</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6180</td><td style="border: 1px solid; margin: 0px; padding: 2px;">35.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">526</td><td style="border: 1px solid; margin: 0px; padding: 2px;">18.55</td><td style="border: 1px solid; margin: 0px; padding: 2px;">72%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">8.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">89</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6690</td><td style="border: 1px solid; margin: 0px; padding: 2px;">38.0</td><td style="border: 1px solid; margin: 0px; padding: 2px;">617</td><td style="border: 1px solid; margin: 0px; padding: 2px;">21.76</td><td style="border: 1px solid; margin: 0px; padding: 2px;">70%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">9.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">11.7</td><td style="border: 1px solid; margin: 0px; padding: 2px;">115</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7200</td><td style="border: 1px solid; margin: 0px; padding: 2px;">40.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;">722</td><td style="border: 1px solid; margin: 0px; padding: 2px;">25.47</td><td style="border: 1px solid; margin: 0px; padding: 2px;">67%</td></tr>
<tr class="userdatacell1" style="font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.9</td><td style="border: 1px solid; margin: 0px; padding: 2px;"><span style="color: red;"><b>13.25<br/>(perigo)</b></span></td><td style="border: 1px solid; margin: 0px; padding: 2px;">144</td><td style="border: 1px solid; margin: 0px; padding: 2px;">7680</td><td style="border: 1px solid; margin: 0px; padding: 2px;">43.6</td><td style="border: 1px solid; margin: 0px; padding: 2px;">817</td><td style="border: 1px solid; margin: 0px; padding: 2px;">28.82</td><td style="border: 1px solid; margin: 0px; padding: 2px;">65%</td></tr>
<tr class="userdatacell2" style="background-color: silver; font-size: 0.9em; margin: 1px; padding: 2px; text-align: center;"><td style="border: 1px solid; margin: 0px; padding: 2px;">GWS HD 10x8</td><td style="border: 1px solid; margin: 0px; padding: 2px;">1</td><td style="border: 1px solid; margin: 0px; padding: 2px;">10.8</td><td style="border: 1px solid; margin: 0px; padding: 2px;"><b><span style="color: red;">18.2<br/>(perigo)</span></b></td><td style="border: 1px solid; margin: 0px; padding: 2px;">196</td><td style="border: 1px solid; margin: 0px; padding: 2px;">6390</td><td style="border: 1px solid; margin: 0px; padding: 2px;">48.4</td><td style="border: 1px solid; margin: 0px; padding: 2px;">733</td><td style="border: 1px solid; margin: 0px; padding: 2px;">25.86</td><td style="border: 1px solid; margin: 0px; padding: 2px;">55%</td></tr>
</tbody></table>
<b><span style="font-size: x-large;"><br/></span></b>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-ThF-HVZREFY/Uj0sqhnBaNI/AAAAAAAAlkA/d_Ald6wA63o/s1600/Grayson-Welgard+2212.13.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://1.bp.blogspot.com/-ThF-HVZREFY/Uj0sqhnBaNI/AAAAAAAAlkA/d_Ald6wA63o/s320/Grayson-Welgard+2212.13.jpg" width="265"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Dados de temperatura do motor (complementando a tabela anterior):<br/>
[ref]&nbsp;<a href="http://www.rcgroups.com/forums/attachment.php?attachmentid=3996646">http://www.rcgroups.com/forums/attachment.php?attachmentid=3996646</a></td></tr>
</tbody></table>
<b><span style="font-size: x-large;"><br/></span></b>
<b><span style="font-size: x-large;"><br/></span></b>
Com hélices de 8x4 os motores juntos conseguem levantar cerca de 2kg no máximo. Para maximizar a vida da bateria o peso máximo deve ser de 900g.<br/>
<br/>
Com hélices de 9x5 os motores juntos conseguem levantar cerca de 2,5kg no máximo.<br/>
Para maximizar a vida da bateria o peso máximo deve ser de 1392g.<br/>
<br/>
O peso estimado do drone (frame[240g]+motores[4x51=204g]+esc[4x27g=108g] -&gt; 552g)<br/>
Ainda falta somar as hélices e placas de controle, sensores e bateria.<br/>
<b><span style="font-size: x-large;"><br/></span></b>
<b><span style="font-size: x-large;">Baterias (LiPo)</span></b></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Bateria - LiPo 5000mAh 50C -&gt; 5 x 50 = 250A de corrente de pico.</div>

<div style="text-align: justify;">
<span style="background-color: white; color: #444444; font-family: arial, sans-serif; font-size: x-small; line-height: 16px;">Banco de baterias nuclear - NanoTritium</span><span style="background-color: white; color: #444444; font-family: arial, sans-serif; font-size: x-small; line-height: 16px;">&nbsp;betavoltaic&nbsp;</span></div>

<div>
<div style="text-align: justify;">
<a href="http://en.wikipedia.org/wiki/Supercapacitor">http://en.wikipedia.org/wiki/Supercapacitor</a></div>
</div>

<div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<span style="font-size: x-large;"><b>Microncontralador ( CPU&nbsp;+ RAM&nbsp;+ FLASH )</b></span></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Para o sistema de estabilização, anti-colisão, controle e comunicação podemos usar um microcontrolador com FreeRTOS ou um sistema com mais recursos para usar Linux.</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Para FreeRTOS existem diversos kit de baixo custo (até US$ 20) com JTAG já embutida.</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Texas</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
ST</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Para Linux também existem diversas placas de baixo custo, com 512MB de RAM e cartão SD de até 64GB. Tudo de baixo custo (até $50)</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Raspberry Pi</div>
<div style="text-align: justify;">
<a href="http://www.raspberrypi.org/">http://www.raspberrypi.org/</a></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Beaglebone</div>
<div style="text-align: justify;">
<a href="http://beagleboard.org/Products/BeagleBone%20Black">http://beagleboard.org/Products/BeagleBone%20Black</a></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<b><span style="font-size: x-large;">Comunicação via RF ISM (433MHz / 915MHz)</span></b></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Existem diversos rádio na banda de automação industrial que podem ser usados para controle remoto do drone. Todos de baixo custo (até US$ 5).</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Texas CC1101</div>
<div style="text-align: justify;">
<a href="http://www.ti.com/product/cc1101">http://www.ti.com/product/cc1101</a></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
ST Spirit</div>
<div style="text-align: justify;">
<a href="http://www.st.com/web/catalog/sense_power/FM1968/CL1976/SC1845/PF253167">http://www.st.com/web/catalog/sense_power/FM1968/CL1976/SC1845/PF253167</a></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<b><span style="font-size: x-large;">Comunicação via WIFI (2.4Ghz / 5GHz)</span></b></div>
<div style="text-align: justify;">
<br/></div>
</div>

<div style="text-align: justify;">
Existem soluções de WIFI embarcado</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Texas CC3000</div>

<div style="text-align: justify;">
<a href="http://www.ti.com/product/cc3000-tiwi-sl">http://www.ti.com/product/cc3000-tiwi-sl</a><br/>
<br/></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/wi-fi-shield-eifi-expansion-board-white-189923">http://dx.com/p/wi-fi-shield-eifi-expansion-board-white-189923</a><br/>
(cerca de $64)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/rt5350f-serial-port-ethernet-network-wireless-network-conversion-module-w-shielding-cover-239155">http://dx.com/p/rt5350f-serial-port-ethernet-network-wireless-network-conversion-module-w-shielding-cover-239155</a>&nbsp; (cerca de $16)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b><span style="font-size: x-large;">Comunicação via GSM Quad Band</span></b></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Existem soluções para usar a conexão de dados da rede celular.</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Placa com SIM900 um SOC para GSM 850/900/1800/1900 Mhz</div>

<div style="text-align: justify;">
<a href="http://dx.com/p/efcom-pro-wireless-850-900-1800-1900mhz-gprs-gsm-module-w-antenna-white-173749">http://dx.com/p/efcom-pro-wireless-850-900-1800-1900mhz-gprs-gsm-module-w-antenna-white-173749</a></div>

<div style="text-align: justify;">
(cerca de $47)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b><span style="font-size: x-large;">Navegação e automação por GPS</span></b></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
Soluções de GPS embarcado</div>

<div style="text-align: justify;">
<a href="http://dx.com/p/ulbox-atk-neo-6m-v12-gps-module-w-5hz-antenna-blue-yellow-226460">http://dx.com/p/ulbox-atk-neo-6m-v12-gps-module-w-5hz-antenna-blue-yellow-226460</a>&nbsp;(cerca de $24)</div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<b><span style="font-size: x-large;">Navegação por&nbsp;<span style="color: #222222; font-family: inherit; line-height: 22px; white-space: nowrap;">Bússola&nbsp;</span></span></b></div>

<div style="text-align: justify;">
<br/></div>

<div style="text-align: justify;">
<span itemprop="name" style="color: #3d3d3d; font-family: inherit; line-height: 22px;" title="GY-273 HMC5883L 3-Axis Magnetic Electronic Compass - Blue (3~5V)">HMC5883L - ótima para navegar onde não tem sinal de GPS disponível &nbsp;</span></div>

<div style="text-align: justify;">
<a href="http://dx.com/p/gy-273-hmc5883l-3-axis-magnetic-electronic-compass-blue-3-5v-214312"><span style="font-family: inherit;">http://dx.com/p/gy-273-hmc5883l-3-axis-magnetic-electronic-compass-blue-3-5v-214312</span></a></div>

<div style="text-align: justify;">
<br/></div>

  

<div style="text-align: justify;">
<br/></div>

____  

<div style="text-align: justify;">
<b><b><span style="font-size: large;">Giroscópio de 3 eixos&nbsp;+&nbsp;<span style="background-color: white; color: #444444; line-height: 16px;">Acelerômetro de 3 eixos (estabilizador)</span></span></b></b></div>

____
  

<div style="text-align: justify;">
<span style="font-family: inherit;"><br/></span></div>

<div style="text-align: justify;">
<span style="font-family: inherit;">MPU6050 - Sensor da Invense 6 DOF</span></div>

<h3 class="r" style="background-color: white; color: #222222; font-family: arial, sans-serif; font-size: medium; font-weight: normal; margin: 0px; overflow: hidden; padding: 0px; text-align: justify; text-overflow: ellipsis; white-space: nowrap;">
<a href="http://dx.com/p/gy-521-mpu6050-3-axis-acceleration-gyroscope-6dof-module-blue-154602" style="background-color: transparent;">http://dx.com/p/gy-521-mpu6050-3-axis-acceleration-gyroscope-6dof-module-blue-154602</a></h3>

<div>
<div style="text-align: justify;">
<br/></div>
<div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<b><span style="font-size: x-large;">Sensor de distância até 5 metros (anti-colisão)</span></b></div>
</div>
</div>

<div>
<div style="text-align: justify;">
6 x Sonar - &nbsp;- evitar colisão nos eixos x,y,z</div>
</div>

<div>
<div style="text-align: justify;">
<a href="http://dx.com/p/hc-sr04-ultrasonic-sensor-distance-measuring-module-133696">http://dx.com/p/hc-sr04-ultrasonic-sensor-distance-measuring-module-133696</a></div>
</div>

<div>
<div style="text-align: justify;">
(em breve como construir um&nbsp;<span style="background-color: white; color: #444444; font-family: arial, sans-serif; font-size: x-small; line-height: 16px;">sonar</span>)</div>
</div>

<div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<b><span style="font-size: x-large;">Sensor de pressão (altitude)</span></b></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
MS5611-01BA03 -Altímetro com precisão de +-10cm</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<a href="http://dx.com/p/gy-63-ms5611-high-resolution-atmospheric-pressure-height-sensor-module-for-arduino-148866">http://dx.com/p/gy-63-ms5611-high-resolution-atmospheric-pressure-height-sensor-module-for-arduino-148866</a>&nbsp; &nbsp; (<span style="background-color: white; color: red; font-family: verdana, Geneva, Arial, Helvetica, sans-serif; font-size: 13px; text-align: center;">$26.70)</span></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
BMP085 - Altímetro da BOSH com precisão de&nbsp;+-25cm segundo o datasheet</div>
<div style="text-align: justify;">
<a href="http://dx.com/p/bmp085-barometric-pressure-height-sensor-module-for-arduino-blue-148612">http://dx.com/p/bmp085-barometric-pressure-height-sensor-module-for-arduino-blue-148612</a>&nbsp;($7,20)</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<b><span style="font-size: x-large;">Câmeras</span></b></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
Existem soluções prontas de alta definição e também versões embarcadas.</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
ov7670 300kpixel 640x480 vga 30fps</div>
<div style="text-align: justify;">
<a href="http://dx.com/p/ov7670-300kp-vga-camera-module-for-arduino-147742">http://dx.com/p/ov7670-300kp-vga-camera-module-for-arduino-147742</a>&nbsp; (cerca de $12)</div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<span style="font-size: large;"><b>Referências</b></span>:</div>
<div style="text-align: justify;">
[ 1 ]&nbsp;<a href="http://www.scoutuav.com/">http://www.scoutuav.com/</a></div>
<div style="text-align: justify;">
[ 2 ]&nbsp;<a href="http://www.seeedstudio.com/depot/crazyflie-nano-quadcopter-kit-10dof-with-crazyradio-bccfk02b-p-1365.html">http://www.seeedstudio.com/depot/crazyflie-nano-quadcopter-kit-10dof-with-crazyradio-bccfk02b-p-1365.html</a></div>
<div style="text-align: justify;">
[ 3 ]&nbsp;<a href="http://www.flybrushless.com/">http://www.flybrushless.com/</a></div>
<div style="text-align: justify;">
[ 4 ]&nbsp;<a href="http://www.geek.com/science/spacex-video-shows-grasshopper-rocket-making-a-sci-fi-landing-1561397/">http://www.geek.com/science/spacex-video-shows-grasshopper-rocket-making-a-sci-fi-landing-1561397/</a></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
<div style="text-align: justify;">
<br/></div>
</div>