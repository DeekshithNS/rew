#define p1 4
#define p2 5
#define p3 6
#define p4 7
unsigned int device;

void setup() 
{
  Serial.begin(9600);
  pinMode(p1,OUTPUT);
  pinMode(p2,OUTPUT);
  pinMode(p3,OUTPUT);
  pinMode(p4,OUTPUT);
  digitalWrite(p1,HIGH);
  digitalWrite(p2,HIGH);
  digitalWrite(p3,HIGH);
  digitalWrite(p4,HIGH);
  
}

void loop() 
{
  if(Serial.available())
    {
      device = Serial.parseInt(); 
      
      switch(device)
      {
        case 10 : digitalWrite(p1,HIGH);
                  Serial.println('y');
                  break;
        case 11 : digitalWrite(p1,LOW);
                  break;          
        case 20 : digitalWrite(p2,HIGH);
                  break;
        case 21 : digitalWrite(p2,LOW);
                  break;
        case 30 : digitalWrite(p3,HIGH);
                  break;
        case 31 : digitalWrite(p3,LOW);
                  break;          
        case 40 : digitalWrite(p4,HIGH);
                  break;
        case 41 : digitalWrite(p4,LOW);
                  break;     
      }
    }
}
