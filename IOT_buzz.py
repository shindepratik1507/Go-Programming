Python program to turn a buzzer ON and OFF using Raspberry Pi GPIO

import RPi.GPIO as GPIO
from time import sleep

# Ignore warnings
GPIO.setwarnings(False)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Define GPIO pin for the Buzzer
BUZZER = 18

# Set up the GPIO pin as output and set initial state to LOW
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        # Turn ON the Buzzer
        GPIO.output(BUZZER, True)
        sleep(1)  # Sleep for 1 second
        
        # Turn OFF the Buzzer
        GPIO.output(BUZZER, False)
        sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    print("\nProgram stopped by user")

finally:
    GPIO.cleanup()  # Clean up all GPIO settings
