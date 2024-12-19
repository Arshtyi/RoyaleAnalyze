"""
main function of this project
"""

import menu
import operations
import formal
import externs
if __name__ == '__main__':
    menu.creatMenu()
    choice = menu.getChoice()
    operations.judge(choice)
    formal.processExcel(externs.outputFileLocation)
    