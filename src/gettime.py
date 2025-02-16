"""
该模块用于获取当前时间并格式化输出。
在RoyaleAnalyze项目中,该模块的主要功能是提供当前时间的字符串表示,
格式为 "月-日-时-分",以便在项目的其他部分中使用时间戳进行记录或显示。
函数:
    get_current_time: 获取当前时间并格式化为 "月-日-时-分" 的字符串。

"""
from datetime import datetime
def get_current_time():
    # 获取当前时间
    current_time = datetime.now()
    
    # 格式化当前时间为 "月-日-时-分"
    formatted_time = current_time.strftime("%m月-%d日-%H时-%M分")
    
    return formatted_time