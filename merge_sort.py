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
plt.plot(x,y)
plt.xlabel("Lenth of array")
plt.ylabel("Time taken in micro s")
x1=[n for n in range(1,int(pow(2,18)+1))]
y1=[n*log2(n) for n in range(1,int(pow(2,18)+1))]#this is the n log n array
plt.plot(x1,y1)
plt.legend(["Actual time taken","Expected time complexity(nlog n)"])
plt.title("Time Complexity analysis of Merge sort")
plt.show()

y2=[]
y2=[(y[i]/y1[x[i]-1]) for i in range(len(y))]
coeff=np.median(y2)#this is the median of the constant
print(coeff)

y_norm=preprocessing.normalize([np.array(y)])
y1_norm=preprocessing.normalize([np.array(y1)])#normalisation
print(y1_norm,y_norm)
y3=np.array(y1)
y3=np.multiply(y3,coeff)#generating coeff*(n logn)
plt.plot(x,y_norm[0])
plt.plot(x1,y1_norm[0])
plt.plot(x,preprocessing.normalize([y2])[0])
plt.plot(x1,preprocessing.normalize([y3])[0],'b-',alpha=0.5)
plt.ylabel("Normalized Time taken")
plt.xlabel("Size of array")
plt.title("Normalized display")
plt.legend(["Normalized time","nlog n","constant","k*(nlog n)"])
plt.show()
