#include <PID_v1.h>
#define LEDw A2
#define LEDb A3
#define LEDg A4
#define LEDy A5
#define LEDr 4
int led = 1;
int servo = 9;
int angle;
int pwm;
int current = 0;
int lenMicroSecondsOfPeriod = 25 * 1000; // 25 milliseconds (ms)
int lenMicroSecondsOfPulse = 1 * 1000; // 1 ms is 0 degrees
int first = 0.5 * 1000; //0.5ms is 0 degrees in HS-422 servo
int end = 3.7 * 1000;
int increment = 0.01 * 1000;

String p = "";
const int MotorPower_1 = 2; // Connected to H-bridge pin 1A
const int MotorGnd_1 = 3; // Connected to H-bridge pin 2A
const int MotorEnabler_1 = 10; //4 originally // Connected to H-bridge pin 1,2EN
const int MotorGnd_2 = 5;  //Connected to H-bridge pin 4A
const int MotorPower_2 = 6; //Connected to H-bridge pin 3A
const int MotorEnabler_2 = 11; //7 originally //Connected to H-bridge pin 3,4EN
const int MotorPot_1 = A0; // Used to read analog value of poteniometer in motor 1 (x-direction)
const int MotorPot_2 = A1; // Used to read analog vlaue ofpoteniometer in motor 2 (y-direction)
int potVal_1 = 0; // Holds the potentiometer value of motor 1
int potVal_2 = 0; // Holds the potentiometer value of motor 2 
char positionInput = 0; //Variable to read the characters of the position input by user in the Serial
int positionRecord = 0; //Variable to keep track whether (1) PositionX Read, (2) PositionY Read, (3) Moving to Position, (4) Reached Position 
String positionXstr = ""; 
String positionYstr = "";
int positionX = -1;
int positionY = -1;
int stopCheck_1 = 0; // For Motor 1: Variable to tell system which direction motor is moving, so to establish proper stopping parameters
int stopCheck_2 = 0; // For Motor 2: Variable to tell system which direction motor is moving, so to establish proper stopping parameters
int motorStatus_1 = 0; // (1) Motor 2 active and moving, (2) Motor 1 done moving
int motorStatus_2 = 0; // (1) Motor 2 active and moving, (2) Motor 1 done moving
int servoRecord = 0; // For Servo to tell system when to move it or not to move it (1) Servo needs to be moved, find value to move to (2) Ready to move
char servoStr1 = 0;
char servoStr2 = 0;
int servoAngle = -1; // Keeps track of what angle servo motor should move to.
String serialString = "";
double Setpoint1, Input1, Output1;
double aggKp=4, aggKi=0.2, aggKd=1;
double consKp=1, consKi=0.05, consKd=0.25;
PID myPID(&Input1, &Output1,  &Setpoint1, aggKp, aggKi, aggKd, DIRECT);
void setup() {
  //Attach arduino to servo motor
  //Initialize Serial for input/output
  Serial.begin(9600);
  //servo_test.attach(9);
  //Initialize all arduino pins as OUTPUTs for motor control
  pinMode(MotorPower_1, OUTPUT);
  pinMode(MotorGnd_1, OUTPUT);
  pinMode(MotorPower_2, OUTPUT);
  pinMode(MotorGnd_2, OUTPUT);
  pinMode(MotorEnabler_1, OUTPUT);
  pinMode(MotorEnabler_2, OUTPUT);
  pinMode(MotorPot_1, INPUT);
  pinMode(MotorPot_2, INPUT);
  pinMode(servo, OUTPUT);
  pinMode(LEDw, OUTPUT);
  pinMode(LEDr, OUTPUT);
  pinMode(LEDb, OUTPUT);
  pinMode(LEDg, OUTPUT);
  pinMode(LEDy, OUTPUT);
  //Initialize the H-Bridge enablers as ON
  analogWrite(MotorEnabler_1, 50);
  analogWrite(MotorEnabler_2, 50);

  // Turn off all motor mechanics, by writing LOW to all pins
  digitalWrite(MotorPower_1, LOW);
  digitalWrite(MotorPower_2, LOW);
  digitalWrite(MotorGnd_1, LOW);
  digitalWrite(MotorGnd_2, LOW);  

  //Write the current position of both motors
  //Serial.println("Send (X,Y) position");
  potVal_1 = analogRead(MotorPot_1);
  potVal_2 = analogRead(MotorPot_2);
  //Serial.print("Current X: ");
  //Serial.println(potVal_1);
  //Serial.print("Current Y: ");
  //Serial.println(potVal_2);  
  Input1 = potVal_1;
  myPID.SetOutputLimits(1, 50);
  myPID.SetMode(AUTOMATIC);
  //myPID_b.SetMode(AUTOMATIC);
}

