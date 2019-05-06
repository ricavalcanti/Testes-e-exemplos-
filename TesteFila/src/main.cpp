// Integrar a funcionalidade de armazenar os dados em fila ao Saiot
// Enviar os dados computados ao sistema

#include <Arduino.h>
#include <QueueList.h>
#include <Ticker.h>

#define tempCont 0.2 //

#define tempPush 5 //

#define tempEmpty 8 //


class dados{
  public: 
  int valor;
  unsigned long time;
};

int volatile cont = 0;

QueueList<dados> filaPulsos;

Ticker Contar;

Ticker PushFila;

Ticker EmptyFila;

void FuncContar()
{
  cont+= random(1,5);
}

void FuncPush()
{
  dados d;
  d.valor = cont;
  d.time = millis() / 1000;
  filaPulsos.push(d);
  cont = 0;
}

void FuncEmpty()
{
  while (filaPulsos.count() > 0)
  {
    dados x = filaPulsos.pop();
    Serial.print(x.valor);
    Serial.print('\t');
    Serial.println(x.time);
  }
}

void setup()
{
  Serial.begin(115200);
  Serial.println("Comecou");
  // put your setup code here, to run once:
  //interrupcao por tempo para gravar na flash
  Contar.attach(tempCont, FuncContar);
  PushFila.attach(tempPush, FuncPush);

  EmptyFila.attach(tempEmpty, FuncEmpty);
}

void loop()
{
  // put your main code here, to run repeatedly:
}
