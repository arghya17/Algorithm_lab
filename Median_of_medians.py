from statistics import median
import numpy as np
import time
from test_ascending import correct
from quick_test_data import generator
import matplotlib.pyplot as plt
from math import log2
from sklearn import preprocessing
from read_test_results import read_results
from numpy import random
#test_ascending is used for checking whether sorted array is ascending or not
class optimal_quick:
    def __init__(self,divide_size=5):
        self.count=0 #instance variable
        self.divide_size=divide_size
    def median(self,nums):
        if len(nums)%2==0:
            nums=np.sort(nums)
            return nums[len(nums)//2]
        else:
            return np.median(nums)
        
    
    def median_of_medians(self,nums):
        if len(nums)<self.divide_size:
            return self.median(nums)

        arr_size=0
        arr_size=len(nums)//self.divide_size
        if len(nums)%self.divide_size!=0:
            arr_size=arr_size+1
        arr=[]
        j=0
        for i in range(arr_size):
            end_index=j+self.divide_size
            if end_index>len(nums):
                end_index=len(nums)
            arr.append(self.median(nums[j:end_index]))
            j=end_index
        return self.median_of_medians(arr)
    def quick_sort(self,low,high,nums):
        if(low>=high):
            return
        pi=self.partition(low,high,nums)
        self.quick_sort(low,pi-1,nums)
        self.quick_sort(pi+1,high,nums)
    def partition(self,low,high,nums):
        pivot=self.median_of_medians(nums[low:high+1])
        start=low
        end=high
        while(start<end):
            while start<len(nums) and nums[start]<pivot:
                start=start+1
            while nums[end]>pivot and end>0:
                end=end-1
            if nums[start]==nums[end]:
                start+=1
            if start<end:
                nums[start],nums[end]=nums[end],nums[start]
                self.count=self.count+1
        self.count=self.count+1
        return end


r=optimal_quick()
a=[9,0,8,1,4,2,6,7,11,45,31,21,7]
r.quick_sort(0,len(a)-1,a)
print(a)
x=[]
y=[]
operations=[]
'''
This is for the uniform data distribution only
'''
data=generator("Uniform.txt")
for i in range(len(data)):
    x.append([])
    y.append([])
    for j in range(len(data[i])):
        q=optimal_quick()
        start=time.time()
        q.quick_sort(0,len(data[i][j])-1,data[i][j])
        stop=time.time()
        x[i].append(len(data[i][j]))
        y[i].append((stop-start)*pow(10,6))#this is the time recording array
    if not correct(data[i][0]):
        print("Incorrect sort")

# y,operations=read_results('rquick_uniform_data.txt')
# x1=[np.mean(x[i]) for i in range(len(x))]
# y1=[np.mean(y[i]) for i in range(len(y))]#Uniform distribution data

# print(x,y)

# '''This is for normal distribution
# '''
# x2=[]
# y2=[]
# operations2=[]
# data=generator("Normal.txt")
# for i in range(len(data)):
#     x2.append([])
#     for j in range(len(data[i])):
#         x2[i].append(len(data[i][j]))

# y2,operations2=read_results('rquick_normal_data.txt')
# print(x2,'\n',y2)
# x3=[np.mean(x2[i]) for i in range(len(x2))]
# y3=[np.mean(y2[i]) for i in range(len(y2))]#for normal distribution


# #Diagram details
# x_log=[n for n in range(1,int(pow(2,18)+1))]
# y_log=[n*log2(n) for n in range(1,int(pow(2,18)+1))]
# plt.plot(x1,y1)
# plt.plot(x_log,y_log, color='#FFA500',alpha=0.5)
# plt.plot(x3,y3)
# for i in range(len(x)):
#     plt.plot(x[i],y[i],'--',color='#F3A520')
# for i in range(len(x2)):
#     plt.plot(x2[i],y2[i],'-',color='#FAB400')
# plt.title('Randomized Quick sort time analysis')
# plt.xlabel('Array size')
# plt.ylabel('Time in micro seconds')
# plt.legend(['Mean time taken(Uniform distribution)','nlogn','Mean time taken(Normal distribution)'])
# plt.show()

# coeff_uni=[y1[i]/y_log[int(x1[i]-1)] for i in range(len(y1))]
# coeff_norm=[y3[i]/y_log[int(x3[i]-1)] for i in range(len(y3))]#finding coeff

# print([y_log[int(x3[i]-1)] for i in range(len(y3))])
# print('\n\n',y3,"\n\n\n",coeff_norm,x3)
# plt.plot(x1,coeff_uni,'.')
# plt.plot(x3,coeff_norm,'*')
# plt.title("Coefficient in Time complexity for Randomized quick sort")
# plt.xlabel('Array size')
# plt.ylabel('Pure ratio')
# plt.legend(['Coefficient for Uniform distribution','Coefficient for normal distribution'])
# plt.show()


# y_min1=[np.min(y[i]) for i in range(len(y))]
# y_max1=[np.max(y[i]) for i in range(len(y))]
# y_min2=[np.min(y2[i]) for i in range(len(y2))]
# y_max2=[np.max(y2[i]) for i in range(len(y2))]
# plt.plot(x1,y_min1)
# plt.plot(x1,y_max1)
# plt.plot(x3,y_min2)
# plt.plot(x3,y_max2)
# plt.title('Operations analysis of Randomized quick sort')
# plt.legend(['Minimum operation(Uniform)','Maximum operation(Uniform)',' Minimum operation(Normal)','Maximum operation(Normal)'])
# plt.xlabel('Array size')
# plt.ylabel('Number of operations')
# plt.show()

# y_mean1=[np.mean(y[i])/y_log[int(x1[i]-1)] for i in range(len(y))]
# y_mean2=[np.mean(y2[i])/y_log[int(x3[i])-1] for i in range(len(y))]
# plt.plot(x1,y_mean1,'o')
# plt.plot(x3,y_mean2,'.')
# plt.title("Coefficients of Randomized Quick sort")
# plt.legend(['Uniform data coefficient','Normal data coefficent'])
# plt.xlabel('Array size')
# plt.ylabel('ratio')
# plt.show()