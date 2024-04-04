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


