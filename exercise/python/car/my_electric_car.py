#!/usr/bin/python
# -*- coding: utf-8 -*-

from car import *;

my_new_car=ElectricCar('tesla', 'model s', '2018')
print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
my_new_car.battery.get_range()