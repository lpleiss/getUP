"""
Python script that turns on a given LED matrix connected to the RaspberryPi's GPIO.
"""

import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Define matrix
matrix = matrix.Matrix16x8(i2c)

# Fill the matrix.
matrix.fill(1)
brightness = 15
matrix.show()
