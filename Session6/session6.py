#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##sesion 6 ## assignment 2
## import the math function for sqrt
import math
''' the function will take take dfault values as 1 and pass the same to the nested function 
inner function uses same paremer as of module and closure is formed'''

def in_v(n:int=1)->int:
    #print(n)
    # fromul to find the next fib number a = n * (1 + math.sqrt(5)) / 2.0;
    def calc_feb(n:int=1):
        a = n * (1 + math.sqrt(5)) / 2.0;
        return round(a)
    return calc_feb
nxt_val=in_v() ### calling the inner cal_feb function on the same parametr as of main scope
nxt_val(3)


# In[ ]:


##sesion 6 ## assignment 3
def add(a,b):
    return a+b
def mul(a,b) :
     return a*b  
'''created two functions'''
###setup and dict to accumulate the results
counters=dict()
def counter(fn):
    cnt=0
    '''a function counter has been created and fn : funtion has been passed
    in the sun function a closre is created which refer the nonloacl cnt
    which will accumlate every time the function haas been called'''

    def inner(*args,**kwargs):
        nonlocal cnt
        cnt=cnt+1
        counters[fn.__name__]=cnt #### globalvariable counetrs has  been assigned the cnt value
        return fn(*args,**kwargs)
    return inner
cnt_add=counter(add)
cnt_mul=counter(mul)
cnt_add(2,3)
cnt_add(3,5)
cnt_mul(2,3)
counters

