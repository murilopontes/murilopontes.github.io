---
layout: post
title: RabbitMQ server configure 
categories:
 - MQTT
date: 2016-08-10 05:58:00 +0100
---

<pre>
# enable plugins and restart
rabbitmq-plugins enable rabbitmq_management
rabbitmq-plugins enable rabbitmq_mqtt
rabbitmq-plugins enable rabbitmq_web_stomp
rabbitmq-plugins enable rabbitmq_shovel
rabbitmq-plugins enable rabbitmq_management_visualiser 
rabbitmq-plugins enable rabbitmq_recent_history_exchange 
rabbitmq-plugins enable rabbitmq_top 
rabbitmq-plugins enable rabbitmq_tracing

# install and enable mqtt over websockets
cd /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.5/plugins
wget http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_web_mqtt-3.6.x-3b6a09bb.ez
 rabbitmq-plugins enable rabbitmq_web_mqtt

/etc/init.d/rabbitmq-server restart

#change default passwrd
rabbitmqctl change_password guest s0m3p4ssw0rd

#configure new user
rabbitmqctl add_user newadmin s0m3p4ssw0rd
rabbitmqctl set_user_tags newadmin administrator
rabbitmqctl set_permissions -p / newadmin ".*" ".*" ".*"

</pre>

Generate SSL/TLS chain

<pre></pre>

Edit /etc/rabbitmq/rabbitmq.config

<pre>
[
 {rabbit,
   {ssl_listeners, [5671]},
    {ssl_options, [
     {cacertfile,           "/opt/rabbitmq-ssl/testca/cacert.pem"},
     {certfile,             "/opt/rabbitmq-ssl/server/cert.pem"},
     {keyfile,              "/opt/rabbitmq-ssl/server/key.pem"},
     {verify,               verify_peer},
     {fail_if_no_peer_cert, false}]}
  ]},
 {rabbitmq_mqtt,
    {default_user, &lt;&lt;"guest"&gt;&gt;},
    {default_pass, &lt;&lt;"guest"&gt;&gt;},
    {allow_anonymous, true},
    {tcp_listeners, [1883]},
    {ssl_listeners, [8883]}
  ]},
].
</pre>

Restart server

<pre>
/etc/init.d/rabbitmq-server restart

#Test TLS
openssl s_client -connect 127.0.0.1:5671 -tls1

# Test MQTT
mosquitto_sub -h localhost -v -t '#'
mosquitto_pub -h localhost -t 'test' -m 'msg'

# Test MQTT with TLS
mosquitto_sub -h localhost -p 8883 -v -t '#' \
 --key /opt/rabbitmq-ssl/client/key.pem \
 --cert /opt/rabbitmq-ssl/client/cert.pem \
 --cafile /opt/rabbitmq-ssl/testca/cacert.pem
mosquitto_pub -h localhost -p 8883 -t 'test' -m 'msg' \
 --key /opt/rabbitmq-ssl/client/key.pem \
 --cert /opt/rabbitmq-ssl/client/cert.pem \
 --cafile /opt/rabbitmq-ssl/testca/cacert.pem

</pre>