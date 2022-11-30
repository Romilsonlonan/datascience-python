import os 
import numpy as np
filename = os.path.join("iris.csv")

arquivo = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)



