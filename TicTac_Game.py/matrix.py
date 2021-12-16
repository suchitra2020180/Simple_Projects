import numpy as np
list= ['A', 'B', '0', 'B', 'B', 'B', 'A', 'B', 'A']
array_list = np.asarray(list)
mat = array_list.reshape(3, 3)
print(mat)
row2 =mat[1]
print(row2)
if 'B' is in row2:
    print("yes")

