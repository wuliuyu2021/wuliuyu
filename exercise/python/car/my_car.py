#!/usr/bin/python
# -*- coding: utf-8 -*-

from car import *;

my_new_car=Car('马自达', '昂克赛拉', '2018')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()