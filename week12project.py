#Numpy + Pandas + Matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "date":['1','2','3','4','5','6','7','8','9','10','11','12'],
    "moisture":[5,6,7,8,9,10,11,12,13,14,15,16],
    "temperature":[10,11,12,13,14,16,16,17,18,19,20,25],
    "Irrigation":[50,60,70,80,90,100,110,120,130,140,150,150]
}
df = pd.DataFrame(data)
print("Average moisture :",np.mean(df["moisture"]))
print("Average temperature :",np.max(df["temperature"]))
print("Total Irrigation : ", np.sum(df["Irrigation"]))
plt.plot(df["date"],df["moisture"])
plt.title("Average moisture")
plt.show()
plt.bar(df["date"],df["irrigation"])
plt.title("Average irrigation")
plt.show()