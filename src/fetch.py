"""
fetch and save
"""
import urllib.request
import urls
import logging
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
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
import os
logging.disable(logging.CRITICAL)
def deleteAll():
    if os.path.exists(externs.outputFileLocation):
         os.remove(externs.outputFileLocation)
    else:
        print("The file does not exist")

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
        ###print(url_war_race)
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
    logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.CRITICAL)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)
    edge_options = Options()
    edge_options.add_argument("--headless") 
    edge_options.add_argument("--disable-gpu") 
    edge_options.add_argument("--no-sandbox")  
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    edge_options.add_argument("--disable-extensions")  
    edge_options.add_argument("--remote-debugging-port=0") 
    edge_options.add_argument("--log-level=OFF")
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    print("驱动配置完成")
    for clan in clans:
        data_num = 0
        url_last_month_war = url_0 + clans[clan] +"/war/analytics"
        driver.get(url_last_month_war)
        print("驱动正在运行......在驱动退出前请不要结束进程，否则将导致数据不完整！")
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table_contributions = soup.find('table', id='roster')
        trs = table_contributions.find_all('tr')
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
                all_contribution = all_contribution + (contribution)
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
            ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
            start_row = now_row + 1
    wb.save(filename = externs.outputFileLocation)
    driver.quit()
    print("驱动正确退出")

def queryLastMonthDonation():
    sheet_name = formal.lastMonthDonationSheetName
    url_0 = urls.url_clan
    formal.creatSheet(operations.creat_last_month_donation_sheet())
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[sheet_name]
    data_num = 0
    now_row = 1
    start_row = 2
    logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.CRITICAL)
    logging.getLogger('urllib3').setLevel(logging.CRITICAL)
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    edge_options.add_argument("--disable-extensions")
    edge_options.add_argument("--remote-debugging-port=0")
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    print("驱动配置完成")
    for clan in clans:
        data_num = 0
        url_last_month_donation = url_0 + clans[clan]+"/history"
        #print(url_last_month_donation)
        driver.get(url_last_month_donation)
        print("驱动正在运行......在驱动退出前请不要结束进程，否则将导致数据不完整！")
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table_donnations = soup.find('table', id='roster')
        trs = table_donnations.find_all('tr')
        trs = trs[1:]
        data = []
        for tr in trs:
            data = [clan]
            td_name = tr.find('td',class_='sticky_col')
            if td_name:
                player_name = formal.keep_before_first_newline(td_name.get_text().strip())
                player_name = player_name.replace('\u200c','').replace('\u2006','')
                data.append(player_name)
            else:
                continue
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
            #print(data)
            if len(data) > 1:
                data_num = data_num + 1
                ws.append(data)
        if data_num:
            now_row = now_row + data_num
            wb.save(filename = externs.outputFileLocation)
            formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 7)
            wb = op.load_workbook(externs.outputFileLocation)
            ws = wb[sheet_name]
            ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
            start_row = now_row + 1
    wb.save(filename = externs.outputFileLocation)
    driver.quit()
    print("驱动正确退出")

def queryAndSort():
    queryLastMonthWar()
    queryLastMonthDonation()
    weight_1 = externs.weightContribution
    weight_2 = externs.weightDonation
    formal.creatSheet(operations.creat_sort_sheet())
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
    formal.sort_xlsx_data(externs.outputFileLocation,formal.sortedSheetName,start_row = 2,end_row = end,sort_column = 5)
    wb = op.load_workbook(externs.outputFileLocation)
    ws = wb[formal.sortedSheetName]
    ws.append(['贡献权重','捐赠权重'])
    ws.append([weight_1,weight_2])
    wb.save(filename = externs.outputFileLocation)