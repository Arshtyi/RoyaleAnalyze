"""
This module provides various operations for managing and querying data.
Functions:
    updateInformation():
        Updates information. Returns -1.
    deleteAll():
        Deletes all data. Returns 0.
    queryContribution():
        Queries contribution data. Returns 1.
    queryDonation():
        Queries donation data. Returns 2.
    queryActivity():
        Queries activity data. Returns 3.
    queryLastMonthWar():
        Queries last month's war data. Returns 4.
    queryLastMonthDonation():
        Queries last month's donation data. Returns 5.
    queryAndSort():
        Queries and sorts data. Returns 6.
    queryRecentChange():
        Queries recent changes. Returns 7.
    queryExit():
        Exits the program. Returns 99.
    judge(choice):
        Executes the appropriate function based on the given choice.
    creat_contribution_sheet():
        Creates a contribution sheet. Returns 1.
    creat_donation_sheet():
        Creates a donation sheet. Returns 2.
    creat_activity_sheet():
        Creates an activity sheet. Returns 3.
    creat_last_month_war_sheet():
        Creates a last month war sheet. Returns 4.
    creat_last_month_donation_sheet():
        Creates a last month donation sheet. Returns 5.
    creat_sort_sheet():
        Creates a sorted sheet. Returns 6.
    creat_recent_change_sheet():
        Creates a recent change sheet. Returns 7.

"""
import src.fetch as fetch
import constant
import src.menu as menu
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
    if updateInformation() == choice:
        fetch.updateInformation()
    elif deleteAll() == choice:
        fetch.deleteAll()
    elif queryContribution() == choice:
        fetch.queryContribution(menu.filterOrNot())
    elif queryDonation() == choice:
        fetch.queryDonation(menu.filterOrNot())
    elif queryActivity() == choice:
        fetch.queryActivity(menu.filterOrNot())
    elif queryLastMonthWar() == choice:
        fetch.queryLastMonthWar(menu.filterOrNot())
    elif queryLastMonthDonation() == choice:
        fetch.queryLastMonthDonation(menu.filterOrNot())
    elif queryAndSort() == choice:
        menu.weight()
        fetch.queryAndSort(menu.filterOrNot())
    elif queryRecentChange() == choice:
        fetch.queryRecentChange()
    elif queryExit == choice:
        print("[OPERATIONS][INFO]: Exit Successfully.")
    else :
        print("[OPERATIONS][ERROR]: Undefined Query Type, Please Check Input Validity.")

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