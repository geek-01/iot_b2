int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0){
    String value = Serial.readString();
    if(value=="1"){
      digitalWrite(led,HIGH);
    }
    else if(value=="0"){
      digitalWrite(led,LOW);
    }
  }
}
