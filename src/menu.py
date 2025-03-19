"""
菜单模块 (menu.py)
该模块负责展示RoyaleAnalyze项目的主菜单,并提供用户交互功能。主要功能包括:
1. 创建并显示主菜单,提供项目地址、更新日志、使用说明等信息。
2. 获取用户选择的操作类型。
3. 设置权重参数,用于贡献和捐赠的比重调整。
4. 选择是否对结果进行筛选,仅保留群内非请假玩家。
5. 显示操作失败日志,提示用户检查环境完整性。
函数:
- creatMenu(): 创建并显示主菜单。
- getChoice(): 获取用户选择的操作类型。
- weight(): 设置贡献和捐赠的权重参数。
- filterOrNot(): 选择是否对结果进行筛选。
- faultsDisplay(): 显示操作失败日志。
依赖模块:
- src.clansInformation: 提供部落和玩家信息。
- src.externs: 提供外部资源路径和操作类型。
- src.urls: 提供项目相关的URL地址。
- os: 提供操作系统相关功能。

"""
import src.clansInformation as infor
import src.externs as externs
import src.urls as urls
import os
import src.log as log
def welcome():
    print("欢迎使用RoyaleAnalyze-V1.1.5(By Arshtyi)！")
    print(f"本项目地址:'{urls.url_repository}',此外,本项目于2025/2/18结束所有开发与维护,后续开发工作见'{urls.url_repository_2}'")
    print(f"更新日志:'{urls.url_changelog}'")
    print(f"使用说明:'{urls.url_readme}'或'{externs.readme_path}'")
    input("键入任意内容以继续...\n")
    
def creatMenu():
    print("当前操作对象:")
    for clan in infor.clans:
        print(clan,end = " ")###输出部落名
    print("\n请选择操作编号（不支持组合输入）:")
    for key in externs.operations:
        print(f"{key}:{externs.operations[key]}")


def getChoice():
    while True:
        try:
            choice = int(input("请输入操作编号: \n"))
            return choice
        except ValueError:
            print("输入非法，请重新输入！")

def weight():
    print(f"是否修改权重？(y/n)当前值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}")
    weight_change = input().lower()
    if weight_change == "n" or weight_change == "no":
        print(f"未修改权重,启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}")
        log.log("INFO", "MENU", f"未修改权重,启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}", externs.log_path)
    elif weight_change == "y" or weight_change == "yes":
        print("请输入贡献权重(0-1);")
        pre_weight = (float)(input())
        if pre_weight < 0 or pre_weight > 1:
            print(f"输入错误！启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}")
            log.log("INFO", "MENU", f"输入错误！启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}",externs.log_path)
        else:
            externs.weightContribution = pre_weight
            externs.weightDonation = 1 - pre_weight
    else:
        log.log("INFO", "MENU", f"输入错误！启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}",externs.log_path)
        print(f"输入错误！启用默认值:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}")
    log.log("INFO", "MENU", f"权重设置完成:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}",externs.log_path)
    print(f"权重设置完成:贡献--{externs.weightContribution},捐赠--{externs.weightDonation}")

def filterOrNot():
    if len(infor.players) == 0:
        log.log("INFO", "MENU", "未读取到玩家信息！", externs.log_path)
        print("未读取到玩家信息！")
        return False
    print("是否对结果进行群内非请假玩家筛选？(y/n)默认为否...")
    print(f"当前'{externs.inputGroupPlayerInformationLocation}'文件中共{len(infor.players)}名玩家")
    filter_choice = input().lower()
    if filter_choice == "n" or filter_choice == "no":
        return False
    elif filter_choice == "y" or filter_choice == "yes":
        return True
    else:
        print("输入错误！启用默认值:否")
        log.log("INFO", "MENU", "输入错误！启用默认值:否", externs.log_path)
        return False
    
def faultsDisplay():
    if os.path.exists(externs.FaultsLog_path) == False:
        print("本次运行中没有操作失败")
        log.log("INFO", "MENU", "本次运行中没有操作失败", externs.log_path)
        return
    with open(externs.FaultsLog_path, "r") as f:
        failures = f.read().split()
        if len(failures) == 0:
            print("本次运行中没有操作失败")
            log.log("INFO", "MENU", "本次运行中没有操作失败", externs.log_path)
            return
        else:
            print("本次运行中以下操作失败:")
            for failure in failures:
                failure = (int)(failure)
                print(f"{failure}:{externs.operations[failure]}")
            print("建议检查环境是否完整后重新尝试...")
            return