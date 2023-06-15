---
layout: post
title: prevent hard disk from going to sleep in windows
categories:
 - post
date: 2016-07-31 17:59:00 +0100
---

<pre>
powercfg -x disk-timeout-ac 0
powercfg -x disk-timeout-dc 0
</pre>