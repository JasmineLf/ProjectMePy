'''
时间：2020-4-6 21:47:11
作者：LF
邮箱：jksj27250@gmail.com
内容：python OS 文件操作方法
    1.os.open()
        功能：打开一个文件,模式参数可选，默认0777
        语法：os.open(file,flags[mode]
        参数：
            file:要打开的文件
            flags：改参数可以是以下选项，多用"|"隔开
                os.O_RDONLY:以只读方式打开
                os.O_WRONLY:以只写方式打开
                os.O_RDWR:以读写方式打开
                os.O_NONBLOCK:打开时不阻塞
                os.O_APPEND:已追加方式打开
                os.O_CREAT:创建并打开一个新文件
                os.O_TRUNC:打开一个文件并截断它的长度为0（必须有写权限
                os.O_EXCL:如果指定法人文件存在，返回错误
                os.O_SHLOCK:自动获取共享锁
                os.O_EXLOCK:自动获取独立锁
                os.O_DIRECT:消除或减少缓存效果
                os.O_FSYNC:同步写入
                os.O_NOFOLLOW:不追宗软连接
        返回值：返回新打开文件的描述符
    2.os.read()
        功能：用于从文件描述符fd中读取最多N个字节，返回包含读取字节的字符串，文件描述符fd对应文件已到达结尾，返回一个空字符串
        语法：os.read(fd,n)
        参数：
            fd：文件描述符
            n：读取的字节。os.O_RDONLY:以只读方式打开
        返回值：返回包含字节的字符串
    3.os.dup()
        功能：用于复制文件描述符fd
        语法：os.dup(fd)
        参数：
            fd:文件描述符
        返回值：返回复制的文件描述符
    4.os.duo2()
        功能：用于将一个文件描述符fd1复制到另一个fd2
        语法：os.dup2(fd1,fd2)
        参数：
            fd1:要被复制的文件描述符
            fd2：复制的文件描述符
        返回值：无
    5.os.write()
        功能：用于写入字符串到文件描述符fd中，返回实际写入的字符串长度
        语法：os.write(fd,str)
        参数：
            fd：文件描述符
            str：写入的字符串
        返回值：该方法返回写入的实际位数
    6.os.close()
        功能：用于关闭指定的文件描述符
        语法：os。close(fd)
        参数：
            fd：文件描述符
        返回值：无
    7.os.closerange()
        功能：用于关闭所有文件描述符fd
        语法：os.closerange(fd_low,fd_high)
        参数：
            fd_low:最小文件描述符
            fd_high:最大文件描述符
        返回值：无
    8.os.fchdir()
        功能：通过文件描述符改变当前工作目录
        语法：os.fchdir(fd)
        参数：
            fd:文件描述符
        返回值：无
'''

import os
import sys

fd = os.open("test.txt",os.O_RDWR|os.O_CREAT)
os.write(fd,str.encode("hello"))
os.close(fd)

fd = os.open("test.txt",os.O_RDWR)
str = os.read(fd,12)
print(str)
os.close(fd)

fd = os.open("test.txt",os.O_RDWR|os.O_CREAT)
d_fd = os.dup(fd)
os.write(d_fd,"基于文件描述符复制的写入测试".encode())
os.closerange(fd,d_fd)
'''
file = open("hello.txt",os.O_RDWR|os.O_CREAT)
os.dup2(file.filone(),1)
file.close()

'''
