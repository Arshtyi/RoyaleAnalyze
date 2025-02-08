"""
This script is the main entry point for the RoyaleAnalyze project.
Modules:
    menu: Handles the creation and interaction with the menu.
    operations: Contains functions for various operations and decision-making.
    formal: Provides functionality for formatting and processing Excel files.
    externs: Contains external configurations and file locations.
    clansInformation: Provides functions for reading and processing information from Excel sheets related to clans and group players.
    fetch: Contains functions for fetching data from URLs.
    gettime: Provides functions for getting the current time.
    path: Provides functions for managing file paths.
    urls: Contains URL configurations and HTTP request settings for the project.
Execution:
    The script runs an infinite loop to display a menu and process user choices.
    It exits the loop when the user chooses to exit.
    After exiting the loop, it processes an Excel file and waits for user input before closing.
Functions:
    menu.creatMenu(): Displays the menu to the user.
    menu.getChoice(): Gets the user's menu choice.
    operations.queryExit(): Checks if the user's choice is to exit.
    operations.judge(choice): Processes the user's choice.
    formal.processExcel(file_location): Formats and processes the Excel file at the given location.

"""
import src.menu as menu
import src.operations as operations
import src.formal as formal
import src.externs as externs
if __name__ == '__main__':
    while True:
        menu.creatMenu()
        choice = menu.getChoice()
        if operations.queryExit() == choice:
            break
        else :
            operations.judge(choice)
    print("[MAIN][INFO]: 准备进行格式化...")
    formal.processExcel(externs.outputFileLocation)
    input("[MAIN][INFO]: 格式化完成，程序准备退出，键入任意内容以退出...\n")
    print("[MAIN][INFO]: 正在关闭进程...")
    print("[MAIN][INFO]: 进程已关闭，程序结束并退出...")