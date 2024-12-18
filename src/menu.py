"""
Creat the menu and judge choice which chosen by user
"""
import clansInformation as infor
def creat_menu():
    print("当前操作对象：")
    for clan in infor.clans:
        print(clan,end = " ")
    print("\n请选择操作类型:")
    print("1.查询部落战贡献")
    print("2.查询部落成员捐赠")


def getChoice():
    choice = (int)(input())
    return choice
