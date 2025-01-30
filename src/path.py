""""
Path Concatenation
"""
import os

def pathConcatenationForGroupPlayerInformationTable():##玩家信息路径拼接
    currentDir = os.getcwd()
    playerDir = os.path.join(currentDir,"data")
    playerDir = os.path.join(playerDir,"input")
    playerInformationPath = os.path.join(playerDir,"groupInformation.xlsx")
    return playerInformationPath

def pathConcatenationForClansInformationTable(): ##部落信息路径拼接
    currentDir = os.getcwd()
    clansDir = os.path.join(currentDir,"data")
    clansDir = os.path.join(clansDir,"input")
    clansInformationPath = os.path.join(clansDir,"clansInformation.xlsx")
    return clansInformationPath

def pathConcatenationForOutputTable(): ##输出路径拼接
    currentDir = os.getcwd()
    outputDir = os.path.join(currentDir,"data")
    outputDir = os.path.join(outputDir,"output")
    outputInformationPath = os.path.join(outputDir,"Information.xlsx")
    return outputInformationPath
def log_path1():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"logs")
    logPath = os.path.join(logDir,"brower.log")
    return logPath
def log_path2():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"logs")
    logPath = os.path.join(logDir,"log2.log")
    return logPath
def log_path3():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"logs")
    logPath = os.path.join(logDir,"log3.log")
    return logPath