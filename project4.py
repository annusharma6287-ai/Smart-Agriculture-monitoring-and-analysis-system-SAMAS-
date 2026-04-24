#modular_farm.py
farm_records = []
def validate_moisture():
    while True:
        try:
            m = float(input("Please enter the moisture: "))
            if 0 <= m <= 100:
                return m
        except:
            pass
        print("Invalid moisture")
def validate_temperature():
    while True:
        try:
            t = float(input("Please enter the temperature: "))
            if 0 <= t <= 100:
                return t
        except:
            pass
        print("Invalid temperature")
def add_record():
    date = input("Please enter the date: ")
    crop_name = input("Please enter the crop name: ")
    crop_moisture = input("Please enter the moisture: ")
    crop_temperature = input("Please enter the temperature: ")
    farm_records.append({
        "date": date,
        "crop_name": crop_name,
        "crop_moisture": crop_moisture,
        "crop_temperature": crop_temperature
    })
    print("Added record successfully")
def view_records():
    if not farm_records:
        print("No farm records added")
    for record in farm_records:
        print(record)
    for i , r in enumerate (farm_records):
        print(f"{r['crop_moisture']} - {r['crop_temperature']}")

def search_record():
    key = input("search date / crop: ").lower()
    if key in farm_records:
        print(key)
def delete_record():
    key = input("delete record / crop: ")
    if key in farm_records:
        del farm_records[key]
        print("Deleted record successfully")
def update_record():
    view_records()
    date = input("Enter date to update: ")
    if date in farm_records:
        farm_records[date] = [
            input("Enter crop date "),
            input ("enter crop name").lower(),
            validate_moisture(),
            validate_temperature(),
        ]
while True:
    print("1. Add record\n2.view records\n3.Delete record\n4.Update record\n6.search record\n5.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_record()
    elif choice == 2:
        view_records()
    elif choice == 3:
        delete_record()
    elif choice == 4:
        update_record()
    elif choice == 5:
        search_record()
    elif choice == 6:
        break
    else:
        print("Invalid choice")

