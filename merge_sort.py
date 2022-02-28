import numpy as np
import time
from test_ascending import correct
from merge_test_data import generator
import matplotlib.pyplot as plt
from math import log2
from sklearn import preprocessing
#test_ascending is used for checking whether sorted array is ascending or not
class merge_1:
    def __init__(self) -> None:
        self.count=0 #for counting number of read write operations
    def merge_sort(self,low,high,nums):
        mid=(high+low)//2
        if low==high:
            return
        self.merge_sort(low,mid,nums)
        self.merge_sort(mid+1,high,nums)
        self.merge(low,high,nums)

    def merge(self,low,high,nums):
        mid=(high+low)//2
        a=np.zeros((mid-low+1,))
        b=np.zeros((high-mid,))
        j=0
        for i in range(low,mid+1):
            a[j]=nums[i]
            self.count=self.count+1
            j=j+1
        j=0
        for i in range(mid+1,high+1):
            b[j]=nums[i]
            self.count=self.count+1
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
            self.count=self.count+1
        while i<len(a):
            nums[k]=a[i]
            i=i+1
            k=k+1
            self.count=self.count+1
        while j<len(b):
            nums[k]=b[j]
            j=j+1
            k=k+1
            self.count+=1
        return 
x=[]
y=[]
operations=[]
'''
This is for the uniform data distribution only
'''
data=generator("Uniform.txt")
for i in range(len(data)):
    m=merge_1()
    start=time.time()
    m.merge_sort(0,len(data[i])-1,data[i])
    stop=time.time()
    x.append(len(data[i]))
    y.append((stop-start)*pow(10,6))#this is the time recording array
    operations.append(m.count)#this is the number of operations
    if not correct(data[i]):
        print("Incorrect sort")
#print(x,y) 
operations=np.array(operations)
'''
This is for the normal data distribution
'''
x2=[]
y2=[]
operations2=[]
data=generator("Normal.txt")
for i in range(len(data)):
    m=merge_1()
    start=time.time()
    m.merge_sort(0,len(data[i])-1,data[i])
    stop=time.time()
    x2.append(len(data[i]))
    y2.append((stop-start)*pow(10,6))#this is the time recording array
    operations2.append(m.count)
    if not correct(data[i]):
        print("Incorrect sort")

operations2=np.array(operations2)


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
plt.plot(x,operations/x,'.',color='#FFA009',alpha=0.2)
plt.plot(x2,operations/x2,alpha=0.7)
plt.ylabel("Pure constant")
plt.xlabel("Size of array")
plt.title("Constant Comparison")
plt.legend(["Constant k1(for uniform distribution)","Constant k2(for normal distribution)", 'Uniform distribution constant(operations)','Normal distribution constant(operations)'])
plt.show()
print("This is operations ratio", operations/x,operations,x)
plt.plot(x,operations,alpha=0.5)
plt.plot(x2,operations2,alpha=0.7)
plt.xlabel('Array size')
plt.ylabel('Number of operations')
plt.title('Operations in Merge sort')
plt.legend(['uniform distribution','Normal distribution'])
plt.show()