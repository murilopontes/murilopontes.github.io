---
layout: post
title: Scaling up number of tcp/ip connections in linux
categories:
 - Linux
date: 2016-08-23 16:25:00 +0100
---

<pre>#as client
sysctl net.ipv4.ip_local_port_range="20000 65535"
sysctl net.ipv4.tcp_fin_timeout=30

#as server
ifconfig eth0 txqueuelen 10000
sysctl net.core.somaxconn=10240
sysctl net.core.netdev_max_backlog=10000
sysctl net.ipv4.tcp_max_syn_backlog=2560
echo 3000000 &gt; /proc/sys/fs/nr_open
ulimit -n 2000000
</pre>