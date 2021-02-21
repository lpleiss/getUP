"""
Python script that turns off a given LED matrix connected to the RaspberryPi's GPIO.
"""

import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Define matrix
matrix = matrix.Matrix16x8(i2c)

# Clear the matrix.
matrix.fill(0)
matrix.show()
