import common
from manage_db import cur, main
import os


def get_col_titles(database_name):
    database_name_str = str(database_name)
    cur.execute("Select * FROM " + database_name_str + ";")
    colnames = [title[0] for title in cur.description]
    return colnames


def mentor_search_menu():
    while True:
        common.print_menu("Search in mentors's database menu",
                          ["Search by first name", "Search by last name", "Search by nick name",
                           "Search by phone number", "Search by email adress", "Search by city",
                           "Search by favourite number"])

        user_input = input("Please choose a menu point! ")

        if user_input == "1":
            search_in_mentors_db("first_name")

        elif user_input == "2":
            search_in_mentors_db("last_name")

        elif user_input == "3":
            search_in_mentors_db("nick_name")

        elif user_input == "4":
            search_in_mentors_db("phone_number")

        elif user_input == "5":
            search_in_mentors_db("email")

        elif user_input == "6":
            search_in_mentors_db("city")

        elif user_input == "7":
            search_in_mentors_db("favourite_number")

        elif user_input == "0":
            main()

        else:
            raise KeyError("There is no such an option!")


def search_in_mentors_db(column):
    if column == "favourite_number":
        valid_user_input = common.input_verification("Insert a number input to search by: ", "number")
        cur.execute("SELECT * FROM mentors\
                     WHERE " + column + " = " + str(valid_user_input) + "\
                     ORDER BY first_name ASC;")

    else:
        valid_user_input = common.input_verification("Insert text to search by: ", "string")
        cur.execute("SELECT * FROM mentors\
                     WHERE lower(" + column + ") LIKE " + "\'%" + valid_user_input + "%\' \
                     ORDER BY first_name ASC;")
    search_result = cur.fetchall()

    # Get rid of None elements to be able to print list with common.print_table function
    result_to_list = [list(element) for element in search_result]
    for element in result_to_list:
        if element[7] is None:
            element[7] = "Nothing"
    os.system('clear')
    MENTOR_DB_COL_TITLES = get_col_titles("mentors")
    common.print_table(result_to_list, MENTOR_DB_COL_TITLES)
