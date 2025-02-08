"""
This module processes and transforms clan and player information.
Functions:
    - getClansInformation: Retrieves the original dictionary of clans.
    - getGroupPlayersInformation: Retrieves the original dictionary of players.
Workflow:
1. Retrieve the original clan and player dictionaries using functions from the externs module.
2. For each clan in the original_clans dictionary, remove the first character.
3. For each player in the original_players dictionary, remove the first character of the third element.
4. Convert the modified original_clans and original_players dictionaries to immutable MappingProxyType objects.
Variables:
    - original_clans (dict): The original dictionary of clans.
    - original_players (dict): The original dictionary of players.
    - clans (MappingProxyType): An immutable version of the modified original_clans dictionary.
    - players (MappingProxyType): An immutable version of the modified original_players dictionary.

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