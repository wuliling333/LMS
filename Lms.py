# coding=utf-8
# coding=gbk
# @author: rourou
# @file: Lms.py
# @time: 2024/5/20 14:22
# @desc:
import os

# 菜单函数
def memu():
    print("*****************************")
    print("*      图书管理系统           *")
    print("* 1. 添加新图书信息           *")
    print("* 2. 通过图书ID修改图书信息      *")
    print("* 3. 通过图书ID删除图书信息      *")
    print("* 4. 通过书名删除图书信息      *")
    print("* 5. 通过图书ID查询图书信息      *")
    print("* 6. 通过书名查询图书信息      *")
    print("* 7. 显示所有图书信息         *")
    print("* 8. 退出系统                *")
    print("*****************************")
    select_op = input("输入编号选择操作：")
    return select_op

# 定义一个全局变量
books = []
# 编号（sid), 书名（name), 价格（price), 简介（summary) 四个信息
def getID():
    sid =input("请输入编号：")
    return sid
def getName():
    name = input("请输入书名：")
    return name
def getPrice():
    while True:
        price = input("请输入价格：")
        if len(price)>0 and price.isdigit():
           return int(price)
        else:
            print("输入的价格不合法")
def getSummary():
    summary = input("请输入简介：")
    return summary

# 实现添加图书函数(addBook)
def addBook(sid,name,price,summary):
    for b in books:
        if b["sid"] == sid:
            print("此ID的书已存在")
            return "添加失败"
    else:
        b={'sid':sid,'name':name,'price':price,'summary':summary}
        books.append(b)
        print(b)
        return addBook
# 实现通过编号修改图书信息函数(modifyBookByID)
def modifyBookByID(sid):
    for b in books:
        if b["sid"] == sid:
            name = getName()
            price = getPrice()
            summary = getSummary()
            b["name"] =name
            b["price"] = price
            b["summary"] = summary
            print("更改成功")
            return "更改成功"
    else:

        print(f"此ID:{sid}的图书不存在")
        return "更改失败"
# 实现通过图书ID删除图书函数（deleteBookByID）
def deleteBookByID(sid):
    for b in books:
        if b["sid"] == sid:
            books.remove(b)
            print("删除成功")
            return "删除成功"
    else:

        print(f"此ID:{id}的图书不存在")
        return "更改失败"

# 通过图书书名 删除所有符合的图书
def deleteBookByName(name):
    exit_name=[]
    for b in books:
        if b["name"] == name:
            exit_name.append(b)

        if len(exit_name)>0:
            for i in exit_name:
                books.remove(i)
                print(i)
                print(f"删除成功，书的书名{name},被删除")
            return "删除成功"
        else:
            print("查询失败")
# 实现通过ID函数(queryBookByID)
def queryBookByID(sid):

    for b in books:
        if b["sid"] == sid:
            print(f"查询成功，书的书{sid}")
            return "查询成功"
        else:
            print("查询失败")

# 实现通过书名查询图书函数(queryBookByName)
def queryBookByName(name):
    exit_name=[]
    for b in books:
        if b["name"] == name:
            exit_name.append(b)
            if len(exit_name)>0:
                print(f"查询成功，书的书名{name},图书一共{len(exit_name)}本")
                for i in exit_name:
                    print(i)
                return "查询成功"
        else:
            print("查询失败")


# 实现数据存储函数（save_data)
def save_data():
#     # 打开文件以写入模式
     with open("data.txt", "w") as file:
         for item in books:
             bookStr=""
             print(item)
             for v in item.values():
                 bookStr=bookStr + str(v) + "-"

             file.write(bookStr[:-1]+'\n')

     print("数据已成功写入到 data.txt 文件中。")

# 实现数据加载函数（load_data)
def load_data():
    if os.path.exists("data.txt"):
        with open("data.txt","r") as file:
            data=file.read()
            data=data.split("\n")
            data.remove("")
            for i in data:
                book={}
                print(i)
                i=i.split("-")
                book["sid"]=i[0]
                book["name"] = i[1]
                book["price"] = i[2]
                book["summary"] = i[3]
                books.append(book)


def showAllInfo():
    for b in books:
        print(b)

def bookManager():
    while True:
        select_op=memu()
        if len(select_op)>0 and select_op in "12345678":
            if select_op == "1":
                sid = getID()
                name = getName()
                price = getPrice()
                summary = getSummary()
                addBook(sid, name, price, summary)
            elif select_op == "2":
                sid = getID()
                modifyBookByID(sid)
            elif select_op == "3":
                sid = getID()
                deleteBookByID(sid)
            elif select_op == "4":
                name = getName()
                deleteBookByName(name)
            elif select_op == "5":
                sid = getID()
                queryBookByID(sid)
            elif select_op == "6":
                name = getName()
                queryBookByName(name)
            elif select_op == "7":
                showAllInfo()
            else:
                save_data()
                break

        else:
            print("请输入正确的序号")




if __name__ == '__main__':
    bookManager()