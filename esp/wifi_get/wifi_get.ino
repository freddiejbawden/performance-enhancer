#include <ESP8266WiFi.h>;
#include <ESP8266HTTPClient.h>;
 
const char* ssid = "MassiveGarbage";
const char* password = "fuckrightoff";
int on = 0;
int id = -1;
 
void setup () {
 
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  pinMode(0,OUTPUT);
 
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.print("Connecting..");
 
  }

  while(id < 0) getId();
 
}
 
void loop() {

  on = getStatus();

  if(on == 1) digitalWrite(0, HIGH);
  else digitalWrite(0, LOW);
 
}

int getStatus(){
  if (WiFi.status() != WL_CONNECTED) {
    return on;
  }
  HTTPClient http;  //Declare an object of class HTTPClient
 
  http.begin("/api/things/" + id);  //Specify request destination
  int httpCode = http.GET();                                                                  //Send the request
 
  if (httpCode > 0) { //Check the returning code
    
    String payload = http.getString();   //Get the request response payload
    http.end();
    return payload.toInt();                     //Print the response payload
 
  }
  return on;
}
