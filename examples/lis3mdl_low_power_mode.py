# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis3mdl import lis3mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis3mdl.LIS3MDL(i2c)

lis.low_power_mode = lis3mdl.LP_DISABLED

while True:
    for low_power_mode in lis3mdl.low_power_mode_values:
        print("Current Low power mode setting: ", lis.low_power_mode)
        for _ in range(10):
            magx, magy, magz = lis.magnetic
            print("x:{:.2f}uT, y:{:.2f}uT, z:{:.2f}uT".format(magx, magy, magz))
            print()
            time.sleep(0.5)
        lis.low_power_mode = low_power_mode
