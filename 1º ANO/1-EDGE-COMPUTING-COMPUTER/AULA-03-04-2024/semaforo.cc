// C++ code

/*comentando blocos inteiros
no c++ */

int red  =  13;
int yellow = 12;
int green = 11;

void setup()
{
  
pinMode(red, OUTPUT);
pinMode(yellow, OUTPUT);
pinMode(green, OUTPUT);
  
}

void loop()
{
  //HIGH = led ligado; LOW = led desligado
digitalWrite(green, HIGH);
delay(2000);
digitalWrite(green, LOW);
delay(1000);
  
digitalWrite(yellow, HIGH);
delay(2000);
digitalWrite(yellow, LOW);
delay(1000);

digitalWrite(red, HIGH);
delay(2000);
digitalWrite(red, LOW);
delay(1000);
