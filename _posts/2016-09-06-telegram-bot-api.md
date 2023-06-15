---
layout: post
title: telegram bot api
categories:
 - post
date: 2016-09-06 13:11:00 +0100
---

<pre>
1) get an apikey from @botfather

2) check bot
curl -i -X GET https://api.telegram.org/bot{apikey}/getMe

3) get chatid 
curl -i -X GET https://api.telegram.org/bot{apikey}/getUpdates

4) be happy
curl -i -X GET https://api.telegram.org/bot{apikey}/sendMessage?chat_id={chatId}&amp;text={someText}
</pre>