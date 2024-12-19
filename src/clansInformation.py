"""
Information of clans
"""
from types import MappingProxyType
import externs
original_clans = externs.getClansInformation() #获取原始字典

for clan in original_clans:
    original_clans[clan] = original_clans[clan][1:] ##切掉井号
 
clans = MappingProxyType(original_clans) ##转不可修改
