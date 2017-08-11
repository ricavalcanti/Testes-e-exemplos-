#include <Arduino.h>
#include <Time.h>
#include <TimeLib.h>
#include <Ticker.h>
#include <QueueList.h>
#include <stdlib.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>// comunica com o dns (ArduinoOTA)
#include <DNSServer.h> // habilita servidor dns no esp (WiFiManager)
#include <ESP8266WebServer.h>
#include <WiFiManager.h>
#include <ArduinoOTA.h>
#include <EEPROM.h>




void eAtual();
void blink();
bool eLed = 0;

class Sinalizador
{
    public:
        Sinalizador(int e);
        int getEstado();
        void setEstado(int e);
        int getCont();
        void setCont(int c);
        //Ticker getTicker();
        Ticker tsinalizador;
        Ticker setBlink;
        //Ticker setBlink2;



    private:
        int estado, cont = 0;




};


Sinalizador::Sinalizador(int e)
{
    estado = e;
    cont = 0;
    tsinalizador.attach_ms(100, eAtual);


}

int Sinalizador::getEstado()
{
    return this->estado;
}

int Sinalizador::getCont()
{
    return this->cont;
}

void Sinalizador::setEstado(int e)
{
    estado = e;
}

void Sinalizador::setCont(int c)
{
    cont = c;
}

Sinalizador s(5);

void eAtual()
{
  //Serial.println("eAtual");
  if(s.getEstado() == 5)//deverá dar duas piscadas longas e uma rapida
  {
    //Serial.println("ok estado");
    if(s.getCont() == 0)
    {
      Serial.print("Entrou em 1: ");
      Serial.println(s.getCont());
      s.setCont(16);
      //s.setBlink2.detach();
      s.setBlink.attach_ms(3000, blink);

    }
    else if(s.getCont() == 11)
    {
      Serial.print("entrou em 2: ");
      Serial.println(s.getCont());
      //s.setBlink.detach();
      s.setCont(10);
      s.setBlink.attach_ms(300, blink);
    }

  }

}

void blink()
{
    eLed = !eLed;
    Serial.print("BLINK: ");
    Serial.println(s.getCont());
    digitalWrite(LED_BUILTIN, eLed);
    s.setCont(s.getCont() - 1);
}


/*
                                              tttt
                                           ttt:::t
                                           t:::::t
                                           t:::::t
    ssssssssss       eeeeeeeeeeee    ttttttt:::::ttttttt    uuuuuu    uuuuuu ppppp   ppppppppp
  ss::::::::::s    ee::::::::::::ee  t:::::::::::::::::t    u::::u    u::::u p::::ppp:::::::::p
ss:::::::::::::s  e::::::eeeee:::::eet:::::::::::::::::t    u::::u    u::::u p:::::::::::::::::p
s::::::ssss:::::se::::::e     e:::::etttttt:::::::tttttt    u::::u    u::::u pp::::::ppppp::::::p
 s:::::s  ssssss e:::::::eeeee::::::e      t:::::t          u::::u    u::::u  p:::::p     p:::::p
   s::::::s      e:::::::::::::::::e       t:::::t          u::::u    u::::u  p:::::p     p:::::p
      s::::::s   e::::::eeeeeeeeeee        t:::::t          u::::u    u::::u  p:::::p     p:::::p
ssssss   s:::::s e:::::::e                 t:::::t    ttttttu:::::uuuu:::::u  p:::::p    p::::::p
s:::::ssss::::::se::::::::e                t::::::tttt:::::tu:::::::::::::::uup:::::ppppp:::::::p
s::::::::::::::s  e::::::::eeeeeeee        tt::::::::::::::t u:::::::::::::::up::::::::::::::::p
 s:::::::::::ss    ee:::::::::::::e          tt:::::::::::tt  uu::::::::uu:::up::::::::::::::pp
  sssssssssss        eeeeeeeeeeeeee            ttttttttttt      uuuuuuuu  uuuup::::::pppppppp
                                                                              p:::::p
                                                                              p:::::p
                                                                             p:::::::p
                                                                             p:::::::p
                                                                             p:::::::p
                                                                             ppppppppp*/



void setup ()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  //s.setEstado(5);




}

/*
lllllll
l:::::l
l:::::l
l:::::l
 l::::l    ooooooooooo      ooooooooooo   ppppp   ppppppppp
 l::::l  oo:::::::::::oo  oo:::::::::::oo p::::ppp:::::::::p
 l::::l o:::::::::::::::oo:::::::::::::::op:::::::::::::::::p
 l::::l o:::::ooooo:::::oo:::::ooooo:::::opp::::::ppppp::::::p
 l::::l o::::o     o::::oo::::o     o::::o p:::::p     p:::::p
 l::::l o::::o     o::::oo::::o     o::::o p:::::p     p:::::p
 l::::l o::::o     o::::oo::::o     o::::o p:::::p     p:::::p
 l::::l o::::o     o::::oo::::o     o::::o p:::::p    p::::::p
l::::::lo:::::ooooo:::::oo:::::ooooo:::::o p:::::ppppp:::::::p
l::::::lo:::::::::::::::oo:::::::::::::::o p::::::::::::::::p
l::::::l oo:::::::::::oo  oo:::::::::::oo  p::::::::::::::pp
llllllll   ooooooooooo      ooooooooooo    p::::::pppppppp
                                           p:::::p
                                           p:::::p
                                          p:::::::p
                                          p:::::::p
                                          p:::::::p
                                          ppppppppp*/

void loop()
{

    //Serial.println(s.getEstado());
    delay(5000);
    //Serial.println("Mudei o estado");


}
