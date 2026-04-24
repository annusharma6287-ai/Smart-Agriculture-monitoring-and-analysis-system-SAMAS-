#Basic farm_entry.py
print("Smart Agriculture Monitoring System!!")
print("Daily farm entry!!")
date = input("Enter date (yyyy-mm-dd):")
crop_name = input("Enter crop name:")
while(1):
    try:
        soil_moisture = float(input("Enter soil moisture:"))
        if 0<= soil_moisture <= 100:
            break
        else:
            print("Please enter a value between 0 and 100")
    except ValueError:
        print("Please enter a valid value")
while True:
    try:
        soil_temperature = float(input("Enter soil temperature:"))
        if 0<= soil_temperature <= 100:
            break
        else:
            print("Temperature out of range")
    except ValueError:
        print("Please enter a valid value")

print("Farm Records")
print(f"Date:{date}")
print(f"Crop name:{crop_name}")
print(f"Soil moisture:{soil_moisture}")
print(f"Soil temperature:{soil_temperature} degree celcius")

