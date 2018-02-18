from globals import *
import matplotlib.pyplot as plt

df = pd.read_csv('workload.csv',header=None)
x = df[0]
y = df[1]
plt.ylabel('Core usage')
plt.xlabel('Time slot in five-minute intervals')
plt.plot(x,y)
plt.show()