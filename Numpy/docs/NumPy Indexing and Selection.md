
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
