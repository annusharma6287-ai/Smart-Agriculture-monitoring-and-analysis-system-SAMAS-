import pandas as pd

# File to store data
FILE = "farm_data.csv"
# Initialize empty list
records = []


# Load existing data
def load_data():
    global records
    try:
        df = pd.read_csv(FILE)
        records = df.to_dict(orient='records')
    except FileNotFoundError:
        records = []
    # Save data to CSV


def save_data():
    df = pd.DataFrame(records)
    df.to_csv(FILE, index=False)


# Add farm record
def add_record():
    print("\nEnter Farm Details:")
    date = input("Date: ")
    crop = input("Crop: ")
    moisture = float(input("Soil Moisture: "))
    ph = float(input("Soil pH: "))
    temp = float(input("Temperature: "))

    humidity = float(input("Humidity: "))
    rainfall = float(input("Rainfall: "))
    irrigation = float(input("Irrigation: "))
    fertilizer = input("Fertilizer: ")
    record = {
        "Date": date,
        "Crop": crop,
        "Moisture": moisture,
        "pH": ph,
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Irrigation": irrigation,
        "Fertilizer": fertilizer
    }
    records.append(record)
    save_data()
    print("Record added successfully!")


# View all records
def view_records():
    if not records:
        print("No records found!")
        return
    df = pd.DataFrame(records)
    print("\nFarm Records:\n")
    print(df)


# Search record
def search_record():
    key = input("Enter crop or date to search: ").lower()
    found = False
    for r in records:
        if key in r["Crop"].lower() or key in r["Date"]:
            print(r)
            found = True
    if not found:
        print("No record found!")
    # Analyze data


def analyze_data():
    if not records:
        print("No data to analyze!")
        return
    df = pd.DataFrame(records)
    print("\n--- Analysis ---")
    print("Average Moisture:", df["Moisture"].mean())
    print("Max Temperature:", df["Temperature"].max())
    print("Min Temperature:", df["Temperature"].min())
    print("Total Irrigation:", df["Irrigation"].sum())


# Main menu
def main():
    load_data()
    while True:
        print("\n--- SMART AGRICULTURE MONITORING & ANALYTICS SYSTEM  MENU ---")

        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Analyze Data")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_record()
        elif choice == '4':
            analyze_data()
        elif choice == '5':
            print("Exiting SAMAS...")
            break
        else:
            print("Invalid choice!")
        # Run program


main()