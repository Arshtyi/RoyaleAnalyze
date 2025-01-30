"""
Definations of operations based on the choices of user and the judging program
"""
import fetch
import constant
import menu
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
    return 9

def judge(choice):
    if deleteAll() == choice:
        fetch.deleteAll()
    elif queryContribution() == choice:
        fetch.queryContribution()
    elif queryDonation() == choice:
        fetch.queryDonation()
    elif queryActivity() == choice:
        fetch.queryActivity()
    elif queryLastMonthWar() == choice:
        fetch.queryLastMonthWar()
    elif queryLastMonthDonation() == choice:
        fetch.queryLastMonthDonation()
    elif queryAndSort() == choice:
        menu.weight()
        fetch.queryAndSort()
    elif queryRecentChange() == choice:
        fetch.queryRecentChange()
    elif queryExit == choice:
        print("Exit Successfully.")
    else :
        print("Undefined Query Type, Please Check Input Validity.")

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