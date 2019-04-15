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
serial = "240319CAS2"
email = "ricardodev@email.com"
kFatorPotencia = "kfp"
kPotencia = "kpa"
nomeDispositivo = "Medidor de potencia2"
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
                    "name": nomeDispositivo,
                    "serial": serial,
                    "controllers": [],
                    "sensors": [
                        {
                            "key": kPotencia,
                            "tag": "Potencia",
                            "unit": "Kw",
                            "type": "number",
                            "class" : "ActivePower"
                        },
                        {
                            "key": kFatorPotencia,
                            "tag": "Fator de potencia",
                            "type": "number",
                            "class" : "PowerFactor"
                        }
                    ]
                }
            }
    retornoCadastro = requests.post(urlCadastro, json=jsonDevice)
    print("Retorno do cadastro: " + retornoCadastro.text)


def sendData():
    dataFP = random.randint(75,90) / 100.0
    dataAP = random.randint(2,9)
    dt = datetime.datetime.now()         
    dateMinusTwoM = str(datetime.datetime(dt.year, dt.month, dt.day,dt.hour,dt.minute - 3,dt.second,dt.microsecond))
    
    jsonReport = {
        "token": token,
        "data": [{
            "data": [{
                "serial": serial,
                kFatorPotencia: dataFP,
                kPotencia: dataAP
            }],
            "dateTime": dateMinusTwoM
        }]
    }
    retornoData = requests.post(urlHist, json=jsonReport)
    print(retornoData.text)

cadastraDeviceSaiot()
while(1):
    sendData()
    time.sleep(2)