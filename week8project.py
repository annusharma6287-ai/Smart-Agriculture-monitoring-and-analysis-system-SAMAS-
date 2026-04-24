#file handling(Csv+Pandas)
import pandas as pd
import os
NewFile = 'farm_log.csv'
def load_data(NewFile):
    if not os.path.exists(NewFile):
        return pd.DataFrame(columns = ['date','crop','moisture','temperature'])
    return pd.read_csv(NewFile)
def save_data(df):
    df.to_csv(NewFile,index=False)
    return
def add_record(df):
    date = input('Date: ')
    crop = input('Crop: ')
    moisture = float(input('Moisture: '))
    temperature = float(input('Temperature: '))
    df.loc[len(df)] = [date,crop,moisture,temperature]
    save_data(df)
    return df
def main():
    df = load_data(NewFile)
    while True:
        print("\n1.Add record\n2.View records\n3.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            df = add_record(df)
            print("Added record")
        elif choice == '2':
            print(df)
        elif choice == '3':
            break
        else:
            print("Invalid choice")
main()