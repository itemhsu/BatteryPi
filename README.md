# BatteryPi
Measuring the Status of Charge (SoC) on Pi
## problem
The Li-ion battery voltage does not linearly correlate with the State of Charge (SoC) during dynamic loading conditions is crucial for battery management systems. This is because, under load, the battery voltage can drop due to internal resistance, and it may not accurately reflect the true SoC. When the load is removed, the voltage may recover slightly, but still, this voltage is not a direct indicator of SoC, especially in dynamic conditions.<img width="437" alt="image" src="https://github.com/itemhsu/BatteryPi/assets/25599185/abc12d77-91a8-44d8-b9ea-5b7a1ed1ce84">

## Solution MAX17043
https://www.analog.com/media/en/technical-documentation/data-sheets/max17043-max17044.pdf

## Module
https://item.taobao.com/item.htm?_u=420ekghrq84fe9&id=533982828160&spm=a1z09.2.0.0.449c2e8d0WaVnR
<img width="248" alt="image" src="https://github.com/itemhsu/BatteryPi/assets/25599185/3a0f82fe-f73c-4734-968b-f6ef5287cd31">

## Pin Connection
<img width="540" alt="image" src="https://github.com/itemhsu/BatteryPi/assets/25599185/ecf6c59b-ac07-4877-83ad-b89f81187810">
<img width="360" alt="image" src="https://github.com/itemhsu/BatteryPi/assets/25599185/eaec721c-a29a-47df-b53d-72c6040688bc">

## Config
### Install I2C Tools: apt 
```
sudo apt install i2c-tools
```
### Loading I2C Kernel Module:
append `i2c-dev` to `/etc/modules`

### Check booting config
make sure `dtparam=i2c_arm=on` in `/boot/firmware/config.txt`

### List I2C bus
```
root@aicar-fae30a:/home/pi# dmesg | grep i2c
[    1.630223] i2c /dev entries driver
[    2.365666] i2c i2c-11: Added multiplexed i2c bus 0
[    2.365899] i2c i2c-11: Added multiplexed i2c bus 10
```
### Detceting I2C
The bus contains `36` is what we want.
```
root@aicar-fae30a:/home/pi# sudo i2cdetect -y 10
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- 0c -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 2f 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- 51 -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         
root@aicar-fae30a:/home/pi# sudo i2cdetect -y 0
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- 36 -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```
### Install I2C Python Lib
```
pip install smbus2
```
### Using Example
```
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

```
## File List
| Name  | Function |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

