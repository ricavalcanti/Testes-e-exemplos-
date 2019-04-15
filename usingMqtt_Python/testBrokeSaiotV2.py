import paho.mqtt.client as mqtt
import time

broker = "10.7.227.49"
port = 1883
client = mqtt.Client('pythonTestBroker')
print (client.connect(broker, port=port))
print (client.publish('message', payload='Hello world'))

while(1):
    print (client.publish('presence2', payload='Hello world'))
