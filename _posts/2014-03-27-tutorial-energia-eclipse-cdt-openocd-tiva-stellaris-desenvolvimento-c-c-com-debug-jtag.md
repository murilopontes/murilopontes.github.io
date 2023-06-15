---
layout: post
title: Tutorial Energia + Eclipse CDT + OpenOCD + Tiva + Stellaris = Desenvolvimento C/C++ com debug+JTAG
categories:
 - tutorial
date: 2014-03-27 03:48:00 +0000
---

Tutorial completo com exemplos.  

  

<a name="more"></a>  
  

[update 2014/03/29]  

  

O código do projeto usado no projeto pode ser clonado do meu github  

https://github.com/murix/energia-0101E0012-eclipse-cdt-openocd  

  

[post original]  

  

Como montar um ambiente de desenvolvimento C/C++ para ARM embarcado?  

<div>
Minha sugestão é usar o já consagrado eclipse CDT com os toolkits / frameworks / compiladores do projeto Energia. O projeto Energia (http://energia.nu) é um fork do Arduino para as placas de desenvolvimento da Texas (MSP430 e ARM). Por ser um fork do Arduino, o projeto Energia sofre da falta de ferramentas de debug / JTAG. O projeto Energia já vem com a ferramenta de depuração GDB, mas carece de ferramentas para JTAG como o OpenOCD. Toda essa problemática de falta de ferramentas por ser resolvida facilmente. Como todas essas ferramentas são opensource, é só baixar todas e configurar tudo para funcionar junto.</div>

<div>
<br/></div>

<div>
<br/></div>

<div>
<b><span style="font-size: x-large;">1) Downloads das ferramentas</span></b></div>

<div>
<br/></div>

<div>
Então vamos ao que interessa, primeiro precisamos baixar todas ferramentas atualizadas.</div>

<div>
Este tutorial é voltado para Windows e Linux, infelizmente o MacOS X ficou de fora pois não tenho nenhum Mac para testar (aceito doações).</div>

<div>
<br/></div>

<div>
1) Eclipse CDT</div>

<div>
http://eclipse.c3sl.ufpr.br/technology/epp/downloads/release/kepler/SR2/eclipse-cpp-kepler-SR2-win32.zip</div>

<div>
<br/></div>

<div>
2) Energia&nbsp;</div>

<div>
http://energia.nu/download/downloadv3.php?file=energia-0101E0012-windows.zip</div>

<div>
<br/></div>

<div>
3) OpenOCD</div>

<div>
http://www.freddiechopin.info/en/download/category/4-openocd?download=99%3Aopenocd-0.7.0</div>

<div>
<br/></div>

<div>
No Linux (ArchLinux) algumas ferramentas podem ser instalados com uma única linha de comando:</div>

<div>
<br/></div>

<div>
1) Eclipse CDT e Openocd</div>

<div>
pacman -S eclipse-cdt openocd</div>

<div>
<br/></div>

<div>
2) Energia&nbsp;</div>

<div>
http://energia.nu/download/downloadv3.php?file=energia-0101E0012-linux.tgz (32bits)</div>

<div>
http://energia.nu/download/downloadv3.php?file=energia-0101E0012-linux64.tgz (64bits)</div>

<div>
<br/></div>

<div>
<span style="font-size: x-large;"><b>2) Montando o ambiente</b></span></div>

<div>
<br/></div>

<div>
O primeiro passo é extrair o eclipse-cdt, openocd e energia.</div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-u5s6iOYunrY/UzN8tCE2BSI/AAAAAAAApow/YmVS6-C0qQA/s1600/arm-toolchain.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="326" src="http://3.bp.blogspot.com/-u5s6iOYunrY/UzN8tCE2BSI/AAAAAAAApow/YmVS6-C0qQA/s1600/arm-toolchain.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Para facilitar recomendo criar uma pasta com todos os downloads das ferramentas e extrair tudo dentro.<br/>
Como exemplo, criei a pasta arm-toolchain e extrai as ferramentas dentro.</td></tr>
</tbody></table>

<div>
<br/>
<span style="font-size: x-large;"><b>3) Configurando o OpenOCD</b></span></div>

<div>
Primeiro vamos testar o OpenOCD que é o nosso debug / JTAG.</div>

