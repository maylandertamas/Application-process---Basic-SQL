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


def input_verification(input_text, in_type):
    if in_type == "number":

        input_checker = True
        while input_checker:
            try:
                user_input = int(input(input_text))
            except ValueError:
                print("Please insert a correct input!")
            else:
                input_checker = False

        return user_input

    if in_type == "string":

        input_checker = True
        while input_checker:
            try:
                user_input = str(input(input_text))
            except ValueError:
                print("Please insert a correct input!")
            else:
                input_checker = False

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
        print_table(manage_db.show_all_db("mentors"), ['ID', 'First name', 'Last name',
                                                       'Phone number', 'Email', 'Application Code'])

    elif user_input == "9":
        print_table(manage_db.show_all_db("applicants"), ['ID', 'First name', 'Last name',
                                                          'Phone number', 'Email', 'Application Code'])

    elif user_input == "10":
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
