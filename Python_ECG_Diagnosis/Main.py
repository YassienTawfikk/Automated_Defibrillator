import sys
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtCore import Qt
import serial
import time

# Import the generated UI class
from Design import Ui_MainWindow


# Function to calculate heart rate and analyze for arrhythmia
def analyze_ecg(ecg_signal, sampling_rate):
    peaks, _ = find_peaks(ecg_signal, distance=sampling_rate / 2.5)  # Assumes minimum heart rate of ~24 BPM
    rr_intervals = np.diff(peaks) / sampling_rate
    heart_rate = 60 / rr_intervals
    average_bpm = np.mean(heart_rate)
    irregular_beat_count = np.sum((heart_rate < 60) | (heart_rate > 100))

    if average_bpm < 60:
        diagnosis = "Bradycardia"
    elif average_bpm > 100:
        diagnosis = "Tachycardia"
    elif irregular_beat_count > len(heart_rate) * 0.2:
        diagnosis = "Arrhythmia"
    else:
        diagnosis = "Healthy"

    return average_bpm, diagnosis


# PyQt-based main window with integrated UI
class ECGAnalyzer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI from the .ui file
        self.file_path = ""
        self.arduino = None
        self.initUI()

    def initUI(self):
        # Connect the buttons to their functions
        self.upload_signal.clicked.connect(self.open_file_dialog)
        self.quit_app.clicked.connect(self.close_application)

        # Replace `widget` with a PlotWidget for ECG plotting
        self.plot_widget = PlotWidget(self.groupBox)  # ECG plot area within groupBox
        self.plot_widget.setGeometry(10, 30, 1250, 561)  # Position and size within groupBox
        self.plot_widget.setBackground('k')  # Set background to black

        # Attempt to connect to Arduino
        self.connect_to_arduino()

    def connect_to_arduino(self):
        try:
            self.arduino = serial.Serial('/dev/cu.usbmodem14201', 9600, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
            print("Connected to Arduino")
        except serial.SerialException:
            print("Could not connect to Arduino")

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select ECG CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_path:
            self.file_path = file_path
            self.analyze_and_plot()

    def close_application(self):
        if self.arduino:
            self.arduino.close()
        QApplication.quit()

    def analyze_and_plot(self):
        # Load the ECG data from CSV file
        data = pd.read_csv(self.file_path)

        # Check if "ECG" column exists
        if "ECG" not in data.columns:
            self.status_label.setText("CSV file does not contain 'ECG' column.")
            return

        # Assuming a sampling rate of 250 Hz (typical for ECG data)
        sampling_rate = 200

        # Analyze the ECG signal
        ecg_signal = data["ECG"].values
        average_bpm, diagnosis = analyze_ecg(ecg_signal, sampling_rate)

        # Display the results inside the status_label within status_group
        self.status_label.setText(f"Average BPM: {average_bpm:.2f} - Diagnosis: {diagnosis}")

        # Clear previous plot and plot the ECG signal in the new plot_widget
        self.plot_widget.clear()
        self.plot_widget.plot(np.arange(len(ecg_signal)), ecg_signal,
                              pen=pg.mkPen(color='w', width=1))  # White line for visibility

        # Set x-axis and y-axis constraints with extra padding for x-axis
        self.plot_widget.setXRange(0, min(1200, len(ecg_signal)))  # Display first 1200 samples or full data if smaller
        self.plot_widget.setYRange(np.min(ecg_signal) - 1, np.max(ecg_signal) + 1)  # Adjust to ECG signal range

        # To limit zooming out beyond initial constraints, add more padding for x-axis
        self.plot_widget.setLimits(xMin=-100, xMax=len(ecg_signal) + 200, yMin=np.min(ecg_signal) - 0.3,
                                   yMax=np.max(ecg_signal) + 0.3)

        # Send the average BPM and diagnosis to Arduino if connected
        self.send_to_arduino(average_bpm, diagnosis)

    def send_to_arduino(self, bpm, diagnosis):
        if self.arduino:
            try:
                # Send ECG information to display on LCD
                message = f"BPM:{bpm:.0f} - {diagnosis}\n"
                self.arduino.write(message.encode())
                print(f"Sent to Arduino: {message}")

                # If diagnosis isn't "Healthy," also send a trigger for capacitor charging
                if diagnosis != "Healthy":
                    self.arduino.write(b"CAPACITOR_CONTROL\n")
            except serial.SerialException:
                print("Failed to send data to Arduino")


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    analyzer = ECGAnalyzer()
    analyzer.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