<div>
O método é: abrir um terminal (windows+r, cmd.exe, enter) e fazer como abaixo</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-YS6oggEaedQ/UzN-VB_f_bI/AAAAAAAApo4/t1I7gLs1PZc/s1600/openocd-windows-firewall.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="640" src="http://2.bp.blogspot.com/-YS6oggEaedQ/UzN-VB_f_bI/AAAAAAAApo4/t1I7gLs1PZc/s1600/openocd-windows-firewall.JPG" width="600"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Ao executar o openocd pela primeira vez é preciso liberar as portas no firewall do windows,<br/>
ou então desativar o firewall do windows completamente.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-fSaxVS9JL_4/UzN_KWnc7yI/AAAAAAAAppA/txDPShHdPB0/s1600/openocd-lm4f120xl.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="152" src="http://1.bp.blogspot.com/-fSaxVS9JL_4/UzN_KWnc7yI/AAAAAAAAppA/txDPShHdPB0/s1600/openocd-lm4f120xl.jpg" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">OpenOCD usando configuração da board EK-LM4F120XL.<br/>
Esta configuração é usada para depurar a Stellaris LM4F120XL, Tiva C Series, Tiva Ethernet.</td></tr>
</tbody></table>

<div>
No windows algumas placas se recusam a funcionar com OpenOCD por motivo ainda desconhecido, no Linux todas as minhas 10 stellaris LM4F120XL e duas Tiva C Series, funcionaram sempre de primeira.</div>

<div>
Já atualizei o firmware de todas as 12 placas usando o LMFLASH Programmer como expliquei no outro post (http://dronespersonalizados.blogspot.com.br/2014/03/atualizar-firmware-do-icdi-jtag-da-tiva.html).</div>

<div>
Mas ainda não resolveu esse problema de somente algumas não funcionarem com o OpenOCD do Windows, se alguém tiver uma ideia ou souber a solução me conte. [ No Mac parece que o problema também não existe, o bug pelo jeito é no Windows 8 e 8.1 ]</div>

<div>
<br/></div>

<div>
O OpenOCD deve ficar aberto durante todo o processo de depuração, ele age como um servidor GDB na porta 3333. É nesta porta que vamos conectar o cliente GDB do Energia através do Eclipse CDT.</div>

<div>
<br/>
<b><span style="font-size: large;">4) Criando o projeto do Energia (C++) no Eclipse</span></b><br/>
<br/></div>

<div>
Agora vamos iniciar o Eclipse CDT e criar um novo projeto C++ com GCC Cross Compiler.</div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-mcRac8SSDK8/UzODXW6FGxI/AAAAAAAAppM/g9avywMCmaE/s1600/openocd-energia-demo.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="480" src="http://3.bp.blogspot.com/-mcRac8SSDK8/UzODXW6FGxI/AAAAAAAAppM/g9avywMCmaE/s1600/openocd-energia-demo.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">O projeto deve ser o C++ vazio com Cross GCC,</td></tr>
</tbody></table>

__<span style="font-size: large;">4.1 ) Configurando Cross Compiler</span>__  

  

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-U9c2CkVWUGc/UzOFFXvNSsI/AAAAAAAAppY/4rasvJE8dkQ/s1600/eclipse-cdt-cross-gcc.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="478" src="http://4.bp.blogspot.com/-U9c2CkVWUGc/UzOFFXvNSsI/AAAAAAAAppY/4rasvJE8dkQ/s1600/eclipse-cdt-cross-gcc.JPG" width="640"/></a><br/>
<br/></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na última tela de criação do projeto, é pedido para configurar o caminho do Cross GCC e o prefixo.<br/>
Para facilitar vamos usar o GCC do Energia, que está no caminho mostrado na foto.<br/>
Se você pode usar qualquer outro toolchain como: Linaro, Codesourcery, Mentor, buildroot,<br/>
mas se essa for a primeira vez, use o que vem no Energia que é de certeza funcionar.</td></tr>
</tbody></table>

<div>
<br/>
<b><span style="font-size: large;">4.2 ) Configurando tipo do Builder</span></b><br/>
<br/>
Nas propriedades do projeto é preciso mudar o tipo de builder<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td><a href="http://1.bp.blogspot.com/-nKmUHu5bhcA/UzOI9QJmYEI/AAAAAAAAppw/k7iN9ZAxK3U/s1600/eclipse-use-internal-builder.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="436" src="http://1.bp.blogspot.com/-nKmUHu5bhcA/UzOI9QJmYEI/AAAAAAAAppw/k7iN9ZAxK3U/s1600/eclipse-use-internal-builder.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="font-size: 13px;">Abra as configurações do projeto e mude o tipo de builder para "internal"</td></tr>
</tbody></table>
<br/></div>

