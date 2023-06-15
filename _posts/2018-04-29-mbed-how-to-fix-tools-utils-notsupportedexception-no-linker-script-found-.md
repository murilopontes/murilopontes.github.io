---
layout: post
title: MBED how to fix- tools.utils.NotSupportedException- No linker script found.
categories:
 - post
date: 2018-04-29 19:31:00 +0100
---

You try to export the MBED project to Eclipse, but the following error raise:  

  

&nbsp; &nbsp; raise NotSupportedException("No linker script found.")  

tools.utils.NotSupportedException: No linker script found.  

<div>
<br/></div>

To fix this problem append " --source $PWD" to command line.  

  

mbed export -m NUCLEO_F429ZI -i eclipse_gcc_arm --source $PWD  

  