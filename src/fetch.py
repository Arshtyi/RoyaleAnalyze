"""
该模块用于从指定的URL获取部落和玩家信息,并将其更新到Excel文件中。模块主要功能包括:
1. updateInformation: 更新部落和玩家信息。
2. deleteAll: 删除输出文件。
3. queryContribution: 查询部落战贡献信息。
4. queryDonation: 查询部落捐赠信息。
5. queryActivity: 查询玩家活动信息。
6. queryLastMonthWar: 查询上个月的部落战信息。
7. queryLastMonthDonation: 查询上个月的捐赠信息。
8. queryAndSort: 查询并排序贡献和捐赠信息。
9. queryRecentChange: 查询最近的成员变动信息。
模块依赖于以下库和模块:
- urllib.request: 用于发送HTTP请求。
- selenium: 用于自动化浏览器操作。
- BeautifulSoup: 用于解析HTML内容。
- openpyxl: 用于操作Excel文件。
- src.urls: 包含URL和请求头信息。
- src.operations: 包含Excel操作函数。
- src.clansInformation: 包含部落和玩家信息。
- src.formal: 包含格式化和排序函数。
- src.externs: 包含外部配置和路径信息。
模块通过调用上述函数,实现对部落和玩家信息的自动化获取、更新和处理,并将结果保存到指定的Excel文件中。

"""
import urllib.request
import src.urls as urls
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import src.operations as operations
from bs4 import BeautifulSoup
from src.clansInformation import clans
from src.clansInformation import players
import openpyxl as op
from openpyxl.styles import PatternFill
import src.formal as formal
import src.externs as externs
import os
def updateInformation():
    flag = True
    print("[FETCH][INFO]: 准备更新部落信息和玩家信息...")
    print("[FETCH][INFO]: 检查文件...")
    if os.path.exists(externs.inputClansInformationLocation):
        print("[FETCH][INFO]: 文件存在,准备读取...")
        wb = op.load_workbook(externs.inputClansInformationLocation)
        ws = wb[externs.clansInformationSheetName]
        max_row = ws.max_row
        print("[FETCH][INFO]: 文件读取完成,准备更新部落信息...")
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
            print(f"[FETCH][INFO]: <{clan_name}>更新完成！")
        wb.save(filename = externs.inputClansInformationLocation)
        print("[FETCH][INFO]: 全部部落信息更新完成！准备格式化...")
        formal.processExcel(externs.inputClansInformationLocation)
        print("[FETCH][INFO]: 格式化完成！")
    else:
        print(f"[FETCH][INFO]: The file '{externs.inputClansInformationLocation}' does not exist")
    if os.path.exists(externs.inputGroupPlayerInformationLocation):
        print("[FETCH][INFO]: 文件存在,准备读取...")
        wb = op.load_workbook(externs.inputGroupPlayerInformationLocation)
        ws = wb[externs.groupPlayerInformationSheetName]
        max_row = ws.max_row
        print("[FETCH][INFO]: 文件读取完成,准备玩家更新...")
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
            else :
                fill = PatternFill(fill_type=None)
                ws.cell(row=row, column=1).fill = fill
            ws.cell(row = row,column = 2).value = player_name
            print(f"[FETCH][INFO]: <{player_name}>更新完成！")
        wb.save(filename = externs.inputGroupPlayerInformationLocation)
        print("[FETCH][INFO]: 全部玩家信息更新完成！准备格式化...")
        formal.processExcel(externs.inputGroupPlayerInformationLocation)
        print("[FETCH][INFO]: 格式化完成！")
    else:
        print(f"[FETCH][INFO]: The file '{externs.inputGroupPlayerInformationLocation}' does not exist")
    return flag

def deleteAll():
    flag = True
    print("[FETCH][INFO]: 准备删除输出文件...")
    print("[FETCH][INFO]: 检查文件...")
    if os.path.exists(externs.outputFileLocation):
        os.remove(externs.outputFileLocation)
        print(f"[FETCH][INFO]: The file '{externs.outputFileLocation}' has been deleted")
    else:
        print(f"[FETCH][INFO]: The file '{externs.outputFileLocation}' does not exist")
    return flag
