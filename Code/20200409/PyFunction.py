'''
日期：2020-4-9 21:27:44
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.python 函数
内容：
    1.函数声明：
        a. 定义函数使用def关键字,例如：
            def 函数名(参数列表)
                函数体
                return 返回值

'''

def add(a,b):
    c = a+b
    print("%d + %d = %d\n"%(a,b,c))
    return c

def main():
    a = int(input("输入数字："))
    b = int(input("输入数字："))
    d =  add(a,b)

if __name__ == '__main__':
    main()
    e = add(3,4)
    print(e)

