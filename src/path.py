""""
Path Concatenation
"""
import os

def pathConcatenationForGroupPlayerInformationTable():##玩家信息路径拼接
    currentDir = os.getcwd()
    playerDir = os.path.join(currentDir,"..","input")##与src同级目录##output同样
    playerInformationPath = os.path.join(playerDir,"groupInformation.xlsx")
    return playerInformationPath

def pathConcatenationForClansInformationTable():
    currentDir = os.getcwd()
    clansDir = os.path.join(currentDir,"..","input")
    clansInformationPath = os.path.join(clansDir,"clansInformation.xlsx")