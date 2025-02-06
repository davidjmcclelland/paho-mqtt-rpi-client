# python 3.11

import random
import time

from paho.mqtt import client as mqtt_client
from paho import mqtt

# broker = 'e8cced050d434a399601fa55cd92b924.s2.eu.hivemq.cloud'
broker = '192.168.1.50'
port = 1883
topic = "lightStatus"

# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'raspberryPi_1'
password = 'nXfU8rc*JAAr&f'

def connect_mqtt():
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("return code "+str(rc)+"\n", rc)
    
    client = mqtt_client.Client(client_id=client_id, userdata="true", protocol=mqtt_client.MQTTv5)
    #client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    print("lightStatus2.py")
    client.connect(broker, port)
    return client


def publish(client, payload):
    time.sleep(1)
    result = client.publish(topic, payload)
    status = result[0]
    if status == 0:
        print(f"Send `{payload}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run(payload):
    client = connect_mqtt()
    client.loop_start()
    publish(client, payload)
    client.loop_stop()


if __name__ == '__main__':
    # run(payload)
    run("true")