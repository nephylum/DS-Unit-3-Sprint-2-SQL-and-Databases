"""
Sprint Assignment. Create Table and Queries using SQL
"""
import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

def run_query(query):
    curs=conn.cursor()
    print(curs.execute(query).fetchall())
    conn.commit()
    curs.close()

def make_table():
    create_table = """
    CREATE TABLE sprint (
    s VARCHAR(30),
    x INT,
    y INT
    )
    """

    run_query(create_table)

    insert_form = """
    INSERT INTO sprint (s, x, y) VALUES (
    """

    run_query(insert_form + "'g', 3, 9);")
    run_query(insert_form + "'v', 5, 7);")
    run_query(insert_form + "'f', 8, 7);")

def do_tasks():
    # Count how many rows you have - it should be 3!
    print('Number of rows:')
    run_query("SELECT COUNT(s) FROM sprint;")

    # How many rows are there where both `x` and `y` are at least 5?
    print('Number of rows where both x and y are at least 5:')
    run_query("SELECT COUNT(*) FROM sprint WHERE x >= 5 AND y >= 5;")

    # How many unique values of `y` are there?
    print('Number of unique values of y:')
    run_query("SELECT COUNT(DISTINCT y) FROM sprint;")
    pass

if __name__ == "__main__":
    make_table()
    do_tasks()
