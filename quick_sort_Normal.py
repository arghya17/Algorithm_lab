import numpy as np
import time
from test_ascending import correct
from quick_test_data import generator
from quick_sort import quick
import sys

sys.setrecursionlimit(1500)

x=[]
y=[]
'''
This is for the normal data distribution only
'''
file=open('quick_normal_data.txt','w')
data=generator("Normal.txt")
for i in range(len(data)):
    x.append([])
    y.append([])
    for j in range(len(data[i])):
        q=quick()
        start=time.time()
        q.quick_sort(0,len(data[i][j])-1,data[i][j])
        stop=time.time()
        x[i].append(len(data[i][j]))
        y[i].append((stop-start)*pow(10,6))#this is the time recording array
        nums=f'{(stop-start)*pow(10,6)} {q.count} '
        file.write(nums)
    file.write('\n')
    if not correct(data[i][0]):
        print("Incorrect sort")
file.close()