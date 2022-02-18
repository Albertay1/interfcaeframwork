# import csv
# import operator
#
# # dic = {"testA": 2, "testC": 1, "testD": 3, "testB": 4}
# # dicn = sorted(dic.items(), key=operator.itemgetter(1))
# # for n in dicn:
# #     print(n[0])
#
# # dic2 = [{"testA": "/w/q", "num": 2, }, {"testC": "/w/q", "num": 1, }, {"testD": "/w/q", "num": 3},
# #         {"testB": "/w/q", "num": 4}]
# # dic1 = sorted(dic2, key=operator.itemgetter("num"))
# # for i in range(0, 3):
# #     # print(dic1)
# #     n = 0
# #     for content in dic1[i].items():
# #         if n == 0:
# #             print(content[0])
# #             print(content[1])
# #             n = n + 1
# file = open("F:\interfcaeframwork\config\config.csv", 'r')
# line = len(open("F:\interfcaeframwork\config\config.csv").readlines())
# # line = open("F:\interfcaeframwork\config\config.csv").readline()
# #
# # print(line)
# table = csv.reader(file)
# dic = {}
# n = 0
# liste = []
# for raw in table:
#     if n > 0:
#         # 将文件中取出的数据存入字典中
#         dic = {}
#         dic[raw[1]] = raw[0]
#         dic["num"] = raw[2]
#         # print(dic)
#     n = n + 1
#     if dic != {}:
#         liste.append(dic)
# print(liste)
#
# dicn = sorted(liste, key=operator.itemgetter("num"))
# # print(dicn)
# for i in range(0, line - 1):
#     n = 0
#     for content in dicn[i].items():
#         if n == 0:
#             filename = content[1]
#             fail = content[0]
#             print(filename + fail)
#         n = n+1
#
#
#
# ###############################练习文本#################################################################################
import csv
import operator
import unittest

if __name__ == '__main__':
    # 以只读方式打开文件，获取配置文件中的信息
    file = open("F:\interfcaeframwork\config\config.csv", "r")
    # 获取文件的行数，为后续循环做铺垫
    line = len(open("F:\interfcaeframwork\config\config.csv").readlines())
    table = csv.reader(file)
    dic = {}
    n = 0
    lestt = []
    # 添加for循环，进行文件内数据的获取
    for row in table:
        # 跳过第一行描述文字
        if n > 0:
            dic = {}
            # 将文件中的数据取出后放入字典中
            dic[row[1]] = row[0]
            dic["num"] = row[3]
            dic["state"] = row[2]
            # print(dic)
        n = n + 1
        if dic != {}:
            # 将字典中的数据按取出的数据依次放入列表中，按字典的格式
            lestt.append(dic)
    # print(lestt)
    # 使用排序方法将列表中的数据进行排序，根据num排序
    dicn = sorted(lestt, key=operator.itemgetter("num"))
    # print(dicn)
    for i in range(0, line - 1):
        num = 0
        for content in dicn[i].items():
            if num == 0:
                # print(content)
                fname = content[0]
                fail = content[1]
            if num == 2:
                state = content[1]
                print(state)
                if state == "Yes":
                    print("文件名", fname)
                    descover = unittest.defaultTestLoader.discover(fail, pattern=fname)
                    runner = unittest.TextTestRunner()
                    runner.run(descover)


                # 调用程序运行

            num = num + 1
