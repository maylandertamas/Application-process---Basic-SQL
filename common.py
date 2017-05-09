import manage_db
import sys
import os


def print_table(table, title_list):
    border_horizontal = '_'
    border_vertical = '|'
    border_cross = '+'
    columns = [list(x) for x in zip(*table, title_list)]
    lengths = [max(map(len, map(str, col))) for col in columns]
    separate_rows = border_vertical + border_vertical.join(' {:^%d} ' % l for l in lengths) + border_vertical
    separate_crosses = border_cross + border_cross.join(border_horizontal * (l+2) for l in lengths) + border_cross

    print(separate_crosses)
    print(separate_rows.format(*title_list))
    print(separate_crosses)
    for row in table:
        print(separate_rows.format(*row))
        print(separate_crosses)


def usr_input_verification(user_input):
    try:
        user_input = int(user_input)
    except ValueError as error:
        print("Please insert a correct input!")
        print(error)
    return user_input

def menu_options():
    user_input = input("Please choose a menu point! ")
    input_verified = usr_input_verification(user_input)

    if input_verified == 1:
        print_table(manage_db.query_nicknames(), ["Nick names"])
    elif input_verified == 2:
        manage_db.query_nicknames()
    elif input_verified == 3:
        manage_db.query_for_carol()
    elif input_verified == 4:
        manage_db.query_for_other_girl()
    elif input_verified == 5:
        manage_db.insert_into_app_database()
    elif input_verified == 6:
        manage_db.update_phone_num()
    elif input_verified == 7:
        manage_db.delete_applicants()
    elif user_input == 0:
        sys.exit(0)
    else:
        raise KeyError("There is no such an option!")


def print_menu():
    print("Database Manager")
    menu_points = ["Menup1", "Menup2", "Menup3", "Menup4", "Menup5", "Menup6", "Menup7", "Exit"]
    for index, option in enumerate(menu_points):
        print("[{0}] {1}".format(index+1, option))
