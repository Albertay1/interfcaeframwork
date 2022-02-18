import csv

import requests


class workflow():
    def workflow_test(self, url, userinfo, interface, inter):
        userdate = {}
        s = requests.Session()
        response = s.post(url, data=userinfo).text
        print(response)
        userdate["接口结果"] = response
        r = response.find(interface)
        if r > 0:
            print(inter + "测试通过")
            userdate["测试结果"] = "测试通过"
        else:
            print(inter + "测试失败")
            userdate["测试结果"] = "测试失败"
        return userdate

    def filecase(self, userdate, face_name, filename):
        file2 = open(filename, "a")
        for key, value in userdate.items():
            file2.write(face_name + "," + key + "," + value + ",")
            file2.write("\n")
            file2.close()


if __name__ == '__main__':
    workflow_1 = workflow()
    filename = "..\date_test\\test_1"
    file = open("..\date_test\workflow_test.csv", "r")
    table = csv.reader(file)
    for row in table:
        url = row[1]
        interface = row[3]
        inter = row[5]
        userinfo = {}
        restuledate = {}
        j = int(row[6])
        for i in range(7, j * 2 + 7, 2):
            userinfo[row[i]] = row[i + 1]
