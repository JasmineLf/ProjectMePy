'''
时间：2020-4-10 21:38:17
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.python 面向对象编程
内容：
    1.基本概念
        （1）类：用来描述具有相同属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。
        （2）成员函数/方法：类中定义的函数
        （3）成员变量：类中定义的变量
        （4）方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写。这个过程叫方法的覆盖，也称作方法的重写，方法重写的结果是多态。
        （5）类的继承：即一个派生类继承基类的字段和方法。继承也允许把一个派生类的对象作为一个基类对待。
        （6）类的实例：即对象，通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
    2.类的声明：
        （1）语法格式：
            class ClassName：
                <statement-1>:成员变量

                <statement-N>:成员函数
        （2）注意事项：
            类声明关键字：class；
            冒号：类名字后紧跟冒号其后是类的正文内容；
            缩进：次行缩进，相同缩进代表同一类下面成员
            成员函数：默认带self参数（必须）
            成员变量：必须赋初值，无值设置为None
            成员函数内访问成员变量：通过self.成员变量进行
    3.类的内置函数
        （1） __init__(self,...)  构造函数：初始化对象，在创建新对象时调用
        （2） __del__(self) 析构函数：释放对象，在对象被删除之前调用
        （3） __new__(cls,*args,**kwd) 实例生成操作
        （4） __str__(self) 在使用print语句是被调用
        （5） __getitem__(self,key) 获取序列的索引可以对应十五值，等价于色情【key】
        （6） __len__(self) 在调用内联函数len()时被调用
        （7） __cmp__(stc,dst) 比较两个对象src和dst（python3.x无效）
        （8） __getattr__(s,name) 获取属性不存在是调用
        （9） __setattr__(s,name,value) 设置属性的值
        （10） __delattr__(s,name) 删除name属性
        （11） __getattribute__() 获取属性时被调用
        （12） __gt__(self,other) 判断self对象是否大于other对象
        （13） __lt__(self,other) 判断self对象是否小于other对象
        （14） __ge__(self,other) 判断self对象是否大于或者等于other对象
        （15） __le__(self,other) 判断self对象是否小于或者等于other对象
        （16） __cq__(slef,other) 判断self对象是否等于other对象
'''

class MyClass:
    age = None

    def set_age(self):
        print(self.age)
        return self.age

    def get_age(self,age):
        self.age = age
        print(age)
        return age

def main():
    myclass = MyClass()
    myclass.set_age()
    myclass.get_age(23)

if __name__ == '__main__':
    main()
