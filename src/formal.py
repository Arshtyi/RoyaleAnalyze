"""
some formatting operations
"""
import externs
import openpyxl as op
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import operations 
import os
outputName = externs.outputFileLocation
contributionSheetName = externs.contributionsSheetName
donationSheetName = externs.donationsSheetName
clansInformationSheetName = externs.clansInformationSheetName
def clearSheet(fileName, sheetName):
    """
    清除指定工作表的所有内容、格式和合并单元格，完全重置工作表。
    
    :param file_name: Excel 文件的名称
    :param sheet_name: 目标工作表的名称
    """
    # 加载工作簿
    wb = op.load_workbook(fileName)
    
    # 获取目标工作表
    ws = wb[sheetName]
    # 取消所有合并单元格
    for merged_range in list(ws.merged_cells):
        ws.unmerge_cells(str(merged_range))  # 取消合并
    
    # 清除所有单元格的内容和格式
    for row in ws.iter_rows():
        for cell in row:
            cell.value = None  # 清空内容
            cell.style = 'Normal'  # 清除格式

    # 保存修改后的工作簿
    wb.save(fileName)

def checkFile(fileName):##当前目录下是否存在输出workbook
    if os.path.isfile(fileName):
        return True
    else:
        return False
    
def delSheetFromWorkbook(fileName,sheetName):##特定的sheet是否存在
    wb = op.load_workbook(filename = fileName)
    if sheetName in wb.sheetnames :##存在即删除
        if len(wb.sheetnames) > 1:##删或者清除
            del wb[sheetName]
        else :
            clearSheet(fileName,sheetName)
    wb.save(filename = fileName)
    ###不存在无事

def keep_before_first_newline(input_string):
    # 使用split方法按照 '\n' 切分字符串，取第一个部分
    return input_string.split('\n')[0]

def creatSheet(operation):
    if operations.creat_contribution_sheet() == operation:
        sheetName = contributionSheetName
        if checkFile(outputName):##输出文件是否存在
            ###存在则删除贡献sheet
            delSheetFromWorkbook(outputName,sheetName)
            wb = op.load_workbook(outputName)
            wb.create_sheet(title = sheetName)
        else :##不存在新建
            wb = op.Workbook()
            wb.create_sheet(title = sheetName)
        ws = wb[sheetName]
        ws.append(['部落','玩家','总使用卡组数','总袭击战船次数','总贡献'])##表头
        wb.save(filename = outputName)
    elif operations.creat_donation_sheet() == operation:
        sheetName = donationSheetName
        if checkFile(outputName): ##输出文件是否存在
            delSheetFromWorkbook(outputName,sheetName)
            wb = op.load_workbook(outputName)
            wb.create_sheet(title = sheetName)
        else: ##不存在新建
            wb = op.Workbook()
            wb.create_sheet(title = sheetName)
        ws = wb[sheetName]
        ws.append(['部落','玩家','近七天捐赠'])
        wb.save(filename = outputName)
    else :
        print("Undefined Query Type, Please Check Input Validity.")

def calculateAdjustedWidth(value):
    """
    根据单元格内容计算宽度，处理中文繁体和宽字符的显示宽度。
    :param value: 单元格内容
    :return: 调整后的宽度（适配 Excel 的列宽标准）
    """
    if value is None:
        return 0
    value = str(value)
    width = 0
    for char in value:
        # 宽字符 (中文、繁体、日文、韩文、emoji等)
        if '\u4e00' <= char <= '\u9fff' or ord(char) > 127:
            width += 2  # 宽字符占用2单位宽度
        else:
            width += 1  # 普通字符占用1单位宽度
    return width

def adjustColumnWidth(sheet):
    """
    动态调整工作表的列宽，确保中文繁体和宽字符正确显示。
    :param sheet: 当前工作表
    """
    for col in sheet.columns:
        max_width = 0
        col_letter = get_column_letter(col[0].column)  # 获取列号字母
        for cell in col:
            if cell.value is not None:
                # 根据内容计算宽度
                adjusted_width = calculateAdjustedWidth(cell.value)
                max_width = max(max_width, adjusted_width)
        # Excel的列宽与字符宽度不同，这里乘1.2是一个经验调整值
        sheet.column_dimensions[col_letter].width = max_width * 1.2

def processExcel(fileName):
    """
    处理Excel文件：
    1. 检查当前目录是否存在指定的Excel文件。
       - 如果不存在，抛出错误提示。
    2. 删除名为 "Sheet" 的工作表（如果 sheetnames 数量大于1）。
    3. 对剩下的每个工作表：
        - 调整列宽。
        - 设置单元格内容居中。
    :param file_name: str, Excel 文件名。
    """
    # 检查当前目录是否存在指定文件
    if not os.path.exists(fileName):
        print(f"文件 '{fileName}' 不存在！请检查文件名和路径。")
        return

    # 加载工作簿
    wb = op.load_workbook(fileName)

    # 删除 "Sheet" 工作表
    if len(wb.sheetnames) > 1 and "Sheet" in wb.sheetnames:
        del wb["Sheet"]

    # 遍历每个工作表
    for sheet in wb.worksheets:
        # 调整列宽
        adjustColumnWidth(sheet)

        # 设置单元格居中
        for row in sheet.iter_rows():
            for cell in row:
                cell.alignment = Alignment(horizontal="center", vertical="center")

    # 保存更改
    wb.save(fileName)

def sort_xlsx_data(file_path, sheet_name, start_row, end_row, sort_column):
    """
    按照给定的依据列对指定范围的行进行降序排序，
    其中，依据列内容为整数，且不能直接交换数据。

    :param file_path: Excel文件路径
    :param sheet_name: 工作表名
    :param start_row: 起始行
    :param end_row: 终止行
    :param sort_column: 排序依据列（从1开始，1表示第一列）
    :return: 排序后的数据（二维列表）
    """
    # 加载工作簿
    wb = op.load_workbook(file_path)
    sheet = wb[sheet_name]

    # 读取指定范围的行和列数据
    rows_to_sort = []
    for row in sheet.iter_rows(min_row=start_row, max_row=end_row, min_col=1, max_col=sheet.max_column, values_only=False):
        row_data = [cell.value for cell in row]
        # for data in row_data:
        #     print(f"type of data is {type(data)},data = {data}")  # 获取当前行的数据
        rows_to_sort.append(row_data)

    # 处理 None 值，确保排序时不会出错
    def sort_key(value):
        # 如果值为 None，则将其视为负无穷（float('-inf')），确保它排在最后
        if value is None:
            return float('-inf')
        return value

    # 依据列为整数，直接按整数进行排序（降序）
    rows_to_sort.sort(key=lambda x: sort_key(x[sort_column - 1]), reverse=True)

    # 根据排序后的数据更新工作表
    for i, row_data in enumerate(rows_to_sort, start=start_row):
        for j, value in enumerate(row_data):
            # 将排序后的数据写回相应的单元格
            sheet.cell(row=i, column=j + 1, value=value)

    # 保存修改后的文件
    wb.save(file_path)