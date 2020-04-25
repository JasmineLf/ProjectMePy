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
    3.线程同步：
        3.1互斥锁
        3.2条件变量
        3.3信号量
        3.4事件
        3.5定时器
    4.线程通信
        1.共享内存
        2.全局变量
        3.消息队列
    5.线程池
'''



import os
import time
import threading
from threading import Thread,Event
from threading import Semaphore
import random
from datetime import datetime

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

'''
#多线程编程的类和对象
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
'''

'''
#互斥锁
class MyThread(threading.Thread):
    def __init__(self,name=None,lock=None):
        #super().__init__()
        threading.Thread.__init__(self)
        self.name = name
        self.lock = lock

    def run(self):
        print('-----------------------start:%s-------------\n'%self.getName())
        self.lock.acquire()  #获取锁
        global num_0
        temp = num_0
        time.sleep(0.2)
        temp -= 1
        num_0 = temp
        print('t_name = %s : num = %s' %(self.getName(),temp))
        self.lock.release()
        print('-----------------------end:%s---------------\n'%self.getName())


#主线程
print('--------------启动主线程-----------')
thread_lst = []
num_0 = 10
lock = threading.Lock() #互斥锁对象
for i in range(10):
    t = MyThread(name=str(i),lock=lock)
    thread_lst.append(t)
    t.start()
[t.join() for t in thread_lst]
print('num_0 最后的值为：{}'.format(num_0))
'''

'''
#条件变量
#生产者线程
class ProduceThread(threading.Thread):
    def __init__(self,name=None,con=None):
        super().__init__()
        self.name = name
        self.con = con

    def run(self):
        #锁定线程
        global num
        self.con.acquire()
        print('工厂开始生产……')
        while True:
            num += 1;
            print("已生产商品数量：{}\n".format(num))
            if num >= 5:
                print("商品数量达到5件，仓库饱满，停止生产...")
                con.notify()              #唤醒消费者
                con.wait()                #生产者自身陷入沉睡
        #释放锁
        self.con.release()

#消费者线程
class ConsumerThread(threading.Thread):
    def __init__(self,name=None,con=None):
        super().__init__()
        self.name = name
        self.con = con

    def run(self):
        #获取锁
        con.acquire()
        global num
        print("消费者开始消费....")
        while True:
            num -= 1
            print("剩余商品数量：{}\n".format(num))
            time.sleep(2)
            if num <= 0:
                print("库存为0，通知工厂生产......")
                con.notify()            #唤醒生产线程
                con.wait()              #消费者自身陷入沉睡
        #释放锁
        self.con.release()

if __name__ == '__main__':
    print("主线程启动")
    con = threading.Condition()
    num = 0
    p = ProduceThread("生产者线程", con)
    c = ConsumerThread("消费者线程", con)
    p.start()
    c.start()
'''

'''
#信号量
class MyThread(Thread):
    def __init__(self,name=None,semaph=None,customer=None):
        super().__init__()
        self.name = name
        self.sem = semaph
        self.custom = customer

    def run(self):
        self.sem.acquire()    #获取信号量
        print('{}号顾客：上座，开始就餐\n'.format(self.custom))
        time.sleep(random.random())
        print("{}号顾客：离座，就餐结束\n".format(self.custom))
        self.sem.release()



if __name__ == '__main__':
    sem = Semaphore(3)
    for i in range(20):
        p = MyThread("线程%d\n"%i,sem,i)
        p.start()
'''

'''
#事件
def func(e):
    print("子线程：开始运作...\n")
    while True:
        print("现在的秒数是：{}\n".format(datetime.now().second))
        e.wait()
        time.sleep(1)



if __name__ == '__main__':
    e = Event()
    p = Thread(target=func,args=(e,))
    p.daemon = True
    p.start()

    for i in range(10):
        s = int (str(datetime.now().second)[-1])
        if s < 5:
            print("子线程进入阻塞状态\n")
            e.clear() #使插入的Flag为False
        else:
            print("子线程取消阻塞状态\n")
            e.set() #线程进入非阻塞状态
        time.sleep(1)
    e.set()
    print("主线程运行结束")
'''

'''
#定时器 每隔XX执行一次
def sayTime(name):

    print("您好，{} 为您报时，现在的时间是：{}".format(name,time.ctime()))
    global timer
    timer = threading.Timer(3.0,sayTime,[name])
    timer.start()

if __name__ == '__main__':
    timer = threading.Timer(2.0,sayTime,["python"])
    timer.start()
'''



