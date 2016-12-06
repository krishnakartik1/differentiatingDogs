import numpy as np
import matplotlib.pyplot as plt

greyhounds=500
labs=500

greyHeight=28+4*np.random.randn(greyhounds)
labHeight=24+4*np.random.randn(labs)

plt.hist([greyHeight,labHeight],stacked=True,color=['b','g'])
plt.show()