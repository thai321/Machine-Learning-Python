<h1 id="numpy-arrays">NumPy Arrays</h1>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">my_list <span class="op">=</span> [<span class="dv">1</span>,<span class="dv">2</span>,<span class="dv">3</span>]</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">my_list</code></pre></div>
<pre><code>[1, 2, 3]</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.array(my_list)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([1, 2, 3])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">my_mat <span class="op">=</span> [[<span class="dv">1</span>,<span class="dv">2</span>,<span class="dv">3</span>],[<span class="dv">4</span>,<span class="dv">5</span>,<span class="dv">6</span>],[<span class="dv">7</span>,<span class="dv">8</span>,<span class="dv">9</span>]]</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">my_mat</code></pre></div>
<pre><code>[[1, 2, 3], [4, 5, 6], [7, 8, 9]]</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.array(my_mat) <span class="co"># 2-D array</span></code></pre></div>
<pre><code>array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">0</span>,<span class="dv">10</span>)</code></pre></div>
<pre><code>array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">0</span>,<span class="dv">11</span>,<span class="dv">2</span>)</code></pre></div>
<pre><code>array([ 0,  2,  4,  6,  8, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.zeros(<span class="dv">3</span>)</code></pre></div>
<pre><code>array([ 0.,  0.,  0.])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.zeros((<span class="dv">5</span>,<span class="dv">5</span>))</code></pre></div>
<pre><code>array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.zeros((<span class="dv">2</span>,<span class="dv">3</span>))</code></pre></div>
<pre><code>array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.ones(<span class="dv">4</span>)</code></pre></div>
<pre><code>array([ 1.,  1.,  1.,  1.])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.ones((<span class="dv">3</span>,<span class="dv">4</span>))</code></pre></div>
<pre><code>array([[ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.linspace(<span class="dv">0</span>,<span class="dv">5</span>, num<span class="op">=</span><span class="dv">10</span>) <span class="co"># Return evenly spaced 10 numbers from 0 to 5 over a i</span></code></pre></div>
<pre><code>array([ 0.        ,  0.55555556,  1.11111111,  1.66666667,  2.22222222,
        2.77777778,  3.33333333,  3.88888889,  4.44444444,  5.        ])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.eye(<span class="dv">4</span>) <span class="co"># Return a 2-D array with ones on the diagonal and zeros elsewhere.</span></code></pre></div>
<pre><code>array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.rand(<span class="dv">5</span>) <span class="co"># Random values in a given shape.</span></code></pre></div>
<pre><code>array([ 0.81196545,  0.39364676,  0.72236114,  0.96902902,  0.82653307])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.rand(<span class="dv">3</span>,<span class="dv">4</span>) </code></pre></div>
<pre><code>array([[ 0.91087473,  0.31986599,  0.19593056,  0.85526034],
       [ 0.77069016,  0.96677132,  0.54901604,  0.77209475],
       [ 0.13386707,  0.99559857,  0.24016006,  0.38782812]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randn(<span class="dv">2</span>) <span class="co"># Return a sample (or samples) from the &quot;standard normal&quot; distribution.</span></code></pre></div>
<pre><code>array([-1.33547666, -0.93276433])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randn(<span class="dv">4</span>,<span class="dv">4</span>)</code></pre></div>
<pre><code>array([[ 0.9757095 , -0.42453131, -0.35028787,  0.15471295],
       [-0.43493919,  1.25727371, -0.05624962, -1.3123685 ],
       [-0.34914826,  0.49923061, -0.37204579, -0.11461038],
       [ 0.55749406, -1.47358475,  0.88510184, -0.40627032]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randint(<span class="dv">1</span>,<span class="dv">100</span>) <span class="co"># Return random integers from `low` (inclusive) to `high` (exclusive).</span></code></pre></div>
<pre><code>47</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randint(<span class="dv">1</span>,<span class="dv">100</span>,<span class="dv">10</span>)</code></pre></div>
<pre><code>array([64, 93, 44, 32, 43, 62, 90, 48, 98, 67])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">25</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr <span class="op">=</span> np.random.randint(<span class="dv">0</span>,<span class="dv">50</span>,<span class="dv">10</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr</code></pre></div>
<pre><code>array([13,  5, 25, 39, 42, 15, 38, 22, 27,  0])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.reshape(<span class="dv">5</span>,<span class="dv">5</span>) <span class="co"># cause there are 25 elements --&gt; can reshape to 5x5</span></code></pre></div>
<pre><code>array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr.<span class="bu">max</span>()</code></pre></div>
<pre><code>42</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr.<span class="bu">min</span>()</code></pre></div>
<pre><code>0</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr.argmax() <span class="co"># max value 42 is in index 4</span></code></pre></div>
<pre><code>4</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr.argmin() <span class="co"># min value 0 is in index 9</span></code></pre></div>
<pre><code>9</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.shape</code></pre></div>
<pre><code>(25,)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> arr.reshape(<span class="dv">5</span>,<span class="dv">5</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.shape</code></pre></div>
<pre><code>(5, 5)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.dtype</code></pre></div>
<pre><code>dtype(&#39;int64&#39;)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">ranArr.dtype</code></pre></div>
<pre><code>dtype(&#39;int64&#39;)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">from</span> numpy.random <span class="im">import</span> randint</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">randint(<span class="dv">2</span>,<span class="dv">10</span>)</code></pre></div>
<pre><code>6</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<h1 id="numpy-indexing">NumPy Indexing</h1>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">0</span>,<span class="dv">11</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[<span class="dv">8</span>]</code></pre></div>
<pre><code>8</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[<span class="dv">1</span>:<span class="dv">5</span>]</code></pre></div>
<pre><code>array([1, 2, 3, 4])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[<span class="dv">0</span>:<span class="dv">5</span>]</code></pre></div>
<pre><code>array([0, 1, 2, 3, 4])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[:<span class="dv">6</span>]</code></pre></div>
<pre><code>array([0, 1, 2, 3, 4, 5])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[<span class="dv">5</span>:]</code></pre></div>
<pre><code>array([ 5,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[<span class="dv">0</span>:<span class="dv">5</span>] <span class="op">=</span> <span class="dv">100</span></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">0</span>,<span class="dv">11</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">slice_of_arr <span class="op">=</span> arr[<span class="dv">0</span>:<span class="dv">6</span>]</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">slice_of_arr</code></pre></div>
<pre><code>array([0, 1, 2, 3, 4, 5])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">slice_of_arr[:] <span class="op">=</span> <span class="dv">99</span></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">slice_of_arr</code></pre></div>
<pre><code>array([99, 99, 99, 99, 99, 99])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_copy <span class="op">=</span> arr.copy()</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_copy</code></pre></div>
<pre><code>array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_copy[:] <span class="op">=</span> <span class="dv">100</span></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_copy</code></pre></div>
<pre><code>array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([99, 99, 99, 99, 99, 99,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d <span class="op">=</span> np.array([[<span class="dv">5</span>,<span class="dv">10</span>,<span class="dv">15</span>],[<span class="dv">20</span>,<span class="dv">25</span>,<span class="dv">30</span>],[<span class="dv">35</span>,<span class="dv">40</span>,<span class="dv">45</span>]])</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d</code></pre></div>
<pre><code>array([[ 5, 10, 15],
       [20, 25, 30],
       [35, 40, 45]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">0</span>][<span class="dv">0</span>]</code></pre></div>
<pre><code>5</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">0</span>]</code></pre></div>
<pre><code>array([ 5, 10, 15])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">2</span>,<span class="dv">1</span>]</code></pre></div>
<pre><code>40</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">2</span>,<span class="dv">1</span>] <span class="op">==</span> arr_2d[<span class="dv">2</span>][<span class="dv">1</span>]</code></pre></div>
<pre><code>True</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[:<span class="dv">2</span>,<span class="dv">1</span>:] <span class="co"># row 0,1 and col 1,2</span></code></pre></div>
<pre><code>array([[10, 15],
       [25, 30]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[:<span class="dv">2</span>]</code></pre></div>
<pre><code>array([[ 5, 10, 15],
       [20, 25, 30]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">1</span>:]</code></pre></div>
<pre><code>array([[20, 25, 30],
       [35, 40, 45]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">1</span>,<span class="dv">11</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">&gt;</span> <span class="dv">5</span></code></pre></div>
<pre><code>array([False, False, False, False, False,  True,  True,  True,  True,  True], dtype=bool)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">bool_arr <span class="op">=</span> arr <span class="op">&gt;</span> <span class="dv">5</span></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">bool_arr</code></pre></div>
<pre><code>array([False, False, False, False, False,  True,  True,  True,  True,  True], dtype=bool)</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[bool_arr]</code></pre></div>
<pre><code>array([ 6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[arr <span class="op">&gt;</span> <span class="dv">5</span>] <span class="co"># in 1 Step</span></code></pre></div>
<pre><code>array([ 6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr[arr <span class="op">&lt;</span> <span class="dv">3</span>]</code></pre></div>
<pre><code>array([1, 2])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d <span class="op">=</span> np.arange(<span class="dv">50</span>).reshape(<span class="dv">5</span>,<span class="dv">10</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d</code></pre></div>
<pre><code>array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr_2d[<span class="dv">1</span>:<span class="dv">3</span>,<span class="dv">3</span>:<span class="dv">5</span>]</code></pre></div>
<pre><code>array([[13, 14],
       [23, 24]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<h1 id="numpy-operation">NumPy Operation</h1>
<ul>
<li><strong>Array with Array</strong></li>
<li><strong>Array with Scalars</strong></li>
<li><strong>Universal Array Functions</strong></li>
</ul>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">0</span>,<span class="dv">11</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr</code></pre></div>
<pre><code>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">+</span> arr</code></pre></div>
<pre><code>array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">-</span> arr</code></pre></div>
<pre><code>array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">*</span> arr</code></pre></div>
<pre><code>array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">+</span> <span class="dv">100</span></code></pre></div>
<pre><code>array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">/</span> arr</code></pre></div>
<pre><code>/Users/YoungNguyen/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in true_divide
  &quot;&quot;&quot;Entry point for launching an IPython kernel.





array([ nan,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.,   1.])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">**</span> <span class="dv">2</span></code></pre></div>
<pre><code>array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.sqrt(arr)</code></pre></div>
<pre><code>array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
        2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ,
        3.16227766])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.<span class="bu">max</span>(arr)</code></pre></div>
<pre><code>10</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.<span class="bu">max</span>()</code></pre></div>
<pre><code>10</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.sin(arr)</code></pre></div>
<pre><code>array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
       -0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849,
       -0.54402111])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.log(arr)</code></pre></div>
<pre><code>/Users/YoungNguyen/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: RuntimeWarning: divide by zero encountered in log
  &quot;&quot;&quot;Entry point for launching an IPython kernel.





array([       -inf,  0.        ,  0.69314718,  1.09861229,  1.38629436,
        1.60943791,  1.79175947,  1.94591015,  2.07944154,  2.19722458,
        2.30258509])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<h1 id="numpy-exercises">NumPy Exercises</h1>
<h4 id="import-numpy-as-np">Import NumPy as np</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np</code></pre></div>
<h4 id="create-an-array-of-10-zeros">Create an array of 10 zeros</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.zeros(<span class="dv">10</span>)</code></pre></div>
<pre><code>array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])</code></pre>
<h4 id="create-an-array-of-10-ones">Create an array of 10 ones</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.ones(<span class="dv">10</span>)</code></pre></div>
<pre><code>array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])</code></pre>
<h4 id="create-an-array-of-10-fives">Create an array of 10 fives</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.ones(<span class="dv">10</span>) <span class="op">*</span> <span class="dv">5</span></code></pre></div>
<pre><code>array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.zeros(<span class="dv">10</span>) <span class="op">+</span> <span class="dv">5</span></code></pre></div>
<pre><code>array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])</code></pre>
<h4 id="create-an-array-of-the-integers-from-10-to-50">Create an array of the integers from 10 to 50</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">10</span>,<span class="dv">51</span>)</code></pre></div>
<pre><code>array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49, 50])</code></pre>
<h4 id="create-an-array-of-all-the-even-integers-from-10-to-50">Create an array of all the even integers from 10 to 50</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">10</span>,<span class="dv">51</span>,<span class="dv">2</span>)</code></pre></div>
<pre><code>array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
       44, 46, 48, 50])</code></pre>
<h4 id="create-a-3x3-matrix-with-values-ranging-from-0-to-8">Create a 3x3 matrix with values ranging from 0 to 8</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr <span class="op">=</span> np.arange(<span class="dv">9</span>)</code></pre></div>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">arr.reshape(<span class="dv">3</span>,<span class="dv">3</span>)</code></pre></div>
<pre><code>array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">9</span>).reshape(<span class="dv">3</span>,<span class="dv">3</span>)</code></pre></div>
<pre><code>array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])</code></pre>
<h4 id="create-a-3x3-identity-matrix">Create a 3x3 identity matrix</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.eye(<span class="dv">3</span>)</code></pre></div>
<pre><code>array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])</code></pre>
<h4 id="use-numpy-to-generate-a-random-number-between-0-and-1">Use NumPy to generate a random number between 0 and 1</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.rand(<span class="dv">1</span>)</code></pre></div>
<pre><code>array([ 0.63014358])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.rand(<span class="dv">4</span>)</code></pre></div>
<pre><code>array([ 0.87723824,  0.37650919,  0.25542703,  0.840097  ])</code></pre>
<h4 id="use-numpy-to-generate-an-array-of-25-random-numbers-sampled-from-a-standard-normal-distribution">Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randn(<span class="dv">25</span>)</code></pre></div>
<pre><code>array([ 0.19300069, -1.10465034, -0.17460169,  0.8790007 ,  0.68101474,
       -0.17313564,  0.18981315,  1.21170574,  0.35995229, -1.1242471 ,
       -2.0194464 , -0.24483055,  1.93109696, -0.65750283,  0.57590261,
       -0.70323009,  1.72649396,  1.23331433, -0.19985483,  0.89310901,
       -0.81475588,  0.179291  , -1.43815581,  1.2144338 ,  0.90117396])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.random.randn(<span class="dv">25</span>).shape</code></pre></div>
<pre><code>(25,)</code></pre>
<h4 id="create-the-following-matrix">Create the following matrix:</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.arange(<span class="dv">1</span>,<span class="dv">101</span>).reshape(<span class="dv">10</span>,<span class="dv">10</span>)<span class="op">/</span><span class="dv">100</span></code></pre></div>
<pre><code>array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.linspace(<span class="fl">0.01</span>,<span class="dv">1</span>,num<span class="op">=</span><span class="dv">100</span>).reshape(<span class="dv">10</span>,<span class="dv">10</span>)</code></pre></div>
<pre><code>array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])</code></pre>
<h4 id="create-an-array-of-20-linearly-spaced-points-between-0-and-1">Create an array of 20 linearly spaced points between 0 and 1:</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">np.linspace(<span class="dv">0</span>, <span class="dv">1</span>, num<span class="op">=</span><span class="dv">20</span>)</code></pre></div>
<pre><code>array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
        0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
        0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
        0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ])</code></pre>
<h2 id="numpy-indexing-and-selection">Numpy Indexing and Selection</h2>
<p>Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat <span class="op">=</span> np.arange(<span class="dv">1</span>,<span class="dv">26</span>).reshape(<span class="dv">5</span>,<span class="dv">5</span>)
mat</code></pre></div>
<pre><code>array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="co"># WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW</span>
<span class="co"># BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON&#39;T</span>
<span class="co"># BE ABLE TO SEE THE OUTPUT ANY MORE</span>
mat[<span class="dv">2</span>:, <span class="dv">1</span>:]</code></pre></div>
<pre><code>array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<pre><code>array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="co"># WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW</span>
<span class="co"># BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON&#39;T</span>
<span class="co"># BE ABLE TO SEE THE OUTPUT ANY MORE</span>
mat[<span class="dv">3</span>,<span class="op">-</span><span class="dv">1</span>]</code></pre></div>
<pre><code>20</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<pre><code>20</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="co"># WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW</span>
<span class="co"># BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON&#39;T</span>
<span class="co"># BE ABLE TO SEE THE OUTPUT ANY MORE</span>
mat[:<span class="dv">3</span>, <span class="dv">1</span>]</code></pre></div>
<pre><code>array([ 2,  7, 12])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat[:<span class="dv">3</span>, <span class="dv">1</span>:<span class="dv">2</span>]</code></pre></div>
<pre><code>array([[ 2],
       [ 7],
       [12]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<pre><code>array([[ 2],
       [ 7],
       [12]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="co"># WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW</span>
<span class="co"># BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON&#39;T</span>
<span class="co"># BE ABLE TO SEE THE OUTPUT ANY MORE</span>
mat[<span class="dv">4</span>, :]</code></pre></div>
<pre><code>array([21, 22, 23, 24, 25])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat[<span class="op">-</span><span class="dv">1</span>, :]</code></pre></div>
<pre><code>array([21, 22, 23, 24, 25])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat[<span class="op">-</span><span class="dv">1</span>]</code></pre></div>
<pre><code>array([21, 22, 23, 24, 25])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<pre><code>array([21, 22, 23, 24, 25])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="co"># WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW</span>
<span class="co"># BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON&#39;T</span>
<span class="co"># BE ABLE TO SEE THE OUTPUT ANY MORE</span>
mat[<span class="op">-</span><span class="dv">2</span>:, :]</code></pre></div>
<pre><code>array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat[<span class="dv">3</span>:<span class="dv">5</span>, :]</code></pre></div>
<pre><code>array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"></code></pre></div>
<pre><code>array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</code></pre>
<h3 id="now-do-the-following">Now do the following</h3>
<h4 id="get-the-sum-of-all-the-values-in-mat">Get the sum of all the values in mat</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat.<span class="bu">sum</span>() <span class="co"># or np.sum(mat)</span></code></pre></div>
<pre><code>325</code></pre>
<h4 id="get-the-standard-deviation-of-the-values-in-mat">Get the standard deviation of the values in mat</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat.std() <span class="co"># np.std(mat)</span></code></pre></div>
<pre><code>7.2111025509279782</code></pre>
<h4 id="get-the-sum-of-all-the-columns-in-mat">Get the sum of all the columns in mat</h4>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat</code></pre></div>
<pre><code>array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat.<span class="bu">sum</span>(axis<span class="op">=</span><span class="dv">0</span>) <span class="co"># sum of all the columns</span></code></pre></div>
<pre><code>array([55, 60, 65, 70, 75])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat.<span class="bu">sum</span>(axis<span class="op">=</span><span class="dv">1</span>) <span class="co"># sum of all the rows</span></code></pre></div>
<pre><code>array([ 15,  40,  65,  90, 115])</code></pre>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">mat.<span class="bu">sum</span>(axis<span class="op">=</span><span class="dv">1</span>).reshape(<span class="dv">5</span>,<span class="dv">1</span>) <span class="co"># sum of all the rows and reshape to 5 x 1 array</span></code></pre></div>
<pre><code>array([[ 15],
       [ 40],
       [ 65],
       [ 90],
       [115]])</code></pre>
