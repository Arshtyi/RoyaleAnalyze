"""
ops
"""
import ops_defines
import fetch
def judge(choice):
    if ops_defines.contribution() == choice:
        fetch.contribution()
    elif ops_defines.donation() == choice:
        fetch.donation()
    else :
        print("Undefined control sequence.")
