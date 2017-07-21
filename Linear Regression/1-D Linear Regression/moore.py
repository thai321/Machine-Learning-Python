import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
  r = line .split('\t')

  x = int(non_decimal.sub('',r[2].split('[')[0])) # year
  y = int(non_decimal.sub('',r[1].split('[')[0])) # trasition count
  X.append(x)
  Y.append(y)

X = np.array(X)
Y = np.array(Y)

# without scalling
plt.scatter(X,Y)
plt.title('RAW DATA')
plt.show()

# after scalling
Y = np.log(Y)
plt.scatter(X,Y)
plt.title('After log(DATA)')
plt.show()

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

Yhat = a*X + b

plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.title('Predicted, close to line')
plt.show()

d1 = Y - Yhat # how far we off from the actual value
d2 = Y - Y.mean() # how far we off if we just predicted the mean
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print ("a: ", a, "b: ", b)
print ("The R-Squared is: ", r2)

# tc = trasition time
# log(tc) = a*year + b
# tc = exp(b) * exp(a * year)
# 2*tc = 2 * exp(b) * exp(a * year) = exp(ln(2)) * exp(b) * exp(a * year)
# = exp(b) * exp(a * year + ln(2))

# --> exp(b) * exp(a*year2) = exp(b) * exp(a*year1 + ln2)
# a*year2 = a*year1 + ln2
# year2 = year1 + ln2/a
print("time to double: ", np.log(2)/a, " years")
"""
('a: ', 0.35104357336499337, 'b: ', -685.00028438165475)
('The R-Squared is: ', 0.95294428522857566)
('time to double: ', 1.974533172379868, ' years')
"""
