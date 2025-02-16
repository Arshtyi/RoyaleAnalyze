"""
clansInformation 模块
这个模块是RoyaleAnalyze项目的一部分,负责处理和管理有关部落和玩家的信息。它从`externs`模块导入必要的函数来检索部落和玩家的原始数据。然后,该模块通过删除特定字符来处理这些数据,并使用`MappingProxyType`将字典转换为不可变类型。
函数:
- getClansInformation: 检索部落信息的原始字典。
- getGroupPlayersInformation: 检索玩家信息的原始字典。
处理过程:
- 对于原始部落字典中的每个部落,删除第一个字符。
- 对于原始玩家字典中的每个玩家,删除第三个字符。
- 然后将处理后的字典转换为不可变类型,以防止进一步修改。
该模块确保部落和玩家信息被处理并以只读格式存储,以便在RoyaleAnalyze项目中进行进一步分析。
"""
from types import MappingProxyType
import src.externs as externs
original_clans = externs.getClansInformation() #获取原始字典
original_players = externs.getGroupPlayersInformation() #获取原始玩家字典
for clan in original_clans:
    original_clans[clan] = original_clans[clan][1:] ##切掉井号
 
for player in original_players:
    original_players[player] = original_players[player][2][1:] ##切掉井号
clans = MappingProxyType(original_clans) ##转不可修改
players = MappingProxyType(original_players) ##转不可修改