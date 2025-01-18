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
    formal.processExcel(externs.outputFileLocation)