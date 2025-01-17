"""
fetch and save
"""
import urllib.request
import urls
import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib
import operations
from bs4 import BeautifulSoup
from clansInformation import clans
import openpyxl as op
import formal
import externs
def queryContribution():
    sheet_name = externs.contributionsSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_contribution_sheet())
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    now_row = 1
    start_row = 2
    for clan in clans:
        url_war_race = url_0 + clans[clan] + "/war/race"#部落战信息
        ####先找timeline，看看是不是对战日
        ####定制请求头
        requests = urllib.request.Request(url = url_war_race,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        div_time = soup.find('div',{'class' : 'timeline'})
        ####找li标签
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
            ####爬取总量
            trs = soup.find_all('tr')#####完全匹配，速度慢不少
            trs_players = [tr for tr in trs if 'player' in tr.get('class', []) and len(tr['class']) == 1]
            for tr in trs_players:
                data = [clan]
                player_name_location = tr.find('a',{'class':'player_name force_single_line_hidden'}) 
                if player_name_location:
                    player_name = player_name_location.get_text().strip()
                    player_name = player_name.replace('\u200c','').replace('\u2006','')
                    data.append(player_name)
                player_decks_used = tr.find('div',{'class':'value_bg decks_used'})
                if player_decks_used:
                    decks_uesd = (int)(player_decks_used.get_text())
                    data.append(decks_uesd) 
                player_boat_attack = tr.find('div',{'class':'value_bg boat_attacks'})
                if player_boat_attack:
                    boat_attack = (int)(player_boat_attack.get_text())
                    data.append(boat_attack)
                player_medal = tr.find('div',{'class':'value_bg fame'})
                if player_medal:
                    medal = (int)(player_medal.get_text())
                    data.append(medal)
                if len(data) > 1:
                    data_num = data_num + 1
                    ws.append(data)
            if data_num:
                    now_row = now_row + data_num
                    wb.save(filename = externs.outputFileLocation)
                    formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 5) 
                    wb = op.load_workbook(externs.outputFileLocation)
                    ws = wb[sheet_name]
                    ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
                    start_row = now_row + 1
        elif 0 == in_war:
            data = [clan]
            data.append('该部落未处于战斗日！')
            data.append('')
            data.append('')
            data.append('')
            ws.append(data)
            now_row = now_row + 1
            start_row = now_row
            ws.merge_cells(start_column = 2,end_column = 5,start_row = now_row,end_row = now_row)
    wb.save(filename = externs.outputFileLocation)

def queryDonation():
    sheet_name = formal.donationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_donation_sheet())
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    for clan in clans:
        data_num = 0
        url_donation = url_0 + clans[clan]
        # print(url_donation)
        requests = urllib.request.Request(url = url_donation,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        table_donation = soup.find('table', id='roster', class_='ui unstackable hover striped attached compact sortable table')##找到捐赠表
        ##print(table_donation)
        trs = table_donation.find_all('tr')
        for tr in trs:
            data = [clan]
            a_ty = tr.find('a',class_='block member_link')
            if a_ty:
                player_name = formal.keep_before_first_newline(a_ty.get_text().strip())
                player_name = player_name.replace('\u200c','').replace('\u2006','') 
                data.append(player_name)
            else:
                continue
            td_donation = tr.find('td',class_='donations right aligned mobile-hide')
            if td_donation:
                donation = (int)(td_donation.get_text().strip().replace(',',''))
                data.append(donation)
            if len(data) > 1:
                data_num = data_num + 1
               ### print(data)
                ws.append(data)
        if data_num:
                now_row = now_row + data_num
                wb.save(filename = externs.outputFileLocation)
                formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 3)
                wb = op.load_workbook(externs.outputFileLocation)
                ws = wb[sheet_name]
                ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
                start_row = now_row + 1
                #print(f"now_row = {now_row},start_row = {start_row}")
    wb.save(filename = externs.outputFileLocation)    

