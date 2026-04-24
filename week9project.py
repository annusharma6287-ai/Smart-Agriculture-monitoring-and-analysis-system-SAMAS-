#multi module + OOP (Basic classes)
class Crop:
    def __init__(self,name,height):
        self.name = name
        self.height = height
class Soil:
    def __init__(self,moisture):
        self.moisture = moisture
class Environment:
    def __init__(self,temperature):
        self.temperature = temperature
class Farmlogs:
    def __init__(self,date,crop,soil,environment):
        self.date = date
        self.crop = crop
        self.soil = soil
        self.environment = environment
    def display(self):
        print("The crop details are as: date,name,height,moisture , environment temperature:")
        print(self.date,self.crop.name,self.crop.height,self.soil.moisture,self.environment.temperature)
logs = []
while True:
    print("\n1.Add data\n2.View data\n3.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        date = input("Enter date:")
        name = input("Enter crop name:")
        height = float(input("Enter height:"))
        moisture = float(input("Enter moisture:"))
        temperature = float(input("Enter temperature:"))
        Crop = Crop(name,height)
        soil = Soil(moisture)
        environment = Environment(temperature)
        log = Farmlogs(date,Crop,soil,environment)
        logs.append(log)
        print("added data")
    elif choice == 2:
        for log in logs:
            log.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice")