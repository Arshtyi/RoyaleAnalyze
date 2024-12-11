"""
ops
"""
import ops_defines
import fetch
def judge(choice):
    if ops_defines.contribution() == choice:
        fetch.contribution()
    else :
        print("Undefined control sequence.")
