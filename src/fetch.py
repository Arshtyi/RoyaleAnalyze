"""
fetch and save
"""
import urllib.request
import urls
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import urllib
import operations
from bs4 import BeautifulSoup
from clansInformation import clans
import openpyxl as op
from openpyxl.styles import PatternFill
import formal
import externs
import os
def updateInformation():
    print("准备更新部落信息和玩家信息...")
    print("检查文件...")
    if os.path.exists(externs.inputClansInformationLocation):
        print("文件存在，准备读取...")
        wb = op.load_workbook(externs.inputClansInformationLocation)
        ws = wb[externs.clansInformationSheetName]
        max_row = ws.max_row
        print("文件读取完成，准备更新部落信息...")
        for row in range(2,max_row + 1):
            clan = ws.cell(row = row,column = 2).value
            if clan is None:
                break
            clan = clan[1:]
            url_clan = urls.url_clan + clan
            requests = urllib.request.Request(url = url_clan,headers = urls.HEADERS)
            response = urllib.request.urlopen(requests)
            content = response.read().decode("utf-8")
            soup = BeautifulSoup(content, 'html.parser')
            hs = soup.find('h1',class_ = 'ui header margin0')
            clan_name = hs.get_text().strip().replace(' ','')
            ws.cell(row = row,column = 1).value = clan_name
            print(f"<{clan_name}>更新完成！")
        wb.save(filename = externs.inputClansInformationLocation)
        print("全部部落信息更新完成！准备格式化...")
        formal.processExcel(externs.inputClansInformationLocation)
        print("格式化完成！")
    else:
        print(f"The file '{externs.inputClansInformationLocation}' does not exist")
    if os.path.exists(externs.inputGroupPlayerInformationLocation):
        print("文件存在，准备读取...")
        wb = op.load_workbook(externs.inputGroupPlayerInformationLocation)
        ws = wb[externs.groupPlayerInformationSheetName]
        max_row = ws.max_row
        print("文件读取完成，准备玩家更新...")
        for row in range(2,max_row + 1):
            player = ws.cell(row = row,column = 4).value
            if player is None:
                break
            player = player[1:]
            url_player = urls.url_player + player
            requests = urllib.request.Request(url = url_player,headers = urls.HEADERS)
            response = urllib.request.urlopen(requests)
            content = response.read().decode("utf-8")
            soup = BeautifulSoup(content, 'html.parser')
            hs = soup.find('h1',class_ = 'ui header')
            player_name = hs.get_text().strip().replace('\u200c','').replace('\u2006','')
            div = soup.find('div',class_ = 'ui horizontal divided list')
            div = div.find('div',class_ = 'ui header item')
            a = div.find('a')
            if a is None:
                clan = "无"
            else:
                clan = a.get_text().strip().replace(' ','')
            ws.cell(row = row,column = 1).value = clan
            if clan not in externs.clans:
                fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
                ws.cell(row = row,column = 1).fill = fill
            ws.cell(row = row,column = 2).value = player_name
            print(f"<{player_name}>更新完成！")
        wb.save(filename = externs.inputGroupPlayerInformationLocation)
        print("全部玩家信息更新完成！准备格式化...")
        formal.processExcel(externs.inputGroupPlayerInformationLocation)
        print("格式化完成！")
    else:
        print(f"The file '{externs.inputGroupPlayerInformationLocation}' does not exist")

def deleteAll():
    print("准备删除输出文件...")
    print("检查文件...")
    if os.path.exists(externs.outputFileLocation):
        os.remove(externs.outputFileLocation)
        print(f"The file '{externs.outputFileLocation}' has been deleted")
    else:
        print(f"The file '{externs.outputFileLocation}' does not exist")

