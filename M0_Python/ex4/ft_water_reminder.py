#!/usr/bin/env python3

def ft_water_reminder():
    day_reminder = int(input("Days since last watering:  "))
    if (day_reminder > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
