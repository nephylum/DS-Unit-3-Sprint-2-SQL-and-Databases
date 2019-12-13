import psycopg2
import pandas as pd

dbname = 'kwxglone'
user = 'kwxglone'
password = 'paWtQ3llY-skzfTjRXWD0q3YKLbZHydh'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_cursor = pg_conn.cursor()

t_table = pd.read_csv('titanic.csv')

create_test_table = """
CREATE TABLE test(
Survived BOOl,
Pclass INT,
Name VARCHAR(30),
Sex VARCHAR(30),
Age INT,
Siblings_Spouses_Aboard BOOL,
Parents_Children_Aboard BOOL,
Fare FLOAT
)
"""

# create_t_table = """
# CREATE TABLE titanic(
# Survived BOOl,
# Pclass INT,
# Name VARCHAR(30),
# Sex VARCHAR(30),
# Age INT,
# Siblings_Spouses_Aboard BOOL,
# Parents_Children_Aboard BOOL,
# Fare FLOAT
# )
# """
#
# pg_cursor.execute(create_t_table)

# pg_cursor.close()
# pg_conn.commit()
# pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
# pg_cursor = pg_conn.cursor()
# print(t_table.iloc[0])

t_table.rename(columns={'Siblings/Spouses_Aboard': 'Siblings_Spouses_Aboard', 'Parents/Children_Aboard': 'Parents_Children_Aboard'})
t_table.replace({'/':'-', "'": " "})

print(t_table)
example_add =  """
INSERT INTO test
(Survived, Pclass, Name, Sex, Age, Sbilings_Spouses_Aboard,
Parents_Children_Aboard, Fare)
VALUES (""" + str(t_table.iloc[0]['Survived']) + ',' + str(t_table.iloc[0]['Pclass']) + ',' + str(t_table.iloc[0]['Name']) + ',' + str(t_table.iloc[0]['Sex']) + ',' + str(t_table.iloc[0]['Age']) + ");"
print(example_add)

# pg_cursor.execute(example_add)

# pg_cursor.close()
# pg_conn.commit()

# for pass in t_table:
#     add_pass = """
#     INSERT INTO titanic ()
#     """
