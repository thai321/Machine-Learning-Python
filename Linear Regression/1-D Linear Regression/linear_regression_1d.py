import numpy as np
import matplotlib.pyplot as plt

# Load the data
X = []
Y = []
for line in open('data_1d.csv'):
  x, y = line.split(',')
  X.append(float(x))
  Y.append(float(y))

# turn X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)


# plot to see what it look like
plt.scatter(X,Y)
plt.show()

# apply the equations we learned to calculate a and b
denominator = X.dot(X) - X.mean() * X.sum()
a = (X.dot(Y) - Y.mean()*X.sum()) / denominator
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

# Calculated predicted Y
Yhat = a*X + b

# Plot it all
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# Calculate R-Squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print "The R-Squared is ", r2
# The R-Squared is  0.991183820298
