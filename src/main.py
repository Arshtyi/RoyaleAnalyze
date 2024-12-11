import menu
import ops
import formal
if __name__ == '__main__':
    menu.creat_menu()
    choice = menu.Get_choices()
    ops.judge(choice)
    formal.process_excel(formal.output_name)
    