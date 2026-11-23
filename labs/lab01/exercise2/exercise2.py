# Lab 01 Exercise 2: Camping Logistics
import math

def calculate_tent_cost(participants, tent_capacity, tent_price):
    tents = math.ceil(participants / tent_capacity)
    return tents * tent_price

print(f"{calculate_tent_cost(12, 4, 100)}")
print(f"{calculate_tent_cost(13, 4, 100)}")