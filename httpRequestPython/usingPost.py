import requests
import json
import time
import random
import datetime
#rotas 
urlLogin = 'http://dev.api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://dev.api.saiot.ect.ufrn.br/v1/device/manager/device'
urlHist = 'http://dev.api.saiot.ect.ufrn.br/v1/device/history/logs'
broker = "api.saiot.ect.ufrn.br"

# parametros
serial = "PYPostEle"
email = "ricardodev@email.com"
kCurrente = "sensorCorrente"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}

# pickup token
r = requests.post(urlLogin, json=jsonLogin)
if(r.status_code):
    print("Get token successful")

    token = r.text
else:
    print("Error get token, status_code: " + r.status_code)


def cadastraDeviceSaiot():
    jsonDevice = {"token":
                token,
                "data": {
                    "name": "Teste medidor energia",
                    "serial": serial,
                    "controllers": [],
                    "sensors": [
                        {
                            "key": kCurrente,
                            "tag": "Medidor de corrente",
                            "unit": "Kw",
                            "type": "number",
                            "class" : "ActivePower"
                        }
                    ]
                }
            }
    retornoCadastro = requests.post(urlCadastro, json=jsonDevice)
    print("Retorno do cadastro: " + retornoCadastro.text)


def sendData(dCorrente,dt):
    x = str(datetime.datetime(dt.year, dt.month, dt.day,dt.hour,dt.minute - 3,dt.second,dt.microsecond))
    
    jsonReport = {
        "token": token,
        "data": [{
            "data": [{
                "serial": serial,
                kCurrente: dCorrente
            }],
            "dateTime": x
        }]
    }
    retornoData = requests.post(urlHist, json=jsonReport)
    print(retornoData.text)

cadastraDeviceSaiot()
while(1):
    sendData(random.randint(4,20),datetime.datetime.now())
    time.sleep(2)