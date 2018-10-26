import requests
import json

# pickup token
jsonLogin = {"email": "ricardo@email.com",
             "password": "12345678910", "serial": "SO261018LAB"}
urlLogin = 'http://api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://api.saiot.ect.ufrn.br/v1/device/manager/device'

r = requests.post(urlLogin, json=jsonLogin)
token = r.text
print(token)
jsonDevice = {"token":
              token,
              "data": {
                  "name": "SmartOrdenha",
                  "serial": "SO261018LAB",
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

retornoCadastro = requests.post(urlCadastro,json =jsonDevice)
print(retornoCadastro.text)

