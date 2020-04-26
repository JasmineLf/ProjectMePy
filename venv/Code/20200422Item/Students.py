'''
时间：2020-4-22 23:13:49
作者：LF
邮箱：jksj27250#gmail.com
主题：
    学生信息管理系统
内容：
    1.学生信息维护
        1.1.录入学生信息
        1.2.删除学生信息
        1.3.修改学生信息
    2.查询/统计
        2.1.按学生姓名查找
        2.2.按学生ID查找
        2.3.查询并显示所有学生信息
        2.4.统计学生总人数
    3.排序
        3.1升序排序
        3.2降序排序
'''
# -*- coding: UTF-8 -*-
import  os,re,sys

#显示菜单函数
def menu():
    #输出菜单
    print(""
          "$###################学生信息管理系统####################$\n"
          "$                                                      $\n"
          "$                    功 能 菜 单                        $\n"
          "$                   1.录入学生信息                      $\n"
          "$                   2.查找学生信息                      $\n"
          "$                   3.删除学生信息                      $\n"
          "$                   4.修改学生信息                      $\n"
          "$                   5.排序                             $\n"
          "$                   6.统计学生总人数                    $\n"
          "$                   7.显示所有学生信息                  $\n"
          "$                   0.退出系统                         $\n"
          "$                                                      $\n"
          "$######################################################$"
          "")

#保存学生信息到文件
def save(student):
    try:
        student_txt = open("student_information.txt",'a')                        #以追加的方式打开
    except Exception as e:
        student_txt = open("student_information.txt",'W')                        #文件不存在，创建文件并打开
    for info in  student:
        student_txt.write(str(info)+'\n')                       #按行存储，添加换行符
    student_txt.close()                                         #关闭文件

#录入学生信息函数
def insert():
    print("开始录入学生信息......\n")
    studentList = []                                            #保存学生信息列表
    mark = True
    while mark:
        id = input("请输入学生学号ID（如1001）：")
        if not id :
            break
        name = input("请输入学生姓名：（如赵海棠):")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩：(如100）"))
            python = int(input("请输入python成绩：（如100）"))
            C = int(input("请输入C语言成绩：（如100"))
        except:
            print("输入无效，不是整数数值......重新录入信息\n")
            continue
        #将学生成绩保存到字典
        stdent = {"ID":id,"name":name,"english":english,"python":python,"C":C}
        studentList.append(stdent)                              #将学生字典添加到列表
        inputMark = input("是否继续添加？（Y/N):")
        if inputMark == 'Y':
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！！！\n")

#将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:                                        #如果没有要显示的数据
        print("(^@_@^) 无数据信息 （^@_@^)\n")
        return
    #定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^12}"
    print(format_title.format("ID","姓名","英语成绩","Python成绩",
                              "C语言成绩","总成绩"))
    #定义具体内容显示格式
    format_data = "{:^6}{:^14}\t{:^12}\t{:^12}\t{:^12}\t{:^14}"
    for info in studentList:                                #通过for循环将列表中的数据全部显示出来
        print(format_data.format(str(info.get("ID")),
                                 info.get("name"),str(info.get("english")),
                                 str(info.get("python")),str(info.get("C")),
                                 str(info.get("english")+info.get("python")+
                                     info.get("C")).center(12)))


#查找学生信息函数
def search():
    print("开始查找学生信息......\n")

#删除学生信息函数
def delete():
    print("开始删除学生信息......\n")
    mark = True
    while mark:
        studentId = input("请输入需删除学生ID：")
        if studentId != "":                                         #判断输入要删除的学生是否存在
            if os.path.exists("student_information.txt"):               #判断文件是否存在
                with open("student_information.txt",'r') as rfile:      #打开文件
                    student_old = rfile.readlines()                     #读取全部内容
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open("student_information.txt","w") as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['ID'] != studentId:
                            wfile.write(str(d)+"\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID 为 %s 的学生信息已经删除......"%studentId)
                    else:
                        print("没有找到ID为%s 的学生信息......"%studentId)
            else:
                print("无学生信息......")
                break
            show()
            inputMark = input("是否继续删除？(Y/N):")
            if inputMark == 'Y':
                mark = True
            elif inputMark == 'y':
                mark = True
            else:
                mark = False

#修改学生信息函数
def modify():
    print("修改学生信息\n")

#排序
def sort():
    print("排序\n")

#统计学生总数
def total():
    print("统计学生总数\n")

#显示所有学生信息
def show():
    print("开始显示所有学生信息\n")
    student_new = []
    if os.path.exists("student_information.txt"):
        with open("student_information.txt",'r') as rfile:
            student_old = rfile.readlines()                      #读取全部内瓤
        for list in student_old:
            student_new.append(eval(list))                      #将找到的学生信息保存到列表中
        if student_new:
            show_student(student_new)
    else:
        print("占未保存学生信息\n")
    print("已录入学生信息答应完成！！！")

#主函数
def main():
    ctrl = True                                         #标记是否退出系统
    while(ctrl):
        menu()                                          #显示菜单
        option = input("请选择：")                      #选择菜单项
        option_str = re.sub("\D","",option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int = int(option_str)
            if option_int == 0:                         #退出系统
                print("您已经退出学生信息系统！\n")
                ctrl = False
            elif option_int == 1:                       #录入学生信息
                insert()
            elif option_int == 2:                       #查找学生成绩信息
                search()
            elif option_int == 3:                       #删除学生成绩信息
                delete()
            elif option_int == 4:                       #修改学生成绩信息
                modify()
            elif option_int == 5:                       #排序
                sort()
            elif option_int == 6:                       #统计学生总数
                total()
            elif option_int == 7:                       #显示所有学生信息
                show()



if __name__ == '__main__':
    main()