import json
sensorAP =	{
    "key": "keyap",
    "tag": "Sensor Potencia",
    "unit": "Kw",
    "type": "number",
    "class" : "ActivePower"
}
sensorFP = {
    "key": "keyfp",
    "tag": "Medidor de Fator de Potencia",
    "type": "number",
    "class" : "PowerFactor"
}

jsonDevice = {"token":
           " token",
            "data": {
                "name": "Teste medidor energia",
                "serial": "serial",
                "controllers": [],
                "sensors": [
                    {
                        "oi":"oi"
                    }
                ]
            }
        }
print(jsonDevice)