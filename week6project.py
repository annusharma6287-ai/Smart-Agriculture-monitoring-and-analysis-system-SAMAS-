#OOPs classes and objects
from crop import crop
from soil import soil
from environment import environment
crop1 = crop("Tomato","Hybrid","field A",25,"vegetative")
soil1 = soil(40,6.5)
environment1 = environment(35,25,100)
print("Crop data", crop1.to_dict())
print("Soil data", soil1.to_dict())
print("Environment data", environment.to_dict)
crop1.update_height(30)
soil1.update_moisture(45)
print("After updates: ")
print("Updated crop height:",crop1.height)
print("Updated soil moisture:",soil1.moisture)