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
# start_time = 0
# def quick_sort(x):
#     global start_time
#     start_time = time.time()
#     if len(x) < 2:
#         return x
#     else:
#         pivot = x[0]
#         less = [i for i in x[1:] if i <= pivot]
#         greater = [i for i in x[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
#
# quick_sort([1, 2, 3, 5, 6, 7, 4, 1])
# print(start_time, time.time())
# a = [time.time() - start_time]
# quick_sort([random.random() for i in range(40)])
# a.append(time.time() - start_time)
# quick_sort([random.random() for i in range(400)])
# a.append(time.time() - start_time)
# print(a)
#
# b = [i for i in range(1, 10000, 10)]
# c = [i * math.log1p(i) for i in b]
# plt.plot(c, b)
# plt.show()

def quick_sort(x):
    # global start_time
    # start_time = time.time()
    if len(x) < 2:
        return x
    else:
        pivot = x[len(x) // 2]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort2(x, l, r):
    # if l >= r:
    #     return
#    print(l,'  ',r)
#    print(x)
    pivot = x[(l+r) // 2]
#    print("piv", pivot)
    i = l
    j = r
    while i<j:
        while x[i] <pivot:
            i += 1
        while x[j] > pivot:
            j -= 1
        if i<=j:
            x[i], x[j] = x[j], x[i]
 #           print("swap", i, j )
 #            w = x[i]
 #            x[i] = x[j]
 #            x[j] = w
            i +=1
            j -=1
    if l < j:
#        print('l=', l, '  j=',j)
        quick_sort2(x, l, j)
    if i < r:
#        print('i=', i, '  r=',r)
        quick_sort2(x, i, r)


m = 1000000





res = [1 for i in range(m)]
# res = [1,1,1,1,1,1,1,1,1,1]
# res.append()
# print( res)
res2 = [res]
# print(res2)

quick_sort2(res, 0, len(res)-1)
# print(res)
t = []
def g_run():
    # global res
    # global res2

    final = []
    #:for i in res2:
        #start_time = time.time()
       # final.append(quick_sort(i))
        #t.append(time.time() - start_time)
    start_time = time.time()
    m = quick_sort2(res, 0, len(res)-1)
    t.append(time.time() - start_time)
    print(t)
    # if res:
    #
    # # print(final)
    # print("exit norm")
    # print(t)
    # print(len(final[0]))

    # res.clear()

g_run()
