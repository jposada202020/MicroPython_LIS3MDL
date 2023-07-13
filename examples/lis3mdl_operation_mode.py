# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lis3mdl import lis3mdl

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lis = lis3mdl.LIS3MDL(i2c)

lis.operation_mode = lis3mdl.POWER_DOWN

while True:
    for operation_mode in lis3mdl.operation_mode_values:
        print("Current Operation mode setting: ", lis.operation_mode)
        for _ in range(10):
            magx, magy, magz = lis.magnetic
            print(f"X:{magx:0.2f}, Y:{magy:0.2f}, Z:{magz:0.2f} uT")
            print()
            time.sleep(0.5)
        lis.operation_mode = operation_mode
