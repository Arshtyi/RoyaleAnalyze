"""
ClansInfor
"""
from types import MappingProxyType

original_clans = {
    '零度轩辕':'#QRL0PYQL',
    '勾指起誓':'#R8RJYCCU',
    '啟明星之夢':'#GQPV9Y2R',
}#原始字典
for clan in original_clans:
    original_clans[clan] = original_clans[clan][1:] 
 
clans = MappingProxyType(original_clans)#转不可修改
#print(clans)