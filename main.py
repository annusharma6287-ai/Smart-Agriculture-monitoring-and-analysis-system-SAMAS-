from crop import crop
from soil import soil
from environment import environment
from farm_log import farm_log
crop1 = crop("Tomato","hybrid","field A",30,"vegetative")
soil1 = soil(45,6.5)
env1 = environment(31,65,2)
log1 = farm_log("2025-01-15",crop1,soil1,env1)
print(log1)
print("Summary ::",log1.summary())
print("Time stamp:",log1.get_timestamp())