def queryActivity():
    sheet_name = formal.activitySheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_activity_sheet())
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    for clan in clans:
        data_num = 0
        url_activity = url_0 + clans[clan]
        requests = urllib.request.Request(url = url_activity,headers = urls.HEADERS)
        response = urllib.request.urlopen(requests)
        content = response.read().decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        table_activity = soup.find('table', id='roster', class_='ui unstackable hover striped attached compact sortable table')
        trs = table_activity.find_all('tr')
        for tr in trs:
            data = [clan]
            a_ty = tr.find('a',class_='block member_link')
            if a_ty:
                player_name = formal.keep_before_first_newline(a_ty.get_text().strip())
                player_name = player_name.replace('\u200c','').replace('\u2006','')
                data.append(player_name)
            div = tr.find('div',class_='i18n_duration_short')
            ###print(div)
            if div:
                activity = formal.convert_time_format(div.get_text().strip())
                data.append(activity)
            if len(data) > 1:
                data_num = data_num + 1
                ws.append(data)
        if data_num:
            now_row = now_row + data_num
            wb.save(filename = externs.outputFileLocation)
            wb = op.load_workbook(externs.outputFileLocation)
            ws = wb[sheet_name]
            ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
            start_row = now_row + 1
    wb.save(filename = externs.outputFileLocation)

def queryLastMonthWar():
    sheet_name = formal.lastMonthWarSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_war_sheet())
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    cnt = 1
    # 禁用 selenium 和浏览器相关的日志
    logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.CRITICAL)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)
    # 设置无头模式
    edge_options = Options()
    edge_options.add_argument("--headless")  # 启用无头模式
    edge_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（无头模式下常用）
    edge_options.add_argument("--no-sandbox")  # 不使用沙箱（某些环境中无头模式可能需要）
    edge_options.add_experimental_option('excludeSwitches',['enable-logging'])
    # 关闭 DevTools 相关日志
    edge_options.add_argument("--disable-extensions")  # 禁用扩展
    edge_options.add_argument("--remote-debugging-port=0")  # 禁用 DevTools 调试端口
    # 配置并启动浏览器
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    driver_2 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    for clan in clans:
        data_num = 0
        url_last_month_war = url_0 + clans[clan] +"/war/analytics"
        driver.get(url_last_month_war)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        url_last_month_donation = url_0 + clans[clan] + "/history"
        print(url_last_month_donation)
        driver_2.get(url_last_month_donation)
        content_2 = driver_2.page_source
        soup_2 = BeautifulSoup(content_2, 'html.parser')
        table_contributions = soup.find('table', id='roster')
        trs = table_contributions.find_all('tr')
        table_donation = soup_2.find('table', id='roster')
        trs_3 = table_donation.find_all('tr')
        table_decks = soup.find('table', id='roster2')
        trs_2 = table_decks.find_all('tr')
        length = max(len(trs),len(trs_2))
        data = []
        for i in range(length):
            tr = trs[i]
            data = [clan]
            td = tr.find('td',class_="sep fix first_col sticky")##名字标签
            if td:
                player_name = formal.keep_before_first_newline(td.get_text().strip())
                player_name = player_name.replace('\u200c','').replace('\u2006','') 
                data.append(player_name)
            else:
                continue
            tds_contributions = tr.find_all('td',limit = 8)
            tds_contributions = tds_contributions[4:]
            all_contribution = 0
            for td in tds_contributions:
                contribution = td.get_text().strip()
                if contribution == "":
                    contribution = 0
                contribution = (int)(contribution)
                data.insert(2,contribution)
                all_contribution = all_contribution + (int)(contribution)
            data.insert(7,all_contribution)
            td_paticipate = tr.find('td',class_='sorting_1')
            if td_paticipate:
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
            if len(data) > 1:
                data_num = data_num + 1
                ws.append(data)
        if data_num:
            now_row = now_row + data_num
            wb.save(filename = externs.outputFileLocation)
            formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 9)
            wb = op.load_workbook(externs.outputFileLocation)
            ws = wb[sheet_name]
            ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
            start_row = now_row + 1
    wb.save(filename = externs.outputFileLocation)
    driver.quit()
    driver_2.quit()