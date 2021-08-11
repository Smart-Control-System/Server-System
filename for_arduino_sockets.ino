#include <WiFi.h>
#include <DHT.h>
#include <Dictionary.h>
const char* ssid = "Linteh-work";
const char* password =  "SKART082020";
 
const uint16_t port = 6767;
const char * host = "192.168.1.100";

String sensor_name("light_sensor_mainroom");
String sensor_type("light");
String sensor_value;
String json_out;
int Lenght;
String sensor_name1("dht11_mainroom");
String sensor_type1("dht11");
String sensor_value_temp;
String sensor_value_hum;
bool flag = false;

Dictionary &main_json = *(new Dictionary(3));
Dictionary &json_data = *(new Dictionary(3));
Dictionary &dh_values = *(new Dictionary(2));
DHT dht(5, DHT11);

void setup()
{
  Serial.begin(115200);

  dht.begin();

  DHT dht(5, DHT11);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP()); 
}  
void loop()
{
    WiFiClient client;

    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }


  // getting sensor_data
  
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  
  sensor_value = (analogRead(34));

  // maing jsons

  
  // light json
  if (flag == true){
  json_data("sensor_name", sensor_name);
  json_data("sensor_type", sensor_type);
  json_data("values", sensor_value);
  main_json("type", "data");
  main_json("data", json_data.json());
  main_json("timestamp", "0");
    
  json_out = main_json.json();
  
  client.print(json_out.length());
  client.print(json_out);
  Serial.println(json_out);
   
  delay(5000);

  flag = false;
  }
  else{
  // dht json
  json_data("sensor_name", sensor_name1);
  json_data("sensor_type", sensor_type1);
  dh_values("temp", t);
  dh_values("wet", h);
  json_data("values", dh_values.json());
  main_json("type", "data");
  main_json("data", json_data.json());
  main_json("timestamp", "0");

  json_out = main_json.json();
  
  client.print(json_out.length());
  client.print(json_out);
  Serial.println(json_out);

  delay(5000);

  flag = true;
  }
}
