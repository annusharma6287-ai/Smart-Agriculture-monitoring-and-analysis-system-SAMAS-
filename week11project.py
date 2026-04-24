#Exception handling + Validation
def get_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Invalid input")
def main():
    while True:
        try:
            date = input("Enter your date: ")
            moisture = get_float("Enter moisture: ")
            temp = get_float("Enter temperature: ")
            print("Saved Data : ",date ,moisture ,temp)
        except Exception as e:
            print("Error: ",e)

        ch = input("Do you want to add another record? (y/n): ")
        if ch == "no":
            break

main()