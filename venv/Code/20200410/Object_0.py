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
    4.对象的声明和访问
        （1）语法格式
        变量名 = 类名():五参数情况
        变量名 = 类名():有参数情况
            __init__(self,参数1,参数2……）
            注意事项：
                先声明后引用
                有参数的情况，需要重写初始化函数
                self代表类的实例，而非类
                类的方法与普通的函数只有一个特别的区别————他们必须有一个额外的第一个参数名称，按照惯例它的名称是self
    5.对象成员的访问：
        （1）语法格式：
        obj.name
        变量名.成员变量
        变量名.成员函数
            注意事项：
            成员访问符号“ . " ;
            成员访问权限：默认都是共有成员变量和共有成员函数
    6.类的属性访问控制：
        （1）语法格式：
        公有成员变量/函数：公有成员：对所有人公开，可以在类的外部直接访问；默认
        私有成员变量/函数(__XXX):双下划线开始，无双下划线结束；类的外部不能直接访问，需要滴哦啊用类的公开成员方法访问；
        保护成员变量/函数(_XXX):不能够通过“form module import *方式导入
        特殊成员函数(__XXX__(self)):双下划线开始+双下划线结束，系统定义的特殊函数，不能在类的外部访问
    7.类的继承
        （1）语法格式：
        单继承：class DriverdClassName(BaseClassName)
        多继承：class DriverdClassName(BaseClassName1,BaseClassName2,……）
            注意事项：
            基类顺序：基类中有相同的方法名，而在子类使用时未指定，python从左到右搜索，即方法在子类中未找到时，从左到右找基类中是否包含方法
            BaseClassName必须与派生类定义在一个作用域内
            子类继承父类的公有/保护成员变量和成员函数
            子类不能访问父类的私有成员变量和成员函数
    8.类的多态
        （1）语法格式：
        专有方法重载：通过重写父类已经实现的成员函数，实现父类已有函数的重载
        自定义方法重载：重写父类以实现成员函数，实现父类已有函数的重载
            注意事项：
            默认调用子类重载后的方法，除非在该父类中显示调用基类方法

'''
#不带参数
class MyClass:
    age = None

    def set_age(self):
        print(self.age)
        return self.age

    def get_age(self,age):
        self.age = age
        print(age)
        return age

#带参数
class MyClass0:
    def __init__(self,name,aga,obj):
        self.name = name              #公有成员：对所有人公开，可以直接在类的外面访问
        self._aga = aga               #保护成员：不能通过“form module import *"的方式导入
        self.__obj = obj              #私有成员：双下划线开始，无双下划线结束；类的外部不能直接访问，需要累的公开成员方法访问

        print("MyClass0 init")

    def get_name(self):
        print(self.name)
        return self.name

    def set_name(self,name):
        self.name = name
        print(name)

    def _get_aga(self):
        print(self._aga)
        return self._aga


class DeriveMyClass0(MyClass0):
    def __init__(self,name,aga,obj,cardno):
        MyClass0.__init__(self,name,aga,obj)
        self.cardno = cardno
        print("DeriveMyClass0 init")

    def get_name(self):
        print('DeriveMyClass0')

def main():
    myclass = MyClass()
    myclass.set_age()
    myclass.get_age(23)
    myclas0 = MyClass0('liming',12,'工程师')
    myclas0.get_name()
    myclas0.set_name('lixiang')
    myclas0._get_aga()
    deriveMyClass0 = DeriveMyClass0('liming',23,'工程师','123456')
    deriveMyClass0.set_name('libai')
    deriveMyClass0.get_name()

if __name__ == '__main__':
    main()
