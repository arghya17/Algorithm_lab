import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def plot(file_name):
    with open(file_name) as file:
        nums=file.read()
        nums=nums.split()
        nums=list(map(int,nums))
    nums=np.array(nums)
    """the above is the process to extract or read from file"""
    unique, counts=np.unique(nums, return_counts=True)

    plt.plot(unique,counts,'bo')
    plt.xlabel("Range")
    plt.ylabel("Frequency")
    plt.show()


