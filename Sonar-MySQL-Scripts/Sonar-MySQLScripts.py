#coding=utf-8

import pymysql
import re
import time


#连接数据库
db = pymysql.connect(host='10.240.7.140', port=3306, user='root', passwd='123456', database='sonar')
cursor=db.cursor()
print("Result: ", db)

#查询sonar所有项目：
sql1 = "SELECT NAME FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
#将项目名称写入文件
with open('project-name.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data12) )

#查询sonar所有项目的日期：
sql1 = "SELECT created_at FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
#将项目名称写入文件
with open('date.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data12) )

print("=====Will sleep 5S=====")
time.sleep(0.005)

#统计并存储uuid，按时间顺序
sql2 = "SELECT project_uuid FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data26 = cursor.execute(sql2)
data27 = cursor.fetchall()
with open('uuid.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data27) )

print("=====Will sleep 5S=====")
time.sleep(0.005)

#按行取uuid，通过每次取到的uuid 来查询并存储BLOCKER
file21=open('uuid.csv')
for cache in file21:
    sql2="SELECT count(*) FROM issues WHERE project_uuid='" + cache.replace("\n","")+ "' and issue_type IN(2) AND severity IN('BLOCKER');"
    data21 = cursor.execute(sql2)
    data22 = cursor.fetchall()
    data23 = str(data22)
    print("====BLOCKER Will sleep 0.3s======")
    time.sleep(0.03)
    data23 = re.sub("\D","",data23)
#    print(type(data23))
#    print(data23)
    open('BLOCKER.csv','+a').write( ''.join(data23+"\n"))


#按行取uuid，通过每次取到的uuid 来查询并存储BLOCKER
file21=open('uuid.csv')
for cache in file21:
    sql3="SELECT count(*) FROM issues WHERE project_uuid='" + cache.replace("\n","")+ "' and issue_type IN(3) AND severity IN('CRITICAL');"
    data31 = cursor.execute(sql3)
    data32 = cursor.fetchall()
    data33 = str(data32)
    print("====CRITICAL Will sleep 0.3s======")
    time.sleep(0.03)
    data33 = re.sub("\D","",data33)
#    print(data23[2])
    open('CRITICAL.csv','+a').write( ''.join(data33+"\n"))


#按行取uuid，通过每次取到的uuid 来查询并存储BLOCKER
file21=open('uuid.csv')
for cache in file21:
    sql4="SELECT count(*) FROM issues WHERE project_uuid='" + cache.replace("\n","")+ "' and issue_type IN(3) AND severity IN('MAJOR');"
    data41 = cursor.execute(sql4)
    data42 = cursor.fetchall()
    data43 = str(data42)
    print("====MAJOR Will sleep 0.3s======")
    time.sleep(0.03)
    data43 = re.sub("\D","",data43)
#    print(data23[2])
    open('MAJOR.csv','+a').write( ''.join(data43+"\n"))

