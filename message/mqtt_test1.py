"""
实现MQTT协议需要客户端和服务器端通讯完成，在通讯过程中，MQTT协议中有三种身份：
发布者（Publish）、代理（Broker）（服务器）、订阅者（Subscribe）。
其中，消息的发布者和订阅者都是客户端，消息代理是服务器，消息发布者可以同时是订阅者。

　　MQTT传输的消息分为：主题（Topic）和负载（payload）两部分：

　　（1）Topic，可以理解为消息的类型，订阅者订阅（Subscribe）后，就会收到该主题的消息内容（payload）；

　　（2）payload，可以理解为消息的内容，是指订阅者具体要使用的内容。
"""

import paho.mqtt.client as mqtt

broker_url = "mqtt.eclipse.org"
# HOST = "localhost"
PORT = 1883 #MQTT的默认端口号

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("/+")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))

def on_message_from_kitchen(client, userdata, message):
   print("Message Recieved from Kitchen: "+message.payload.decode())

def on_message_from_bedroom(client, userdata, message):
   print("Message Recieved from Bedroom: "+message.payload.decode())

# def on_message(client, userdata, message):
#    print("Message Recieved from Others: "+message.payload.decode())

def test():
    client = mqtt.Client()    # 可能需要设置ClientId
    client.username_pw_set("admin", "password")  # 必须设置，否则会返回「Connected with result code 4」 #设置用户后，只会收到该登录用户下的Topic,如果不设置，不受用户限制

    client.on_connect = on_connect
    client.on_message = on_message
    # client.connect(HOST, PORT, 210)
    client.connect(broker_url, PORT, 210)

    client.subscribe("TestingTopic", qos=1) #订阅主题
    client.subscribe("KitchenTopic", qos=1)
    client.subscribe("BedroomTopic", qos=1)
    # client.message_callback_add("KitchenTopic", on_message) #订阅不同主题，callback不一样
    # client.message_callback_add("BedroomTopic", on_message)
    client.message_callback_add("KitchenTopic", on_message_from_kitchen) #订阅不同主题，callback不一样
    client.message_callback_add("BedroomTopic", on_message_from_bedroom)

    client.publish(topic="KitchenTopic", payload="KitchenPayload", qos=1, retain=False)  # 发布在订阅之后才有效
    client.publish(topic="BedroomTopic", payload="BedroomPayload", qos=1, retain=False)

    # client.loop()
    client.loop_forever() #用来保持无穷阻塞调用loop()???没有该行代码为什么不可以？

if __name__ == '__main__':
    test()