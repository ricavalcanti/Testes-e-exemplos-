#include <Arduino.h>
#define ledPin LED_BUILTIN

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin,LOW);
  delay(1000);
  digitalWrite(ledPin,HIGH);
  delay(1000);
}