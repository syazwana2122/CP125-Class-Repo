# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        return 2.0
    elif vehicle_type == "Hybrid" and (hour >= 22 or hour <= 6):
        return 2.0
    else:
        return 5.0

print(f"{get_hourly_rate("Hybrid", 23)}")
print(f"{get_hourly_rate("Hybrid", 13)}")
print(f"{get_hourly_rate("Sedan", 2)}")