import requests
import json
import time
import random
import datetime
def sendData(dVolume,dateTime):
    jsonReport = {
        "token": token,
        "data": [{
            "data": [{
                "serial": serial,
                kVol: dVolume,
            }],
            "dateTime": dateTime
        }]
    }
    retornoData = requests.post(urlHist, json=jsonReport)
    print(retornoData.text)

# parametros
serial = "150419Lab"
email = "ricardo@email.com"
kVol = "sensorVolume1"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}
urlLogin = 'http://api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://api.saiot.ect.ufrn.br/v1/device/manager/device'
urlHist = 'http://api.saiot.ect.ufrn.br/v1/device/history/logs'
broker = "api.saiot.ect.ufrn.br"
# pickup token
r = requests.post(urlLogin, json=jsonLogin)
token = r.text
print(token)
# cadastro device
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

retornoCadastro = requests.post(urlCadastro, json=jsonDevice)
print("Retorno do cadastro: " + retornoCadastro.text)

while(1):
    sendData(random.randint(1,20),str(datetime.datetime.now()))
    time.sleep(2)