def queryContribution(filter):
    flag = True
    sheet_name = externs.contributionsSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_contribution_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        url_war_race = url_0 + clans[clan] + "/war/race"
        requests = urllib.request.Request(url = url_war_race,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        div_time = soup.find('div',{'class' : 'timeline'})
        lis = div_time.find_all('li')
        day = 1##第四天开始战斗日
        in_war = 0##可能需要别的状态,不用bool
        data_num = 0
        for li in lis:
            div_unjudge = li.find('div',{'class' : "dot active"})
            if div_unjudge != None and day > 3:##active war-in day
                in_war = 1
                break
            day = day + 1 
        data = [clan]
        if 1 == in_war:
            print(f"[FETCH][INFO]: <{clan}>正处于战斗日,开始查询...")
            trs = soup.find_all('tr')
            trs_players = [tr for tr in trs if 'player' in tr.get('class', []) and len(tr['class']) == 1]
            trs_players = trs_players[1:]
            for tr in trs_players:
                data = [clan]
                player_name_location = tr.find('a',{'class':'player_name force_single_line_hidden'})
                player_name = player_name_location.get_text().strip().replace('\u200c','').replace('\u2006','')
                if filter and player_name not in players:
                    continue
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
            print(f"[FETCH][INFO]: <{clan}>未处于战斗日,格式输出正在进行...")
            data = [clan]
            data.append('该部落未处于战斗日！')
            data.append('')
            data.append('')
            data.append('')
            ws.append(data)
            now_row = now_row + 1
            start_row = now_row
            ws.merge_cells(start_column = 2,end_column = 5,start_row = now_row,end_row = now_row)
        print(f"[FETCH][INFO]: <{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=5,max_col=5):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 5).fill = fill
    wb.save(filename = externs.outputFileLocation)
    return flag

def queryDonation(filter):
    flag = True
    sheet_name = formal.donationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_donation_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        print(f"[FETCH][INFO]: <{clan}>开始查询...")
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
            player_name = formal.keep_before_first_newline(a_ty.get_text().strip().replace('\u200c','').replace('\u2006','') )
            if filter and player_name not in players:
                continue
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
        print(f"[FETCH][INFO]: <{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=3,max_col=3):
        if row[0].value == 0:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
    wb.save(filename = externs.outputFileLocation)    
    return flag

def queryActivity(filter):
    flag = True
    sheet_name = formal.activitySheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_activity_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        print(f"[FETCH][INFO]: <{clan}>开始查询...")
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
            player_name = formal.keep_before_first_newline(a_ty.get_text().strip()).replace('\u200c','').replace('\u2006','')
            if filter and player_name not in players:
                continue
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
        print(f"[FETCH][INFO]: <{clan}>查询已完成！")
    for row in ws.iter_rows(min_row = 2,max_row = ws.max_row,min_col=3,max_col=3):
        if row[0].value >= externs.inactivity:
            fill = PatternFill(fill_type = 'solid',fgColor = 'FF0000')
            ws.cell(row = row[0].row,column = 3).fill = fill
        ws.cell(row = row[0].row,column = 3).value = formal.convert_time_from_number(row[0].value)
    wb.save(filename = externs.outputFileLocation)
    return flag

def queryLastMonthWar(filter):
    flag = True
    sheet_name = formal.lastMonthWarSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_war_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        print("[FETCH][INFO]: 开始配置驱动...")
        edge_options = Options()
        edge_options.add_argument("--headless") 
        edge_options.add_argument("--disable-gpu") 
        edge_options.add_argument("--no-sandbox")  
        edge_options.add_argument("--disable-extensions")  
        edge_options.add_argument("--remote-debugging-port=0") 
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--ignore-ssl-errors")
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("[FETCH][INFO]: 驱动相关设置完成,准备配置日志输出...")
        log_path = externs.Contributionslog_path + "\\" + clans[clan] + ".log"
        service = EdgeService(EdgeChromiumDriverManager().install(), service_args=["--verbose", " --log-path="+log_path])
        print(f"[FETCH][INFO]: 驱动启动项初始化完毕,日志输出为'{log_path}',准备启动...")
        print("[FETCH][INFO]: 驱动配置完成,准备启动...")
        driver = webdriver.Edge(service = service,options = edge_options)
        print("[FETCH][INFO]: 驱动已启动,准备开始查询...")
        print(f"[FETCH][INFO]: <{clan}>开始查询...")
        data_num = 0
        url_last_month_war = url_0 + clans[clan] +"/war/analytics"
        driver.get(url_last_month_war)
        print("[FETCH][INFO]: 驱动正在运行......在驱动正确退出前请不要结束进程,否则将导致数据不完整和其他可能的错误！")
        print("[FETCH][INFO]: 页面加载中...")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,externs.XPaths["LastMonthWar"]
            )))
            print("[FETCH][INFO]: 页面加载完成,准备解析...")
            content = driver.page_source
        except:
            print("[FETCH][ERROR]: 页面加载超时,驱动即将退出...")
            driver.quit()
            print("[FETCH][INFO]: 驱动已正确退出")
            flag = False
            continue
        soup = BeautifulSoup(content, 'html.parser')
        table_contributions = soup.find('table', id='roster')
        trs = table_contributions.find_all('tr')
        trs = trs[1:]
        table_decks = soup.find('table', id='roster2')
        trs_2 = table_decks.find_all('tr')
        trs_2 = trs_2[1:]
        length = max(len(trs),len(trs_2))##其实是一样的
        data = []
        for i in range(length):
            tr = trs[i]
            data = [clan]
            td = tr.find('td',class_="sep fix first_col sticky")##名字标签
            player_name = formal.keep_before_first_newline(td.get_text().strip()).replace('\u200c','').replace('\u2006','') 
            if filter and player_name not in players:
                continue
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
        wb.save(filename = externs.outputFileLocation)
        formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 12)
        wb = op.load_workbook(externs.outputFileLocation)
        ws = wb[sheet_name]
        ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
        start_row = now_row + 1
        print(f"[FETCH][INFO]: <{clan}>查询已完成！驱动准备退出...")
        driver.quit()
        print("[FETCH][INFO]: 驱动已正确退出")
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
    print("[FETCH][INFO]: 所有查询已完成,准备保存数据...")
    wb.save(filename = externs.outputFileLocation)
    print("[FETCH][INFO]: 数据已保存,查询结束")
    return flag

