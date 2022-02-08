import numpy as np
import sys,os


int_max=pow(2,18)
def generator(file_name):
    with open(file_name) as file:
        nums=file.read()
        nums=nums.split()
        nums=list(map(int,nums))
    nums=np.array(nums)
    data=[]
    i=2
    while(i<=int_max):
        data.append(nums[0:i])
        i=i*2
    data=np.array(data)
    print(data)
    return data
