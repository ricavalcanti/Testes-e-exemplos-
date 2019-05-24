#include <Arduino.h>
#include <queue>
#include <vector>


struct waterMeterData{
  volatile unsigned int pulsosAcumulados;
  String dateTime;
};

std::queue<waterMeterData> myqueue;
void setup()
{
  // put your setup code here, to run once:
  waterMeterData d1;
  waterMeterData d2;
  waterMeterData d3;
  myqueue.push(d1); 
  myqueue.push(d2); 
  myqueue.push(d3);
  Serial.begin(115200);
  delay(1000);
  Serial.println("Start!");
}

void loop()
{
  while (!myqueue.empty()) { 
    Serial.println(myqueue.front().pulsosAcumulados);
    myqueue.pop(); 
  } 
}