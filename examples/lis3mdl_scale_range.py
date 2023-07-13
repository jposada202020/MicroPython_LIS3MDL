# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis3mdl import lis3mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis3mdl.LIS3MDL(i2c)

lis.scale_range = lis3mdl.SCALE_16_GAUSS

while True:
    for scale_range in lis3mdl.scale_range_values:
        print("Current Scale range setting: ", lis.scale_range)
        for _ in range(10):
            magx, magy, magz = lis.magnetic
            print(f"X:{magx:0.2f}, Y:{magy:0.2f}, Z:{magz:0.2f} uT")
            print()
            time.sleep(0.5)
        lis.scale_range = scale_range
