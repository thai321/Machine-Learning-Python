
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

# NumPy Indexing


```python
import numpy as np
```


```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr[8]
```




    8




```python
arr[1:5]
```




    array([1, 2, 3, 4])




```python
arr[0:5]
```




    array([0, 1, 2, 3, 4])




```python
arr[:6]
```




    array([0, 1, 2, 3, 4, 5])




```python
arr[5:]
```




    array([ 5,  6,  7,  8,  9, 10])




```python
arr[0:5] = 100
```


```python
arr
```




    array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])




```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
slice_of_arr = arr[0:6]
```


```python
slice_of_arr
```




    array([0, 1, 2, 3, 4, 5])




```python
slice_of_arr[:] = 99
```


```python
slice_of_arr
```




    array([99, 99, 99, 99, 99, 99])




```python
arr
```




    array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])




```python
arr_copy = arr.copy()
```


```python
arr
```




    array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])




```python
arr_copy
```




    array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])




```python
arr_copy[:] = 100
```


```python
arr_copy
```




    array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])




```python
arr
```




    array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])




```python

```


```python

```


```python

```


```python
import numpy as np
```


```python
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
```


```python
arr_2d
```




    array([[ 5, 10, 15],
           [20, 25, 30],
           [35, 40, 45]])




```python
arr_2d[0][0]
```




    5




```python
arr_2d[0]
```




    array([ 5, 10, 15])




```python
arr_2d[2,1]
```




    40




```python
arr_2d[2,1] == arr_2d[2][1]
```




    True




```python
arr_2d[:2,1:] # row 0,1 and col 1,2
```




    array([[10, 15],
           [25, 30]])




```python
arr_2d[:2]
```




    array([[ 5, 10, 15],
           [20, 25, 30]])




```python
arr_2d[1:]
```




    array([[20, 25, 30],
           [35, 40, 45]])




```python
arr = np.arange(1,11)
```


```python

```


```python

```


```python
arr
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr > 5
```




    array([False, False, False, False, False,  True,  True,  True,  True,  True], dtype=bool)




```python
bool_arr = arr > 5
```


```python
bool_arr
```




    array([False, False, False, False, False,  True,  True,  True,  True,  True], dtype=bool)




```python
arr[bool_arr]
```




    array([ 6,  7,  8,  9, 10])




```python
arr[arr > 5] # in 1 Step
```




    array([ 6,  7,  8,  9, 10])




```python
arr[arr < 3]
```




    array([1, 2])




```python

```


```python

```


```python
arr_2d = np.arange(50).reshape(5,10)
```


```python
arr_2d
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
           [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
           [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])




```python
arr_2d[1:3,3:5]
```




    array([[13, 14],
           [23, 24]])




```python

```

# NumPy Operation
- **Array with Array**
- **Array with Scalars**
- **Universal Array Functions**


```python
import numpy as np
```


```python
arr = np.arange(0,11)
```


```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr + arr
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])




```python
arr - arr
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
arr * arr
```




    array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])




```python
arr + 100
```




    array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])




```python
arr / arr
```

    /Users/YoungNguyen/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in true_divide
      """Entry point for launching an IPython kernel.





    array([ nan,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.])




```python
arr ** 2
```




    array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])




```python

```


```python

```


```python
np.sqrt(arr)
```




    array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
            2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ,
            3.16227766])




```python
np.max(arr)
```




    10




```python
arr.max()
```




    10




```python
np.sin(arr)
```




    array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
           -0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849,
           -0.54402111])




```python
np.log(arr)
```

    /Users/YoungNguyen/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: RuntimeWarning: divide by zero encountered in log
      """Entry point for launching an IPython kernel.





    array([       -inf,  0.        ,  0.69314718,  1.09861229,  1.38629436,
            1.60943791,  1.79175947,  1.94591015,  2.07944154,  2.19722458,
            2.30258509])




```python

```

# NumPy Exercises 


#### Import NumPy as np


```python
import numpy as np
```

#### Create an array of 10 zeros 


```python
np.zeros(10)
```




    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])



