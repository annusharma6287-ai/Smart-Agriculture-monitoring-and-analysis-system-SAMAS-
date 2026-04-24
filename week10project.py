#packages concept
def add_record(data):
    date = input("Enter date: ")
    crop = input("Enter crop: ")
    data.append({"date":date,"crop":crop})
    print("added data")
def view_record(data):
    for d in data:
        print(d)
data = []
while True:
    print("Welcome to Farm")
    print("1.Add Record\n2.View Record\n3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_record(data)
    elif choice == 2:
        view_record(data)
    elif choice == 3:
        break
    else:
        print("Invalid choice")