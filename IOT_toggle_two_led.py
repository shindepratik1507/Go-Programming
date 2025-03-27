Python program to toggle two LEDs using Raspberry Pi GPIO

import RPi.GPIO as GPIO
from time import sleep

# Ignore warnings
GPIO.setwarnings(False)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins for RED and GREEN LEDs
RED_LED = 14
GREEN_LED = 15

# Set up the GPIO pins as output and set initial state to LOW
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        # Turn ON RED LED and OFF GREEN LED
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
        sleep(1)  # Sleep for 1 second

        # Turn OFF RED LED and ON GREEN LED
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
        sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    GPIO.cleanup()  # Clean up all GPIO settings
