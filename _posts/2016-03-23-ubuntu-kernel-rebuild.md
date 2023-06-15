---
layout: post
title: Ubuntu kernel Rebuild
categories:
 - Linux
date: 2016-03-23 18:10:00 +0000
---

<div>
<br/></div>

<div>
# Get source</div>

<div>
apt-get source linux-image-$(uname -r)</div>

<div>
<br/></div>

<div>
# Get tools</div>

<div>
apt-get build-dep linux-image-$(uname -r)</div>

<div>
<br/></div>

<div>
# Copy current config</div>

<div>
cp -v /boot/config-$(uname -r) &nbsp; .config</div>

<div>
<br/></div>

<div>
# Customize config</div>

<div>
make menuconfig</div>

<div>
<br/></div>

<div>
# parallel build</div>

<div>
make -j</div>

<div>
<br/></div>

<div>
# Install kernel modules first (~260MB with debug symbols stripped)</div>

make INSTALL_MOD_STRIP=1 modules_install  

<div>
<br/></div>

<div>
# Install kernel image (~6MB)<br/>
<div>
make install</div>
<div>
<br/></div>
<div>
# Reboot</div>
<div>
<br/></div>
<div>
<br/></div>
<div>
<br/></div>
<div>
References:</div>
<div>
https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel</div>
</div>

<div>
<br/></div>

<div>
<br/></div>