def queryContribution():
    sheet_name = externs.contributionsSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_contribution_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        url_war_race = url_0 + clans[clan] + "/war/race"
        requests = urllib.request.Request(url = url_war_race,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        div_time = soup.find('div',{'class' : 'timeline'})
        lis = div_time.find_all('li')
        day = 1####第四天开始战斗日
        in_war = 0##可能需要别的状态，不用bool
        data_num = 0
        for li in lis:
            div_unjudge = li.find('div',{'class' : "dot active"})
            if div_unjudge != None and day > 3:##active war-in day
                in_war = 1
                break
            day = day + 1 
        data = [clan]
        if 1 == in_war:
            print(f"<{clan}>正处于战斗日，开始查询...")
            trs = soup.find_all('tr')
            trs_players = [tr for tr in trs if 'player' in tr.get('class', []) and len(tr['class']) == 1]
            trs_players = trs_players[1:]
            for tr in trs_players:
                data = [clan]
                player_name_location = tr.find('a',{'class':'player_name force_single_line_hidden'})
                player_name = player_name_location.get_text().strip()
                player_name = player_name.replace('\u200c','').replace('\u2006','')
                data.append(player_name)
                player_decks_used = tr.find('div',{'class':'value_bg decks_used'})
                decks_uesd = (int)(player_decks_used.get_text())
                data.append(decks_uesd) 
                player_boat_attack = tr.find('div',{'class':'value_bg boat_attacks'})
                boat_attack = (int)(player_boat_attack.get_text())
                data.append(boat_attack)
                player_medal = tr.find('div',{'class':'value_bg fame'})
                medal = (int)(player_medal.get_text())
                data.append(medal)
                data_num = data_num + 1
                ws.append(data)
            now_row = now_row + data_num
            wb.save(filename = externs.outputFileLocation)
            formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 5) 
            wb = op.load_workbook(externs.outputFileLocation)
            ws = wb[sheet_name]
            ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
            start_row = now_row + 1
        elif 0 == in_war:
            print(f"<{clan}>未处于战斗日，格式输出正在进行...")
            data = [clan]
            data.append('该部落未处于战斗日！')
            data.append('')
            data.append('')
            data.append('')
            ws.append(data)
            now_row = now_row + 1
            start_row = now_row
            ws.merge_cells(start_column = 2,end_column = 5,start_row = now_row,end_row = now_row)
        print(f"<{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=5,max_col=5):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 5).fill = fill
    wb.save(filename = externs.outputFileLocation)

def queryDonation():
    sheet_name = formal.donationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_donation_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        print(f"<{clan}>开始查询...")
        data_num = 0
        url_donation = url_0 + clans[clan]
        requests = urllib.request.Request(url = url_donation,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        table_donation = soup.find('table', id='roster', class_='ui unstackable hover striped attached compact sortable table')
        trs = table_donation.find_all('tr')
        trs = trs[1:]
        for tr in trs:
            data = [clan]
            a_ty = tr.find('a',class_='block member_link')
            # if a_ty:
            player_name = formal.keep_before_first_newline(a_ty.get_text().strip())
            player_name = player_name.replace('\u200c','').replace('\u2006','') 
            data.append(player_name)
            td_donation = tr.find('td',class_='donations right aligned mobile-hide')
            donation = (int)(td_donation.get_text().strip().replace(',',''))
            data.append(donation)
            data_num = data_num + 1
            ws.append(data)
        now_row = now_row + data_num
        wb.save(filename = externs.outputFileLocation)
        formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 3)
        wb = op.load_workbook(externs.outputFileLocation)
        ws = wb[sheet_name]
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        start_row = now_row + 1
        print(f"<{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=3,max_col=3):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
    wb.save(filename = externs.outputFileLocation)    

def queryActivity():
    sheet_name = formal.activitySheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_activity_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        print(f"<{clan}>开始查询...")
        data_num = 0
        url_activity = url_0 + clans[clan]
        requests = urllib.request.Request(url = url_activity,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        table_activity = soup.find('table', id='roster', class_='ui unstackable hover striped attached compact sortable table')
        trs = table_activity.find_all('tr')
        trs = trs[1:]
        for tr in trs:
            data = [clan]
            a_ty = tr.find('a',class_='block member_link')
            player_name = formal.keep_before_first_newline(a_ty.get_text().strip())
            player_name = player_name.replace('\u200c','').replace('\u2006','')
            data.append(player_name)
            div = tr.find('div',class_='i18n_duration_short')
            activity = formal.convert_time_number(div.get_text().strip())
            data.append(activity)
            data_num = data_num + 1
            ws.append(data)
        now_row = now_row + data_num
        wb.save(filename = externs.outputFileLocation)
        wb = op.load_workbook(externs.outputFileLocation)
        ws = wb[sheet_name]
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        start_row = now_row + 1
        print(f"<{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=3,max_col=3):
        if row[0].value >= externs.inactivity:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
        ws.cell(row = row[0].row,column = 3).value = formal.convert_time_from_number(row[0].value)
    wb.save(filename = externs.outputFileLocation)

def queryLastMonthWar():
    sheet_name = formal.lastMonthWarSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_war_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        print("开始配置驱动...")
        edge_options = Options()
        edge_options.add_argument("--headless") 
        edge_options.add_argument("--disable-gpu") 
        edge_options.add_argument("--no-sandbox")  
        edge_options.add_argument("--disable-extensions")  
        edge_options.add_argument("--remote-debugging-port=0") 
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--ignore-ssl-errors")
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("驱动相关设置完成，准备配置日志输出...")
        service = EdgeService(EdgeChromiumDriverManager().install(),service_args=["--verbose","--log-path="+externs.log_path1])
        print(f"驱动启动项初始化完毕，日志输出为'{externs.log_path1}'，准备启动...")
        print("驱动配置完成，准备启动...")
        driver = webdriver.Edge(service = service,options = edge_options)
        print("驱动已启动，准备开始查询...")
        print(f"<{clan}>开始查询...")
        data_num = 0
        url_last_month_war = url_0 + clans[clan] +"/war/analytics"
        driver.get(url_last_month_war)
        print("驱动正在运行......在驱动正确退出前请不要结束进程，否则将导致数据不完整和其他可能的错误！")
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table_contributions = soup.find('table', id='roster')
        trs = table_contributions.find_all('tr')
        trs = trs[1:]
        table_decks = soup.find('table', id='roster2')
        trs_2 = table_decks.find_all('tr')
        trs_2 = trs_2[1:]
        length = max(len(trs),len(trs_2))
        data = []
        for i in range(length):
            tr = trs[i]
            data = [clan]
            td = tr.find('td',class_="sep fix first_col sticky")##名字标签
            player_name = formal.keep_before_first_newline(td.get_text().strip())
            player_name = player_name.replace('\u200c','').replace('\u2006','') 
            data.append(player_name)
            tds_contributions = tr.find_all('td',limit = 8)
            tds_contributions = tds_contributions[4:]
            all_contribution = 0
            for td in tds_contributions:
                contribution = td.get_text().strip()
                if contribution == "":
                    contribution = 0
                contribution = (int)(contribution)
                data.insert(2,contribution)
                all_contribution = all_contribution + (contribution)
            data.insert(7,all_contribution)
            td_paticipate = tr.find('td',class_='sorting_1')
            times = td_paticipate.get_text().strip().replace(" ","")
            data.append(times)
            tr_2 = trs_2[i]
            tds_2 = tr_2.find_all('td',limit = 8)
            tds_2 = tds_2[4:]
            length = len(tds_2)
            all_decks = 0
            for j in range(length):
                td_2 = tds_2[length - j - 1]
                decks = td_2.get_text().strip()
                if decks == "":
                    decks = 0
                decks = (int)(decks)
                all_decks = all_decks + decks
                data.insert(2 * j + 2,decks)
            data.insert(2 * length + 2,all_decks)
            data_num = data_num + 1
            ws.append(data)
        now_row = now_row + data_num
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        start_row = now_row + 1
        print(f"<{clan}>查询已完成！驱动准备退出...")
        driver.quit()
        print("驱动已正确退出")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=4,max_col=12):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 4).fill = fill
        if row[2].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 6).fill = fill
        if row[4].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 8).fill = fill
        if row[6].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 10).fill = fill
        if row[8].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 12).fill = fill
    print("所有查询已完成，准备保存数据...")
    wb.save(filename = externs.outputFileLocation)
    print("数据已保存，查询结束")

