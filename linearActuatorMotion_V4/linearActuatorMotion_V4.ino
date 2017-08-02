
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
int positionX = 0;
int positionY = 0;
int stopCheck_1 = 0; // For Motor 1: Variable to tell system which direction motor is moving, so to establish proper stopping parameters
int stopCheck_2 = 0; // For Motor 2: Variable to tell system which direction motor is moving, so to establish proper stopping parameters
int motorStatus_1 = 0; // (1) Motor 2 active and moving, (2) Motor 1 done moving
int motorStatus_2 = 0; // (1) Motor 2 active and moving, (2) Motor 1 done moving

void setup() {
  // put your setup code here, to run once:
  
  //Initialize Serial for input/output
  Serial.begin(9600);
  
  //Initialize all arduino pins as OUTPUTs for motor control
  pinMode(MotorPower_1, OUTPUT);
  pinMode(MotorGnd_1, OUTPUT);
  pinMode(MotorPower_2, OUTPUT);
  pinMode(MotorGnd_2, OUTPUT);
  pinMode(MotorEnabler_1, OUTPUT);
  pinMode(MotorEnabler_2, OUTPUT);
  pinMode(MotorPot_1, INPUT);
  pinMode(MotorPot_2, INPUT);

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
}

void loop() {
  //Keep measuring the positions of the motors
  potVal_1 = analogRead(MotorPot_1);
  potVal_2 = analogRead(MotorPot_2);
  
  //Runs if there was a position input in the Serial by the user 
  //Position must be input in the form of '(X,Y)' where X & Y are integers from 1-1024
  if (Serial.available() > 0) {
    positionInput = Serial.read(); //Reads the characters of the user input

    if (positionInput == 'X'){ //If command input for GET CURRENT POSITION
      getCurrentPositionX();
    }
    else if (positionInput == 'Y'){
      getCurrentPositionY();
    }   
    else if (positionInput == '('){ // If left-paranthese, system reads next character (which begins the desired X Position
      //Serial.println("Reading X");
      positionRecord = 1; //System marks that the X postion is being read
    }
    else if ((positionInput >= '0') && (positionInput <= '9') && (positionRecord == 1)){
      positionXstr += positionInput; //System reads the following characters and combines them, marking them as the X Position
    }                                // positionXstr is a string representation of the X Position input
    else if (positionInput == ','){ //If comma, system reads next character (which begins the desired Y Position 
      //Serial.println("Reading Y");
      positionRecord = 2; // System marks that the Y position is being read
      }
    else if ((positionInput >= '0') && (positionInput <= '9') && (positionRecord == 2)){
      positionYstr += positionInput; //System reads the following characters and combines them, marking them as the Y Position 
      }                              // positionYstr is a strin representation of the Y Position input
    else if (positionInput == ')'){ // If right-paranthese, system finishes reading position, and spits back out the input
      //Serial.print("X-Position: ");
      //Serial.println(positionXstr);
      //Serial.print("Y-Position: ");
      //Serial.println(positionYstr);
      positionX = positionXstr.toInt();
      positionY = positionYstr.toInt();
      positionRecord = 3; //System marks it is ready to turn motor on and move plate to required position
      }
   }

  if ((positionX != 0) && (positionY != 0) && (positionRecord == 3)) { //Only runs if X & Y Positions were successfully read
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
    reset();
    }
}

void reset(){
  stopCheck_1 = 0;
  stopCheck_2 = 0;
  motorStatus_1 = 0;
  motorStatus_2 = 0;
  positionRecord = 0;
  positionInput = 0;
  positionXstr = "";
  positionYstr = "";
}

void getCurrentPositionX(){
  potVal_1 = analogRead(MotorPot_1);
  Serial.println(potVal_1);
}

void getCurrentPositionY(){
  potVal_2 = analogRead(MotorPot_2);
  Serial.println(potVal_2);
}

