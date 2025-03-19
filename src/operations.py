"""
operations.py
该模块是RoyaleAnalyze项目的核心操作模块,负责处理各种数据操作和查询功能。主要功能包括更新数据、删除数据、查询贡献数据、查询捐赠数据、查询活跃数据、查询上月战争数据、查询上月捐赠数据、查询并排序数据、查询最近变动数据以及退出程序。
函数列表:
- updateInformation(): 更新数据
- deleteAll(): 删除所有数据
- queryContribution(): 查询贡献数据
- queryDonation(): 查询捐赠数据
- queryActivity(): 查询活跃数据
- queryLastMonthWar(): 查询上月战争数据
- queryLastMonthDonation(): 查询上月捐赠数据
- queryAndSort(): 查询并排序数据
- queryRecentChange(): 查询最近变动数据
- queryExit(): 退出程序
- judge(choice): 根据用户选择执行相应操作
- creat_contribution_sheet(): 创建贡献数据表
- creat_donation_sheet(): 创建捐赠数据表
- creat_activity_sheet(): 创建活跃数据表
- creat_last_month_war_sheet(): 创建上月战争数据表
- creat_last_month_donation_sheet(): 创建上月捐赠数据表
- creat_sort_sheet(): 创建排序数据表
- creat_recent_change_sheet(): 创建最近变动数据表
该模块依赖于fetch模块进行具体的数据操作,menu模块进行用户交互,以及externs模块记录错误日志。

"""
import src.fetch as fetch
import constant
import src.menu as menu
import src.externs as externs
import src.log as log
constant
def updateInformation():
    return -1

constant
def deleteAll():
    return 0

constant
def queryContribution():
    return 1

constant
def queryDonation():
    return 2

constant
def queryActivity():
    return 3

constant
def queryLastMonthWar():
    return 4

constant
def queryLastMonthDonation():
    return 5

constant
def queryAndSort():
    return 6

constant
def queryRecentChange():
    return 7

constant
def queryExit():
    return 99

