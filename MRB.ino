const int fan = 7;
const int speaker = 8;
bool firstByte = true;
uint8_t incomingByte = 0;

void play(const uint8_t speaker, const uint8_t tone) {
    auto end = millis() + 10;
    auto half_period = 100000 / ( 3 * tone );    
    while(end > millis()) {
        digitalWrite(speaker, HIGH);
        delayMicroseconds(half_period);
        digitalWrite(speaker, LOW);
        delayMicroseconds(half_period);
    }
}

int convertByteToSpeaker(uint8_t dat) {
    int ret = (dat * 12) + 2000; // Need to get a value between 2k and 5k

    if (ret > 5000) {
        ret = 5000;
    } else if (ret < 2000) {
        ret = 2000;
    }

    return ret;
}

void setup() {
  Serial.begin(9600);
  pinMode(fan, OUTPUT);
  pinMode(speaker, OUTPUT);
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
        //Serial.print("Value: ");
        //Serial.println(data);
        analogWrite(fan, data);
    } else if (incomingByte == 'S') {
        while(Serial.available() == 0) {};
        uint8_t data = Serial.read();
        play(speaker, data);
    }
  }
  delay(1);
}
