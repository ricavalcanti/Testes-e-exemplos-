import json
sensorAP =	{
    "key": "keyap",
    "tag": "Sensor Potencia",
    "unit": "Kw",
    "type": "number",
    "class" : "ActivePower"
}
sensorFP =	{
    "key": "keyfp",
    "tag": "Medidor de Fator de Potencia",
    "type": "number",
    "class" : "PowerFactor"
}

print(type(json.dumps(sensorAP)))