def judge(choice):
    flag = True
    if updateInformation() == choice:
        flag = fetch.updateInformation()
        if flag:
            log.log("INFO", "OPERATIONS", "更新数据成功...", externs.log_path)
            log.log("INFO", "OPERATIONS", "更新数据成功...", )
        else:
            log.log("ERROR", "OPERATIONS", "更新数据失败,第二次尝试...", externs.log_path)
            log.log("ERROR", "OPERATIONS", "更新数据失败,第二次尝试...", )
            flag = fetch.updateInformation()
            if flag:
                log.log("INFO", "OPERATIONS", "第二次更新数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次更新数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次更新数据失败...不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次更新数据失败...不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif deleteAll() == choice:
        flag = fetch.deleteAll()
        if flag:
            log.log("INFO", "OPERATIONS", "删除输出文件成功...", )
            log.log("INFO", "OPERATIONS", "删除输出文件成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "删除输出文件失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "删除输出文件失败,第二次尝试...", externs.log_path)
            flag = fetch.deleteAll()
            if flag:
                log.log("INFO", "OPERATIONS", "第二次删除输出文件成功...", )
                log.log("INFO", "OPERATIONS", "第二次删除输出文件成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次删除输出文件失败...不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次删除输出文件失败...不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryContribution() == choice:
        filter = menu.filterOrNot()
        flag = fetch.queryContribution(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询本周贡献数据成功...", )
            log.log("INFO", "OPERATIONS", "查询本周贡献数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询本周贡献数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询本周贡献数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryContribution(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询本周贡献数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询本周贡献数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询本周贡献数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询本周贡献数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryDonation() == choice:
        filter = menu.filterOrNot()
        flag = fetch.queryDonation(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询本周捐赠数据成功...", )
            log.log("INFO", "OPERATIONS", "查询本周捐赠数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询本周捐赠数据失败,第二次尝试...")
            log.log("ERROR", "OPERATIONS", "查询本周捐赠数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryDonation(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询本周捐赠数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询本周捐赠数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询本周捐赠数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询本周捐赠数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryActivity() == choice:
        filter = menu.filterOrNot()
        flag = fetch.queryActivity(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询当前活跃数据成功...", )
            log.log("INFO", "OPERATIONS", "查询当前活跃数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询当前活跃数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询当前活跃数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryActivity(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询当前活跃数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询当前活跃数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询当前活跃数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询当前活跃数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryLastMonthWar() == choice:
        filter = menu.filterOrNot()
        flag = fetch.queryLastMonthWar(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询上月部落战贡献数据成功...", )
            log.log("INFO", "OPERATIONS", "查询上月部落战贡献数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询上月部落战贡献数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询上月部落战贡献数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryLastMonthWar(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询上月部落战贡献数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询上月部落战贡献数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询上月部落战贡献数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询上月部落战贡献数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryLastMonthDonation() == choice:
        filter = menu.filterOrNot()
        flag = fetch.queryLastMonthDonation(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询上月捐赠数据成功...", )
            log.log("INFO", "OPERATIONS", "查询上月捐赠数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询上月捐赠数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询上月捐赠数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryLastMonthDonation(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询上月捐赠数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询上月捐赠数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询上月捐赠数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询上月捐赠数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryAndSort() == choice:
        menu.weight()
        filter = menu.filterOrNot()
        flag = fetch.queryAndSort(filter)
        if flag:
            log.log("INFO", "OPERATIONS", "查询并排序数据成功...", )
            log.log("INFO", "OPERATIONS", "查询上月贡献数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询并排序数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询上月贡献失败,第二次尝试...", externs.log_path)
            flag = fetch.queryLastMonthWar(filter)
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询并排序数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询并排序数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询并排序数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询并排序数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryRecentChange() == choice:
        flag = fetch.queryRecentChange()
        if flag:
            log.log("INFO", "OPERATIONS", "查询最近成员变动数据成功...", )
            log.log("INFO", "OPERATIONS", "查询最近成员变动数据成功...", externs.log_path)
        else:
            log.log("ERROR", "OPERATIONS", "查询最近成员变动数据失败,第二次尝试...", )
            log.log("ERROR", "OPERATIONS", "查询最近成员变动数据失败,第二次尝试...", externs.log_path)
            flag = fetch.queryRecentChange()
            if flag:
                log.log("INFO", "OPERATIONS", "第二次查询最近成员变动数据成功...", )
                log.log("INFO", "OPERATIONS", "第二次查询最近成员变动数据成功...", externs.log_path)
            else:
                log.log("ERROR", "OPERATIONS", "第二次查询最近成员变动数据失败,不再重新尝试,请进行检查更新后手动重试", )
                log.log("ERROR", "OPERATIONS", "第二次查询最近成员变动数据失败,不再重新尝试,请进行检查更新后手动重试", externs.log_path)
    elif queryExit() == choice:
        log.log("INFO", "OPERATIONS", "退出程序...", )
        log.log("INFO", "OPERATIONS", "退出程序...", externs.log_path)
    else :
        print("[OPERATIONS][ERROR]: 未定义的操作值,请重新输入")
        log.log("ERROR", "OPERATIONS", "未定义的操作值", externs.FaultsLog_path)
    if flag == False:
        log.log("ERROR", "OPERATIONS", f"此次操作失败,该条信息记录到'{externs.FaultsLog_path}'", )
        log.log("ERROR", "OPERATIONS", f"此次操作失败,该条信息记录到'{externs.FaultsLog_path}'", externs.log_path)
        with open(externs.FaultsLog_path, "a") as f:
            f.write(f"{choice} ")
            f.close()
constant
def creat_contribution_sheet():
    return 1

constant 
def creat_donation_sheet():
    return 2

constant
def creat_activity_sheet():
    return 3

constant
def creat_last_month_war_sheet():
    return 4

constant
def creat_last_month_donation_sheet():
    return 5

constant
def creat_sort_sheet():
    return 6

constant
def creat_recent_change_sheet():
    return 7