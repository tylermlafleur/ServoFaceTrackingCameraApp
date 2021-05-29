#include<Servo.h>

Servo servX;
Servo servY;

String serialData;

void setup() {
  // put your setup code here, to run once:

  servX.attach(3);
  servY.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);  //fix latency

}

void loop() {
  // I dont wanna
}

void serialEvent() {
  serialData = Serial.readString();

  servX.write(parseX(serialData));
  servY.write(parseY(serialData));
}

int parseX(String data) {
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);

  return data.toInt();
}

int parseY(String data) {
  data.remove(0, data.indexOf("Y") + 1);

  return data.toInt();
 }
