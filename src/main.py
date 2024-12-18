import menu
import operations
import formal
if __name__ == '__main__':
    menu.creat_menu()
    choice = menu.getChoice()
    operations.judge(choice)
    formal.process_excel(formal.output_name)
    