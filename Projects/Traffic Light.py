// Section 1: setup
void setup()
{
  // RED on 13, YELLOW on 12, GREEN on 11
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);


  // BUTTONs on 5 and 4
  pinMode(5, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
}


// Section 2: variable 
// 13: red on, 12: yellow on, 11: green on
int lightOn = 13; 


// Section 3: loop
void loop()
{
  // if button 5 is pressed
  if (digitalRead(5) == LOW)
  {
    if (lightOn == 13)
    {
      // if red is on, set green on
      lightOn = 11;
     
      digitalWrite(13, 0);
      digitalWrite(12, 0);
      digitalWrite(11, 1);
    }
    else if (lightOn == 12)
    {
      // if yellow is on, set red on
      lightOn = 13;
     
      digitalWrite(13, 1);
      digitalWrite(12, 0);
      digitalWrite(11, 0);
    }
    else if (lightOn == 11)
    {
      // if green is on, set yellow on
      lightOn = 12;
     
      digitalWrite(13, 0);
      digitalWrite(12, 1);
      digitalWrite(11, 0);
    }


    delay(200);
  }