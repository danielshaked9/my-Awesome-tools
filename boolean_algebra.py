from pickletools import int4
import numpy as np
from time import sleep
outputs=np.eye(10)
def exponent_size(num,exp=0):
    if(num==0):
        return exp
    exp=exponent_size(int(num/2),exp)
    return exp+1


def split(word):
    return list(word)
def gen_bin(num):
    exp_size=exponent_size(num)
    table=np.empty((num+1,exp_size),int)
    for i in range(num+1):
        table[i]=list(np.binary_repr(i,width=exp_size))
    return table
    
#num=1e300
#print(f"2^{exponent_size(num)}\t\t next binary bit add is at: {2**exponent_size(num)}")
a=gen_bin(15)

print(a)
