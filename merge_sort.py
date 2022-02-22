import numpy as np
import time
from test_ascending import correct
from merge_test_data import generator
import matplotlib.pyplot as plt
from math import log2
from sklearn import preprocessing
#test_ascending is used for checking whether sorted array is ascending or not
def merge_sort(low,high,nums):
    mid=(high+low)//2
    if low==high:
        return
    merge_sort(low,mid,nums)
    merge_sort(mid+1,high,nums)
    merge(low,high,nums)

def merge(low,high,nums):
    mid=(high+low)//2
    a=np.zeros((mid-low+1,))
    b=np.zeros((high-mid,))
    j=0
    for i in range(low,mid+1):
        a[j]=nums[i]
        j=j+1
    j=0
    for i in range(mid+1,high+1):
        b[j]=nums[i]
        j=j+1
    i=0
    j=0
    k=low
    while (i<len(a) and j<len(b)):
        if a[i]<=b[j]:
            nums[k]=a[i]
            i=i+1
        else:
            nums[k]=b[j]
            j=j+1
        k=k+1
    while i<len(a):
        nums[k]=a[i]
        i=i+1
        k=k+1
    while j<len(b):
        nums[k]=b[j]
        j=j+1
        k=k+1
    return 
x=[]
y=[]
'''
This is for the uniform data distribution only
'''
data=generator("Uniform.txt")
for i in range(len(data)):
    start=time.time()
    merge_sort(0,len(data[i])-1,data[i])
    stop=time.time()
    x.append(len(data[i]))
    y.append((stop-start)*pow(10,6))#this is the time recording array
    if not correct(data[i]):
        print("Incorrect sort")
#print(x,y) 
'''
This is for the normal data distribution
'''
x2=[]
y2=[]
data=generator("Normal.txt")
for i in range(len(data)):
    start=time.time()
    merge_sort(0,len(data[i])-1,data[i])
    stop=time.time()
    x2.append(len(data[i]))
    y2.append((stop-start)*pow(10,6))#this is the time recording array
    if not correct(data[i]):
        print("Incorrect sort")
plt.plot(x,y,alpha=0.5) 
plt.xlabel("Lenth of array")
plt.ylabel("Time taken in micro s")
x1=[n for n in range(1,int(pow(2,18)+1))]
y1=[n*log2(n) for n in range(1,int(pow(2,18)+1))]#this is the n log n array
plt.plot(x1,y1)
plt.plot(x2,y2,alpha=0.5)
plt.legend(["Actual time taken(Uniform Distribution)","Expected time complexity(nlog n)","Actual time taken(Normal Distribution"])
plt.title("Time Complexity analysis of Merge sort")
plt.show()

y3=[]
y3=[(y[i]/y1[x[i]-1]) for i in range(len(y))]
coeff_uni=np.median(y3)#this is the median of the constant
print(coeff_uni,y3)

y4=[]
y4=[(y2[i]/y1[x2[i]-1]) for i in range(len(y2))]
coeff_norm=np.median(y4)
print(coeff_norm,y4)


plt.plot(x,y3,'--', color='#FFA500',alpha=0.5)
plt.plot(x2,y4,'b-',alpha=0.5)
plt.ylabel("Pure constant")
plt.xlabel("Size of array")
plt.title("Constant Comparison")
plt.legend(["Constant k1(for uniform distribution)","Constant k2(for normal distribution)"])
plt.show()
