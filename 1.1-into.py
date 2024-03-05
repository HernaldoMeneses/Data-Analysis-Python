'''
NumPy - Numeric Python
    Extension module for Python
    Mostly written in C. (speed)
    Powerful data structures (Multidimensional arrays and matrices)

Scipy - Scientific Python
    Needs NumPy
    Useful function for:
        Minimization, Regression, Fourier-transformation (and others)
'''


'''
    Simple Exemple demonstrate how we cab use Numpy and Matplotlib
    '''

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

'''
    Graphical representation
    '''
import matplotlib.pyplot as plt 

plt.plot(C)
plt.show()


'''
    Memory Consumption: NDARRAY and list

    using sys
    '''

from sys import getsizeof as size

lst = [24, 12, 57]
size_of_list_object = size(lst) # only green box
size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Size without the size of the elements: ", size_of_list_object)
print("Size of all the elements: ", size_of_elements)
print("Total size of list, including elements: ", total_list_size)

'''
    In previosly exemplo, we made the assimption that all the integer elements of our list have the same size.
    Of course, this is not valid in general, because memory consumpion will be higher for larger integers.
'''
print("one more element")
lst = [24, 12, 57, 42]
size_of_list_object = size(lst) # only green box
size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Size without the size of the elements: ", size_of_list_object)
print("Size of all the elements: ", size_of_elements)
print("Total size of list, including elements: ", total_list_size)


print("Empyt list")
lst = []
size_of_list_object = size(lst) # only green box
size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Size without the size of the elements: ", size_of_list_object)
print("Size of all the elements: ", size_of_elements)
print("Total size of list, including elements: ", total_list_size)

#pag. 15/514
#file:///L:/Linear_/Base-TI/bernd_klein_python_data_analysis_a4.pdf