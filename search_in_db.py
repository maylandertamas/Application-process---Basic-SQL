import common
import manage_db

cur = manage_db.cur

def get_col_titles(database_name):
    database_name_str = str(database_name)
    cur.execute("Select * FROM " + database_name_str)
    colnames = [title[0] for title in cur.description]
    return colnames


MENTOR_DB_COL_TITLES = get_col_titles("mentors")


def mentor_search_menu_points():
    user_input = input("Please choose a menu point! ")
    input_verified = common.usr_input_verification(user_input)
    if input_verified == 1:
        search_in_db("first_name")
    elif input_verified == 2:
        search_in_db("last_name")
    elif input_verified == 3:
        search_in_db("nick_name")
    elif input_verified == 4:
        search_in_db("phone_number")
    elif input_verified == 5:
        search_in_db("email")
    elif input_verified == 6:
        search_in_db("city")
    elif input_verified == 7:
        search_in_db("favourite_number")
    elif input_verified == 0:
        sys.exit(0)
    else:
        raise KeyError("There is no such an option!")


def search_in_db(column):
    if column == "favourite_number":
        try:
            user_input = int(input("Insert a number input to search by"))
        except ValueError as err:
            print("Please give me a real number!")
            print(err)
    else:
        try:
            user_input = str(input("Insert a text input to search by"))
        except ValueError as err:
            print("Please give me a real number!")
            print(err)
    
    cur.execute("SELECT * FROM mentors\
                 WHERE " + column + " LIKE " + "\'" + user_input + "%\'")
    search_result = cur.fetchall()
    common.print_table(search_result, MENTOR_DB_COL_TITLES[1::])