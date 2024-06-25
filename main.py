# Import from libraries
import time
from machine import Pin

# Set the OUTPUT pin to on-board LED
led = Pin("LED", Pin.OUT)

# Runs forever
while True:
    led.on()              # Turn on LED
    time.sleep(0.1)       # Delay for 0.2 seconds
    led.off()             # Turn off LED
    time.sleep(2)       # Delay for 1.0 seconds