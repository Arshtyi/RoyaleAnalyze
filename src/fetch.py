"""
for fetch and save
"""
import urllib.request
import urls
import urllib
import re
from bs4 import BeautifulSoup
import ClansInfor as CLI
import formal 
import openpyxl as op
import ops_defines as od
clans = CLI.clans
def contribution():
    sheet_name = "Contribution"
    url_0 = urls.url_0 + "clan/"
    formal.creat_sheet(od.creat_contribution_sheet())
    ##已创建用于统计贡献情况的工作表
    ##ws.append(['部落','玩家','今日使用卡组数','袭击战船次数','总贡献'])##表头
    ##ABCDE
    wb = op.load_workbook(formal.output_name)
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
        
        """
        需要在非战斗日进行测试需要取消下面第一句的注释并注释掉下方第二句一句判断
        """
        ##if True or 1 == in_war :###战斗日
        if 1 == in_war:
            ####爬取总量
            trs = soup.find_all('tr')#####完全匹配，速度慢不少
            trs_players = [tr for tr in trs if 'player' in tr.get('class', []) and len(tr['class']) == 1]
            ##trs_players = soup.find_all('tr',class_=re.compile(r'\bplayer\b'))##正则###完全匹配
            for tr in trs_players:
               # print(tr)
                data = [clan]
                player_name_location = tr.find('a',{'class':'player_name force_single_line_hidden'}) 
                if player_name_location:
                    player_name = player_name_location.get_text().strip()
                    player_name = player_name.replace('\u200c','')
                    data.append(player_name)
                player_decks_used = tr.find('div',{'class':'value_bg decks_used'})
                if player_decks_used:
                    decks_uesd = player_decks_used.get_text()
                    data.append(decks_uesd) 
                player_boat_attack = tr.find('div',{'class':'value_bg boat_attacks'})
                if player_boat_attack:
                    boat_attack = player_boat_attack.get_text()
                    data.append(boat_attack)
                player_medal = tr.find('div',{'class':'value_bg fame'})
                if player_medal:
                    medal = player_medal.get_text()
                    data.append(medal)
                if len(data) > 1:
                    data_num = data_num + 1
                    ws.append(data)
            if data_num:
                    now_row = now_row + data_num
                    #print(f"start_row = {start_row},now_row = {now_row}")
                    ws.merge_cells(start_row = start_row,end_row = now_row,start_column = 1,end_column = 1)
                    start_row = now_row + 1
                    #print(f"start_row = {start_row},now_row = {now_row}")
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
    wb.save(filename = formal.output_name)

def donation():
    t = 0