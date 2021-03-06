import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("chat")
    client.publish("chat", json.dumps({"user": user, "say": "Hello,anyone!"}))


def on_message(client, userdata, msg):
    #print(msg.topic+":"+str(msg.payload.decode()))
    #print(msg.topic+":"+msg.payload.decode())
    payload = json.loads(msg.payload.decode())
    print(payload.get("user")+":"+payload.get("say"))


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set("admin", "password")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message

    # HOST = "127.0.0.1"
    HOST = "localhost"
    PORT = 1883

    client.connect(HOST, PORT, 60)
    #client.loop_forever()

    user = input("Please input name:")
    client.user_data_set(user) # Set the user data variable passed to callbacks

    client.loop_start()

    # str = input()
    # if str:
    #     client.publish("chat", json.dumps({"user": user, "say": str}))

    while True:
        str = input()
        if str:
            client.publish(topic="chat", payload=json.dumps({"user": user, "say": str}))