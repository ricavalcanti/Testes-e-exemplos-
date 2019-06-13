/**
 * Exemplo de código de uma lâmpada controlada pela plataforma
 * SaIoT usando o protocolo MQTT. Nesse exemplo foi usado a
 * biblioteca para dispositivos IoT se comunicarem com a plata-
 * forma.
 * Autores:
 * Danielly Costa daniellycosta97@ufrn.edu.br
 * Patricio Oliveira patricio@bct.ect.ufrn.br
 * Ricardo Cavalcanti ricavalcanti@bct.ect.ufrn.br
 *
 * */

#include <Arduino.h>
#include <SaIoTDeviceLib.h>
#include <Ticker.h>
#define timeToSend 60 //4pck
#define timeToCollect 15

WiFiClient espClient;
SaIoTDeviceLib hidrometro("DeviceTeste", "110519LAB", "ricardo@email.com"); //name,serial,email
SaIoTController solenoide("on/off", "v.Solenoide", "onoff");                //key,tag,class
SaIoTSensor medidorAgua("hd01", "hidrometro_01", "Litros", "number");       //key,tag,unit,type
String senha = "12345678910";
void callback(char *topic, byte *payload, unsigned int length);

volatile bool stateSolenoide;
volatile int value = 0;

unsigned long tDecorrido;
String getHoraAtual();

// Ticker collectData;
Ticker sendData;

void collect();
void send();
void setup()
{

  hidrometro.addController(solenoide);
  hidrometro.addSensor(medidorAgua);
  // medidorAgua.setPackages(5);
  Serial.begin(115200);
  Serial.println("INICIO");
  // collectData.attach(timeToCollect, collect);
  hidrometro.preSetCom(espClient, callback, 300);
  hidrometro.start(senha);
  sendData.attach(timeToSend, send);

  tDecorrido = millis();
}

void loop()
{
  if ((((millis() - tDecorrido) / 1000) >= timeToCollect) && stateSolenoide)
  {
    Serial.print("Coletando dados: ");
    Serial.println(value);
    medidorAgua.pushOnQueue(value++, SaIoTCom::getDateNow());
    tDecorrido = millis();
  }
  hidrometro.handleLoop();
}

void callback(char *topic, byte *payload, unsigned int length)
{
  String payloadS;
  Serial.print("Topic: ");
  Serial.println(topic);
  for (unsigned int i = 0; i < length; i++)
  {
    payloadS += (char)payload[i];
  }
  if (strcmp(topic, hidrometro.getSerial().c_str()) == 0)
  {
    Serial.println("SerialLog: " + payloadS);
  }
  if (strcmp(topic, (hidrometro.getSerial() + solenoide.getKey()).c_str()) == 0)
  {
    Serial.println("SerialLog: " + payloadS);
    stateSolenoide = payloadS.toInt();
    //
  }
}

// void ICACHE_RAM_ATTR collect()
// {
//   Serial.println("Coletando dados");
//   medidorAgua.pushOnQueue(random(1, 30), SaIoTCom::getDateNow());
// }

void send()
{
  Serial.println("Enviando");
  hidrometro.sendData(medidorAgua, 4);
}
