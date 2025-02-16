"""
RoyaleAnalyze 主模块
该模块是 RoyaleAnalyze 程序的入口点,负责启动程序并进行环境检查.
如果环境检查通过,则启动主菜单并根据用户选择执行相应的操作.
在程序结束时,进行数据格式化并提示用户程序已完成.
模块功能;
1. 环境检查和修复
2. 启动主菜单并处理用户选择
3. 数据格式化
依赖模块;
- src.errorcheck: 用于环境检查和修复
- src.menu: 用于创建和处理主菜单
- src.operations: 用于处理用户选择的操作
- src.formal: 用于数据格式化
- src.externs: 用于获取输出文件位置
"""
import src.errorcheck as errorcheck
import sys
if __name__ == '__main__':
    print("[MAIN][INFO]: RoyaleAnalyze 正在启动...")
    print("[MAIN][INFO]: 开始检查和修复环境...")
    if errorcheck.pathCheckAndFix() == False:
        print("[MAIN][ERROR]: 你的环境存在问题,请检查相关文件夹是否存在以及是否允许访问后重新启动程序")
        print("[MAIN][ERROR]: 程序因为环境不完整且无法修复而终止...")
        sys.exit()
    print("[MAIN][INFO]: 环境检查和修复通过...启动程序...")
    import src.menu as menu
    import src.operations as operations
    import src.formal as formal
    import src.externs as externs
    while True:
        menu.creatMenu()
        choice = menu.getChoice()
        if operations.queryExit() == choice:
            break
        else:
            operations.judge(choice)
    print("[MAIN][INFO]: 准备进行格式化...")
    formal.processExcel(externs.outputFileLocation)
    print("[MAIN][INFO]: 格式化完成...")
    menu.faultsDisplay()
    input("[MAIN][INFO]: 程序结束运行,按任意键退出...\n")
    sys.exit()