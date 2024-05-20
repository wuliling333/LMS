# coding=utf-8
# coding=gbk
# @author: rourou
# @file: Lms.py
# @time: 2024/5/20 14:22
# @desc:
# 功能拆解
# 图书信息包含：
#
# 编号（sid), 书名（name), 价格（price), 简介（summary) 四个信息
# 每个图书信息使用字典形式保存
# 使用列表保存所有图书的信息
# 实现菜单函数(menu)，输出下列信息，返回用户输入的编号
#
# print("*****************************")
# print("*      图书管理系统           *")
# print("* 1. 添加新图书信息           *")
# print("* 2. 通过图书ID修改图书信息      *")
# print("* 3. 通过图书ID删除图书信息      *")
# print("* 4. 通过书名删除图书信息      *")
# print("* 5. 通过图书ID查询图书信息      *")
# print("* 6. 通过书名查询图书信息      *")
# print("* 7. 显示所有图书信息         *")
# print("* 8. 退出系统                *")
# print("*****************************")
# 定义管理函数 (bookManager)，用来实现整体业务逻辑。
#
# 对用户输入内容进行输入校验
# 根据用户输入内容选择不同功能执行
# 因程序中需要多次对编号及书名进行输入，故抽取函数获取对应的数据。
#
# 获取编号函数（getID）, 输入编号并返回（字符串类型）eg. s01
# 获取书名函数（getName）, 输入书名并返回（字符串类型）
# 获取书名函数（getPrice）, 输入价格并返回（整型）
# 获取书名函数（getSummary）, 输入简介并返回（字符串类型）
# 实现添加图书函数(addBook)
#
# 函数参数为编号，书名，价格，简介四个参数
# 返回是否添加成功的结果
# 要求编号不可重复。
# 实现通过编号修改图书信息函数(modifyBookByID)
#
# 参数为图书ID
# 如果图书存在，则进行修改，不存在输出提示
# 返回是否修改成功
# 实现通过图书ID删除图书函数（deleteBookByID）
#
# 参数为图书ID
# 如果图书存在，则进行删除，不存在输出提示，并返回是否删除成功
# 实现通过书名删除图书函数(deleteBookByName)
#
# 参数为书名
# 如果图书存在，则进行删除（同名图书全部删除），不存在输出提示
# 返回是否删除成功
# 实现通过图书ID查询图书函数(queryBookByID)
#
# 参数为图书ID
# 如果图书存在，则输出图书信息，不存在输出提示
# 返回是否查询成功
# 实现通过书名查询图书函数(queryBookByName)
#
# 参数为书名
# 如果图书存在，则输出图书信息（同名图书全部输出），不存在输出提示
# 返回是否删除成功
# 实现显示所有图书信息函数(showAllInfo)
#
# 输出所有图书信息
# 实现数据存储函数（save_data)
#
# 在退出系统时，将数据保存到 db.txt 文件中
# 数据保存格式自定义
# 实现数据加载函数（load_data)
#
# 如果数据文件 db.txt 存在，则从文件中加载数据
# 如果文件不存在则初始为空

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
        if b.sid == sid:
            print("此ID的书已存在")
            return "添加失败"
    else:
        b={'id':sid,'name':name,'price':price,'summary':summary}
        books.append(b)
        print(b)
        return addBook
# 实现通过编号修改图书信息函数(modifyBookByID)
def modifyBookByID(sid):
    for b in books:
        if b.sid == sid:
            name = getName()
            price = getPrice()
            summary = getSummary()
            b.name =name
            b.price = price
            b.summary = summary
            print("更改成功")
            return "更改成功"
    else:

        print(f"此ID{sid}的图书不存在")
        return "更改失败"
# 实现通过图书ID删除图书函数（deleteBookByID）
def deleteBookByID(sid):
    for b in books:
        if b.sid == sid:
            books.remove(b.sid)
            print("删除成功")
            return "删除成功"
    else:

        print(f"此ID{id}的图书不存在")
        return "更改失败"

# 通过图书书名 删除所有符合的图书
def deleteBookByName(name):
    exit_name=[]
    for b in books:
        if b.name == name:
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
        if b.sid == sid:
            print(f"查询成功，书的书{sid}")
            return "查询成功"
        else:
            print("查询失败")

# 实现通过书名查询图书函数(queryBookByName)
def queryBookByName(name):
    exit_name=[]
    for b in books:
        if b.name == name:
            exit_name.append(b)
        if len(exit_name)>0:
            print(f"查询成功，书的书名{name},图书一共{len(exit_name)}本")
            for i in exit_name:
                print(i)
            return "查询成功"
        else:
            print("查询失败")




# 实现数据存储函数（save_data)
# def save_data():
#     b=addBook()
#     # 打开文件以写入模式
#     with open("data.txt", "w") as file:
#         file.write(b)
#
#     print("数据已成功写入到 data.txt 文件中。")

# 实现数据加载函数（load_data)


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
            # else:
            #     save_data()
            #     break


        else:
            print("请输入正确的序号")




if __name__ == '__main__':
    bookManager()