"""
fetch and save
"""
import urllib.request
import urls
import urllib
import re
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
    ##已创建用于统计贡献情况的工作表
    ##ws.append(['部落','玩家','总使用卡组数','总袭击战船次数','总贡献'])##表头
    ##ABCDE
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
                    player_name = player_name.replace('\u200c','')##去除特殊字符
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
                player_name = player_name.replace('\u200c','') 
                data.append(player_name)
            td_donation = tr.find('td',class_='donations right aligned mobile-hide')
            if td_donation:
                donation = (int)(td_donation.get_text().strip())
                data.append(donation)
            if len(data) > 1:
                data_num = data_num + 1
               ### print(data)
                ws.append(data)
        if data_num:
                now_row = now_row + data_num
                #print(f"now_row = {now_row},start_row = {start_row}")
                wb.save(filename = externs.outputFileLocation)
                formal.sort_xlsx_data(externs.outputFileLocation,sheet_name,start_row = start_row,end_row = now_row,sort_column = 3)
                wb = op.load_workbook(externs.outputFileLocation)
                ws = wb[sheet_name]
                ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
                start_row = now_row + 1
                #print(f"now_row = {now_row},start_row = {start_row}")
    wb.save(filename = externs.outputFileLocation)    