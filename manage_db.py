import psycopg2
import pprint

def print_table(table, title_list):
    border_horizontal = '━'
    border_vertical = '┃'
    border_cross = '╋'
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



# Connect to an existing database
conn = psycopg2.connect("dbname=maylandertamas user=maylandertamas")

# Open a cursor to perform database operations
cur = conn.cursor()

def query_full_names():
    cur.execute("SELECT first_name, last_name FROM mentors")
    list_of_full_names = cur.fetchall()
    return list_of_full_names

def query_nicknames():
    cur.execute("SELECT nick_name FROM mentors")
    list_of_nicknames = cur.fetchall()
    return list_of_full_names

cur.execute("SELECT TEXTCAT(TEXTCAT(first_name,text ' '),last_name) from applicants WHERE first_name='Carol'")
asd = cur.fetchall()
print(asd)


"""
print_table(query_full_names(), ["First Name", "Last Name"])
print_table(query_nicknames(), ["Nick Name"])
"""
