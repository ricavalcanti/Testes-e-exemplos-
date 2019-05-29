import requests
import json
import time
import random
import datetime
import paho.mqtt.client as mqtt

def sendData(dVolume):
    jsonReport = {
        "token": token,
        "data": {
            "serial": serial,
            "key":kVol,
            "value": dVolume,
        }
    }
    print(client.publish(rotaPSensor,json.dumps(jsonReport)))
    print(jsonReport)

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+connack_string(rc))

def getToken_saiot():
    r = requests.post(urlLogin, json=jsonLogin)
    token = r.text
    print(token)
    return token

def formatJsonCadastro(token):
    jsonDevice = {"token":
              token,
              "data": {
                  "name": "TesteMQTTPython",
                  "serial": serial,
                  "controllers": [],
                  "sensors": [
                      {
                          "key": kVol,
                          "tag": "Leite Produzido",
                          "unit": "Litros",
                          "type": "number"
                      },
                  ]
              }
              }
    return jsonDevice

def begin_saiot(token):
    client.username_pw_set(email,token)
    time.sleep(2)
    print(client.connect(broker, port=port))
    time.sleep(2)
    jsonCadastro = formatJsonCadastro(token)
    print(client.publish(rotaCadastro,json.dumps(jsonCadastro)))

# parametros dispositivo
serial = "150419Lab1NEW"
email = "ricardo@email.com"
kVol = "sensorVolume1"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}
urlLogin = 'http://api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://api.saiot.ect.ufrn.br/v1/device/manager/device'

#rotas servidor
rotaCadastro = '/manager/post/device/'
rotaPSensor = '/history/post/logs/sensor/'
broker = "api.saiot.ect.ufrn.br"
port = 8000

client = mqtt.Client(serial)
client.on_connect = on_connect
token = getToken_saiot()
begin_saiot(token)

while(1):
    sendData(random.randint(1,20))
    client.loop(timeout=1.0, max_packets=1)
    time.sleep(2)

