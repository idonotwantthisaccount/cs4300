import numpy as np

#using numpy to calc dot product
def dot_prod():
    array1 = np.array([3, 3, 3])
    array2 = np.array([2, 7, 2])
    return np.dot(array1, array2)

print(dot_prod())

#test to confirm result
def test_compute_dot_product():
    assert dot_prod() == 33