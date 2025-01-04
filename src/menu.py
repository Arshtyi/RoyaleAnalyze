"""
Creat the menu and judge choice which chosen by user
"""
import clansInformation as infor
import os
def creatMenu():
    print("欢迎使用皇室战争部落信息查询系统(By Arshtyi)！")
    print("本项目地址: https://github.com/Arshtyi/Clashofroyale ,建议阅读README.md.")
    print("请确保input文件夹下已正确导入clansInformation.xlsx文件以及存在output文件夹！")
    input("键入任意内容以继续...\n")###暂停
    os.system('cls')###清屏
    print("当前操作对象：")
    for clan in infor.clans:
        print(clan,end = " ")###输出部落名
    print("\n请选择操作类型:")
    print("1.查询部落战贡献")
    print("2.查询部落成员捐赠")
    print("3.查询部落成员最近活跃情况")
    print("...更多功能敬请期待...")
    print("9.退出")


def getChoice():
    choice = (int)(input())
    return choice
