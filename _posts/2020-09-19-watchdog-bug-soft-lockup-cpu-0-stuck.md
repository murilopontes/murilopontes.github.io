---
layout: post
title: watchdog- BUG- soft lockup - CPU#0 stuck
categories:
 - post
date: 2020-09-19 21:25:00 +0100
---

&nbsp;systemd freezing execution

<div class="separator" style="clear: both; text-align: center;"><a href="https://lh3.googleusercontent.com/-VxupUPA4l5c/X2YkPG30hNI/AAAAAAACJ6A/elmlAxaeoAobWLY24VgsYGndv7Rmkw26ACNcBGAsYHQ/image.png" style="margin-left: 1em; margin-right: 1em;"><img alt="" data-original-height="182" data-original-width="953" src="https://lh3.googleusercontent.com/-VxupUPA4l5c/X2YkPG30hNI/AAAAAAACJ6A/elmlAxaeoAobWLY24VgsYGndv7Rmkw26ACNcBGAsYHQ/s16000/image.png"/></a></div>

  

<div><div>To mitigate this in Cloudatcost.com, you can put this in crontab:</div><div><br/></div><div>0 0 * * * reboot &gt;/dev/null 2&gt;&amp;1</div><div>0 12 * * * pacman -Syu --noconfirm &gt;/dev/null 2&gt;&amp;1</div></div>

<div><br/></div>