<div>
<b><span style="font-size: large;">4.3 ) Adicionando arquivos para o projeto</span></b><br/>
<br/>
Vamos adicionar os arquivos do Energia.</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-s-BlLpEWLFY/UzOHdKnnibI/AAAAAAAAppk/HlD_el-k1rs/s1600/energia-copy-to-eclipse.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="484" src="http://3.bp.blogspot.com/-s-BlLpEWLFY/UzOHdKnnibI/AAAAAAAAppk/HlD_el-k1rs/s1600/energia-copy-to-eclipse.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">A pasta para se arrastar é a lm4f que fica dentro da pasta hardware do Energia,<br/>
quando terminar de copiar vai ficar como está na foto.<br/>
Para compilar esse código é preciso excluir da configuração algumas pastas.</td></tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><br/></td></tr>
</tbody></table>

<div>
<b><span style="font-size: large;">4.4 ) Excluindo do build bibliotecas não mandatórias</span></b><br/>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-OFeWxbAaADg/UzOKTbSPKlI/AAAAAAAApp4/hPFiNYcKl84/s1600/eclipse-exclude-libs-from-build.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="638" src="http://4.bp.blogspot.com/-OFeWxbAaADg/UzOKTbSPKlI/AAAAAAAApp4/hPFiNYcKl84/s1600/eclipse-exclude-libs-from-build.png" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Remova as libs marcadas de todos os builds (Debug e Release)</td></tr>
</tbody></table>

<div>
<br/>
<b><span style="font-size: large;">4.5 ) Configurando includes C e C++</span></b><br/>
<br/></div>

<div>
Configure no projeto os diretórios de include C e C++</div>

<div>
<div>
"${workspace_loc:/${ProjName}/lm4f/cores/lm4f}"</div>
<div>
"${workspace_loc:/${ProjName}/lm4f/libraries/EEPROM}"</div>
<div>
"${workspace_loc:/${ProjName}/lm4f/libraries/SPI}"</div>
<div>
"${workspace_loc:/${ProjName}/lm4f/libraries/Wire}"</div>
<div>
"${workspace_loc:/${ProjName}/lm4f/variants/stellarpad}"</div>
</div>

<div>
<br/></div>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-x-54YHDVfEc/UzOMUYZLQHI/AAAAAAAApqE/Y5Gk8fWvqac/s1600/eclipse-include-c-cpp.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="496" src="http://4.bp.blogspot.com/-x-54YHDVfEc/UzOMUYZLQHI/AAAAAAAApqE/Y5Gk8fWvqac/s1600/eclipse-include-c-cpp.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Configure os includes do C e C++, o projeto Energia precisa de ambos</td></tr>
</tbody></table>

<div>
<span style="font-size: large;"><b>4.6) Configurações Misc do Compilador</b></span><br/>
<br/>
Nas configurações Misc do Projeto é preciso complementar a linha:<br/>
-c -fmessage-length=0<br/>
<br/>
Com esse trecho para C++:</div>

<div>
-fno-rtti -fno-exceptions -ffunction-sections -fdata-sections -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -fsingle-precision-constant -DF_CPU=80000000L -DARDUINO=101 -DENERGIA=12</div>

<div>
<br/>
Com esse trecho em C (tudo do C++ menos o RTTI ):</div>

