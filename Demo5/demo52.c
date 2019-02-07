
#include <wiringPi.h>
#include <stdio.h>

int main()
{

  wiringPiSetupGpio();

  pinMode(4, INPUT); //pir
  pinMode(22, INPUT);  //nappi
  
  pinMode(5, OUTPUT);//led auto red
  pinMode(6, OUTPUT);//led auto yellow
  pinMode(13, OUTPUT);//led auto green
  
  pinMode(21, OUTPUT);//led jalan go
  pinMode(20, OUTPUT);//led jalan stop
  pinMode(12, OUTPUT);//led merkki
  
  //initial setup, autot menee, jalan ei
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(13, HIGH);
  
  digitalWrite(21, LOW);
  digitalWrite(12, LOW);
  digitalWrite(20, HIGH);
  
  int autoilleGreen = 1;
    
    // while loop terminates when button is pressed
    while (1) 
  {
      if(digitalRead(22)==1){
        printf("nappi");
        digitalWrite(12,HIGH);
        
        if(digitalRead(4)==1){
          printf("liike");
          sleep(3);//waits for three seconds

          digitalWrite(6, HIGH);
          digitalWrite(13, LOW);
          sleep(1);
          digitalWrite(5, HIGH);
          digitalWrite(6, LOW);
          sleep(1);
          
          digitalWrite(12,LOW);
          digitalWrite(21, HIGH);
          digitalWrite(20, LOW);
          sleep(3);//waits for three seconds
          
          digitalWrite(20, HIGH);
          digitalWrite(21, LOW);
          sleep(1);
          
          digitalWrite(6, HIGH);
          sleep(1);
          digitalWrite(13, HIGH);
          digitalWrite(5, LOW);
          digitalWrite(6, LOW);
          sleep(1);
          
          if(digitalRead(22)==1) break;//ohjelman lopetus kun nappi on tassa kohtaa pohjassa
          continue;
        } 
          printf("ei liike");
        
          digitalWrite(6, HIGH);
          digitalWrite(13, LOW);
          sleep(1);
          digitalWrite(5, HIGH);
          digitalWrite(6, LOW);
          sleep(1);
          
          digitalWrite(12,LOW);
          digitalWrite(21, HIGH);
          digitalWrite(20, LOW);
          sleep(3);//waits for three seconds
          
          digitalWrite(20, HIGH);
          digitalWrite(21, LOW);
          sleep(1);
          
          digitalWrite(6, HIGH);
          sleep(1);
          digitalWrite(13, HIGH);
          digitalWrite(5, LOW);
          digitalWrite(6, LOW);
          sleep(1);
        
          if(digitalRead(22)==1) break; //ohjelman lopetus kun nappi on tassa kohtaa pohjassa
      }
  }
    digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(13, LOW);
  
  digitalWrite(21, LOW);
  digitalWrite(12, LOW);
  digitalWrite(20, LOW);
    return 0;
}
