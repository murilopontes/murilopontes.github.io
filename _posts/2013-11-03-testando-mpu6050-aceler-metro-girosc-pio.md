---
layout: post
title: Testando MPU6050 - Acelerômetro & Giroscópio
categories:
 - post
date: 2013-11-03 15:38:00 +0000
---

Testando o acelerômetro a intensidade dos leds variando em função da inclinação.  

Implementada task do driver do MPU-6050 no FreeRTOS com API do Arduino/Energia  

  

<a name="more"></a>  
  

led verde: posição estável.  

led vermelho: inclinação no eixo x em relação a gravidade  

led azul: inclinação no eixo y em relação a gravidade  

  

O MPU-6050 fornece:  

- Acelerômetro: aceleração nos eixos x,y,z em m/s^2  

- Giroscópio: velocidade angular nos eixos x,y,z em rad/s  

- Temperatura: em graus&nbsp;<span style="background-color: white; color: #444444; font-family: arial, sans-serif; font-size: x-small; font-weight: bold; line-height: 16px;">Celsius.</span>  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/Qzp3Nm3zKIs" width="420"></iframe>