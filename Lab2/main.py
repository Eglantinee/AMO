import math
import time
import matplotlib
import matplotlib.pyplot as plt
import random

# Data for plotting

# t = (0.0, 2.0, 0.01)
# s = [ 1 + math.sin(2 * math.pi * i) for i in t]
#
# fig, ax = plt.subplots()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#
# fig.savefig("test.png")
# plt.show()
start_time = 0
def quick_sort(x):
    global start_time
    start_time = time.time()
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


quick_sort([1, 2, 3, 5, 6, 7, 4, 1])
# print(start_time, time.time())
a = [time.time() - start_time]
quick_sort([random.random() for i in range(40)])
a.append(time.time() - start_time)
quick_sort([random.random() for i in range(400)])
a.append(time.time() - start_time)
print(a)

b = [i for i in range(1, 10000, 10)]
c = [i * math.log1p(i) for i in b]
plt.plot(c, b)
plt.show()
print(math.log1p(2.8))
