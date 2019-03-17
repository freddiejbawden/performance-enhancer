#include <ESP8266WiFi.h>;
#include <ESP8266HTTPClient.h>;
 
const char* ssid = "shaba2";
const char* password = "";

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.print("Connecting..");
 
  }

  Serial.println(WiFi.localIP());

}

void loop() {
  HTTPClient http;
  http.begin("http://10.42.0.27:5000");
  int code = http.GET();
  delay(1000);
  Serial.println(code);
  http.end();

}
