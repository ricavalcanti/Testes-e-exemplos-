import requests
import json
import time
import paho.mqtt.client as paho

# parametros
serial = "TEST271018"
email = "rodolfo@email.com"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}
urlLogin = 'http://api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://api.saiot.ect.ufrn.br/v1/device/manager/device'
urlHist = 'api.saiot.ect.ufrn.br/v1/device/history/logs'
broker = "api.saiot.ect.ufrn.br"
# pickup token
r = requests.post(urlLogin, json=jsonLogin)
r = requests.post(urlLogin, json=jsonLogin)
token = r.text
print(token)
# cadastro device
jsonDevice = {"token":
              token,
              "data": {
                  "name": "SmartOrdenha",
                  "serial": serial,
                  "controllers": [
                      {
                          "key": "onOff",
                          "class": "onoff",
                          "tag": "testePublish"
                      }
                  ],
                  "sensors": [
                      {
                          "key": "sensorVolume1",
                          "tag": "Volume teteiras 01",
                          "unit": "Litros",
                          "type": "number"
                      }
                  ],
              }
              }

retornoCadastro = requests.post(urlCadastro, json=jsonDevice)
print(retornoCadastro.text)


# define callback


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


client = paho.Client(serial, email, token)
client.on_message = on_message
print("connecting to broker ", broker)
client.connect(broker, port=8000)
print("subscribing ")
print(client.subscribe(serial))
print(client.subscribe((serial + "onOff")))  # subscribe
#print("publishing ")
jsonReport = {
    "token": token,
    "data": {
        "serial": serial,
        "key": "onOff",
        "value": "1"
    }
}
print("Json report: " + json.dumps(jsonReport))
client.publish("/control/put/me/", payload = json.dumps(jsonReport))  # publish
jsonSensor = { "serial": serial, "key": "sensorVolume1", "value": 18 }
time.sleep(4)
client.loop_start()
while 1:
    print("In loop")
    time.sleep(2)
    client.publish("/history/post/logs/sensor/", json.dumps(jsonSensor))
    #client.publish("/control/put/me/", json.dumps(jsonReport))  # publish
