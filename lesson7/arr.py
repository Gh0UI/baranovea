import numpy as np
arr = np.random.random_integers(10, size=(3,3))
tarr=arr.transpose()

print(f"{arr}\n")
print(tarr)