"""
Query a database using SQL according to assignment
Questions to address:
How many total Characters are there?
How many of each specific subclass?
How many total Items?
How many of the Items are weapons? How many are not?
How many Items does each character have? (Return first 20 rows)
How many Weapons does each character have? (Return first 20 rows)
On average, how many Items does each Character have?
On average, how many Weapons does each character have?
"""
import sqlite3

#setup the database, setup first query to create table
conn = sqlite3.connect('rpg_db.sqlite3')

#Return total Characters
curs2 = conn.cursor()
query2 = 'SELECT COUNT(character_id) FROM charactercreator_character;'
print('\nTotal Characters:', curs2.execute(query2).fetchall())
curs2.close()
conn.commit()
# query = 'CREATE TABLE rpg_db (name varchar(30), size int);'
#
# #instantiate the cursor
# curs = conn.cursor()
#
# #close and execute first query
# curs.execute(query)
# curs.close()
# conn.commit()

#Return total subclasses
curs3 = conn.cursor()
query3 = 'SELECT COUNT(*) FROM charactercreator_mage;'
print('\nTotal Mages:',curs3.execute(query3).fetchall())
curs3.close()
conn.commit()

#Return total theives
curs_t = conn.cursor()
query_t = 'SELECT COUNT(*) FROM charactercreator_thief;'
print('Total Thieves:', curs_t.execute(query_t).fetchall())
curs_t.close()
conn.commit()


# curs_c = conn.cursor()
# query_c = ''
# print('', curs_c.execute(query_c).fetchall())
# curs_c.close()
# conn.commit()

#Return total clerics
curs_c = conn.cursor()
query_c = 'SELECT COUNT() FROM charactercreator_cleric;'
print('Total Clerics:', curs_c.execute(query_c).fetchall())
curs_c.close()
conn.commit()

#Return total fighters
curs_f = conn.cursor()
query_f = 'SELECT COUNT() FROM charactercreator_fighter;'
print('Total Fighters:', curs_f.execute(query_f).fetchall())
curs_f.close()
conn.commit()

#Reutrn total Items
curs4 = conn.cursor()
query4 = 'SELECT COUNT (item_id) FROM armory_item;'
print('\nTotal Items:', curs4.execute(query4).fetchall())
curs4.close()
conn.commit()

#Return total Weapons
curs_w = conn.cursor()
query_w = 'SELECT COUNT() FROM armory_weapon as aw, armory_item as ai WHERE aw.item_ptr_id = ai.item_id;'
print('Total Weapons in Items:', curs_w.execute(query_w).fetchall())
curs_w.close()
conn.commit()

#Return total items each character has (first 20 rows)
curs_cti = conn.cursor()
query_cti = 'SELECT character_id, COUNT (*) Total_Items FROM charactercreator_character_inventory INNER JOIN armory_item USING (item_id) GROUP BY character_id LIMIT 20;'
print('\nTotal items each character has:', curs_cti.execute(query_cti).fetchall())
curs_cti.close()
conn.commit()

#Return total weapons each character has (first 20 rows)
curs_ctw = conn.cursor()
query_ctw = 'SELECT * FROM armory_item as ai, charactercreator_character_inventory as cci, armory_weapon as aw WHERE ai.item_id = cci.item_id AND ai.item_id = aw.item_ptr_id ORDER BY cci.character_id ASC LIMIT 20;'
print('\nTotal weapons each character has:', curs_ctw.execute(query_ctw).fetchall())
curs_ctw.close()
conn.commit()
