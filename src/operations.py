"""
Definations of operations based on the choices of user and the judging program
"""
import fetch
import constant

constant
def queryContribution():
    return 1

constant
def queryDonation():
    return 2

constant
def queryExit():
    return 9

def judge(choice):
    if queryContribution() == choice:
        fetch.queryContribution()
    elif queryDonation() == choice:
        fetch.queryDonation()
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
