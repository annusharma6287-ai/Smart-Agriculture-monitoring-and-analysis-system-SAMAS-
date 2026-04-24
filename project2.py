#farm_menu.py
farm_records = []
def add_records():
    date = input("Enter date (yyyy-mm-dd):")
    crop_name = input("Enter crop name:")
    soil_moisture = float(input("Enter soil moisture:"))
    soil_temperature = float(input("Enter soil temperature:"))
    farm_records.append({
        "date":date,
        "crop_name":crop_name,
        "soil_moisture":soil_moisture,
        "soil_temperature":soil_temperature
    })
    print("Record Added")
def view_records():
    if not farm_records:
        print("No farm records found")
        return
    for record in farm_records:
        print(record)
while True:
    print("1.Add Record")
    print("2.View Records")
    print("3.Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        add_records()
    elif choice == 2:
        view_records()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
