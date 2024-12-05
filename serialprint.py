void setup() {
    Serial1.begin(9600);
    while (!Serial);
}
 
void loop() {
    Serial1.println("Hello,World");
    delay(1000);
}
