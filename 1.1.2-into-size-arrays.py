
import numpy as np 
from sys import getsizeof as size
#lista lst
e = np.array([])
print(size(e))

lst = [24]
a = np.array(lst)
print(size(a))

lst = [24, 12]
a = np.array(lst)
print(size(a))

lst = [24, 12, 57]
a = np.array(lst)
print(size(a))

lst = [24, 12, 57, 42]
a = np.array(lst)
print(size(a))



#What this means?
#empty array = 96 Bytes
#ech element mens ++ 4 Bytes
#:. Total Bytes of = 96 + n*8 Bytes


#pag. 17/514
#file:///L:/Linear_/Data-Analysis-Python/bernd_klein_python_data_analysis_a4.pdf
#Time comparison Between Python Lists and Numpy Arrays