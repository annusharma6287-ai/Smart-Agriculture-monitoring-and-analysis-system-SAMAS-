#dictionary based farm monitoring
farm_records = []
unique_crops = set()
activity_logs = []

def add_records():
    date = input("Enter date{dd/mm/yyyy}: ")
    crop = input("Enter crop name: ")
    moisture = float(input("Enter moisture level: "))
    temperature = float(input("Enter temperature level: "))
    rainfall = float(input("Enter rainfall level: "))
    fertilizer = input("Enter fertilizer used: ")
    irrigation = float(input("Enter irrigation {litres}: "))
    records = {
        "date": date,
        "crop": crop,
        "moisture": moisture,
        "temperature": temperature,
        "rainfall": rainfall,
        "fertilizer": fertilizer,
        "irrigation": irrigation
    }
    farm_records.append(records)
    unique_crops.add(crop)
    activity_logs.append((date,"Added Record ",crop ))
    print("Record added successfully")

def view_records():
    if not farm_records:
        print("No farm records added")
        return
    for record in farm_records:
        print(record)
    print()

def search_by_crop():
    crop_name = input("Enter crop name to search: ").strip().title()
    found = False
    for record in farm_records:
        if record["crop"] == crop_name:
            print(record)
            found = True
        if not found:
            print("Crop not found")
            break
def show_unique_crops():
    print("Unique crops found:",unique_crops)

while True:
    print("1.add_records()\n2.view_records()\n3.search_by_crop()\n4. show_unique_crops\n5. exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_records()
    elif choice == 2:
        view_records()
    elif choice == 3:
        search_by_crop()
    elif choice == 4:
        show_unique_crops()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

