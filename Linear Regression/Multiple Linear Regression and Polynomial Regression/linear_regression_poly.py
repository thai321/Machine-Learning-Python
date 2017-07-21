import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []

for line in open('data_poly.csv'):
  x, y = line.split(',')
  x = float(x)
  X.append([1, x, x*x])
  Y.append(float(y))

# convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Let's plot to see what it looks like
plt.scatter(X[:,1], Y)
plt.title("Raw data")
plt.show()


# Calculate weights
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, w)

# plot it all together
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.title("Predicted line")
plt.show()


# Calculate R-Squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print "The R-Squared is ", r2
#The R-Squared is  0.999141229637
