int Xpos = 0;
int Ypos = 0;
int increment = 7;
int circles; 
void setup() {
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  analogWrite(6,127);
  analogWrite(5,54);
  delay(1000);
  circles = 0;
}

void loop() {
  analogWrite(5,255);
  analogWrite(6,200);
  delay(1000);
//  while (circles < 30){
//    for (int i=1;i <= 40;i++) {
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
//    circles++;
//  }
//  analogWrite(5,0);
//  analogWrite(6,0);
}


