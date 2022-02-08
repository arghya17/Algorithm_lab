import numpy as np
import sys
import os
from frequency_plotter import plot

int_max=pow(2,18)
file=open("Uniform.txt","w")
i=1
while(i<=int_max):
    nums=round( np.random.uniform(low=0,high=9000))
    nums=int(nums)
    s=f'{nums} '
    file.write(s)
    i=i+1
file.close()
nums=[]
with open("Uniform.txt") as file:
    nums=file.read()
    nums=nums.split()
    nums=list(map(int,nums))
nums=np.array(nums)
print(nums)
plot("Uniform.txt")
