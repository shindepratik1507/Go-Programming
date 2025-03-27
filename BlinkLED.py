the Python code for blinking an LED using Raspberry Pi GPIO

import RPi.GPIO as GPIO
import time

# Ignore warnings
GPIO.setwarnings(False)

# Set GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pin for RED LED
RED_LED = 14

# Set up the GPIO pin as output
GPIO.setup(RED_LED, GPIO.OUT)

# Initial state of LED
cnt = 0
blink_time = 1

try:
    while True:
        if cnt == 0:
            GPIO.output(RED_LED, False)  # Turn off LED
            cnt = 1
        else:
            GPIO.output(RED_LED, True)   # Turn on LED
            cnt = 0
        
        time.sleep(blink_time)  # Wait for 1 second

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    GPIO.cleanup()  # Clean up all GPIO settings
