from machine import Pin
import time

led = Pin(12, Pin.OUT)
led.value(1)
time.sleep(1)
led.off()

led = Pin(18, Pin.OUT)
led.value(2)
time.sleep(1)
led.off()

led = Pin(19, Pin.OUT)
led.value(3)
time.sleep(1)
led.off()

led = Pin(13, Pin.OUT)
led.value(4)
time.sleep(1)
led.off()
