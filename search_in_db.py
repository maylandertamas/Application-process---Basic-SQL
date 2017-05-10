import common
import manage_db

cur = manage_db.cur


def get_col_titles(database_name):
    database_name_str = str(database_name)
    cur.execute("Select * FROM " + database_name_str)
    colnames = [title[0] for title in cur.description]
    return colnames


MENTOR_DB_COL_TITLES = get_col_titles("mentors")


def mentor_search_menu():
    while True:
        common.print_menu("Search in mentors's database menu",
                          ["Search by first name", "Search by last name", "Search by nick name",
                           "Search by phone number", "Search by email adress", "Search by city",
                           "Search by favourite number"])
        user_input = input("Please choose a menu point! ")
        input_verified = common.input_verification(user_input, "number")
        if input_verified == 1:
            search_in_mentors_db("first_name")
        elif input_verified == 2:
            search_in_mentors_db("last_name")
        elif input_verified == 3:
            search_in_mentors_db("nick_name")
        elif input_verified == 4:
            search_in_mentors_db("phone_number")
        elif input_verified == 5:
            search_in_mentors_db("email")
        elif input_verified == 6:
            search_in_mentors_db("city")
        elif input_verified == 7:
            search_in_mentors_db("favourite_number")
        elif input_verified == 0:
            manage_db.main()
        else:
            raise KeyError("There is no such an option!")


def search_in_mentors_db(column):
    if column == "favourite_number":
        user_input = input("Insert a number input to search by: ")
        common.input_verification(user_input, "number")
        cur.execute("SELECT * FROM mentors\
                     WHERE " + column + " = " + str(user_input) + ";")
        search_result = cur.fetchall()
    else:
        user_input = input("Insert a text input to search by: ")
        common.input_verification(user_input, "string")
        cur.execute("SELECT * FROM mentors\
                     WHERE lower(" + column + ") LIKE " + "\'%" + user_input + "%\'")
        search_result = cur.fetchall()
    common.print_table(search_result, MENTOR_DB_COL_TITLES)