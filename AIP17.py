import numpy as np
x = np.array([[1,2],[3,4]], dtype=np.float64)
y= np.array([[5,6],[7,8]], dtype=np.float64)
# Element Wise sum; both produce the array
# [[ 6.0 8.0]
# [10.0 12.0]]
print(x + y) print(np.add(x, y))
# Element Wise difference; both produce the
array
# [[-4.0 -4.0]
# [-4.0 -4.0]]
print(x - y) print(np.subtract(x, y))
# Element Wise product; both produce the array
# [[ 5.0 12.0]
# [21.0 32.0]]
print(x * y) print(np.multiply(x, y))
# Element Wise division; both produce the array
# [[ 0.20.33333333]
# [ 0.42857143 0.5]]
print(x / y) print(np.divide(x, y))
# Element Wise square root; produces the array
# [[ 1.1.41421356]
# [ 1.73205081 2.]]
print(np.sqrt(x))