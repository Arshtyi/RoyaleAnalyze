""""
Path Concatenation
"""
import os

def pathConcatenationForGroupPlayerInformationTable():##玩家信息路径拼接
    currentDir = os.getcwd()
    playerDir = os.path.join(currentDir,"input")##与src同级目录##output同样
    playerInformationPath = os.path.join(playerDir,"groupInformation.xlsx")
    return playerInformationPath

def pathConcatenationForClansInformationTable(): ##部落信息路径拼接
    currentDir = os.getcwd()
    clansDir = os.path.join(currentDir,"input")
    clansInformationPath = os.path.join(clansDir,"clansInformation.xlsx")
    return clansInformationPath

def pathConcatenationForOutputTable(): ##输出路径拼接
    currentDir = os.getcwd()
    outputDir = os.path.join(currentDir,"output")
    outputInformationPath = os.path.join(outputDir,"Information.xlsx")
    return outputInformationPath
def log_path():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"log")
    logPath = os.path.join(logDir,"log.txt")
    return logPath