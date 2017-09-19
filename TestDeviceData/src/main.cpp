#include <Arduino.h>
#include <DeviceData.cpp>

void setup() {
    // put your setup code here, to run once:
    DeviceData d;
    Serial.begin(115200);
    d.setId("165.104.01");
    EEPROM.begin(sizeof(DeviceData));
    EEPROM.put(0,d);
    EEPROM.commit();
    EEPROM.end();
    Serial.print("Data: ");
    Serial.print(d.getId());
    Serial.print(" FIM");


    delay(500);

    DeviceData d2;
    EEPROM.begin(sizeof(DeviceData));
    EEPROM.get(0,d2);
    EEPROM.commit();
    EEPROM.end();
    Serial.print("Data2: ");
    Serial.print(d2.getId());
    Serial.print(" FIM");

/*    String ip = "192.168.0.1";
    String ip2;
    Serial.begin(115200);
    EEPROM.begin(sizeof(String));
    EEPROM.put(0,ip);
    EEPROM.commit();
    EEPROM.end();
    Serial.println("ok");

    delay(1000);
    EEPROM.begin(sizeof(String));
    EEPROM.get(0,ip2);
    EEPROM.end();
    Serial.print("IP2: ");
    Serial.println(ip2);*/


}

void loop() {
    // put your main code here, to run repeatedly:
}
