---
layout: post
title: Debugando ardrone v1 rebelde, e chegada do GPS, barômetro, hélices e carregador B3AC. 
categories:
 - bitola
date: 2013-11-20 01:09:00 +0000
---

  

Hoje foi um dia produtivo, depois de mexer nas entranhas do ardrone, praticamente confirmei minha teoria no bug no ADC que mede a tensão e corrente da bateria.   

<a name="more"></a>Fato é que eliminando o monitorando de tensão do ardrone ele voa normal até a bateria atingir o limiar descarga de 9V. A bateria completamente carregada tem 12,55V.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-KW1gbvQcR3k/UowCsx0W1UI/AAAAAAAAnWc/dkue2A6vHkI/s1600/IMG_20131119_130016.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-KW1gbvQcR3k/UowCsx0W1UI/AAAAAAAAnWc/dkue2A6vHkI/s320/IMG_20131119_130016.jpg" width="240"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Primeira coisa a fazer é eliminar a bateria suspeita de problema do processo.<br/>
Para isso foi utilizada uma fonte de PC genérica datada de 2006 e fornece até 14A no linha de 12V.<br/>
Com a ligação acima e o firmware no modificado, é possível testar o motores na velocidade máxima de 43 mil RPM.<br/>
Depois de vários teste de alguns minutos a solução se mostrou estável sem falhar nenhuma vez.</td></tr>
</tbody></table>

Só que não dá para voar com um fio deste tamanho. Dai fui troca esse pedaço de preto e amarelo por um fio de extensão de 3 metros, com bitola de menos de 1 mm, mas essa solução não foi feliz. O drone até liga mas fica com resets aleatórios por causa da bitola que é muito fina para sugar a corrente necessária. Dai troquei o fio por outro de bitola de 3 mm que resolveu o problema, e deixou tão estão quanto ligar direto na fonte.  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-bT-RiRYc1CQ/UowE1SuvJ6I/AAAAAAAAnWo/dznUPPWd-cQ/s1600/IMG_20131119_140059.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://3.bp.blogspot.com/-bT-RiRYc1CQ/UowE1SuvJ6I/AAAAAAAAnWo/dznUPPWd-cQ/s320/IMG_20131119_140059.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Drone com fio verde de 3 mm de bitola, ficou tão estável quanto ligar direto na fonte.</td></tr>
</tbody></table>

  

A instalação do firmware opensource é um tanto extensa que vai ficar para outro post, mais em suma, não pode se usar a última versão (1.11.5) de FW que o Freefight do Android instala no drone. Tive de fazer o downgrade para a versão 1.7.6 que era a inicial quando comprei o drone. Com a versão 1.11.5 o código do firmware opensource não consegue inicializar os sensores de navegação (IDG500 e sonar), dai nem consegue decolar. Com a versão 1.7.6, o programa de teste dos sensores de navegação inicializa de primeira e rodar macio e suave como uma pena :D. Para iniciar o novo programa de navegação é necessário matar o processo program.elf (programa oficial que vem no firmware). Após a morte do program.elf, é só iniciar o programa "fly" que vai ser o novo sistema de navegação. No meus testes iniciais com o fly, o Drone decola mais ainda não está muito estável o controle PID só implementa a parte D (derivativa do controle).  

O código está no meu fork do projeto Ardrone no github, depois faço outro post explicando tudo isso com mais detalhes.  

  

Abaixo uma parte do teste de estabilidade com o fio de bitola de 3 mm.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/oMWpWfbdflA" width="560"></iframe>

  

Testando o motores com o programa "rotorboard" que faz parte do firmware opensource forkado no github.  

  

<iframe allowfullscreen="" frameborder="0" height="315" src="//www.youtube.com/embed/OICf9WwICh8" width="560"></iframe>

  

  

Teve mais alguns experimentos com o programa "fly" mas acabei não gravando o drone fazendo a decolagem com ele.  

  

Já no fim do dia chegaram mais algumas partes do outro drone mais potente. Dessa vez chegou as hélices 9x5, 10x4.5, 10x6, carregador B3AC (800mA de carga), o GPS Ublox Neo-6N, o barômetro BMP085 / GY-65, e o conversor de XT60-macho para T-deans-fêmea.  

  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-JgKGJWd5lEI/UowJV3730II/AAAAAAAAnWw/ckrH0wV1J9s/s1600/IMG_20131119_204018.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://2.bp.blogspot.com/-JgKGJWd5lEI/UowJV3730II/AAAAAAAAnWw/ckrH0wV1J9s/s320/IMG_20131119_204018.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Pacote de peças do drone</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-teFLjnXZ6_o/UowKQ9w9I4I/AAAAAAAAnW4/MEH5FtPltiE/s1600/IMG_20131119_203800.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="240" src="http://4.bp.blogspot.com/-teFLjnXZ6_o/UowKQ9w9I4I/AAAAAAAAnW4/MEH5FtPltiE/s320/IMG_20131119_203800.jpg" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Já deu para carregar a bateria do drone com o B3AC, que ficou verde quando a bateria atingiu os 12,55V.<br/>
Pelo jeito o carregador original do drone deve ter um bug também, já que com o B3AC carregou sem frescura.</td></tr>
</tbody></table>

  

  

  

  

  