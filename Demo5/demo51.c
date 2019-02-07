#include <wiringPi.h>
int main()
{

  wiringPiSetupGpio();

  pinMode(14, INPUT); //pir
  pinMode(6, INPUT);  //nappi
  pinMode(5, OUTPUT);//led
  digitalWrite(5, LOW);
    
    // while loop terminates when button is pressed
    while (digitalRead(6)==0) 
  {
    if(digitalRead(5)==1){
      digitalWrite(5, HIGH);
      printf("Pin 6 tila on HIGH\n");
    }
      digitalWrite(5, LOW);
      Sleep(1000);//waits for a second
  }

    return 0;
}
