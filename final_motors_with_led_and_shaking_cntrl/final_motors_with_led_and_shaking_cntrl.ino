#include <Servo.h> 

#define LEDY 9
#define LEDB 12
#define LEDW 13
#define LEDR 8
#define LEDG 7
#define LEDg A2
#define LEDb A3
#define LEDy A4
#define MOTORX 5       //Linear Actuator Digital Pin
#define MOTORY 6        //Linear Actuator Digital Pin

#define LINEARX_MIN      1000  //
#define LINEARX_MAX      1700 //
#define LINEARY_MIN  1000     //
#define LINEARY_MAX  2000    //

Servo MotorX, MotorY;  

int linearXValue = 1000;   //current positional value being sent to the linear actuator. 
int linearYValue = 1000;  //current positional value being sent to the linear actuator. 
int XPotVal = 0;
int YPotVal = 0;
int XPotValNew = 0;
int YPotValNew = 0;
int moveCheck = -1; 

String circlesStr = "";
String positionXstr = ""; 
String positionYstr = "";
String serialString = "";
char positionInput = 0;
int positionXperc = -1;
int positionYperc = -1;
float positionXpwm = -1.0;
float positionYpwm = -1.0;
float XAnalogPercentValue = -1.0;
float YAnalogPercentValue = -1.0;
int circles = -1;
int current = 0;
int Xpos = 0;
int Ypos = 0;
int increment = 7;

void setup() {
  Serial.begin(9600);
  pinMode(LEDW, OUTPUT);
  pinMode(LEDR, OUTPUT);
  pinMode(LEDB, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDY, OUTPUT);
  pinMode(LEDy, OUTPUT);
  pinMode(LEDg, OUTPUT);
  pinMode(LEDb, OUTPUT);
    //initialize servos
  MotorX.attach(MOTORX, LINEARX_MIN, LINEARX_MAX);      // attaches/activates the linear actuator as a servo object 
  MotorY.attach(MOTORY , LINEARY_MIN, LINEARY_MAX);  // attaches/activates the linear actuator as a servo object 

  //Analog pins do not need to be initialized
  
  //use the writeMicroseconds to set the linear actuators to their default positions
  MotorX.writeMicroseconds(1080); 
  MotorY.writeMicroseconds(1080);
//  pinMode(MotorX, OUTPUT);
//  pinMode(MotorY, OUTPUT);
//  analogWrite(MotorX, 200);
//  analogWrite(MotorY, 255);
  delay(2000);
}

void loop() {
      XPotVal = analogRead(A0);
      YPotVal = analogRead(A1);
    if (Serial.available() > 0) {
    positionInput = Serial.read();
    if (positionInput == 'M'){
      serialString = Serial.readString();
      motorProtocol();
    }
    else if (positionInput == 'S'){
      serialString = Serial.readString();
//      shakeProtocol();
    }
    else if (positionInput == 'L'){
      serialString = Serial.readString();
      LEDProtocol();
    }
    if ((positionXpwm >= 0) && (positionYpwm >= 0)){
      MotorX.writeMicroseconds(positionXpwm); 
      MotorY.writeMicroseconds(positionYpwm);
      moveCheck = 1;
      while (moveCheck == 1){
        delay(500);
        XPotValNew = analogRead(A0);
        YPotValNew = analogRead(A1);
        
        if((XPotValNew == XPotVal) && (YPotValNew == YPotVal)){
          moveCheck = 0;
          Serial.print("X Pot: ");
          Serial.println(XPotVal);
          Serial.print("Y Pot: ");
          Serial.println(YPotVal);
          Serial.println(positionXpwm);
          Serial.println(positionYpwm);
          Serial.println('D');
        }
        else {
          XPotVal = XPotValNew;
          YPotVal = YPotValNew;
        }
      } 
      reset();
    }
  }
}

void motorProtocol() {
  int splitIndex = serialString.indexOf(',');
  int len = serialString.length();
  positionXstr += serialString.substring(0,splitIndex);
  positionYstr = serialString.substring(splitIndex+1,len);
  positionXperc = positionXstr.toFloat();
  positionYperc = positionYstr.toFloat();
  positionXpwm = (positionXperc/100.0)*1000.0+1000.0;
  positionYpwm = (positionYperc/100.0)*1000.0+1000.0;
}

void LEDProtocol(){
  if ((serialString == "B") && (digitalRead(LEDB)==LOW)){
    digitalWrite(LEDB,!digitalRead(LEDB));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDG,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);
    digitalWrite(LEDg,LOW);
  }
  else if ((serialString == "G")&& (digitalRead(LEDG)==LOW)){
    digitalWrite(LEDG,!digitalRead(LEDG));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDY,LOW);    
  }
  else if ((serialString == "R")&& (digitalRead(LEDR)==LOW)){
    digitalWrite(LEDR,!digitalRead(LEDR));
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDG,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);
    digitalWrite(LEDg,LOW);
  }
  else if ((serialString == "Y")&& (digitalRead(LEDY)==LOW)){
    digitalWrite(LEDY, !digitalRead(LEDY));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDG,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);
    digitalWrite(LEDg,LOW);
  }
  else if ((serialString == "W")&& (digitalRead(LEDW)==LOW)){
    digitalWrite(LEDW, !digitalRead(LEDW));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDG,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);
    digitalWrite(LEDg,LOW);
  }
  else if ((serialString == "g")&& (digitalRead(LEDg)==LOW)){
    digitalWrite(LEDg,!digitalRead(LEDg));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);     
  }
  else if ((serialString == "b")&& (digitalRead(LEDb)==LOW)){
    digitalWrite(LEDb,!digitalRead(LEDb));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDy,LOW);     
  }
  else if ((serialString == "y")&& (digitalRead(LEDy)==LOW)){
    digitalWrite(LEDy,!digitalRead(LEDy));
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDW,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDb,LOW);     
  }
  else {
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDR,LOW);
    digitalWrite(LEDB,LOW);
    digitalWrite(LEDG,LOW);
    digitalWrite(LEDY,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);
    digitalWrite(LEDg,LOW);  
  }
  
}
//
//void shakeProtocol(){
//  analogWrite(MotorY,127);
//  analogWrite(MotorX,54);
//  delay(1000);
//  circlesStr = serialString;
//  circles = circlesStr.toInt();
//  current = 0;
//  while (current <= circles){
//     for (int i=1;i <= 40;i++) {
//       if (i <=10){
//         Xpos = Xpos + increment;
//         Ypos = Ypos + increment;
//         analogWrite(5, Xpos);
//         analogWrite(6, Ypos);
//         delay(100);
//      }
//       else if ((i >10) && (i<=20)){
//         Xpos = Xpos + increment;
//         Ypos = Ypos - increment;
//         analogWrite(5, Xpos);
//         analogWrite(6, Ypos);
//        delay(100);
//      }
//       else if ((i >20) && (i<=30)){
//         Xpos = Xpos - increment;
//         Ypos = Ypos - increment;
//         analogWrite(5, Xpos);
//         analogWrite(6, Ypos);
//         delay(100);
//      }
//       else if ((i > 30) && (i<=40)){
//         Xpos = Xpos - increment;
//         Ypos = Ypos + increment;
//         analogWrite(5, Xpos);
//         analogWrite(6, Ypos);
//         delay(100);
//      }
//    }
//    current ++;
//  }
//}

void reset(){
  positionXstr = ""; 
  positionYstr = "";
  serialString = "";
  positionInput = 0;
  positionXperc = -1;
  positionYperc = -1;
  positionXpwm = -1;
  positionYpwm = -1;
  moveCheck = -1;
}

