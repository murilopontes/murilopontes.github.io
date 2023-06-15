---
layout: post
title: Force all network traffic pass through OpenVPN tunnel
categories:
 - OpenVPN
date: 2016-04-17 17:07:00 +0100
---

  

# Flush all rules  

iptables -F  

  

# Let's change the policy to DROP.  

iptables -P INPUT DROP  

iptables -P FORWARD DROP  

iptables -P OUTPUT DROP  

  

# Allow basic INPUT traffic.  

iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT  

iptables -A INPUT -i lo -j ACCEPT  

iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT  

  

# Allow basic OUTPUT traffic.  

iptables -A OUTPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT  

iptables -A OUTPUT -o lo -j ACCEPT  

iptables -A OUTPUT -p icmp -j ACCEPT  

  

# Allow traffic to the OpenVPN server, DNS and via the tunnel.  

iptables -A OUTPUT -o tun+ -j ACCEPT  

iptables -A OUTPUT -p udp -m udp -d 8.8.8.8 --dport 53 -j ACCEPT  

iptables -A OUTPUT -p udp -m udp -d 8.8.4.4 --dport 53 -j ACCEPT  

iptables -A OUTPUT -p udp -m udp -d vpn.server.example.com --dport 1194 -j ACCEPT  

  

# Reject everything else.  

iptables -A INPUT -m conntrack --ctstate INVALID -j DROP  

iptables -A INPUT -j REJECT --reject-with icmp-port-unreachable  

iptables -A FORWARD -j REJECT --reject-with icmp-port-unreachable  

iptables -A OUTPUT -j REJECT --reject-with icmp-port-unreachable  

  

  