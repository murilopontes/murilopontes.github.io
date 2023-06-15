---
layout: page
title: Artigo- Bitcoin e LiteCoin
categories:
 - page
date: 2020-04-25 04:17:00 +0100

---

<div>
Guia básico para começar a minerar crypto currencies.<br/>
<br/></div>

<div>
<br/></div>

<div>
<b><u>O básico para minerar bitcoin</u></b><br/>
<br/></div>

<div>
1) Criar uma carteira de bitcoin&nbsp;</div>

<div>
<a href="https://blockchain.info/">https://blockchain.info</a></div>

<div>
<br/></div>

<div>
2) Baixar o software minerador para CPU</div>

<http://sourceforge.net/projects/cpuminer/files/>  

<div>
<br/></div>

<div>
3) Rodar o software conectado em algum pool de mineração&nbsp;</div>

<div>
<div>
minerd --url=stratum+tcp://us.clevermining.com:3333 --userpass=<b><span style="color: red;">numero_da_carteira</span></b>:anything</div>
</div>

<div>
bfgminer -o us1.eclipsemc.com:3333 -O&nbsp;<b><span style="color: red;">numero_da_carteira</span></b><br/>
cgminer -o us1.eclipsemc.com:3333 -u&nbsp;<b><span style="color: red;">numero_da_carteira</span></b>&nbsp;-p x -I 9<br/>
<br/></div>

<div>
4) Verificar as estatísticas da mineração</div>

<div>
<span style='background-color: white; font-family: "open sans" , sans-serif; font-size: 13px; line-height: 18.5714282989502px;'>http://www.clevermining.com/users/</span><b><span style="color: red;">numero_da_carteira</span></b></div>

<div>
<br/></div>

<div>
5) Trocar os bitcoins minerados por Reais / R$ / &nbsp;BRL</div>

<div>
<a href="https://www.mercadobitcoin.com.br/">https://www.mercadobitcoin.com.br/</a><br/>
<br/>
<b><u>O básico para minerar litecoin</u></b><br/>
<br/>
1) Criar um endereço litecoin<br/>
Vá <a href="https://litecoin.org/">https://litecoin.org/</a> , baixe e instalar o Eletrum Litecoin<br/>
<br/>
2) Baixar o software minerador para CPU<br/>
<a href="http://sourceforge.net/projects/cpuminer/files/">http://sourceforge.net/projects/cpuminer/files/</a><br/>
<br/>
3) Conectar no pool de mineração<br/>
<a href="https://www.litecoinpool.org/">https://www.litecoinpool.org</a><br/>
No campo "Payment address" coloque o endereço gerado pelo Eletrum Litecoin<br/>
<br/>
4) Rodar o software de mineração com o login e senha de cada Worker<br/>
minerd --url=stratum+tcp://us.litecoinpool.org:3333 --userpass=<b><span style="color: red;">usuario</span></b>:<b><span style="color: red;">senha</span></b><br/>
bfgminer -S opencl:auto --scrypt -o stratum+tcp://us.litecoinpool.org:3333 -u <b><span style="color: red;">user</span></b> -p <span style="color: red;"><b>senha</b></span><br/>
<br/>
5) Acompanhar o progresso pelo portal do pool de mineração<br/>
<a href="https://www.litecoinpool.org/account">https://www.litecoinpool.org/account</a><br/>
<br/>
<div>
6) Trocar os litecoins minerados por Reais / R$ / &nbsp;BRL</div>
<div>
<a href="https://www.mercadobitcoin.com.br/">https://www.mercadobitcoin.com.br/</a></div>
<br/>
<b><u>O básico para minerar com GPU / OpenCL</u></b><br/>
<br/>
1) Instalar o driver fglrx<br/>
2) Instalar o AMD OpenCL APP SDK<br/>
<br/>
bfgminer -S opencl:auto -n<br/>
<br/>
&nbsp;[2015-08-25 15:21:56] CL Platform 0 vendor: Advanced Micro Devices, Inc.<br/>
&nbsp;[2015-08-25 15:21:56] CL Platform 0 name: AMD Accelerated Parallel Processing<br/>
&nbsp;[2015-08-25 15:21:56] CL Platform 0 version: OpenCL 2.0 AMD-APP (1729.3)<br/>
&nbsp;[2015-08-25 15:21:56] Platform 0 devices: 1<br/>
&nbsp;[2015-08-25 15:21:56] <span class="Apple-tab-span" style="white-space: pre;"> </span>0<span class="Apple-tab-span" style="white-space: pre;"> </span>Redwood<br/>
&nbsp;[2015-08-25 15:21:56] GPU 0 AMD Mobility Radeon HD 5000 Series hardware monitoring enabled<br/>
&nbsp;[2015-08-25 15:21:56] 1 GPU devices max detected<br/>
<div>
<br/></div>
bfgminer -S opencl:auto --scrypt<br/>
<br/>
<br/>
<br/>
<br/></div>