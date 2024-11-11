#include <LiquidCrystal_I2C.h>    // Library for I2C LCD
#include <SoftwareSerial.h>       // Library for Bluetooth communication
#include <OneWire.h>
#include <DallasTemperature.h>

// Define pin connections
#define ONE_WIRE_BUS 3            // DS18B20 data pin connected to pin 3 on Arduino
const int capacitorPin = A0;      // Analog input pin for measuring capacitor voltage
const int mosfetPin = 2;          // Digital output pin for controlling MOSFET
const int buzzerPin = 9;          // Digital output pin for the buzzer
const int chargingTime = 500;     // Charging time in milliseconds
const int dischargingTime = 5000; // Discharging time in milliseconds

// Initialize LCD and Bluetooth module on pins 7 (TX) and 8 (RX)
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Adjust address if needed
SoftwareSerial bluetooth(7, 8);      // Bluetooth TX on pin 7, RX on pin 8

// Initialize DS18B20 temperature sensor
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  // Set pin modes
  pinMode(mosfetPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  // Initialize serial and Bluetooth communications
  Serial.begin(9600);
  bluetooth.begin(9600);

  // Initialize LCD
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("ECG Status:");
  delay(2000);

  // Start DS18B20 sensor
  sensors.begin();
}

void loop() {
  // Check temperature and display/send it
  sensors.requestTemperatures();                  
  float temperatureC = sensors.getTempCByIndex(0); // Get temperature in Celsius

  lcd.setCursor(0, 1);  // Second row for temperature display
  lcd.print("Temp: ");
  lcd.print(temperatureC, 1);                     
  lcd.print(" C  ");                              // Extra spaces clear remaining chars

  // Send temperature data via Bluetooth
  bluetooth.println("Temperature: " + String(temperatureC, 1) + " C");
  bluetooth.flush();  // Ensure data is sent out completely

  delay(1000);  // Wait a second before updating

  // Check for incoming serial data
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n'); // Read data from serial
    Serial.println("Received Data: " + receivedData);   // Debugging statement

    if (receivedData.startsWith("BPM")) {
      // Display ECG details on the LCD
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("BPM: ");               // Display BPM on the first row
      lcd.print(receivedData.substring(4)); // Skip "BPM " prefix

      // Send diagnosis to mobile via Bluetooth
      bluetooth.print("Diagnosis: ");
      bluetooth.println(receivedData);
      bluetooth.flush();  // Ensure data is sent out completely
    } 
    else if (receivedData.startsWith("CAPACITOR_CONTROL")) {
      // Trigger capacitor charging/discharging
      chargeAndDischargeCapacitor();
    }
  }
}

void chargeAndDischargeCapacitor() {
  // Activate the buzzer during discharge
  digitalWrite(buzzerPin, HIGH);
  
  // Charge the capacitor
  digitalWrite(mosfetPin, HIGH);  // Turn on MOSFET to start charging
  delay(chargingTime);            // Wait for the capacitor to charge

  // Measure and print the charging voltage
  int voltage = analogRead(capacitorPin);
  float voltageValue = (voltage / 1023.0) * 5.0;
  Serial.print("Charging Voltage: ");
  Serial.print(voltageValue, 2);
  Serial.println(" V");
  
  // Discharge the capacitor
  digitalWrite(mosfetPin, LOW);  // Turn off MOSFET to start discharging
  delay(dischargingTime);        // Wait for the capacitor to discharge
  digitalWrite(buzzerPin, LOW);  // Turn off the buzzer

  // Measure and print the discharging voltage
  voltage = analogRead(capacitorPin);
  voltageValue = (voltage / 1023.0) * 5.0;
  Serial.print("Discharging Voltage: ");
  Serial.print(voltageValue, 2);
  Serial.println(" V");

  // Display capacitor discharge notification on LCD
  lcd.setCursor(0, 1);           // Second row for capacitor status
  lcd.print("Shock Given       "); // Clear extra chars with spaces

  // Notify mobile that a shock is given
  bluetooth.println("Shock Given");
  bluetooth.flush();  // Ensure data is sent out completely
  delay(1000);  // Delay between cycles
}
