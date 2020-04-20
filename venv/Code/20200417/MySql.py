'''
时间：2020-4-19 21:30:08
作者：LF
邮箱：jksj27250@gmail.com
主题：
    MySQL数据库编程
内容：
    1.MySQL数据库基础
        （1）下载安装
            [1]官网：https://www.mysql.com/
                下载地址：https://dev.mysql.com/downloads/mysql/
            [2]解压将 bin目录添加到环境变量path
            [3]跳转到mysql的bin目录下执行：mysqld --initialize --console   得到临时密码 如：2020-04-20T03:14:42.038079Z 0 [System] [MY-013169] [Server] H:\Program Files\mysql\mysql-8.0.19-winx64\mysql-8.0.19-winx64\bin\mysqld.exe (mysqld 8.0.19) initializing of server in progress as process 11596
2020-04-20T03:14:46.040055Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: ksg0ZKGf1g(:
            [4]安装服务(win10) 安装服务：mysqld -install  卸载服务： mysqld -remove  运行服务： net start mysql 停止服务: net stop mysql 登录服务：MySQL -u root -p
            [5] 修改密码：ALTER user 'root'@'localhost' IDENTIFIED BY '123456'；
            [6]常用数据库操作：
                            . show databases; #查看显示所有数据库
                            . select database(); #产看当前使用的数据库
                            . show varibles like 'port'; #查看数据库使用端口
                            . use information_schema #查看当前数据库大小
                            . use information_schema #查看数据所占的空间大小
                            . show variables like 'charcter%'; #查看数据库编码
                            . use databasename; #切换到数据库
                            . show tables; #查看数据库所在表
                            . show grants root@localhost; #查看用户权限
                            . show variables like '%max_connections%'; #查看最大链接
                            . show status like 'Threads%'; #查看线程数
                            . show variables like '%datadir%'; #查看文件路径
                            . create database name; #创建数据库
                            . drop database name; #删除数据库
                            . describe tablename #查看表的描述信息
        （2）MySQL模块概述
            [1]安装：python3 -m pip install PyMySQL
                版本查看：pip show PyMySQL
         (3)PyMySQL数据库连接：
            [1]类初始化
            [2]
'''


import pymysql.cursors

#import mysql.connector
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "show databases"
        dbs = cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "show tabls"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()