---
layout: post
title: Instalando Sourcery G++ Lite no Ubuntu
categories:
 - post
date: 2013-11-26 19:26:00 +0000
---

Depois do teclado configurado, e compilado o SDK 2.0.1 do ardrone, é hora de dar prosseguimento ao build de ferramentas DIY para o ardrone.  

  

<a name="more"></a>  
  

Primeiro precisando instalar o cross-compiler que é compatível com a versão 1.7.6 do firmware do ardrone.  

  

<span style="background-color: #cfe2f3;">\# cat /proc/version</span>  

<span style="background-color: #cfe2f3;">Linux version 2.6.27.47-parrot (aferran@FR-B-800-0053) (gcc version 4.3.3 (Sourcery G++ Lite 2009q1-203) ) \#1 PREEMPT Tue Aug 30 12:05:09 CEST 2011</span>  

O kernel do Linux do ardrone foi compilado com o Sourcery G++ Lite 2009q1  

<div>
Como esse release de 2009 está um pouco antigo, fiz vários testes com o Sourcery G++ lite 2011.03.</div>

<div>
E recomendo usar ele nas experiências que seguem.</div>

<div>
Para instalar o Sourcery G++ lite é necessário ajustar o shell do Ubuntu, que por padrão usa a shell dash, que é incompatível com diversos scripts e causa vários problemas. Enfim, vamos remover essa shell esquisita e usar a consagrada Bash.</div>

<div>
<br/></div>

<div>
1) resolvendo problema da shell esquisita do Ubuntu</div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# rm /bin/sh</span></div>

<span style="background-color: #cfe2f3;">root@ubuntu:~\# ln -s /bin/bash /bin/sh</span>  

  

2) Baixar e instalar o Sourcery G++ lite  

<span style="background-color: #cfe2f3;">root@ubuntu:~\# &nbsp;wget https://sourcery.mentor.com/GNUToolchain/package8741/public/arm-none-linux-gnueabi/arm-2011.03-41-arm-none-linux-gnueabi.bin</span>  

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# chmod&nbsp;+x arm-2011.03-41-arm-none-linux-gnueabi.bin</span></div>

<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~#&nbsp;./arm-2011.03-41-arm-none-linux-gnueabi.bin</span></div>

<div>
<br/>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="http://1.bp.blogspot.com/-WjbJSBhrO4s/UpT1yW0zZFI/AAAAAAAAncs/XTtDb2xUKCk/s1600/instalando-codesourcery.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="239" src="http://1.bp.blogspot.com/-WjbJSBhrO4s/UpT1yW0zZFI/AAAAAAAAncs/XTtDb2xUKCk/s1600/instalando-codesourcery.png" width="320"/></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Instalando Sourcery G++ Lite no xUbuntu 12.04 32 bit</td></tr>
</tbody></table>
<br/>
<br/></div>

<div>
3) testando para ver se instalou tudo certo</div>

<div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# su -</span></div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~# arm-none-linux-gnueabi-gcc -v</span></div>
<div>
<span style="background-color: #cfe2f3;">Using built-in specs.</span></div>
<div>
<span style="background-color: #cfe2f3;">COLLECT_GCC=arm-none-linux-gnueabi-gcc</span></div>
<div>
<span style="background-color: #cfe2f3;">COLLECT_LTO_WRAPPER=/root/CodeSourcery/Sourcery_G++_Lite/bin/../libexec/gcc/arm-none-linux-gnueabi/4.5.2/lto-wrapper</span></div>
<div>
<span style="background-color: #cfe2f3;">Target: arm-none-linux-gnueabi</span></div>
<div>
<span style="background-color: #cfe2f3;">Configured with: /scratch/janisjo/arm-linux-lite/src/gcc-4.5-2011.03/configure --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu --target=arm-none-linux-gnueabi --enable-threads --disable-libmudflap --disable-libssp --disable-libstdcxx-pch --enable-extra-sgxxlite-multilibs --with-arch=armv5te --with-gnu-as --with-gnu-ld --with-specs='%{save-temps: -fverbose-asm} %{funwind-tables|fno-unwind-tables|mabi=*|ffreestanding|nostdlib:;:-funwind-tables} -D__CS_SOURCERYGXX_MAJ__=2011 -D__CS_SOURCERYGXX_MIN__=3 -D__CS_SOURCERYGXX_REV__=41 %{O2:%{!fno-remove-local-statics: -fremove-local-statics}} %{O*:%{O|O0|O1|O2|Os:;:%{!fno-remove-local-statics: -fremove-local-statics}}}' --enable-languages=c,c++ --enable-shared --enable-lto --enable-symvers=gnu --enable-__cxa_atexit --with-pkgversion='Sourcery G++ Lite 2011.03-41' --with-bugurl=https://support.codesourcery.com/GNUToolchain/ --disable-nls --prefix=/opt/codesourcery --with-sysroot=/opt/codesourcery/arm-none-linux-gnueabi/libc --with-build-sysroot=/scratch/janisjo/arm-linux-lite/install/arm-none-linux-gnueabi/libc --with-gmp=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-mpfr=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-mpc=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-ppl=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-host-libstdcxx='-static-libgcc -Wl,-Bstatic,-lstdc++,-Bdynamic -lm' --with-cloog=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --with-libelf=/scratch/janisjo/arm-linux-lite/obj/host-libs-2011.03-41-arm-none-linux-gnueabi-i686-pc-linux-gnu/usr --disable-libgomp --enable-poison-system-directories --with-build-time-tools=/scratch/janisjo/arm-linux-lite/install/arm-none-linux-gnueabi/bin --with-build-time-tools=/scratch/janisjo/arm-linux-lite/install/arm-none-linux-gnueabi/bin</span></div>
<div>
<span style="background-color: #cfe2f3;">Thread model: posix</span></div>
<div>
<span style="background-color: #cfe2f3;">gcc version 4.5.2 (Sourcery G++ Lite 2011.03-41)&nbsp;</span></div>
<div>
<span style="background-color: #cfe2f3;">root@ubuntu:~#&nbsp;</span></div>
</div>

<div>
<br/></div>