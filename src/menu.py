"""
Creat the menu and judge choice which chosen by user
"""
import clansInformation as infor
import os
import externs
import urls
def creatMenu():
    print("欢迎使用皇室战争部落信息分析系统(By Arshtyi)！")
    print(f"本项目地址:'{urls.url_repository}',建议阅读README.md:'{urls.url_readme}'")
    print("本项目最新版本V1.1.0更新于2025年1月30日")
    print(f"请确保目录结构完整且'{externs.inputClansInformationLocation}'文件无误")
    input("键入任意内容以继续...\n")###暂停
    os.system('cls')###清屏
    print("当前操作对象：")
    for clan in infor.clans:
        print(clan,end = " ")###输出部落名
    print("\n请选择操作类型:")
    print("-1.比对更新部落信息和玩家信息")
    print("0.清除输出文件")
    print("1.查询当前部落战贡献")
    print("2.查询当前部落成员捐赠")
    print("3.查询部落成员最近活跃情况")
    print("4.查询近一月部落战贡献")
    print("5.查询近一月捐赠")
    print("6.根据4、5进行排序")
    print("7.查询近一月成员变动")
    print("...更多功能敬请期待...")
    print("99.格式化并退出")


def getChoice():
    choice = (int)(input())
    return choice

def weight():
    print(f"是否修改权重？（y/n）当前值：贡献——{externs.weightContribution}，捐赠——{externs.weightDonation}")
    weight_change = input()
    if weight == "n" or weight == "N":
        return
    elif weight_change == "y" or weight_change == "Y":
        print("请输入贡献权重（0-1）：")
        pre_weight = (float)(input())
        if pre_weight < 0 or pre_weight > 1:
            print(f"输入错误！启用默认值：贡献——{externs.weightContribution}，捐赠——{externs.weightDonation}")
        else:
            externs.weightContribution = pre_weight
            externs.weightDonation = 1 - pre_weight
        print(f"权重设置完成：贡献——{externs.weightContribution}，捐赠——{externs.weightDonation}")