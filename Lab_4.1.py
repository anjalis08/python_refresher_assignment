import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*3.14,100)
y=np.sin(x)

randNum=np.random.normal(0,1,1000)

fig,ax= plt.subplots(1,2)

ax[0].plot(x, y, label="Sine Wave")
ax[0].set_title("Sine Wave")
ax[0].set_xlabel("X")
ax[0].set_ylabel("sin(X)")
ax[0].legend()

ax[1].hist(randNum, bins=30, label="Normal Data")
ax[1].set_title("Normal Distribution")
ax[1].set_xlabel("Value")
ax[1].set_ylabel("Frequency")
ax[1].legend()

fig.suptitle("Sine Wave and Normal Distribution")

plt.show()
