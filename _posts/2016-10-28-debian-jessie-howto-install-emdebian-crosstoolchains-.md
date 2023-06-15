---
layout: post
title: Debian Jessie howto install Emdebian CrossToolchains 
categories:
 - Debian
date: 2016-10-28 14:11:00 +0100
---

<pre>
echo deb http://emdebian.org/tools/debian/ jessie main &gt; /etc/apt/sources.list.d/crosstools.list
apt-get install -y curl
curl http://emdebian.org/tools/debian/emdebian-toolchain-archive.key | sudo apt-key add -
sudo dpkg --add-architecture arm64
sudo dpkg --add-architecture armel
sudo dpkg --add-architecture armhf
sudo dpkg --add-architecture mips
sudo dpkg --add-architecture mipsel
sudo dpkg --add-architecture powerpc
sudo dpkg --add-architecture ppc64el
sudo apt-get update
sudo apt-get install crossbuild-essential-arm64
sudo apt-get install crossbuild-essential-armel
sudo apt-get install crossbuild-essential-armhf
sudo apt-get install crossbuild-essential-mipsel
sudo apt-get install crossbuild-essential-ppc64el
</pre>

<pre>
# I found problems with powerpc toolchain
sudo apt-get install crossbuild-essential-powerpc

# libc6:powerpc is broken 
Unpacking libc6:powerpc (2.19-18+deb8u6) ...
dpkg: error processing archive /var/cache/apt/archives/libc6_2.19-18+deb8u6_powerpc.deb (--unpack):
 trying to overwrite shared '/lib/ld.so.1', which is different from other instances of package libc6:powerpc

# remove broken powerpc toolchain
sudo apt-get remove libatomic1:powerpc libc6-dev:powerpc libgcc1:powerpc libgomp1:powerpc libstdc++6:powerpc crossbuild-essential-powerpc libgcc-4.9-dev:powerpc libstdc++-4.9-dev:powerpc g++-4.9-powerpc-linux-gnu gcc-4.9-powerpc-linux-gnu g++-powerpc-linux-gnu gcc-powerpc-linux-gnu
</pre>