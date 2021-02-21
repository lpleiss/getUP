"""
Python script that slowly turns on a given LED matrix connected to the RaspberryPi's GPIO.
"""

import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Define matrix
matrix = matrix.Matrix16x8(i2c)

# Fill the matrix with lowest brightness level.
matrix.fill(1)

brightness = 1

# Gradually increase matrix brightness.
while brightness < 16:
	brightness = brightness +1
	matrix.brightness = brightness
	matrix.show()
	time.sleep(0.3)

