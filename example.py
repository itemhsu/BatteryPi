import smbus2
import time

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

# Read and print the SoC and Voltage
soc = read_soc()
voltage = read_voltage()
print(f"State of Charge: {soc}%")
print(f"Voltage: {voltage}V")

# Close the I2C bus
bus.close()

