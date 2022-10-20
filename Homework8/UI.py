import display
import fileio
import func


def menu(data):
    while True:
        answer = display.display_menu()
        if answer == 0:
            display.display_data(data)
        elif answer == 1:
            str_data = input("Please enter your data delimited by ';' : ")
            func.add_row(str_data, data)
        elif answer == 2:
            str_to_del = input("Please enter ID: ")
            func.dell_str(str_to_del, data)
        elif answer == 3:
            fileio.write_data("data.csv", data)
        elif answer == 4:
            print('goodbay')
            break
        else:
            print("Повторите выбор")
