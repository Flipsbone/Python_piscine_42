#!/usr/bin/env python3

def ft_recursive(day_harvest):
    if (day_harvest <= 0):
        return
    ft_recursive(day_harvest - 1)
    print("Day", day_harvest)


def ft_count_harvest_recursive():
    day_harvest = int(input("Days until harvest: "))
    ft_recursive(day_harvest)
    if (day_harvest > 0):
        print("Harvest time!")
