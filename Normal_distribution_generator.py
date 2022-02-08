import numpy as np
import sys, os
from frequency_plotter import plot

mean=50000
std_dev=100
int_max=pow(2,18)

with open("Normal.txt", "w") as file:
    i=1
    while(i<=int_max):
        nums=np.random.normal(loc=mean, scale=std_dev)
        nums=round(nums)
        s=f"{nums} "
        file.write(s)
        i=i+1

plot("Normal.txt")