<div>
-fno-exceptions -ffunction-sections -fdata-sections -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -fsingle-precision-constant -DF_CPU=80000000L -DARDUINO=101 -DENERGIA=12</div>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-GoKJJwtptaY/UzOO5DfFCfI/AAAAAAAApqQ/ckWWeUtzQIA/s1600/eclipse-cdt-misc.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="496" src="http://4.bp.blogspot.com/-GoKJJwtptaY/UzOO5DfFCfI/AAAAAAAApqQ/ckWWeUtzQIA/s1600/eclipse-cdt-misc.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Configurações MISC do projeto</td></tr>
</tbody></table>
<br/>
<span style="font-size: large;"><b>4.7) Configurações Misc do Linker</b></span><br/>
<br/>
Também é necessário configurar o linker MISC do GCC com o seguinte trecho:<br/>
&nbsp;-Os -nostartfiles -nostdlib -Wl,--gc-sections -T &nbsp;"${workspace_loc:/${ProjName}/lm4f/cores/lm4f/lm4fcpp_blizzard.ld}" -Wl,--entry=ResetISR -mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -fsingle-precision-constant&nbsp;</div>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-na-6FK3mXso/UzORq_iQBCI/AAAAAAAApqc/OKolqky6m0w/s1600/eclipse-cdt-linker-misc.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="466" src="http://4.bp.blogspot.com/-na-6FK3mXso/UzORq_iQBCI/AAAAAAAApqc/OKolqky6m0w/s1600/eclipse-cdt-linker-misc.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Configure o link flags com o trecho indicado acima</td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: center;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
<b><span style="font-size: large;">4.8) Bibliotecas mandatórias para o Linker</span></b></div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
É preciso configurar quais bibliotecas do GCC são linkadas ao projeto</div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-OHnWoB9q-Kk/UzOVH97TkzI/AAAAAAAApq0/xi_DZYaMwTI/s1600/eclipse-cdt-linker-libs.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="458" src="http://4.bp.blogspot.com/-OHnWoB9q-Kk/UzOVH97TkzI/AAAAAAAApq0/xi_DZYaMwTI/s1600/eclipse-cdt-linker-libs.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">GCC Linker libs - o projeto Energia depende dos libs: m, c, gcc.<br/>
(math , c runtine, gcc runtine)</td></tr>
</tbody></table>
<div class="separator" style="clear: both; text-align: justify;">
<b><span style="font-size: large;">4.9 ) Criando um Sketch</span></b></div>
<div class="separator" style="clear: both; text-align: justify;">
<br/></div>
<div class="separator" style="clear: both; text-align: justify;">
Crie um arquivo chamado sketch.cpp com o conteúdo da foto&nbsp;</div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-uGK_5oVflP0/UzOTDUXPluI/AAAAAAAApqo/uRHIcXOdBhE/s1600/eclipse-create-sketch.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="324" src="http://1.bp.blogspot.com/-uGK_5oVflP0/UzOTDUXPluI/AAAAAAAApqo/uRHIcXOdBhE/s1600/eclipse-create-sketch.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Arquivo sketch.cpp segue o mesmo estilo do Energia com IDE de Arduino.<br/>
A única diferença é o include para o Energia.h<br/>
Agora toda a API do Energia está pronta para usar: digitalWrite, digitalRead, .analogWrite, analogRead, ..</td></tr>
</tbody></table>
<b><span style="font-size: large;">4.10) Build</span></b><br/>
<br/>
Agora está tudo pronto para fazer o build.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-NlxmEBw937w/UzOV7_kvgGI/AAAAAAAApq8/yvGd9sSLd6s/s1600/eclipse-build-energia-ok.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="378" src="http://1.bp.blogspot.com/-NlxmEBw937w/UzOV7_kvgGI/AAAAAAAApq8/yvGd9sSLd6s/s1600/eclipse-build-energia-ok.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Build do Energia usando o Eclipse perfeito, sem nenhum warning!<br/>
<br/></td></tr>
</tbody></table>
Após o build, o que temos é um arquivo ELF para ARM de 32 bit, que não pode ser gravado diretamente na placa. Para converter de ELF para binário é usada a ferramenta arm-none-eabi-objcopy. Mas não vou entrar em detalhes, pois o foco deste tutorial é gravar e depurar tudo automaticamente usando o OpenOCD.<br/>
<br/>
Lembra do OpenOCD no terminal, ele ainda deve estar aberto, pois agora vamos gravar o projeto usando o GDB client conectado no OpenOCD, tudo isso de dentro do eclipse no view de debug.<br/>
<br/>
<b><span style="font-size: large;">5) Instalar o plugin do GDB para debug de Hardware</span></b><br/>
<br/>
No eclipse, vá até o menu "help" e escolha "install new software"<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-VMmmNaYu4uY/UzOYPCToA6I/AAAAAAAAprI/uDscgydVCJs/s1600/eclipse-mobile-c++-gdb-hardware-debugging.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="494" src="http://1.bp.blogspot.com/-VMmmNaYu4uY/UzOYPCToA6I/AAAAAAAAprI/uDscgydVCJs/s1600/eclipse-mobile-c++-gdb-hardware-debugging.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Escolha o repositório padrão do eclipse,<br/>
no grupo "Mobile and Device Development",<br/>
instale o "C/C++ GDB Hardware Debugging"</td></tr>
</tbody></table>
<b><span style="font-size: large;">6 ) Depurando o projeto com GDB</span></b><br/>
<br/>
Depois de concluída a instalação do C/C++ GDB Hardware Debugging,<br/>
vamos criar um configuração de debug para gravar o Energia recém compilado na placa pelo OpenOCD.<br/>
No eclipse, vá no menu "run", escolha "Debug configurations", e crie uma nova configuração como está na foto.<br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://2.bp.blogspot.com/-JS2bDBIv8eQ/UzOZ3GNG0CI/AAAAAAAAprU/Bj_tunb6BbA/s1600/eclipse-debug-GDB.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="466" src="http://2.bp.blogspot.com/-JS2bDBIv8eQ/UzOZ3GNG0CI/AAAAAAAAprU/Bj_tunb6BbA/s1600/eclipse-debug-GDB.JPG" width="640"/></a><br/>
<br/></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Crie uma nova configuração de debug do tipo GDB Hardware Debbuging</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><div style="text-align: justify;">
<span style="font-size: large;"><b>6.1 ) Configurando GDB: caminho e porta</b></span></div>
<div style="text-align: justify;">
<br/></div>
<a href="http://3.bp.blogspot.com/-Shwt4U85Y-s/UzOa1_LtofI/AAAAAAAAprc/b1bgGsd_Df4/s1600/eclipse-gdb-port.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="466" src="http://3.bp.blogspot.com/-Shwt4U85Y-s/UzOa1_LtofI/AAAAAAAAprc/b1bgGsd_Df4/s1600/eclipse-gdb-port.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na aba Debugger, mude a porta para 3333 e configure o caminho para o GDB.<br/>
O GDB é o cliente do servidor OpenOCD.</td></tr>
</tbody></table>
<b><span style="font-size: large;">6.2 ) Configurando comandos do GDB</span></b></div>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-y8zV10fAmWc/UzOcMUKFZFI/AAAAAAAApro/CXmXlKVnQPw/s1600/eclipse-gdb-startup.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="528" src="http://4.bp.blogspot.com/-y8zV10fAmWc/UzOcMUKFZFI/AAAAAAAApro/CXmXlKVnQPw/s1600/eclipse-gdb-startup.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na aba startup, desmarque a opção "reset and delay" e "halt",<br/>
na caixa de comandos de inicialização escreva: "monitor reset halt"<br/>
na caixa de "run commands" escreva: "monitor reset init",<br/>
dê "apply"e depois "debug" para iniciar a gravação do Energia na placa junto com a View de Debug do Eclipse</td></tr>
</tbody></table>
<b><span style="font-size: x-large;">7) Debug View&nbsp;</span></b><br/>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-kW16Nx_eRt0/UzOdWQwjspI/AAAAAAAAprw/Gj6pN85wlzI/s1600/eclipse-debug-view.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="378" src="http://4.bp.blogspot.com/-kW16Nx_eRt0/UzOdWQwjspI/AAAAAAAAprw/Gj6pN85wlzI/s1600/eclipse-debug-view.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Na view &nbsp;debug do eclipse, as possibilidades são infinitas,<br/>
pode rodar o código step by step, editar as variáveis na RAM no meio da execução,<br/>
além de inúmeros outros recursos, .....</td></tr>
</tbody></table>
<b><span style="font-size: large;">8) Monitorando OpenOCD</span></b><br/>
<br/>
Enquanto isso o OpenOCD está executado todos os comandos enviados pelo Eclipse/GDB.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-7s6ECIM2OLE/UzOfTtqORWI/AAAAAAAApsA/HZKPH_kNe9Q/s1600/openocd-debugging.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="252" src="http://1.bp.blogspot.com/-7s6ECIM2OLE/UzOfTtqORWI/AAAAAAAApsA/HZKPH_kNe9Q/s1600/openocd-debugging.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">OpenOCD debugging</td></tr>
</tbody></table>
<b><span style="font-size: x-large;">9 ) Monitorando porta Serial</span></b><br/>
<br/>
Para concluir com chave de ouro vamos ver se no terminal serial está chegando o texto que foi programado no sketch.<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-xE2OlA0BSTo/UzOem-VT8EI/AAAAAAAApr4/w5U1lTSmVcY/s1600/eclipse-sketch-console.JPG" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://4.bp.blogspot.com/-xE2OlA0BSTo/UzOem-VT8EI/AAAAAAAApr4/w5U1lTSmVcY/s1600/eclipse-sketch-console.JPG" width="640"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Sketch do Energia compilado no Eclipse e gravado e depurado com GDB e OpenOCD</td></tr>
</tbody></table>
<br/>
<span style="font-size: x-large;"><b>10) Considerações finais</b></span><br/>
<br/>
Este tutorial introduziu o uso da API do Energia com um exemplo seguido da depuração com GDB / OpenOCD.<br/>
O próximo tutorial irá introduzir o FreeRTOS no projeto.<br/>
<br/>
<br/>
<br/></div>

<div>
<br/></div>

<div>
<br/></div>

<div>
<br/></div>

<div>
<br/></div>