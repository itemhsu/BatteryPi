import smbus2
import time
import csv
from datetime import datetime

# Define the I2C bus
bus = smbus2.SMBus(0)  # Use 0 since your device is on bus 0

# MAX17043 I2C address
address = 0x36

def read_voltage():
    # Read data from the MAX17043
    read = bus.read_word_data(address, 0x02)
    # Swap bytes
    swapped = ((read & 0xFF) << 8) | (read >> 8)
    # Convert to voltage
    voltage = swapped * 0.078125 / 1000
    return voltage

def read_soc():
    # Read data from the MAX17043
    read = bus.read_word_data(address, 0x04)
    # Swap bytes
    swapped = ((read & 0xFF) << 8) | (read >> 8)
    # Convert to SoC
    soc = swapped / 256
    return soc

# CSV file to append data
filename = "battery_data.csv"

# Loop to continuously monitor SoC and Voltage and write to CSV
try:
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header if file is new/empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "State of Charge (%)", "Voltage (V)"])
        
        while True:
            soc = read_soc()
            voltage = read_voltage()
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"{timestamp}, {soc}, {voltage}")
            writer.writerow([timestamp, soc, voltage])
            
            time.sleep(1)  # Sleep for 2 seconds
except KeyboardInterrupt:
    print("Monitoring stopped.")
    bus.close()

