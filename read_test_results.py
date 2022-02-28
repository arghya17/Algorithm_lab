import numpy as np

def read_results(filename):
    data=[]
    with open(filename) as file:
        data=file.read().splitlines()
    time=[]
    operations=[]
    for i in range(len(data)):
        p=data[i].strip().split()
        a=[]
        b=[]
        for j in range(0,len(p),2):
            a.append(float(p[j]))
            b.append(int(p[j+1]))
        a=np.array(a)
        b=np.array(b)
        time.append(a)
        operations.append(b)
    return time,operations
print(read_results('quick_uniform_data.txt'))