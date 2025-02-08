""""
This module provides functions to concatenate paths for various files used in the project.
Functions:
    pathConcatenationForGroupPlayerInformationTable: Concatenates the path for the group player information table.
    pathConcatenationForClansInformationTable: Concatenates the path for the clans information table.
    pathConcatenationForOutputTable: Concatenates the path for the output table.
    log_path1: Concatenates the path for the first log file.
    log_path2: Concatenates the path for the second log file.
    log_path3: Concatenates the path for the third log file.

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
def log_path():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"logs")
    logPath = os.path.join(logDir,"brower.log")
    return logPath

def readme_path():##readme路径拼接
    currentDir = os.getcwd()
    currentDir = os.path.join(currentDir,"assets")
    readmepath = os.path.join(currentDir,"README.md")
    return readmepath