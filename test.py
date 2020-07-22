import time
from matplotlib import pyplot as plt
import tensorflow as tf

def DeviceTest(device_name,size,sess):
    with tf.device(device_name):       
        M1=tf.random_normal([size,size],name='M1')
        M2=tf.random_normal([size,size],name='M2')
        mul=tf.matmul(M1,M2,name='mul')
        sum_result=tf.reduce_sum(mul,name='sum_result')
        start_time=time.time()
        result=sess.run(sum_result)
        take_time=time.time()-start_time       
        #print(device_name,"  size=",size, " Time:",take_time)
        return take_time  #這樣append到SET才有東西

with tf.Session() as sess:
    Gpu_Set=[];  Cpu_set=[];  Size_set=[]
    for i in range(0,2001,100):
        TestGpu=DeviceTest("/gpu:0",i,sess)
        TestCpu=DeviceTest("/cpu:0",i,sess)
        #print("-"*100)
        Gpu_Set.append(TestGpu)
        Cpu_set.append(TestCpu)
        Size_set.append(i)


fig=plt.gcf()
fig.set_size_inches(5,5)
plt.plot(Size_set, Gpu_Set ,label='GPU')
plt.plot(Size_set, Cpu_set ,label='CPU')
plt.legend()
plt.xlabel('Computation')
plt.ylabel('Computation Time')
plt.show()