'''
时间：2020年4月6日
作者：LF
主题：文件读取操作
'''

#文件打开

print("文件打开")
file = open("test.txt","r+")
print("文件以字符串方式写入")
file.write("my name is python3!\n")
print("文件关闭")
file.close()

#文件列表方式写入
data = ["string1","string2"]
file = open("test.txt",'a+')
#file.writelines(data)
print("文件列表方式写入")
file.writelines([line+'\n' for line in data])
file.close()

print("文件全部读取")
file = open("test.txt","r")
str = file.read()
print(str)
file.close()

print("按行读取")
file = open("test.txt","r")
str_0 = file.readline()
print(str_0)
file.close()

print("按行读取到列表")
file = open("test.txt","r")
line = file.readlines()
print(line)
file.close()
