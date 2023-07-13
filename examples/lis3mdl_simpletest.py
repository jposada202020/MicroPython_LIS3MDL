# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis3mdl import lis3mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis3mdl.LIS3MDL(i2c)

while True:
    mag_x, mag_y, mag_z = lis.magnetic
    print(f"X:{mag_x:0.2f}, Y:{mag_y:0.2f}, Z:{mag_z:0.2f} uT")
    print("")
    time.sleep(0.5)
