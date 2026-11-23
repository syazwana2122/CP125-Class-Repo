# Lab 01 Exercise 6: Leap Year Detector
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(f"{is_leap_year(2024)}")
print(f"{is_leap_year(1900)}")