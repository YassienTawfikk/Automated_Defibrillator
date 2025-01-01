## **Overview**
The Automated Defibrillator System is a project that bridges ECG signal monitoring with automated defibrillation technology. The system analyzes ECG signals in real-time, detects abnormal rhythms (e.g., tachycardia or bradycardia), and administers a controlled shock when needed. It combines hardware components and a GUI for efficient signal visualization and diagnosis.

---

## **Key Features**
- **Real-Time ECG Monitoring:** Calculates BPM and detects arrhythmias.
- **Automated Shock Delivery:** Restores normal heart rhythm in case of tachycardia.
- **Temperature Monitoring:** Ensures safe operating conditions.
- **Intuitive GUI Interface:** Visualizes ECG signals, heart rate, and system actions in real-time.

---

## **Components**
The project uses the following hardware components:
1. **Arduino Uno** – Microcontroller for managing the system.
2. **LCD Display** – Outputs BPM, temperature, and status.
3. **N-Channel MOSFET & Capacitor (1000µF, 50V)** – Controls shock delivery.
4. **220Ω Load Resistance** – Simulates electrode connections.
5. **1mH Inductor** – Limits current for safety during shock delivery.
6. **DS18B20 Temperature Sensor** – Monitors operating temperature.
7. **Piezo Buzzer** – Alerts during shock delivery.
8. **Bluetooth Module** – Sends real-time data to the GUI.
9. **Ammeter** – Measures voltage during shock administration.

---

## **Graphical User Interface (GUI)**
The GUI provides real-time visualization and interaction with the system.

### **Features**
- Displays ECG signals, BPM, and system actions.
- Issues alerts for abnormal rhythms.
- Allows signal updates or resets.

### **Screenshots**
1. **Healthy Signal Visualization**
   
   <img width="800" alt="Screen Shot 2024-11-11 at 2 34 43 AM" src="https://github.com/user-attachments/assets/6ff0c8d4-a733-4c8c-a8b2-a8d7165f26a9">

3. **Tachycardia Detection**
   
   <img width="800" alt="Screen Shot 2024-11-11 at 2 34 53 AM" src="https://github.com/user-attachments/assets/51de96a5-4cbe-4f23-b8b7-d832547c3382">

---

## **How It Works**
1. ECG signals are monitored in real-time to calculate BPM.
2. The system detects arrhythmias (e.g., tachycardia or bradycardia).
3. For tachycardia, the system delivers a shock and logs the action on the LCD and GUI.
4. The GUI provides continuous updates for the user to monitor all system activity.

---

## **Schematic View**
<img width="800" alt="Schematic View for the complete circuit setup" src="https://github.com/user-attachments/assets/03b35447-bc64-4bca-b6b6-df1fa2b5aa09">

<img width="800" alt="Schematic View for the complete circuit setup" src="https://github.com/user-attachments/assets/2c15c587-973a-4e1d-a71a-0d0cb181c3cb">

This schematic outlines the circuit design and connections of the Automated Defibrillator System.

---

## **Simulation & Testing**
- **Tinkercad Simulation:** Test the circuit via [Tinkercad](https://www.tinkercad.com/things/17xpsmsCH1k-automated-defibrillator).

---

## **Images**
### **System in Action**
1. **Breadboard Setup**
  ![IMG_6766](https://github.com/user-attachments/assets/e5fa7e25-3c09-4e1d-8adf-4b4e655ae636)

3. **Healthy Status**
  ![IMG_6764](https://github.com/user-attachments/assets/f989fb18-05f6-4720-8682-14a579e79b2d)

4. **Tachycardia Detected & Shock Delivery**
  ![IMG_6757](https://github.com/user-attachments/assets/8a531e21-6b36-4a14-888d-7205260202b9)
  ![IMG_6765](https://github.com/user-attachments/assets/dfaa1ffa-9c91-41f7-a760-06138bf5c5cf)

---

## **Scenarios**
The system operates under the following scenarios:

### **1. Normal ECG Signal**
- **Description:** Heart rate (BPM) is within a healthy range.
- **Action:** Displays "Healthy" status on the LCD and GUI and sent to mobile.
- **Image:**
  
  ![IMG_6778](https://github.com/user-attachments/assets/ca8578f9-c14c-475c-8047-c3b483583a71)


### **2. Tachycardia Detected & Shock Delivery**
- **Description:** BPM exceeds the normal range, indicating tachycardia. The system automatically administers a shock.
- **Action:** Detects abnormal rhythm and delivers a controlled shock, and then displays "Shock Given" on both LCD, GUI and mobile interfaces.
- **Image:**
![IMG_6772](https://github.com/user-attachments/assets/0cf9955b-b6d2-4c65-b33d-c649f455b413)
![IMG_6773](https://github.com/user-attachments/assets/3812d054-c36c-472e-a004-84e566c11229)


---

## **Dependencies**
To run this project, you'll need to install the required libraries listed in the `requirements.txt` file. These libraries ensure that all components of the project, including the GUI and signal processing modules, function as intended.

[requirements.txt](https://github.com/user-attachments/files/17856621/Libraries.txt)

### **How to Install**
1. Locate the `requirements.txt` file in the root directory of the project.
2. Open a terminal and navigate to the project's folder.
3. Run the following command to install all the required libraries:
   ```
   pip install -r requirements.txt
   ```
   This will automatically install all the dependencies specified in the file.
   
4. Finaly download `LightBlue` to connect bluetooth module with your mobile so the data sent to it
---

## **Team Members**
Special thanks to:
- Nancy Mahmoud
- Madonna Mosaad
- Mazen Marwan
- Youssef Mohamed
