"""
路径拼接模块
该模块提供了一系列函数,用于生成项目中不同文件和目录的路径。这些路径主要用于读取和存储玩家信息、部落信息、输出数据、日志文件等。
函数列表:
- pathConcatenationForGroupPlayerInformationTable(): 生成玩家信息表的路径。
- pathConcatenationForClansInformationTable(): 生成部落信息表的路径。
- pathConcatenationForOutputTableDir(): 生成输出目录的路径。
- pathConcatenationForOutputTable(): 生成输出信息表的路径。
- log_path(): 生成日志文件的路径(已弃用)。
- readme_path(): 生成README文件的路径。
- Contributionslog_path(): 生成部落贡献日志目录的路径(自V1.1.4启用)。
- Donationslog_path(): 生成部落捐赠日志目录的路径(自V1.1.4启用)。
- FaultsLogDir_path(): 生成失败操作日志目录的路径。
- FaultsLog_path(): 生成失败操作日志文件的路径。
这些函数通过获取当前工作目录,并在其基础上拼接相应的子目录和文件名,返回完整的路径字符串。

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

def pathConcatenationForOutputTableDir(): ##输出路径拼接
    currentDir = os.getcwd()
    outputDir = os.path.join(currentDir,"data")
    outputDir = os.path.join(outputDir,"output")
    return outputDir

def pathConcatenationForOutputTable(): ##输出路径拼接
    currentDir = os.getcwd()
    outputDir = os.path.join(currentDir,"data")
    outputDir = os.path.join(outputDir,"output")
    outputInformationPath = os.path.join(outputDir,"Information.xlsx")
    return outputInformationPath

def log_dir_path():##日志目录路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"logs")
    logDir = os.path.join(logDir,"Program")
    return logDir

def log_path():##日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"logs")
    logDir = os.path.join(logDir,"Program")
    logPath = os.path.join(logDir,"program.log")
    return logPath

def readme_path():##readme路径拼接
    currentDir = os.getcwd()
    currentDir = os.path.join(currentDir,"assets")
    readmepath = os.path.join(currentDir,"README.md")
    return readmepath

##以下路径自V1.1.4被启用
def Contributionslog_path():##部落调试日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"logs")
    logDir = os.path.join(logDir,"Contributions")
    return logDir

def Donationslog_path():##部落调试日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"logs")
    logDir = os.path.join(logDir,"Donations")
    return logDir

def FaultsLogDir_path():##失败操作日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"output")
    return logDir

def FaultsLog_path():##失败操作日志路径拼接
    currentDir = os.getcwd()
    logDir = os.path.join(currentDir,"data")
    logDir = os.path.join(logDir,"output")
    logPath = os.path.join(logDir,"faults.log")
    return logPath