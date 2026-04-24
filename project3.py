#farm_search.py
farm_records = []
def add_records():
    date = input("Enter a date: ").strip()
    crop_name = input("Enter a crop name: ").strip().lower()
    crop_moisture = float(input("Enter a moisture: "))
    crop_temperature = float(input("Enter a temperature: "))
    farm_records.append({
        "date": date,
        "crop_name": crop_name,
        "Crop_moisture": crop_moisture,
        "Crop_temperature": crop_temperature
    })
    print("Records added")
def view_records():
    if not farm_records:
        print("No records added")
        return
    for record in farm_records:
        print(record)
def search_date():
    date = input("Enter a date: ").lower()
    for result in farm_records:
        if result["date"] == date:
            view_records()
def search_crop():
    crop_name = input("Enter a crop name: ").lower()
    for r in farm_records:
        if r["crop_name"] == crop_name:
            view_records()
while True:
    print("1.Add Record:")
    print("2.View Records:")
    print("3.Search Date:")
    print("4.Search Crop:")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_records()
    elif choice == 2:
        view_records()
    elif choice == 3:
        search_date()
    elif choice == 4:
        search_crop()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
