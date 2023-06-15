---
layout: post
title: Testando motores na launchpad e monitorando PWM com BusPirate
categories:
 - LM4F120H5QR
date: 2013-11-04 03:15:00 +0000
---

Depois de remove o R9 e R10 chegou a hora de testar os motores na launchpad (<span style="background-color: white; color: #333333; font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 15px; line-height: 25px;">LM4F120H5QR</span><span style="background-color: white; color: #333333; font-family: Helvetica, arial, freesans, clean, sans-serif; font-size: 15px; line-height: 25px;">&nbsp;</span>).  

o duty cycle para ativar os motores é um pouco diferente do usado no Arduino Nano v3 (atmega328p).  

<a name="more"></a>  

Agora já dá para configurar a velocidade pelo Bitlash que integrei junto com o FreeRTOS e Energia,  

Próximo passo é ajustar a velocidade do motores em função do acelerômetro.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/-bGe8sgkUQw" width="420"></iframe>