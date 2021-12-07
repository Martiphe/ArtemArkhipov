import math
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20


def my_cos(x):

    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x ** 2
        if n == 1:
            multiplier = -1/2
        else:
            multiplier *= -1 / (2 * n) / (2 * n + 1)
        partial_sum += x_pow * multiplier

    return partial_sum


help(math.cos)
help(my_cos)

print(math.cos(0.1))
print(my_cos(0.1))

vs = np.vectorize(my_cos)
print(my_cos, vs)

angles = np.r_[0:1:0.01]
plt.plot(angles, vs(angles))
plt.show()


