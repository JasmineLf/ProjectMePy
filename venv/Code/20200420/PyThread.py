'''
日期：2020-4-20 21:33:43
作者：LF
邮箱：jksj27250@gmail.com
主题：
    python多线程编程
内容：
    1.多线程的创建：
        【1】方式一：自定义函数的方式
        【2】方式二：自定义类的方式
    2.多线程编程的类和对象
'''



import os
import time
import threading

'''
#通过自定义函数创建线程
def fun_0(n):
    print('----------------start----------------\n')
    time.sleep(1)
    my_thread_name = threading.current_thread().name
    my_thread_id = threading.current_thread().ident
    print('当前线程名为：{},线程ID为:{},所在线程为：{},参数为：{}\n'.format(my_thread_name,my_thread_id,os.getpid(),n))
    print('----------------end------------------\n')

mythread = threading.Thread(target=fun_0,name="线程一",args=('参数1',))
mythread.start()
time.sleep(2)
'''

'''
#通过自定义类的方式创建线程
class MyTharend(threading.Thread):
    def __init__(self,n,name=None):   #函数重载
        super().__init__()
        self.name = name
        self.n = n

    def run(self):
        print('-----------------start------------------\n')
        time.sleep(1)
        my_thread_name = threading.current_thread().name
        my_thread_id = threading.current_thread().ident
        print('当前线程名为：{},线程ID为:{},所在线程为：{},参数为：{}\n'.format(my_thread_name,my_thread_id,os.getpid(),self.n))
        print("-----------------end--------------------\n")

#创建对象
mythread = MyTharend(n=1,name='线程一')
mythread.start()
time.sleep(2)

main_thread_name = threading.current_thread().name
main_thread_id = threading.current_thread().ident
print("主线程名字为：{},主线程ID为:{}\n".format(main_thread_name,main_thread_id))
'''

def fun_1():
    print('------------------启动子线程--------------------\n')
    for i in range(3):
        time.sleep(1)
        my_thread_name_1 = threading.current_thread().name
        my_thread_id_1 = threading.current_thread().ident
        print('{} - 已运行 ： {} 秒 '.format(my_thread_name_1,i+1))
    print('-------------------子线程结束-------------------\n')

print('-----------------启动主线程---------------------\n')
mythread = threading.Thread(target=fun_1(),name='线程1')
#设置守护线程
mythread.daemon = True
mythread.start()
mythread.join()
for i in range(3):
    time.sleep(1)
    my_thread_name_2 = threading.current_thread().name
    print('{} - 已运行 ： {} 秒 '.format(my_thread_name_2, i + 1))
print('----------------主线程结束-----------------------\n')