def queryLastMonthDonation():
    sheet_name = formal.lastMonthDonationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_donation_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        print("开始配置驱动...")
        edge_options = Options()
        edge_options.add_argument("--headless") 
        edge_options.add_argument("--disable-gpu") 
        edge_options.add_argument("--no-sandbox")  
        edge_options.add_argument("--disable-extensions")  
        edge_options.add_argument("--remote-debugging-port=0") 
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--ignore-ssl-errors")
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("驱动相关设置完成，准备配置日志输出...")
        service = EdgeService(EdgeChromiumDriverManager().install(),service_args=["--verbose","--log-path="+externs.log_path1])
        print(f"驱动启动项初始化完毕，日志输出为'{externs.log_path1}'，准备启动...")
        print("驱动配置完成，准备启动...")
        driver = webdriver.Edge(service = service,options = edge_options)
        print("驱动已启动，准备开始查询...")
        print(f"<{clan}>开始查询...")
        data_num = 0
        url_last_month_donation = url_0 + clans[clan]+"/history"
        driver.get(url_last_month_donation)
        print("驱动正在运行......在驱动正确退出前请不要结束进程，否则将导致数据不完整和其他可能的错误！")
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table_donnations = soup.find('table', id = 'roster')
        trs = table_donnations.find_all('tr')
        trs = trs[1:]
        data = []
        for tr in trs:
            data = [clan]
            td_name = tr.find('td',class_='sticky_col')
            player_name = formal.keep_before_first_newline(td_name.get_text().strip())
            player_name = player_name.replace('\u200c','').replace('\u2006','')
            data.append(player_name)
            tds = tr.find_all('td',limit = 6)
            tds = tds[2:]
            all_donation = 0
            for td in tds:
                donation = td.get_text().strip()
                if donation == "":
                    donation = 0
                donation = (int)(donation)
                all_donation = all_donation + donation
                data.insert(2,donation)
            data.insert(6,all_donation)
            data_num = data_num + 1
            ws.append(data)
        now_row = now_row + data_num
        wb.save(filename = externs.outputFileLocation)
        formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 7)
        wb = op.load_workbook(externs.outputFileLocation)
        ws = wb[sheet_name]
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        start_row = now_row + 1
        print(f"<{clan}>查询已完成！驱动准备退出...")
        driver.quit()
        print("驱动已正确退出")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=3,max_col=7):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
        if row[1].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 4).fill = fill
        if row[2].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 5).fill = fill
        if row[3].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 6).fill = fill
        if row[4].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 7).fill = fill
    print("所有查询已完成，准备保存数据...")
    wb.save(filename = externs.outputFileLocation)
    print("数据已保存，查询结束")


