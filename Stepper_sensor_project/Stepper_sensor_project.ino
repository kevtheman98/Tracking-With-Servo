#include <Servo.h>
#include <LiquidCrystal.h>

int echoPin = 9;
int trigPin = 8;
int pulseTime;
float pulseDist;
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);
int myCmd;
int pos = 0;
Servo myServo;
float targetAngle;
float currentAngle;
float step;
float diffrence = 0;
String myCmdstr;

void setup() {
  Serial.begin(9600);
  // Servo Motor
  myServo.attach(10);
  myServo.write(pos);
  
  // Ultrasonic sensor
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  lcd.begin(16, 2);
  
 


}

void loop() {
  //python to arduino
  while(Serial.available() == 0) {

  }
  
  myCmdstr = Serial.readStringUntil('\r');
  myCmd = myCmdstr.toInt();
  step = myCmd;
  
  targetAngle = step;
  diffrence = targetAngle - currentAngle;

  if(abs(diffrence) > 5) {
    if((diffrence) > 0) {
      currentAngle += 5;
    }
    if((diffrence) < 0) {
      currentAngle -= 5;
    }
    // -180 becuase flip direction(increasing clockwise, decreasing counter)
    myServo.write(180 - currentAngle);
    delay(10);
  }
  
  
  //ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  pulseTime = pulseIn(echoPin, HIGH);
  pulseDist = pulseTime/148.15;
  delay(10);
  
  //Lcd
  lcd.clear();
  delayMicroseconds(10);
  lcd.setCursor(0,0);
  lcd.print("Angle:");
  lcd.print(currentAngle);
  lcd.setCursor(0,1);
  lcd.print("Dist:");
  lcd.print(pulseDist);
  lcd.print("in");

  
  
 
  





}
