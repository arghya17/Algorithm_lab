import numpy as np
import time
from test_ascending import correct
from quick_test_data import generator
import matplotlib.pyplot as plt
from math import log2
from sklearn import preprocessing
#test_ascending is used for checking whether sorted array is ascending or not
def quick_sort(low,high,nums):
    if(low>=high):
        return
    pi=partition(low,high,nums)
    quick_sort(low,pi-1,nums)
    quick_sort(pi+1,high,nums)
def partition(low,high,nums):
    pivot_index=high
    pivot=nums[pivot_index]
    start=low
    end=high
    while(start<end):
        while start<len(nums) and nums[start]<pivot:
            start=start+1
        while nums[end]>=pivot and end>0:
            end=end-1
        if start<end:
            nums[start],nums[end]=nums[end],nums[start]
    nums[start],nums[pivot_index]=nums[pivot_index],nums[start]
    return start

x=[]
y=[]
'''
This is for the uniform data distribution only
'''
data=generator("Uniform.txt")
for i in range(len(data)):
    x.append([])
    y.append([])
    for j in range(len(data[i])):
        start=time.time()
        quick_sort(0,len(data[i][j])-1,data[i][j])
        stop=time.time()
        x[i].append(len(data[i][j]))
        y[i].append((stop-start)*pow(10,6))#this is the time recording array
    if not correct(data[i][0]):
        print("Incorrect sort")
print(x,"\n",y) 
print(data)
x1=[np.mean(x[i]) for i in range(len(x))]
y1=[np.mean(y[i]) for i in range(len(y))]#Uniform distribution data
'''This is for normal distribution'''
x2=[]
y2=[]
data=generator("Normal.txt")
for i in range(len(data)):
    x2.append([])
    y2.append([])
    for j in range(len(data[i])):
        start=time.time()
        quick_sort(0,len(data[i][j])-1,data[i][j])
        stop=time.time()
        x2[i].append(len(data[i][j]))
        y2[i].append((stop-start)*pow(10,6))#this is the time recording array
    if not correct(data[i][0]):
        print("Incorrect sort")

print(x2,'\n',y2)
x3=[np.mean(x2[i]) for i in range(len(x2))]
y3=[np.mean(y2[i]) for i in range(len(y2))]#for normal distribution


#Diagram details
x_log=[n for n in range(1,int(pow(2,18)+1))]
y_log=[n*log2(n) for n in range(1,int(pow(2,18)+1))]
plt.plot(x1,y1)
plt.plot(x_log,y_log, color='#FFA500',alpha=0.5)
plt.plot(x3,y3)
for i in range(len(x)):
    plt.plot(x[i],y[i],'--',color='#F3A520')
for i in range(len(x2)):
    plt.plot(x2[i],y2[i],'-',color='#FAB400')
plt.title('Quick sort time analysis')
plt.xlabel('Array size')
plt.ylabel('Time in micro seconds')
plt.legend(['Mean time taken(Uniform distribution)','nlogn','Mean time taken(Normal distribution)'])
plt.show()

coeff_uni=[y1[i]/y_log(x1[i]-1) for i in range(len(y1))]
coeff_norm=[y3[i]/y_log(x3[i]-1) for i in range(len(y3))]#finding coeff
print(coeff_uni,'\n',coeff_norm)

plt.plot(coeff_uni,x1)
plt.plot(coeff_norm,x3)
plt.title("Coefficient in Time complexity")
plt.xlabel('Array size')
plt.ylabel('Pure ratio')
plt.legend(['Coefficient for Uniform distribution','Coefficient for normal distribution'])
plt.show()