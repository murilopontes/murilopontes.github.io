---
layout: post
title: openwrt set wan with random mac
categories:
 - post
date: 2016-07-20 18:31:00 +0100
---

<pre>uci set network.wan.macaddr=$(hexdump -n6 -e '6/1 ":%02X"' /dev/urandom | cut -f2- -d ":")
uci commit
</pre>