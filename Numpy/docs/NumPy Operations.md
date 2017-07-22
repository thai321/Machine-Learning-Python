
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
