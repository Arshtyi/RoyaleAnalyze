"""
RoyaleAnalyze 主模块
该模块是 RoyaleAnalyze 程序的入口点,负责启动程序并进行环境检查.
如果环境检查通过,则启动主菜单并根据用户选择执行相应的操作.
在程序结束时,进行数据格式化并提示用户程序已完成.
模块功能:
1. 环境检查和修复
2. 启动主菜单并处理用户选择
3. 数据格式化
依赖模块:
- src.errorcheck: 用于环境检查和修复
- src.menu: 用于创建和处理主菜单
- src.operations: 用于处理用户选择的操作
- src.formal: 用于数据格式化
- src.externs: 用于获取输出文件位置
"""
import src.errorcheck as errorcheck
import sys
import src.log as log
import src.externs as externs
if __name__ == '__main__':
    log.log("TRACE", "MAIN", "RoyaleAnalyze 正在启动...", )
    log.log("TRACE", "MAIN", "开始检查和修复环境...", )
    if errorcheck.pathCheckAndFix() == False:
        log.log("CRITICAL", "MAIN", "程序因为环墨不完整且无法修复而终止...", )
        log.log("TRACE", "MAIN", "正在终止程序...", )
        sys.exit()
    log.log("TRACE", "MAIN", "环境检查和修复通过...启动程序...",externs.log_path )
    log.log("TRACE", "MAIN", "环境检查和修复通过...启动程序...", )
    # 以上是环境检查和修复
    import src.menu as menu
    import src.operations as operations
    import src.formal as formal
    import src.externs as externs
    menu.welcome()
    # 欢迎界面
    while True:
        menu.creatMenu()
        # 菜单，获取选择，判断
        choice = menu.getChoice()
        if operations.queryExit() == choice:
            break
        else:
            operations.judge(choice)
    log.log("TRACE", "MAIN", "准备进行格式化...", )
    log.log("TRACE", "MAIN", "准备进行格式化...", externs.log_path)
    formal.processExcel(externs.outputFileLocation)
    log.log("TRACE", "MAIN", "格式化完成...", )
    log.log("TRACE", "MAIN", "格式化完成...", externs.log_path)
    menu.faultsDisplay()
    # 展示未成功操作
    input("程序结束运行,按任意键退出...\n")
    log.log("TRACE", "MAIN", "程序已正常结束.", externs.log_path)
    # 退出
    sys.exit()