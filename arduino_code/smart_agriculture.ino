#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int soilPin = 34;
int relayPin = 25;
int ldrPin = 35;

void setup()
{
  Serial.begin(115200);

  dht.begin();

  pinMode(relayPin, OUTPUT);
}

void loop()
{
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  int soil = analogRead(soilPin);
  int light = analogRead(ldrPin);

  Serial.println("------------");

  Serial.print("Temp: ");
  Serial.println(temp);

  Serial.print("Humidity: ");
  Serial.println(hum);

  Serial.print("Soil: ");
  Serial.println(soil);

  Serial.print("Light: ");
  Serial.println(light);

  if (soil < 1500)
  {
      digitalWrite(relayPin, LOW);
      Serial.println("Pump ON");
  }
  else
  {
      digitalWrite(relayPin, HIGH);
      Serial.println("Pump OFF");
  }

  delay(5000);
}