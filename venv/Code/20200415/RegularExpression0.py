'''
时间：2020-4-15 09:53:09
作者：LF
邮箱：jksj27250@gmail.com
主题：
    1.正则表达式
内容：
    1.正则表达式常用函数
        （1）编译：模式字符串编译生成正则表达式
        （2）检索：
        （3）替换：
        （4）切分：
    2.模块函数
        re.match(pattern,string,flags=0) : 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
        re.search(pattern,string,flags=0) : 扫描整个字符串并返回第一个成功的匹配
        re.sub(pattern,string,flags=0)  : 用于替换字符串中的匹配项，repl：替换的字符串，也可为一个函数
        re.compile(pattern[,flags=0])  : 用于编译正则表达式，生成一个正则表达式（pattern）对象，供match()he search()这两个函数使用
        re.findall(pattern,string[,pos[,endpos]])  :在字符串中找到正则表达式锁匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
        re.split(pattern,str[,maxsplit=0,flags=0])  : 能够匹配的子串将字符串分割后返回列表
    3.修饰字符
        re.I ：使匹配对大小写不敏感
        re.L ：做本地化识别（locale-aware)匹配
        re.M : 多行匹配，影响^和$
        re.S : 使.匹配包括换行在内的所有字符
        re.U ：根据Unicode字符集解析字符，这个标志影响\W,\W,\b,\B
        re.X : 该标志通过基于你更灵活的格式以便你讲正则表达式写的更易于理解

'''

import re

url = "http://abcxueyuan.cloud.baidu.com/#/play_video?id=15157&courseId=15157&mediaId=mda-kauqiwfhq0p2p7zs&videoId=3136&sectionId=15237&type=%E4%BB%98%E8%B4%B9%E8%AF%BE%E7%A8%8B&showCoursePurchaseStatus=true"

#方法一
print("----------------re.match()-----------------")
print(re.match('http',url))

#方法二
patterl = re.compile('http')
print(patterl.match(url))
print(patterl.search(url))
print(patterl.findall(url))
