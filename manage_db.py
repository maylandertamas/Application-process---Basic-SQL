import psycopg2
import common

try:
    conn = psycopg2.connect("dbname='maylandertamas' user='maylandertamas' password='zugzugloller'")
except Exception as e:
    print("You cannot connect!")
    print(e)
cur = conn.cursor()


def query_full_names():
    cur.execute("SELECT first_name, last_name FROM mentors;")
    list_of_full_names = cur.fetchall()
    return list_of_full_names


def query_nicknames():
    cur.execute("SELECT nick_name FROM mentors;")
    list_of_nicknames = cur.fetchall()
    return list_of_nicknames


def query_for_carol():
    cur.execute("SELECT first_name || ' ' || last_name, phone_number  FROM applicants\
                 WHERE first_name='Carol';")
    carols_data = cur.fetchall()
    return carols_data


def query_for_other_girl():
    cur.execute("SELECT first_name || ' ' || last_name, phone_number FROM applicants\
                 WHERE email LIKE '%@adipiscingenimmi.edu';")
    other_girls_data = cur.fetchall()
    return other_girls_data


def insert_into_app_database():
    cur.execute("INSERT INTO applicants\
                (first_name, last_name, phone_number, email, application_code)\
                VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);")
    conn.commit()
    cur.execute("SELECT * FROM applicants\
                 WHERE application_code=54823")
    new_applicants_row = cur.fetchall()
    return new_applicants_row


def update_phone_num():
    cur.execute("UPDATE applicants\
                 SET phone_number = '003670/223-7459'\
                 WHERE first_name='Jemima' AND last_name='Foreman'")
    cur.execute("SELECT * FROM applicants\
                 WHERE first_name='Jemima' AND last_name='Foreman'")
    jemimas_row = cur.fetchall()
    return jemimas_row

def delete_applicants():
    cur.execute("DELETE FROM applicants\
                 WHERE email LIKE '%@mauriseu.net'")
    conn.commit()

#delete_applicants()
#common.print_table(update_phone_num(), ['ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application Code'])
#common.print_table(insert_into_app_database(), ['ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application Code'])
#common.print_table(query_for_other_girl(), ["Full Name", "Phone Number"])
#common.print_table(query_for_carol(), ["Full Name", "Phone Number"])
#common.print_table(query_full_names(), [MENTOR_DB_COL_TITLES[1], MENTOR_DB_COL_TITLES[2]])


def main():
    while True:
        common.print_menu("Database menu",
                          ["Mentors' full name", "Mentors' nickname", "Who the hack is Carol?!",
                           "Who owns the hat if not Carol???", "Add Markus Schaffarzyk to applicants",
                           "Update Jemima's phone number",
                           "Delete applicants with @mauriseu.net email adress"])
        try:
            common.menu_options()
        except KeyError as error:
            print(error)


if __name__ == '__main__':
    main()