void loop() {
  //Keep measuring the positions of the motors
  potVal_1 = analogRead(MotorPot_1);
  potVal_2 = analogRead(MotorPot_2);
  Input1 = potVal_1;
  double gap = abs(Setpoint1-Input1);
  if(gap < 10){
    myPID.SetTunings(consKp, consKi, consKd);
  }
  else{
    myPID.SetTunings(aggKp, aggKi, aggKd);
  }
  if (Serial.available() > 0) {
    positionInput = Serial.read();
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
  if ((positionX >= 0) && (positionY >= 0) && (positionRecord == 3)) { //Only runs if X & Y Positions were successfully read
      Setpoint1 = positionX;
      //myPID_b.Compute();
      //Case 1 -- Motor X moves IN, Motor Y moves IN
      if ((positionX < potVal_1) && (positionY < potVal_2)) {
        stopCheck_1 = 1; // Marks the direction Motor 1 is moving (IN)
        stopCheck_2 = 1; // Marks the direction Motor 2 is moving (IN)
        //Send Motor 1 IN
        digitalWrite(MotorPower_1,HIGH);
        digitalWrite(MotorGnd_1,LOW);
        //Send Motor 2 IN
        digitalWrite(MotorPower_2,LOW);
        digitalWrite(MotorGnd_2,HIGH);
        positionRecord = 4;
        }
      //Case 2 -- Motor X moves IN, Motor Y moves OUT
      else if ((positionX < potVal_1) && (positionY > potVal_2)) {
        stopCheck_1 = 1; // Marks the direction Motor 1 is moving (IN)
        stopCheck_2 = 2; // Marks the direction Motor 2 is moving (OUT)
        //Send Motor 1 IN
        digitalWrite(MotorPower_1,HIGH);
        digitalWrite(MotorGnd_1,LOW);
        //Send Motor 2 OUT
        digitalWrite(MotorPower_2,HIGH);
        digitalWrite(MotorGnd_2,LOW);
        positionRecord = 4;
        }
       //Case 3 -- Motor X moves OUT, Motor Y moves OUT
      else if ((positionX > potVal_1) && (positionY > potVal_2)) {
        stopCheck_1 = 2; // Marks the direction Motor 1 is moving (OUT)
        stopCheck_2 = 2; // Marks the direction Motor 2 is moving (OUT)
        //Send Motor 1 OUT
        digitalWrite(MotorPower_1,LOW);
        digitalWrite(MotorGnd_1,HIGH);
        //Send Motor 2 OUT
        digitalWrite(MotorPower_2,HIGH);
        digitalWrite(MotorGnd_2,LOW);
        positionRecord = 4;
        }
      //Case 4 -- Motor X moves OUT, Motor Y moves IN
      else if ((positionX > potVal_1) && (positionY < potVal_2)) {
        stopCheck_1 = 2; // Marks the direction Motor 1 is moving (OUT)
        stopCheck_2 = 1; // Marks the direction Motor 2 is moving (IN)
        //Send Motor 1 OUT
        digitalWrite(MotorPower_1,LOW);
        digitalWrite(MotorGnd_1,HIGH);
        //Send Motor 2 IN
        digitalWrite(MotorPower_2,LOW);
        digitalWrite(MotorGnd_2,HIGH);
        positionRecord = 4;
      }
  }
  //Runs if motor 1 is moving OUT, stops motor at desired position 
  if ((stopCheck_1 == 2) && (positionRecord == 4)) {
    if (potVal_1 >= (positionX-1)){
      digitalWrite(MotorPower_1,LOW);
      digitalWrite(MotorGnd_1,LOW);
      //Serial.println("Motor 1 Done");
      //Serial.print("Position X: ");
      //Serial.println(potVal_1);
      motorStatus_1 = 1; //Runs if motor 1 is moving IN, stops motor at desired position 
    }
  }
  //Runs if motor 1 is moving IN, stops motor at desired position 
  else if ( (stopCheck_1 == 1) && (positionRecord == 4)) {
    if (potVal_1 <= (positionX+1)){
      digitalWrite(MotorPower_1,LOW);
      digitalWrite(MotorGnd_1,LOW);
      //Serial.println("Motor 1 Done");
      //Serial.print("Position X: ");
      //Serial.println(potVal_1);
      motorStatus_1 = 1; //Runs if motor 1 is moving IN, stops motor at desired position 
    }
  }
  //Runs if motor 2 is moving OUT, stops motor at desired position 
  if ((stopCheck_2 == 2) && (positionRecord == 4)) {
    if (potVal_2 >= (positionY-1)){
      digitalWrite(MotorPower_2,LOW);
      digitalWrite(MotorGnd_2,LOW);
      //Serial.println("Motor 2 Done");
      //Serial.print("Position Y: ");
      //Serial.println(potVal_2);
      motorStatus_2 = 1; //Runs if motor 1 is moving IN, stops motor at desired position 
    }
  }
  //Runs if motor 2 is moving IN, stops motor at desired position 
  else if ( (stopCheck_2 == 1) && (positionRecord == 4)) {
    if (potVal_2 <= (positionY+1)){
      digitalWrite(MotorPower_2,LOW);
      digitalWrite(MotorGnd_2,LOW);
      //Serial.println("Motor 2 Done");
      //Serial.print("Position Y: ");
      //Serial.println(potVal_2);
      motorStatus_2 = 1; //Runs if motor 1 is moving IN, stops motor at desired position 
    }
  }
  // Runs once  both motors reached desired positions 
  // Resets specific values so that a new position can be entered
  if ((motorStatus_1 == 1) && (motorStatus_2 == 1)){
    Serial.println('D');
    motorReset();
    }
  myPID.Compute();
  analogWrite(MotorEnabler_1, Output1);
  delay(500);
}
  
void motorProtocol() {
  int splitIndex = serialString.indexOf(',');
  int len = serialString.length();
  positionXstr += serialString.substring(0,splitIndex);
  positionYstr = serialString.substring(splitIndex+1,len);
  //Serial.print("X:");
  //Serial.println(positionXstr);
  //Serial.print("Y:");
  //Serial.println(positionYstr);

  positionX = positionXstr.toInt()/1.0;
  positionY = positionYstr.toInt();
  positionRecord = 3;
  Setpoint1 = float(positionX);
}

void servoProtocol() {
  if (serialString == "B"){
    angle = .75*1000;
  }
  else if (serialString == "G"){
    angle = 1.3*1000;
  }
  else if (serialString == "Y"){
    angle = 2*1000;
  }
  else if (serialString == "R"){
    angle = 2.7*1000;
  }
  else if (serialString == "W"){
    angle = 3.5*1000;
  }
  servoPulseStart(servo,angle);
  delay(1000);
}

void servoPulseStart (int servo, int angle)
{     
      int current = 0;
      for(current = first; current <angle; current+=increment){
           // Servos work by sending a 25 ms pulse.  
           // 0.7 ms at the start of the pulse will turn the servo to the 0 degree position
           // 2.2 ms at the start of the pulse will turn the servo to the 90 degree position 
           // 3.7 ms at the start of the pulse will turn the servo to the 180 degree position 
           // Turn voltage high to start the period and pulse
           digitalWrite(servo, HIGH);
  
           // Delay for the length of the pulse
           delayMicroseconds(current);
  
           // Turn the voltage low for the remainder of the pulse
           digitalWrite(servo, LOW);
  
           // Delay this loop for the remainder of the period so we don't
           // send the next signal too soon or too late
           delayMicroseconds(lenMicroSecondsOfPeriod - current); 
      }
}
void servoPulseStop (int servo, int angle){
      for(current = angle; current >first; current-=increment){
         // Servos work by sending a 20 ms pulse.
         // 0.7 ms at the start of the pulse will turn the servo to the 0 degree position
         // 2.2 ms at the start of the pulse will turn the servo to the 90 degree position
         // 3.7 ms at the start of the pulse will turn the servo to the 180 degree position
         // Turn voltage high to start the period and pulse
         digitalWrite(servo, HIGH);

         // Delay for the length of the pulse
         delayMicroseconds(current);

         // Turn the voltage low for the remainder of the pulse
         digitalWrite(servo, LOW);

         // Delay this loop for the remainder of the period so we don't
         // send the next signal too soon or too late
         delayMicroseconds(lenMicroSecondsOfPeriod - current);
    }
}

void servoReset(){
  servoAngle = -1;
  serialString = "";
}

void motorReset(){
  stopCheck_1 = 0;
  stopCheck_2 = 0;
  motorStatus_1 = 0;
  motorStatus_2 = 0;
  positionRecord = 0;
  positionInput = 0;
  positionXstr = "";
  positionYstr = "";
}

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

void getCurrentX(){
  potVal_1 = analogRead(MotorPot_1);
  Serial.println(potVal_1);
}

void getCurrentY(){
  potVal_2 = analogRead(MotorPot_2);
  Serial.println(potVal_2);
}