def queryLastMonthDonation(filter):
    flag = True
    sheet_name = formal.lastMonthDonationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_donation_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        print("[FETCH][INFO]: 开始配置驱动...")
        edge_options = Options()
        edge_options.add_argument("--headless") 
        edge_options.add_argument("--disable-gpu") 
        edge_options.add_argument("--no-sandbox")  
        edge_options.add_argument("--disable-extensions")  
        edge_options.add_argument("--remote-debugging-port=0") 
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--ignore-ssl-errors")
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("[FETCH][INFO]: 驱动相关设置完成,准备配置日志输出...")
        log_path = externs.Donationslog_path + "\\" + clans[clan] + ".log"
        service = EdgeService(EdgeChromiumDriverManager().install(), service_args=["--verbose", " --log-path="+log_path])
        print(f"[FETCH][INFO]: 驱动启动项初始化完毕,日志输出为'{log_path}',准备启动...")
        print("[FETCH][INFO]: 驱动配置完成,准备启动...")
        driver = webdriver.Edge(service = service,options = edge_options)
        print("[FETCH][INFO]: 驱动已启动,准备开始查询...")
        print(f"[FETCH][INFO]: <{clan}>开始查询...")
        data_num = 0
        url_last_month_donation = url_0 + clans[clan]+"/history"
        driver.get(url_last_month_donation)
        print("[FETCH][INFO]: 驱动正在运行......在驱动正确退出前请不要结束进程,否则将导致数据不完整和其他可能的错误！")
        print("[FETCH][INFO]: 页面加载中...")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,externs.XPaths["LastMonthDonation"]
            )))
            print("[FETCH][INFO]: 页面加载完成,准备解析...")
            content = driver.page_source
        except:
            print("[FETCH][ERROR]: 页面加载超时,驱动即将退出...")
            driver.quit()
            print("[FETCH][INFO]: 驱动已正确退出")
            flag = False
            continue
        soup = BeautifulSoup(content, 'html.parser')
        table_donnations = soup.find('table', id='roster')
        trs = table_donnations.find_all('tr')
        trs = trs[1:]
        data = []
        for tr in trs:
            data = [clan]
            td_name = tr.find('td',class_='sticky_col')
            player_name = formal.keep_before_first_newline(td_name.get_text().strip()).replace('\u200c','').replace('\u2006','')
            if filter and player_name not in players:
                continue
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
        print(f"[FETCH][INFO]: <{clan}>查询已完成！驱动准备退出...")
        driver.quit()
        print("[FETCH][INFO]: 驱动已正确退出")
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
    print("[FETCH][INFO]: 所有查询已完成,准备保存数据...")
    wb.save(filename = externs.outputFileLocation)
    print("[FETCH][INFO]: 数据已保存,查询结束")
    return flag

def queryAndSort(filter):
    flag = True
    print("[FETCH][INFO]: 准备查询前置信息...")
    flag = queryLastMonthWar(filter) and queryLastMonthDonation(filter)
    if flag == False:
        print("[FETCH][ERROR]: 前置查询失败,程序准备退出...")
        return flag
    print("[FETCH][INFO]: 前置查询完成,准备设定权重并启动程序...")
    contribution_weight = externs.weightContribution
    donation_weight = externs.weightDonation
    print("[FETCH][INFO]: 权重设定完毕,准备创建输出...")
    formal.creatSheet(operations.creat_sort_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
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
                result = (value_1 * contribution_weight) + (value_2 * donation_weight)
                result = (int)(result)
                results.append(value_1)
                results.append(value_2)
                results.append(result)
                ws_3.append(results)
                break
    end = ws_3.max_row
    wb.save(filename = externs.outputFileLocation)
    print("[FETCH][INFO]: 数据已保存,准备排序...")
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
    print("[FETCH][INFO]: 排序完成,准备保存权重信息...")
    ws.append(['贡献权重','捐赠权重'])
    ws.append([contribution_weight,donation_weight])
    wb.save(filename = externs.outputFileLocation)
    print("[FETCH][INFO]: 权重信息已保存,程序已退出")
    return flag

def queryRecentChange():
    flag = True
    sheet_name = formal.recentChangeSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_recent_change_sheet())
    print("[FETCH][INFO]: 输出创建完成,准备启动程序...")
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    print("[FETCH][INFO]: 程序启动,正在运行...")
    for clan in clans:
        print(f"[FETCH][INFO]: <{clan}>开始查询...")
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
        print(f"[FETCH][INFO]: <{clan}>查询已完成！")
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
    return flag