#### Create an array of 10 ones


```python
np.ones(10)
```




    array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])



#### Create an array of 10 fives


```python
np.ones(10) * 5
```




    array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])




```python
np.zeros(10) + 5
```




    array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])



#### Create an array of the integers from 10 to 50


```python
np.arange(10,51)
```




    array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
           27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
           44, 45, 46, 47, 48, 49, 50])



#### Create an array of all the even integers from 10 to 50


```python
np.arange(10,51,2)
```




    array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
           44, 46, 48, 50])



#### Create a 3x3 matrix with values ranging from 0 to 8


```python
arr = np.arange(9)
```


```python
arr.reshape(3,3)
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
np.arange(9).reshape(3,3)
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])



#### Create a 3x3 identity matrix


```python
np.eye(3)
```




    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])



#### Use NumPy to generate a random number between 0 and 1


```python
np.random.rand(1)
```




    array([ 0.63014358])




```python
np.random.rand(4)
```




    array([ 0.87723824,  0.37650919,  0.25542703,  0.840097  ])



#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution


```python
np.random.randn(25)
```




    array([ 0.19300069, -1.10465034, -0.17460169,  0.8790007 ,  0.68101474,
           -0.17313564,  0.18981315,  1.21170574,  0.35995229, -1.1242471 ,
           -2.0194464 , -0.24483055,  1.93109696, -0.65750283,  0.57590261,
           -0.70323009,  1.72649396,  1.23331433, -0.19985483,  0.89310901,
           -0.81475588,  0.179291  , -1.43815581,  1.2144338 ,  0.90117396])




```python
np.random.randn(25).shape
```




    (25,)



#### Create the following matrix:


```python
np.arange(1,101).reshape(10,10)/100
```




    array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
           [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
           [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
           [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
           [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
           [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
           [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
           [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
           [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
           [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])




```python
np.linspace(0.01,1,num=100).reshape(10,10)
```




    array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
           [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
           [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
           [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
           [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
           [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
           [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
           [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
           [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
           [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])



#### Create an array of 20 linearly spaced points between 0 and 1:


```python
np.linspace(0, 1, num=20)
```




    array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
            0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
            0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
            0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ])



## Numpy Indexing and Selection

Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:


```python
mat = np.arange(1,26).reshape(5,5)
mat
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]])




```python
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[2:, 1:]
```




    array([[12, 13, 14, 15],
           [17, 18, 19, 20],
           [22, 23, 24, 25]])




```python

```




    array([[12, 13, 14, 15],
           [17, 18, 19, 20],
           [22, 23, 24, 25]])




```python
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3,-1]
```




    20




```python

```




    20




```python
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[:3, 1]
```




    array([ 2,  7, 12])




```python
mat[:3, 1:2]
```




    array([[ 2],
           [ 7],
           [12]])




```python

```




    array([[ 2],
           [ 7],
           [12]])




```python
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[4, :]
```




    array([21, 22, 23, 24, 25])




```python
mat[-1, :]
```




    array([21, 22, 23, 24, 25])




```python
mat[-1]
```




    array([21, 22, 23, 24, 25])




```python

```




    array([21, 22, 23, 24, 25])




```python
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[-2:, :]
```




    array([[16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]])




```python
mat[3:5, :]
```




    array([[16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]])




```python

```




    array([[16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]])



### Now do the following

#### Get the sum of all the values in mat


```python
mat.sum() # or np.sum(mat)
```




    325



#### Get the standard deviation of the values in mat


```python
mat.std() # np.std(mat)
```




    7.2111025509279782



#### Get the sum of all the columns in mat


```python
mat
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]])




```python
mat.sum(axis=0) # sum of all the columns
```




    array([55, 60, 65, 70, 75])




```python
mat.sum(axis=1) # sum of all the rows
```




    array([ 15,  40,  65,  90, 115])




```python
mat.sum(axis=1).reshape(5,1) # sum of all the rows and reshape to 5 x 1 array
```




    array([[ 15],
           [ 40],
           [ 65],
           [ 90],
           [115]])


