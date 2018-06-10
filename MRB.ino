bool firstByte = true;
uint8_t incomingByte = 0;

void setup() {
  Serial.begin(9600);
}


void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    //Serial.print("I received: ");
    //Serial.println((char)incomingByte);

    if (incomingByte == 'M') {
        while(Serial.available() == 0) {}; // Wait for data
        uint8_t data = Serial.read();
        Serial.print("Value: ");
        Serial.println(data);
    }
  }
  delay(1);
}
