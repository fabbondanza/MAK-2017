#include <Servo.h> 

#define MotorX (8)
#define MotorY (9)
#define MotorLED (10)
#define LEDw A2
#define LEDb A3
#define LEDg A4
#define LEDy A5
#define LEDr 4
Servo myServoX;
Servo myServoY;
Servo myServoLED;

int positionX = 0; // Holds the desired X position
int positionY = 0l; //Holds the desired Y position
int angle = 0;
String serialString = ""; //Holds the string retrieved from the Serial
String positionXstr = ""; //Holds the pieced together string represetning the desired X position, based off of serialString
String positionYstr = ""; //Holds the pieced together string represetning the desired Y position, based off of serialString
char positionInput = 0; //Holds the character read from the Serial

 
void setup() 
{ 
  myServoX.attach(MotorX);
  myServoY.attach(MotorY);
  myServoLED.attach(MotorLED);
  Serial.begin(9600);
} 
  
 
void loop() 
{ 
    if (Serial.available() > 0) { // Checks if any input has been made into the Serial
      positionInput = Serial.read(); // If input made, it is assigned to positionInput. NOTE: this is only the first character that gets read.
      if (positionInput == 'M'){
        serialString = Serial.readString();
        motorProtocol();
      }
      else if (positionInput == 'S'){
        serialString = Serial.readString();
        servoProtocol();
      }
      else if (positionInput == 'L'){
        serialString = Serial.readString();
        LEDProtocol();
      }
      else if (positionInput == 'X'){
        //getCurrentX();
      }
      else if (positionInput == 'Y'){
        //getCurrentY();
      }
      else if (positionInput == 'Z'){
        //servoPulseStop(servo, angle);
      }
    }

    if ((positionX > 0) && (positionY >0)){
      SetStrokePerc((float)positionX, 0);
      SetStrokePerc((float)positionY, 1);
      delay(1000);
      Serial.println('D');
      motorReset(); 
    }   
}

// Functoin: motorProtocol(void)
// Description -- Reads the percentage value read in by the Serial and converts it into an integer so as to be able to input into into Servo Actuator
//      positionXstr - is the string that is read in from the Serial, and contains percentage for only X motor
//      positionYstr - is the string that is read in from the Serial, and contains percentage for only Y motor
//      Proper Input method of String:
//            If the desired X & Y positions are 70mm & 20mm respectively, the input into the serial would be 
//                        M50,7
//              Here 50, represents 50% of stroke length which is 70mm, and 7 represents 7% which is 20mm, the ',' is necessary in order for program to be able to split X & Y positions

void motorProtocol() {
  int splitIndex = serialString.indexOf(',');
  int len = serialString.length();
  positionXstr += serialString.substring(0,splitIndex);
  positionYstr = serialString.substring(splitIndex+1,len);
  positionX = positionXstr.toInt();
  positionY = positionYstr.toInt();
}

void servoProtocol() {
  if (serialString == "B"){
    angle = 30;
  }
  else if (serialString == "G"){
    angle = 60;
  }
  else if (serialString == "Y"){
    angle = 90;
  }
  else if (serialString == "R"){
    angle = 120;
  }
  else if (serialString == "W"){
    angle = 150;
  }
  myServoLED.write(angle);
  delay(1000);
}

// Functoin: motorReset(void)
// Description -- Resets variables relevant to motor controls, so that new positions can be read. 
//
void motorReset(){
  positionInput = 0;
  positionXstr = "";
  positionX = 0;
  positionYstr = "";
  positionY = 0;
}

// Functoin: SetStrokePerc(float) 
// Description -- Maps microseconds that linear actuator is on to position
//      float strokePercentage - input
//            This is the percent of the full strokelength that user wants to extend 
void SetStrokePerc(float strokePercentage,int motor)
{
  if ( strokePercentage >= 1.0 && strokePercentage <= 99.0 )
  {
    int usec = 1000 + strokePercentage * ( 2000 - 1000 ) / 100.0 ;
    if (motor == 0){
      myServoX.writeMicroseconds( usec );
      }
    else if (motor == 1){
      myServoY.writeMicroseconds( usec );
      }
  }
}

// Function: LEDProtocol(void
// Description -- Toggles the desired LED
//          LEDb -> Blue LED
//          LEDr -> Red LED
//          LEDg -> Green LED
//          LEDw -> White LED
//          LEDy -> Yellow LEDb
void LEDProtocol(){
  if ((serialString == "B") && (digitalRead(LEDb)==LOW)){
    digitalWrite(LEDb,!digitalRead(LEDb));
    digitalWrite(LEDr,LOW);
    digitalWrite(LEDw,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDy,LOW);
  }
  else if ((serialString == "G")&& (digitalRead(LEDg)==LOW)){
    digitalWrite(LEDg,!digitalRead(LEDg));
    digitalWrite(LEDr,LOW);
    digitalWrite(LEDw,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDy,LOW);    
  }
  else if ((serialString == "R")&& (digitalRead(LEDr)==LOW)){
    digitalWrite(LEDr,!digitalRead(LEDr));
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDw,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDy,LOW);
  }
  else if ((serialString == "Y")&& (digitalRead(LEDy)==LOW)){
    digitalWrite(LEDy, !digitalRead(LEDy));
    digitalWrite(LEDr,LOW);
    digitalWrite(LEDw,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDb,LOW);
  }
  else if ((serialString == "W")&& (digitalRead(LEDw)==LOW)){
    digitalWrite(LEDw, !digitalRead(LEDw));
    digitalWrite(LEDr,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDy,LOW);
  }
  else {
    digitalWrite(LEDw, LOW);
    digitalWrite(LEDr,LOW);
    digitalWrite(LEDb,LOW);
    digitalWrite(LEDg,LOW);
    digitalWrite(LEDy,LOW);
  }
}
