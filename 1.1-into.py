import numpy as np 
#list with values temperatures in Celsius
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
#Turn or list "cvalues" into a one-dimensiona numpy array
C = np.array(cvalues)
print(C)
type(C)


#Supouse we need turn the values into degrees Fahrenhit
#Solution withe arrays is very easy (Scalar multiplication)
F = (C * 9/5 + 32)
print(F)

### Without Numpy is more complicated
F = [x*9/5 + 32 for x in cvalues]
print(F)
type(F)


#In the following, we will use the terms "array" and "ndarray" in most cases synonymously
#More Precise ndarray is a instance of the class numpy.ndarray