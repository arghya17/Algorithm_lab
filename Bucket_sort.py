import numpy as np
from merge_test_data import generator
from test_ascending import correct
from sklearn import preprocessing
import time
import matplotlib.pyplot as plt

def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucketSort(nums):
	arr = []
	slot_num = 500000
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in nums:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			nums[k] = arr[i][j]
			k += 1
	return nums

def normalize(data):
    x=[]
    for i in range(len(data)):
        x.append(preprocessing.normalize([data[i]])[0])
    data=x
    return data
data=generator('Uniform.txt')
print(data)
data=normalize(data)
print(data)
y=[]
x=[]
for i in range(len(data)):
	x.append(len(data[i]))
	start=time.time()
	data[i]=bucketSort(data[i])
	stop=time.time()
	print(i)
	y.append((stop-start)*pow(10,3))

    
data=generator('Normal.txt')
data=normalize(data)
x1=[]
y1=[]
for i in range(len(data)):
	x1.append(len(data[i]))
	start=time.time()
	data[i]=bucketSort(data[i])
	stop=time.time()
	print(i)
	y1.append((stop-start)*pow(10,3))

plt.plot(x,y,alpha=0.5)
plt.plot(x1,y1)
plt.title('Time analysis of bucket sort')
plt.legend(['Uniform distribution','Normal distribution'])
plt.xlabel('Array size')
plt.ylabel('Time in mili seconds')
plt.show()