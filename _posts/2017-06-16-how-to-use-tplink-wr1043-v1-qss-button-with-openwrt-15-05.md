---
layout: post
title: how to use tplink wr1043 v1 qss button with openwrt 15.05
categories:
 - post
date: 2017-06-16 20:43:00 +0100
---

Create missing folder
  

<pre class="brush: js">mkdir -p /etc/hotplug.d/button
</pre>

Create missing event debug handler /etc/hotplug.d/button/buttons
  

<pre class="brush: js">logger the button was $BUTTON and the action was $ACTION
</pre>

Create missing button event handler /etc/hotplug.d/button/00-button
  

<pre class="brush: js">#!/bin/sh
. /lib/functions.sh
do_button () {
        local button
        local action
        local handler
        local min
        local max

        config_get button $1 button
        config_get action $1 action
        config_get handler $1 handler
        config_get min $1 min
        config_get max $1 max

        [ "$ACTION" = "$action" -a "$BUTTON" = "$button" -a -n "$handler" ] &amp;&amp; {
                [ -z "$min" -o -z "$max" ] &amp;&amp; eval $handler
                [ -n "$min" -a -n "$max" ] &amp;&amp; {
                        [ $min -le $SEEN -a $max -ge $SEEN ] &amp;&amp; eval $handler
                }
        }
}

config_load system
config_foreach do_button button
</pre>

Configure buttons, so append at the end of /etc/system/config

  

<pre class="brush: js">config button
        option button 'wps'
        option action 'pressed'
        option handler 'echo 1 &gt; /sys/class/leds/tp-link\:green\:qss/brightness'

config button
        option button 'wps'
        option action 'released'
        option handler 'echo 0 &gt; /sys/class/leds/tp-link\:green\:qss/brightness'
</pre>