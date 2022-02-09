import numpy as np
from sqlalchemy import false

def correct(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
