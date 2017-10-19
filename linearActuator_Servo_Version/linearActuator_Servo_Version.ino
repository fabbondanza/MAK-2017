#include <Servo.h> 

#define PIN_SERVO (8)
Servo myServo;

int positionX = 0; // Holds the desired X position
int positionY = 0l //Holds the desired Y position
String serialString = ""; //Holds the string retrieved from the Serial
String positionXstr = ""; //Holds the pieced together string represetning the desired X position, based off of serialString
String positionYstr = ""; //Holds the pieced together string represetning the desired Y position, based off of serialString\
char positionInput = 0; //Holds the character read from the Serial

 
void setup() 
{ 
  myServo.attach(PIN_SERVO);
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
        getCurrentX();
      }
      else if (positionInput == 'Y'){
        getCurrentY();
      }
      else if (positionInput == 'Z'){
        servoPulseStop(servo, angle);
      }
    }

    if (positionX > 0){
      SetStrokePerc((float)positionX);
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
  positionX = positionXstr.toInt();
}

// Functoin: motorReset(void)
// Description -- Resets variables relevant to motor controls, so that new positions can be read. 
//
void motorReset(){
  positionInput = 0;
  positionXstr = "";
  positionX = 0;
}

// Functoin: SetStrokePerc(float) 
// Description -- Maps microseconds that linear actuator is on to position
//      float strokePercentage - input
//            This is the percent of the full strokelength that user wants to extend 
void SetStrokePerc(float strokePercentage)
{
  if ( strokePercentage >= 1.0 && strokePercentage <= 99.0 )
  {
    int usec = 1000 + strokePercentage * ( 2000 - 1000 ) / 100.0 ;
    myServo.writeMicroseconds( usec );
  }
}

// Functoin: SetStrokePerc(float) 
// Description -- Tells motor to move to specific millimeter(mm) position. Maps mm position to percentage of total strokelength
//      int strokeReq - input
//            This is the mm position desired
//      int strokeMax - input
//            This is the max stroke length in mm
void SetStrokeMM(int strokeReq,int strokeMax)
{
  SetStrokePerc( ((float)strokeReq) / strokeMax );
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
