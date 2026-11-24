from machine import Pin
from ir_nec import IR
from time import sleep_ms,sleep


led = Pin(2,Pin.OUT)
ir = IR(18)

while True:
    key = ir.read_key()
    
    if key == "1":
        led.on()
    elif key == "0":
        led.off()
    elif key == "OK":
        led.value(not led.value())
    else:
        
        print("key",key)
    sleep_ms(10)
