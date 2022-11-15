import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# УПРАЖНЕНИЕ 1
'''def function(x):
    return np.log((np.e ** (1 / (1 + np.sin(x)))) / ((5 / 4) + (1 / x ** 15))) / np.log(1 + x * x)

x = np.array([1, 10, 1000])
print(function(x))'''

# УПРАЖНЕНИЕ 2
x = np.arange(-4, 5.01, 0.01)
plt.figure(figsize=(10, 5))

plt.plot(x, x**2 - x - 6, label=r'$f_1(x)=x^2-x-6$')
plt.plot([3, 3, 3], [-6, 0, 13], label=r'$f_2(x)=3$')
plt.plot([-2, -2, -2], [-6, 0, 13], label=r'$f_3(x)=-2$')

plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f_(x)$', fontsize=14)

plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()

# УПРАЖНЕНИЕ 3 
x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 8))

plt.plot(x, np.log((x * x + 1) * np.e ** (-(x * x) ** 0.5 / 10)) / np.log(1 + np.tan(1 / (1 + (np.sin(x)) ** 2))), label=r'$f_1(x)=x^2-x-6$')

plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f_(x)$', fontsize=14)

plt.grid(True)

plt.savefig('ex_3.png')
plt.show()

# УПРАЖНЕНИЕ 4
x = np.arange(-10, 10.01, 0.01)
y = input()
with plt.xkcd():
    plt.plot(x, eval(y))
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title('Самый красивый график на планете')
    plt.grid(True)
    plt.show()

# УПРАЖНЕНИЕ 5.1
x = [25, 100, 225, 400, 625, 784, 900, 1089, 1225, 1369] # a^2
y = [35.120, 37.833, 42.885, 49.885, 58.935, 65.383, 70.053, 77.629, 83.242, 88.959] # a * T^2

t = np.array(x)
ft = np.array(y)

a, b = np.polyfit(t, ft, 1)

delta = [y[i] - a*x[i] - b for i in range(10)]
max_delta = round(max(delta), 4)

plt.errorbar(x, y, xerr=1, yerr=0.001)


plt.plot(t, a*t+b, 'r--')
a = round(a, 3)
b = round(b, 3)
plt.text(200, 80, 'a*T^2 = a^2 * {} + {}'.format(a, b))
plt.text(200, 75, 'max(y - (a*x + b)) = {}'.format(max_delta))
plt.xlabel(r'$a^2$')
plt.ylabel(r'$a^2 * T$')

plt.grid()
plt.savefig('poly_deg1.png')
plt.show()

# УПРАЖНЕНИЕ 5.2
x = [1, 2, 3, 4, 5] # r^2
y = [0.99, 0.49, 0.35, 0.253, 0.18] # I

t = np.array(x)
ft = np.array(y)
s = np.arange(1, 5.01, 0.01)

a, b, c = np.polyfit(t, ft, 2)

delta = [y[i] - a * x[i]**2 - b * x[i] - c for i in range(5)]
plt.errorbar(x, y, xerr=0.1, yerr=0.05)

plt.plot(s, a * (s**2) + b*s + c, 'r--')
a = round(a, 4)
b = round(b, 4)
c = round(c, 4)

plt.text(2, 1, 'I = r^2 * {} + r * {} + {}'.format(a, b, c))
plt.text(2, 0.9, 'max(y - (a * x**2 + b * x + c)) = {}'.format(round(max(delta), 4)))
plt.xlabel(r'$r^2$')
plt.ylabel(r'$I$')

plt.grid()
plt.savefig('poly_deg1.png')
plt.show()