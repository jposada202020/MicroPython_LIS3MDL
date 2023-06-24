# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`lis3mdl`
================================================================================

MicroPython Driver for the ST LIS3MDL magnetometer


* Author(s): Jose D. Montoya


"""

from micropython import const
from micropython_lis3mdl.i2c_helpers import CBits, RegisterStruct

try:
    from typing import Tuple
except ImportError:
    pass


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/MicroPython_LIS3MDL.git"


_REG_WHO_AM_I = const(0x0F)
_CTRL_REG1 = const(0x20)
_CTRL_REG2 = const(0x21)
_CTRL_REG3 = const(0x22)
_CTRL_REG4 = const(0x23)
_DATA = const(0x28)

_GAUSS_TO_UT = 100

TEMPERATURE_DISABLED = const(0b0)
TEMPERATURE_ENABLED = const(0b1)
temperature_mode_values = (TEMPERATURE_DISABLED, TEMPERATURE_ENABLED)

RATE_0_625_HZ = const(0b000000)
RATE_1_25_HZ = const(0b000010)
RATE_2_5_HZ = const(0b000100)
RATE_5_HZ = const(0b000110)
RATE_10_HZ = const(0b001000)
RATE_20_HZ = const(0b001010)
RATE_40_HZ = const(0b001100)
RATE_80_HZ = const(0b001110)
RATE_155_HZ = const(0b000001)
RATE_300_HZ = const(0b010001)
RATE_560_HZ = const(0b100001)
RATE_1000_HZ = const(0b110001)
data_rate_values = (RATE_0_625_HZ, RATE_1_25_HZ, RATE_2_5_HZ, RATE_5_HZ, RATE_10_HZ, RATE_20_HZ, RATE_40_HZ, RATE_80_HZ, RATE_155_HZ, RATE_300_HZ, RATE_560_HZ, RATE_1000_HZ)

SCALE_4_GAUSS = const(0b00)
SCALE_8_GAUSS = const(0b01)
SCALE_12_GAUSS = const(0b10)
SCALE_16_GAUSS = const(0b11)
scale_range_values = (SCALE_4_GAUSS, SCALE_8_GAUSS, SCALE_12_GAUSS, SCALE_16_GAUSS)
scale_range_factor = {SCALE_4_GAUSS: 6842, SCALE_8_GAUSS:3421, SCALE_12_GAUSS:2281, SCALE_16_GAUSS:1711}

LP_DISABLED = const(0b0)
LP_ENABLED = const(0b1)
low_power_mode_values = (LP_DISABLED, LP_ENABLED)

CONTINUOUS = const(0b00)
ONE_SHOT = const(0b01)
POWER_DOWN = const(0b10)
operation_mode_values = (CONTINUOUS, ONE_SHOT, POWER_DOWN)


class LIS3MDL:
    """Driver for the LIS3MDL Sensor connected over I2C.

    :param ~machine.I2C i2c: The I2C bus the LIS3MDL is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x1C`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`LIS3MDL` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        from machine import Pin, I2C
        from micropython_lis3mdl import lis3mdl

    Once this is done you can define your `machine.I2C` object and define your sensor object

    .. code-block:: python

        i2c = I2C(1, sda=Pin(2), scl=Pin(3))
        lis3mdl = lis3mdl.LIS3MDL(i2c)

    Now you have access to the attributes

    .. code-block:: python

    """

    _device_id = RegisterStruct(_REG_WHO_AM_I, "B")

    _data_rate = CBits(6, _CTRL_REG1, 1)

    _scale_range = CBits(2, _CTRL_REG2, 5)
    _reset = CBits(1, _CTRL_REG2, 2)

    _low_power_mode = CBits(1, _CTRL_REG3, 5)
    _operation_mode = CBits(2, _CTRL_REG3, 0)

    _raw_magnetic_data = RegisterStruct(_DATA, "<hhh")

    def __init__(self, i2c, address: int = 0x1C) -> None:
        self._i2c = i2c
        self._address = address

        if self._device_id != 0x3D:
            raise RuntimeError("Failed to find LIS3MDL")

        self._operation_mode = CONTINUOUS
        self._scale_cached_factor = scale_range_factor[self._scale_range]

    @property
    def data_rate(self) -> str:
        """
        Sensor data_rate.
        Data rate higher than 80 Hz needs the FAST_ODR bit activated as well as the
        X and Y axes operative mode selection set. Be sure to read the datasheet to
        select the right value according to your needs.

        +-----------------------------------+----------------------+
        | Mode                              | Value                |
        +===================================+======================+
        | :py:const:`lis3mdl.RATE_0_625_HZ` | :py:const:`0b000000` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_1_25_HZ`  | :py:const:`0b000010` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_2_5_HZ`   | :py:const:`0b000100` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_5_HZ`     | :py:const:`0b000110` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_10_HZ`    | :py:const:`0b001000` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_20_HZ`    | :py:const:`0b001010` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_40_HZ`    | :py:const:`0b001100` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_80_HZ`    | :py:const:`0b001110` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_155_HZ`   | :py:const:`0b000001` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_300_HZ`   | :py:const:`0b010001` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_560_HZ`   | :py:const:`0b100001` |
        +-----------------------------------+----------------------+
        | :py:const:`lis3mdl.RATE_1000_HZ`  | :py:const:`0b110001` |
        +-----------------------------------+----------------------+
        """
        values = ("RATE_0_625_HZ", "RATE_1_25_HZ", "RATE_2_5_HZ", "RATE_5_HZ", "RATE_10_HZ", "RATE_20_HZ", "RATE_40_HZ", "RATE_80_HZ", "RATE_155_HZ", "RATE_300_HZ", "RATE_560_HZ", "RATE_1000_HZ")
        return values[self._data_rate]

    @data_rate.setter
    def data_rate(self, value: int) -> None:
        if value not in data_rate_values:
            raise ValueError("Value must be a valid data_rate setting")
        self._data_rate = value

    @property
    def scale_range(self) -> str:
        """
        Sensor scale_range

        +------------------------------------+------------------+
        | Mode                               | Value            |
        +====================================+==================+
        | :py:const:`lis3mdl.SCALE_4_GAUSS`  | :py:const:`0b00` |
        +------------------------------------+------------------+
        | :py:const:`lis3mdl.SCALE_8_GAUSS`  | :py:const:`0b01` |
        +------------------------------------+------------------+
        | :py:const:`lis3mdl.SCALE_12_GAUSS` | :py:const:`0b10` |
        +------------------------------------+------------------+
        | :py:const:`lis3mdl.SCALE_16_GAUSS` | :py:const:`0b11` |
        +------------------------------------+------------------+
        """
        values = ("SCALE_4_GAUSS", "SCALE_8_GAUSS", "SCALE_12_GAUSS", "SCALE_16_GAUSS")
        return values[self._scale_range]

    @scale_range.setter
    def scale_range(self, value: int) -> None:
        if value not in scale_range_values:
            raise ValueError("Value must be a valid scale_range setting")
        self._scale_range = value
        self._scale_cached_factor = scale_range_factor[value]

    def reset(self) -> None:
        """
        Reset the sensor
        """
        self._reset = True
        sleep(0.010)

    @property
    def low_power_mode(self) -> str:
        """
        Sensor low_power_mode. Default value: DISABLED
        If ENABLED, :attr:`data_rate` is set to 0.625 Hz and the system
        performs, for each channel, the minimum number of averages.

        +---------------------------------+-----------------+
        | Mode                            | Value           |
        +=================================+=================+
        | :py:const:`lis3mdl.LP_DISABLED` | :py:const:`0b0` |
        +---------------------------------+-----------------+
        | :py:const:`lis3mdl.LP_ENABLED`  | :py:const:`0b1` |
        +---------------------------------+-----------------+
        """
        values = ("LP_DISABLED", "LP_ENABLED")
        return values[self._low_power_mode]

    @low_power_mode.setter
    def low_power_mode(self, value: int) -> None:
        if value not in low_power_mode_values:
            raise ValueError("Value must be a valid low_power_mode setting")
        self._low_power_mode = value

    @property
    def operation_mode(self) -> str:
        """
        Sensor operation_mode

        +--------------------------------+------------------+
        | Mode                           | Value            |
        +================================+==================+
        | :py:const:`lis3mdl.CONTINUOUS` | :py:const:`0b00` |
        +--------------------------------+------------------+
        | :py:const:`lis3mdl.ONE_SHOT`   | :py:const:`0b01` |
        +--------------------------------+------------------+
        | :py:const:`lis3mdl.POWER_DOWN` | :py:const:`0b10` |
        +--------------------------------+------------------+
        """
        values = ("CONTINUOUS", "ONE_SHOT", "POWER_DOWN")
        return values[self._operation_mode]

    @operation_mode.setter
    def operation_mode(self, value: int) -> None:
        if value not in operation_mode_values:
            raise ValueError("Value must be a valid operation_mode setting")
        self._operation_mode = value

    @property
    def magnetic(self) -> Tuple[float, float, float]:
        """
        Magnetometer values in microteslas
        """
        rawx, rawy, rawz = self._raw_magnetic_data
        x = rawx / self._scale_cached_factor * _GAUSS_TO_UT
        y = rawy / self._scale_cached_factor * _GAUSS_TO_UT
        z = rawz / self._scale_cached_factor * _GAUSS_TO_UT

        return x, y, z
