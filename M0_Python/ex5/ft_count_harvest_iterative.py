#!/usr/bin/env python3

def ft_count_harvest_iterative():
    day_harvest = int(input("Days until harvest: "))
    for k in range(1, day_harvest + 1):
        print("Day", k)
    if (day_harvest > 0):
        print("Harvest time!")
