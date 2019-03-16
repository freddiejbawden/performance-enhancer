#include <ESP8266WiFi.h>;
#include <ESP8266HTTPClient.h>;
 
const char* ssid = "MassiveGarbage";
const char* password = "fuckrightoff";
int on = 0;
 
void setup () {
 
  Serial.begin(115200);
  Serial.println("Start");
  pinMode(0,OUTPUT);
 
}
 
void loop() {

  digitalWrite(0, HIGH);
  delay(1000);
  digitalWrite(0, LOW);
  delay(1000);
  
 
}
