#include <ESP8266WiFi.h>;
#include <ESP8266HTTPClient.h>;
 
const char* ssid = "shaba2";
const char* password = "";
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

  
  while(id < 0){
    Serial.print(id);
    getId();
    Serial.println("Getting ID");
    
    
  }

  Serial.println("ID GOTTEN");
 
}
 
void loop() {

  Serial.print("loop");

  on = getStatus();

  if(on == 1){
    digitalWrite(1, HIGH);
    Serial.println("ON");
  }
  else{
    digitalWrite(1, LOW);
    Serial.println("OFF");
  }
 
}

int getStatus(){
  if (WiFi.status() != WL_CONNECTED) {
    return on;
  }
  HTTPClient http;  //Declare an object of class HTTPClient

  String link = "http://10.42.0.27:5000/api/things/";
  link.concat("" + String(id));
  link.concat("/on");
  http.begin(link);  //Specify request destination
  int httpCode = http.GET();   //Send the request
  delay(50);
 
  if (httpCode > 0) { //Check the returning code
    
    String payload = http.getString();   //Get the request response payload
    Serial.print(payload);
    http.end();
    return payload.toInt();                     //Print the response payload
 
  }
  return on;
}

void getId(){
  if (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    return;
  }
  HTTPClient http;  //Declare an object of class HTTPClient
 
  http.begin("http://10.42.0.27:5000/api/things");  //Specify request destination
  http.addHeader("Content-Type", "application/json");
  int httpCode = 404;
  if (on) httpCode = http.POST("{\"type\":\"SWITCH\", \"address\":\"192.168.1.1\", \"on\":\"true\"}");                //Send the request
  else httpCode = http.POST("{\"type\":\"SWITCH\", \"address\":\"192.168.1.1\", \"on\":\"false\"}");    

  delay(1000);
  Serial.print(httpCode);
  
  if (httpCode == 200) { //Check the returning code
    
    String payload = http.getString();   //Get the request response payload
    Serial.println(payload);
    http.end();
    id = payload.toInt();                     //Print the response payload
 
  }
  
}
