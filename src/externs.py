import path
import openpyxl as op
clansInformationSheetName = "clansInformation"
contributionsSheetName = "Contribution"
donationsSheetName = "Donation"
activitySheetName = "Activity"
lastMonthWarSheetName = "LastMonthWar"
lastMonthDonationSheetName = "LastMonthDonation"
sortedSheetName = "Sorted"
inputClansInformationLocation = path.pathConcatenationForClansInformationTable()
inputGroupPlayerInformationLocation = path.pathConcatenationForGroupPlayerInformationTable()
outputFileLocation = path.pathConcatenationForOutputTable()
log_path1 = path.log_path1()
log_path2 = path.log_path2()
log_path3 = path.log_path3()
weightContribution = 0.25
weightDonation = 0.75
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
        raise ValueError(f"Excel 文件中没有名为 {clansInformationSheetName} 的 sheet")
    
    sheet = workbook[clansInformationSheetName]
    
    # 初始化结果字典
    result = {}
    
    # 遍历从第二行开始的内容
    for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
        key, value = row
        if key is not None:  # 确保 key 不为空
            result[key] = value
    
    return result

clans = getClansInformation()