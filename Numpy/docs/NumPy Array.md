
# NumPy Arrays


```python
my_list = [1,2,3]
```


```python
my_list
```




    [1, 2, 3]




```python
import numpy as np
```


```python
arr = np.array(my_list)
```


```python
arr
```




    array([1, 2, 3])




```python
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
```


```python
my_mat
```




    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




```python
np.array(my_mat) # 2-D array
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
np.arange(0,10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.arange(0,11,2)
```




    array([ 0,  2,  4,  6,  8, 10])




```python
np.zeros(3)
```




    array([ 0.,  0.,  0.])




```python
np.zeros((5,5))
```




    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])




```python
np.zeros((2,3))
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
np.ones(4)
```




    array([ 1.,  1.,  1.,  1.])




```python
np.ones((3,4))
```




    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]])




```python
np.linspace(0,5, num=10) # Return evenly spaced 10 numbers from 0 to 5 over a i
```




    array([ 0.        ,  0.55555556,  1.11111111,  1.66666667,  2.22222222,
            2.77777778,  3.33333333,  3.88888889,  4.44444444,  5.        ])




```python
np.eye(4) # Return a 2-D array with ones on the diagonal and zeros elsewhere.
```




    array([[ 1.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.],
           [ 0.,  0.,  1.,  0.],
           [ 0.,  0.,  0.,  1.]])




```python

```


```python
np.random.rand(5) # Random values in a given shape.
```




    array([ 0.81196545,  0.39364676,  0.72236114,  0.96902902,  0.82653307])




```python
np.random.rand(3,4) 
```




    array([[ 0.91087473,  0.31986599,  0.19593056,  0.85526034],
           [ 0.77069016,  0.96677132,  0.54901604,  0.77209475],
           [ 0.13386707,  0.99559857,  0.24016006,  0.38782812]])




```python
np.random.randn(2) # Return a sample (or samples) from the "standard normal" distribution.
```




    array([-1.33547666, -0.93276433])




```python
np.random.randn(4,4)
```




    array([[ 0.9757095 , -0.42453131, -0.35028787,  0.15471295],
           [-0.43493919,  1.25727371, -0.05624962, -1.3123685 ],
           [-0.34914826,  0.49923061, -0.37204579, -0.11461038],
           [ 0.55749406, -1.47358475,  0.88510184, -0.40627032]])




```python
np.random.randint(1,100) # Return random integers from `low` (inclusive) to `high` (exclusive).
```




    47




```python
np.random.randint(1,100,10)
```




    array([64, 93, 44, 32, 43, 62, 90, 48, 98, 67])




```python

```


```python
arr = np.arange(25)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24])




```python
ranArr = np.random.randint(0,50,10)
```


```python
ranArr
```




    array([13,  5, 25, 39, 42, 15, 38, 22, 27,  0])




```python
arr.reshape(5,5) # cause there are 25 elements --> can reshape to 5x5
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
ranArr.max()
```




    42




```python
ranArr.min()
```




    0




```python
ranArr.argmax() # max value 42 is in index 4
```




    4




```python
ranArr.argmin() # min value 0 is in index 9
```




    9




```python
arr.shape
```




    (25,)




```python
arr = arr.reshape(5,5)
```


```python
arr.shape
```




    (5, 5)




```python
arr.dtype
```




    dtype('int64')




```python
ranArr.dtype
```




    dtype('int64')




```python
from numpy.random import randint
```


```python
randint(2,10)
```




    6




```python

```
