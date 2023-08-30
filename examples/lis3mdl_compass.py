# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from math import atan2, degrees
from machine import Pin, I2C
from micropython_lis3mdl import lis3mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis3mdl.LIS3MDL(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)


while True:
    print(f"heading: {get_heading(lis):.2f} degrees")
    time.sleep(0.2)
