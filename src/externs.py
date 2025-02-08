"""
This module provides functions to read and process information from Excel sheets related to clans and group players.
Constants:
    clansInformationSheetName (str): The name of the sheet containing clans information.
    groupPlayerInformationSheetName (str): The name of the sheet containing group player information.
    contributionsSheetName (str): The name of the sheet containing contributions information.
    donationsSheetName (str): The name of the sheet containing donations information.
    activitySheetName (str): The name of the sheet containing activity information.
    lastMonthWarSheetName (str): The name of the sheet containing last month's war information.
    lastMonthDonationSheetName (str): The name of the sheet containing last month's donation information.
    sortedSheetName (str): The name of the sheet containing sorted information.
    recentChangeSheetName (str): The name of the sheet containing recent changes information.
    inputClansInformationLocation (str): The file path for the clans information table.
    inputGroupPlayerInformationLocation (str): The file path for the group player information table.
    outputFileLocation (str): The file path for the output table.
    log_path1 (str): The file path for the first log.
    log_path2 (str): The file path for the second log.
    log_path3 (str): The file path for the third log.
    weightContribution (float): The weight for contributions.
    weightDonation (float): The weight for donations.
    inactivity (int): The inactivity threshold in minutes.
Functions:
    getClansInformation() -> dict:
        Reads the 'clansInformation' sheet from the specified Excel file and returns its content as a dictionary.
    getGroupPlayersInformation() -> dict:
        Reads the 'groupPlayerInformation' sheet from the specified Excel file and returns its content as a dictionary.
"""
import src.path as path
import openpyxl as op
import os
clansInformationSheetName = "Clans"
groupPlayerInformationSheetName = "Group"
contributionsSheetName = "Contribution"
donationsSheetName = "Donation"
activitySheetName = "Activity"
lastMonthWarSheetName = "LastMonthWar"
lastMonthDonationSheetName = "LastMonthDonation"
sortedSheetName = "Sorted"
recentChangeSheetName = "RecentChange"
inputClansInformationLocation = path.pathConcatenationForClansInformationTable()
inputGroupPlayerInformationLocation = path.pathConcatenationForGroupPlayerInformationTable()
outputFileLocation = path.pathConcatenationForOutputTable()
log_path= path.log_path()
readme_path = path.readme_path()
weightContribution = 0.25
weightDonation = 0.75
inactivity = 5 * 24 * 60
def getClansInformation():
    """
    从指定路径的 Excel 文件中读取 'clansInformation' sheet 的内容，
    从第二行开始，将第一列作为字典的 key，第二列作为对应的 value。
    
    :param file_path: str, Excel 文件路径
    :return: dict, 从 sheet 中读取的字典
    """
    # 加载op簿
    workbook = op.load_workbook(filename = inputClansInformationLocation)
    
    # 确保 sheet 名为 'clansInformation'
    if clansInformationSheetName not in workbook.sheetnames:
        raise ValueError(f"Excel 文件中没有名为 <{clansInformationSheetName}> 的 sheet")
    
    sheet = workbook[clansInformationSheetName]
    
    # 初始化结果字典
    result = {}
    
    # 遍历从第二行开始的内容
    for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
        key, value = row
        if key is not None:  # 确保 key 不为空
            result[key] = value
    workbook.close()
    return result
def getGroupPlayersInformation():
    if not os.path.exists(inputGroupPlayerInformationLocation):
        return {}
    wb = op.load_workbook(filename = inputGroupPlayerInformationLocation)
    if groupPlayerInformationSheetName not in wb.sheetnames:
        raise ValueError(f"Excel 文件中没有名为 <{groupPlayerInformationSheetName}> 的 sheet")
    ws = wb[groupPlayerInformationSheetName]
    result = {}
    for row in ws.iter_rows(min_row=2, min_col=1, max_col=5, values_only=True):
        if row[0] in clans and (row[4] != 'y' and row[4] != 'Y' and row[4] != '是'):
            result[row[1]] = [row[0], row[2], row[3]]
    wb.close()
    return result
clans = getClansInformation()
players = getGroupPlayersInformation()