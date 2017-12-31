#include <Arduino.h>
#include <ArduinoJson.h>

void setup() {
    Serial.begin(115200);
    // put your setup code here, to run once:
    StaticJsonBuffer<200> jsonBuffer;
    char big_json[200];

    //JsonObject& root = jsonBuffer.createObject();
    JsonObject& hidro1 = jsonBuffer.createObject();
    hidro1["serial"] = "salarobotica";
    hidro1["pulso"] = 54;

    JsonObject& hidro2 = jsonBuffer.createObject();
    hidro2["serial"] = "hidroECT";
    hidro2["pulso"] = 500;

    JsonArray& dadosJson = jsonBuffer.createArray();
    dadosJson.add(hidro1);
    dadosJson.add(hidro2);

    /*dadosJson.printTo(big_json);
    Serial.println();
    Serial.print(big_json);*/




    /*
    root["serial"] = "hidroSalaRobotica";//uuid_dispositivo;
    root["pulso"] = 34;//d->pulsos;
    root["data_hora"] = "10/10/2017";//d->data_hora;
    root["meu_nome"] = "Ricardo";

    dadosJson.add(root);

    JsonArray& array = jsonBuffer.createArray();
    array.add(root);

    //array.printTo(big_json);
    dadosJson.printTo(big_json);
    */


}

void loop() {
    // put your main code here, to run repeatedly:
}
