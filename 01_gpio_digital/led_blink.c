#include <wiringPi.h>
#define LED 7
int main(void)
{
    wiringPiSetup();
    pinMode(LED,OUTPUT);
    for(int i =0; i < 100; i++)
    {
        digitalWrite (LED,HIGH); delay(100);
        digitalWrite (LED,LOW); delay(100);
    }
    return 0 ;
}