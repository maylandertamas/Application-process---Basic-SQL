import manage_db
import sys
import search_in_db


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


def input_verification(user_input, in_type):
    if in_type == "number":
        if user_input == "":
            raise TypeError("Insert something please!")
        else:
            try:
                user_input = int(user_input)
            except ValueError as error:
                print("Please insert a correct input!")
                print(error)
            return user_input
    if in_type == "string":
        if user_input == "":
            raise TypeError("Insert something please!")
        else:
            try:
                user_input = str(user_input)
            except ValueError as error:
                print("Please insert a correct input!")
                print(error)
            return user_input


def menu_options():
    user_input = input("Please choose a menu point! ")
    if user_input == "1":
        print_table(manage_db.query_full_names(), ["First name", "Last name"])
    elif user_input == "2":
        print_table(manage_db.query_nicknames(), ["Nick names"])
    elif user_input == "3":
        print_table(manage_db.query_for_carol(), ["Full Name", "Phone Number"])
    elif user_input == "4":
        print_table(manage_db.query_for_other_girl(), ["Full Name", "Phone Number"])
    elif user_input == "5":
        print_table(manage_db.insert_into_app_database(), ['ID', 'First name', 'Last name',
                                                           'Phone number', 'Email', 'Application Code'])
    elif user_input == "6":
        print_table(manage_db.update_phone_num(), ['ID', 'First name', 'Last name',
                                                   'Phone number', 'Email', 'Application Code'])
    elif user_input == "7":
        print_table(manage_db.delete_applicants(), ['ID', 'First name', 'Last name',
                                                    'Phone number', 'Email', 'Application Code'])
    elif user_input == "8":
        search_in_db.mentor_search_menu()
    elif user_input == "0":
        manage_db.cur.close()
        manage_db.conn.close()
        sys.exit(0)
    else:
        raise KeyError("There is no such an option!")


def print_menu(menu_name, menu_points):
    print(menu_name)
    for index, option in enumerate(menu_points):
        print("[{0}] {1}".format(index+1, option))
    print("[0] Exit")