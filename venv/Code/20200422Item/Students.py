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
import  os,re

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
#录入学生信息函数
def insert():
    print("录入学生信息\n")

#查找学生信息函数
def search():
    print("查找学生信息\n")

#删除学生信息函数
def delete():
    print("删除学生信息\n")

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
    print("显示所有学生信息\n")

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