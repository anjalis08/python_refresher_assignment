import numpy as np 

mat = np.random.rand(5,5)

mean = np.mean(mat)
std = np.std(mat)
nor_mat=(mat-mean)/std

diagonal = np.diag(nor_mat)

print("Original Matrix:")
print(mat)

print("\nNormalized Matrix:")
print(nor_mat)

print("\nMain Diagonal:")
print(diagonal)