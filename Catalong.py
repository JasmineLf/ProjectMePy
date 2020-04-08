'''
日期：2020-4-8 21:20:19
作者：LF
邮箱：jksj27250@gmail.com
内容：
    1.os.access()
        功能：使用当前的uid/gid尝试访问路径
        语法：os.access(path,mode)
        参数：
            path: 用来检测是否具有访问权限的路径
            mode：mode为F_OK，测试存在的路径，或者它科技是包含R_OK,W_OK,X_OK或者R_OK,W_OK,X_OK其中之一或者更多
                os.F_OK:作为access()的mode参数，测试path是否存在
                os.R_OK：包含在access()的mode参数钟，测试PATH是否可读
                os.W_OK: 包含在access()的mode参数中，测死PATH是否可写
                os.X_OK: 包含在access()的mode参数中，测试PATH是否可执行
        返回值：
            允许访问返回True，否则返回False
    2.os.chdir()
        功能： 用于改变当前工作目录到指定的路径
        语法:  os.chdir(path)
        参数：
            path: 要切换到的新的路径
        返回值：
            如果允许返回Ture，否则返回Fslse
'''

import os,sys

ret = os.access("./test.txt",os.F_OK)
print("F_OX的返回值 %s" %ret)

ret = os.access("test.txt",os.R_OK)
print("R_OK的返回值 %s" %ret)

ret = os.access("test.txt",os.W_OK)
print("W_OK的返回值 %s" %ret)

ret = os.access("test.txt",os.X_OK)
print("X_OK的返回值 %s" %ret)


path = "/temp"

ret_0 = os.getcwd()
print("当前工作目录为： %s" % ret_0)

os.chdir(path)

ret_1 = os.getcwd()
print("目录修改成功：%s" %ret_1)

