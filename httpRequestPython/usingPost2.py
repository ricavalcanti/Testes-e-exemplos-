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
minutes = 25
seconds = 0

# parametros
serial = "240319CAS2"
email = "ricardodev@email.com"
kFatorPotencia = "kfp"
kPotencia = "kpa"
nomeDispositivo = "Medidor de potencia"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}

# pickup token
r = requests.post(urlLogin, json=jsonLogin)
if(r.status_code):
    print("Get token successful")

    token = r.text
else:
    print("Error get token, status_code: " + r.status_code)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


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


def sendData(minutes,seconds):
    dataFP = random.randint(900,920) / 1000.0
    dataAP = (random.randint(1,20) + 130)/10000
    #dt = datetime.datetime.now()         
    #dateMinusTwoM = str(datetime.datetime(dt.year, dt.month, dt.day,dt.hour,dt.minute - 3,dt.second,dt.microsecond))
    dateMinusTwoM = datetime.datetime(2019, 4, 19,13,minutes,seconds,350879)
    dateMinusTwoM = json.dumps(dateMinusTwoM, default = myconverter)
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
for i in range(5):
    time.sleep(1)
    print("Enviar dados em: ",i)
while(minutes < 46):
    sendData(minutes,seconds)
    seconds = seconds + 30
    if(seconds == 60):
        minutes = minutes + 1
        seconds = 0
    print("Ok")
    time.sleep(1)
print("Terminou")