def queryAndSort():
    queryLastMonthWar()
    queryLastMonthDonation()
    print("前置查询完成，准备设定权重并启动程序...")
    weight_1 = externs.weightContribution
    weight_2 = externs.weightDonation
    print("权重设定完毕，准备创建输出...")
    formal.creatSheet(operations.creat_sort_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws_1 = wb[formal.lastMonthWarSheetName]
    ws_2 = wb[formal.lastMonthDonationSheetName]
    ws_3 = wb[formal.sortedSheetName]
    results = []
    last_clan = ""
    for row_1 in ws_1.iter_rows(min_row=2, max_row=ws_1.max_row, min_col=2, max_col=2):
        results = [(ws_1.cell(row = row_1[0].row, column = 1).value)]
        if results[0]:
            last_clan = results[0]
        else:
            results[0] = last_clan
        str_value = row_1[0].value 
        results.append(str_value)
        for row_2 in ws_2.iter_rows(min_row=2, max_row=ws_2.max_row, min_col=2, max_col=2):
            if row_2[0].value == str_value:
                value_1 = ws_1.cell(row=row_1[0].row, column=12).value
                value_2 = ws_2.cell(row=row_2[0].row, column=7).value
                result = (value_1 * weight_1) + (value_2 * weight_2)
                result = (int)(result)
                results.append(value_1)
                results.append(value_2)
                results.append(result)
                ws_3.append(results)
                break
    end = ws_3.max_row
    wb.save(filename = externs.outputFileLocation)
    print("数据已保存，准备排序...")
    formal.sort_xlsx_data(externs.outputFileLocation,formal.sortedSheetName,start_row = 2,end_row = end,sort_column = 5)
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[formal.sortedSheetName]
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col = 3,max_col = 5):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
        if row[1].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 4).fill = fill
        if row[2].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 5).fill = fill
    print("排序完成，准备保存权重信息...")
    ws.append(['贡献权重','捐赠权重'])
    ws.append([weight_1,weight_2])
    wb.save(filename = externs.outputFileLocation)
    print("权重信息已保存，程序已退出")

