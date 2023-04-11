from machine import Pin, I2C
import bme280
import time
new_i2c = I2C(0, freq=399361, scl=Pin(1), sda=Pin(0))


while True:
    bme = bme280.BME280(i2c=new_i2c)
    print("Temp :{temp} Pressure = {pre} Hum: {hum}".format(temp=bme.values[0],pre=bme.values[1],hum=bme.values[2]))
    time.sleep_ms(500)