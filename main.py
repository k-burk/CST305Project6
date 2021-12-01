# This code is all written by Kara Sumpter
# This program will calculate 2 Taylor Polynomials using the taylor polynomial
# equation and the values that were solved out by hand.
# The Taylor Polynomial equation will then be graphed.
# Part 2 of this program uses a recurrence formula to find the n=8 values of an.
# To do this I logged the values into an array so that they could be used by the
# next value of an that required them. The values are then displayed.

import math
import numpy as np
import matplotlib.pyplot as plt
from part2 import *


# taylor polynomial equation up to 4th power
def talyor4(h, f0, f1, f2, f3, f4):
    yx = f0 + f1*h + (f2/math.factorial(2))*pow(h,2) + (f3/math.factorial(3))*pow(h,3) + \
         (f4/math.factorial(4))*pow(h,4)
    return yx

# values found from hand calculations
h=3.5
f0=1
f1=-1
f2=0
f3=-2
f4=-2

# ensuring initial value is correct
print(talyor4(h, f0, f1, f2, f3, f4))

x = np.linspace(0, 10)
y = []
for i in x:
    y.append(talyor4(i, f0, f1, f2, f3, f4 ))

# plotting equation
plt.plot(x,y)
plt.title("y2-2xy1+x^2y=0")
plt.show()

##################################################

# taylor polynomial equation up to 2nd power
def taylor2(h, f0, f1, f2):
    yx = f0 + f1 * h + (f2 / math.factorial(2)) * pow(h, 2)
    return yx

# values found from hand calculations
y0=6
y1=1
y2=13

#graphing values around 3
x = np.linspace(2, 4, 21)
y = []
# h values to find equation near 3, goes from 2 to 4
h = np.linspace(-1,1,21)

for i in h:
   y.append(taylor2(i,y0, y1, y2))

# plotting equation
plt.plot(x,y)
plt.title("y2-(x-2)y1+2y")
plt.show()

print("########## Part 2 ##########")
run() # running calculations for part 2

