import psycopg2


def connect_to_db(function):
    def wrapper(*args, **kwargs):
        try:
            conn = psycopg2.connect("dbname='SI7_db' user='maylandertamas'")
        except psycopg2.Error as e:
            print("You cannot connect!")
            print(e)
        else:
            cur = conn.cursor()
            with conn:
                with cur:
                    cur.execute(function(*args, **kwargs))
                    data_list = cur.fetchall()
                    return data_list
    return wrapper


@connect_to_db
def database_query(command):
    return command


@connect_to_db
def database_custom_select_query(database_name, first_name, last_name):
    command = "SELECT * FROM {0}\
               WHERE lower(first_name) LIKE lower('%{1}%')\
               AND lower(last_name) LIKE lower('%{2}%');".format(database_name, first_name, last_name)
    return command


select_mentors_by_school = database_query("SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS Mentors, schools.name, schools.country\
                                           FROM mentors\
                                           INNER JOIN schools ON mentors.city = schools.city\
                                           ORDER BY mentors.id;")


select_all_schools = database_query("SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS Mentors, schools.name, schools.country\
                                     FROM mentors\
                                     RIGHT JOIN schools ON mentors.city = schools.city\
                                     ORDER BY mentors.id;")


mentors_by_country = database_query("SELECT schools.country, COUNT(mentors.id) AS Mentors\
                                     FROM mentors\
                                     INNER JOIN schools ON mentors.city = schools.city\
                                     GROUP BY schools.country\
                                     ORDER BY schools.country;")


contacts_by_school = database_query("SELECT schools.name, CONCAT(mentors.first_name, ' ', mentors.last_name) AS Mentors\
                           FROM mentors\
                           INNER JOIN schools ON mentors.id = schools.contact_person\
                           ORDER BY schools.name;")


applicants_with_creaton_dates = database_query("SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date\
                            FROM applicants\
                            INNER JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id\
                            WHERE applicants_mentors.creation_date > '2016-01-01'\
                            ORDER BY applicants_mentors.creation_date DESC;")


applicants_and_their_mentors = database_query("SELECT applicants.first_name, applicants.application_code,\
                                                CONCAT(COALESCE(mentors.first_name, 'None'), ' ', mentors.last_name)\
                                                FROM mentors\
                                                INNER JOIN applicants_mentors ON mentors.id = applicants_mentors.mentor_id\
                                                RIGHT JOIN applicants ON applicants_mentors.applicant_id = applicants.id\
                                                ORDER BY applicants.id;")