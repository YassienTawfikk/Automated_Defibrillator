# **Automated Defibrillator**

The Automated Defibrillator System is a prototype that bridges **desktop signal analysis** with **embedded hardware control**. ECG signals are processed in real time by a laptop application, which detects abnormal rhythms such as tachycardia or bradycardia. When an arrhythmia is detected, the application sends a command to the Arduino-based circuit to administer a controlled low-voltage shock.

> This architecture demonstrates the integration of **biomedical signal processing (software)** with **hardware execution (embedded system)** in a safe, educational environment.
![Overview](https://github.com/user-attachments/assets/73fc50e2-1b82-4d26-bae6-f91fa06e2fbf)


---

## **Key Features**

* **Real-Time ECG Analysis:** Application processes ECG signals and calculates BPM.
* **Automated Shock Delivery:** Application commands Arduino to discharge when tachycardia/bradycardia is detected.
* **Safe Hardware Simulation:** Shock delivered at 5V using resistor load instead of electrodes.
* **Temperature Monitoring:** Ensures safe operating conditions.
* **GUI Visualization:** Displays ECG signals, BPM, arrhythmia alerts, and shock actions.

---

## **Components**

The project uses the following hardware components:

1. **Arduino Uno** – Executes commands from the application and controls the circuit.
2. **LCD Display** – Outputs BPM, temperature, and system status.
3. **N-Channel MOSFET & Capacitor (1000µF, 50V)** – Handles shock delivery.
4. **220Ω Load Resistance** – Simulates electrode connections.
5. **1mH Inductor** – Limits current during shock for safety.
6. **DS18B20 Temperature Sensor** – Monitors system temperature.
7. **Piezo Buzzer** – Alerts during shock delivery.
8. **Bluetooth Module** – Provides communication between laptop application and Arduino.
9. **Multimeter** – Measures voltage across the load during testing.

---

## **Graphical User Interface (GUI)**

The desktop application is the **core intelligence** of the system. It analyzes ECG signals, detects abnormalities, and instructs the Arduino when to trigger a shock.

### **Features**

* Visualizes ECG signals and BPM in real time.
* Detects tachycardia and bradycardia events.
* Logs system actions (e.g., “Shock Given”).
* Provides alerts and reset options.

### **Screenshots**

1. **Healthy Signal Visualization**

   <img width="800" alt="Healthy ECG" src="https://github.com/user-attachments/assets/6ff0c8d4-a733-4c8c-a8b2-a8d7165f26a9">

3. **Tachycardia Detection**

   <img width="800" alt="Tachycardia ECG" src="https://github.com/user-attachments/assets/51de96a5-4cbe-4f23-b8b7-d832547c3382">

---

## **How It Works**

1. ECG signals are processed by the laptop application.
2. Application calculates BPM and detects arrhythmias.
3. On arrhythmia detection, the application sends a shock command via Bluetooth.
4. Arduino executes the command by discharging the capacitor through the load resistor.
5. LCD, buzzer, and GUI display/log the action.

---

## **Schematic View**

<img width="800" alt="Schematic View" src="https://github.com/user-attachments/assets/03b35447-bc64-4bca-b6b6-df1fa2b5aa09">  

This schematic outlines the circuit connections for the Automated Defibrillator System.

---

## **Simulation & Testing**

* **Tinkercad Simulation:** [Try the circuit](https://www.tinkercad.com/things/17xpsmsCH1k-automated-defibrillator).

---

## **Images**

### **System in Action**

1. **Breadboard Setup**
   ![IMG\_6766](https://github.com/user-attachments/assets/e5fa7e25-3c09-4e1d-8adf-4b4e655ae636)

2. **Healthy Status**
   ![IMG\_6764](https://github.com/user-attachments/assets/f989fb18-05f6-4720-8682-14a579e79b2d)

3. **Tachycardia Detection & Shock Delivery**
   ![IMG\_6757](https://github.com/user-attachments/assets/8a531e21-6b36-4a14-888d-7205260202b9)
   ![IMG\_6765](https://github.com/user-attachments/assets/dfaa1ffa-9c91-41f7-a760-06138bf5c5cf)

---

## **Scenarios**

### **1. Normal ECG Signal**

* **Description:** BPM is within a healthy range.
* **Action:** GUI and LCD display “Healthy.”
* **Image:**
  ![IMG\_6778](https://github.com/user-attachments/assets/ca8578f9-c14c-475c-8047-c3b483583a71)

### **2. Tachycardia Detected & Shock Delivery**

* **Description:** BPM exceeds normal range.
* **Action:** Application commands Arduino to deliver a shock. LCD, buzzer, and GUI log “Shock Given.”
* **Image:**
  ![IMG\_6772](https://github.com/user-attachments/assets/0cf9955b-b6d2-4c65-b33d-c649f455b413)
  ![IMG\_6773](https://github.com/user-attachments/assets/3812d054-c36c-472e-a004-84e566c11229)

---

## **Dependencies**

To run this project, install the required libraries listed in the `requirements.txt` file.

[requirements.txt](https://github.com/user-attachments/files/17856621/Libraries.txt)

### **How to Install**

```bash
pip install -r requirements.txt
```

Download **LightBlue** to connect the Bluetooth module with your mobile if testing on phone.

---

## **Contributors**

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/YassienTawfikk" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/126521373?v=4" width="150px;" alt="Yassien Tawfik"/>
        <br /><sub><b>Yassien Tawfik</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Mazenmarwan023" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/127551364?v=4" width="150px;" alt="Mazen Marwan"/>
        <br /><sub><b>Mazen Marwan</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/madonna-mosaad" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/127048836?v=4" width="150px;" alt="Madonna Mosaad"/>
        <br /><sub><b>Madonna Mosaad</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/nancymahmoud1" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/125357872?v=4" width="150px;" alt="Nancy Mahmoud"/>
        <br /><sub><b>Nancy Mahmoud</b></sub>
      </a>
    </td>
  </tr>
</table>  