def queryRecentChange():
    sheet_name = formal.recentChangeSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_recent_change_sheet())
    print("输出创建完成，准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("程序启动，正在运行...")
    for clan in clans:
        print(f"<{clan}>开始查询...")
        data_num = 0
        url_change = url_0 + clans[clan] + "/history/join-leave"
        requests = urllib.request.Request(url = url_change,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        table_change = soup.find('div',class_ ='ui attached container sidemargin0 clan_history_join_leave')
        a_s = table_change.find_all('a')
        dict_change = {}
        for a in a_s:
            change_div = a.find('div',class_ = 'header')
            player_name = change_div.get_text().strip()
            if player_name not in dict_change:
                dict_change[player_name] = 0
            if "green plus icon" in str(a):
                dict_change[player_name] = dict_change[player_name] + 1
            elif "red minus icon" in str(a):
                dict_change[player_name] = dict_change[player_name] - 1
        in_num = 0
        out_num = 0
        for player in dict_change:
            data = [clan]
            if dict_change[player] == 0:
                continue
            elif dict_change[player] == 1:
                data.append(player)
                data.append("是")
                data.append("")
                data_num = data_num + 1
                in_num = in_num + 1
                ws.append(data)
            elif dict_change[player] == -1:
                data.append(player)
                data.append("")
                data.append("是")
                data_num = data_num + 1
                out_num = out_num + 1
                ws.append(data)
        ws.append([clan,"合计",in_num,out_num])
        url_all_members = url_0 + clans[clan]
        requests = urllib.request.Request(url = url_all_members,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        col = soup.find('div',class_ = 'doubling three column row')
        cols = col.find_all('div',class_ = 'column',limit = 4)
        cols = cols[3]
        members =cols.find('div',class_ = 'value').get_text().split('/')[0].strip()
        members = (int)(members)
        ws.append([clan,"目前成员数",members,members])
        data_num = data_num + 2
        now_row = now_row + data_num
        wb.save(filename = externs.outputFileLocation)
        wb = op.load_workbook(externs.outputFileLocation)
        ws = wb[sheet_name]
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        ws.merge_cells(start_row = now_row,start_column = 3,end_row = now_row,end_column = 4)
        start_row = now_row + 1
        print(f"<{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col = 3,max_col = 4):
        if row[0].value == "是":
            ws.cell(row = row[0].row,column = 3).value = ""
            fill = PatternFill(fill_type = 'solid',fgColor = '538DD5')
            ws.cell(row = row[0].row,column = 3).fill = fill
        elif row[1].value == "是":
            ws.cell(row = row[1].row,column = 4).value = ""
            fill = PatternFill(fill_type = 'solid',fgColor = 'DA9694')
            ws.cell(row = row[0].row,column = 4).fill = fill
    wb.save(filename = externs.outputFileLocation)