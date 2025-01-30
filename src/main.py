"""
main function of this project
"""
import menu
import operations
import formal
import externs
import operations
if __name__ == '__main__':
    while True:
        menu.creatMenu()
        choice = menu.getChoice()
        if operations.queryExit() == choice:
            break
        else :
            operations.judge(choice)
    print("准备进行格式化...")
    formal.processExcel(externs.outputFileLocation)
    input("格式化完成，程序准备退出，键入任意内容以退出...\n")
    print("正在关闭进程...")
    print("进程已关闭，程序结束并退出...")