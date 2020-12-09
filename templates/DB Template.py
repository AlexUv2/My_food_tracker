import sqlite3
conn = sqlite3.connect('food_log.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE log_date
   ( id integer primary key autoincrement,
    entry_date date not null )
    """)


cursor.execute(""" CREATE TABLE food
    (id integer primary key autoincrement,
    name text not null,
    protein integer not null,
    carbohydrates integer not null,
    fat integer not null,
    calories integer not null)
     """)


cursor.execute("""CREATE TABLE food_date
    (food_id integer not null,
    lod_date_id integer not null,
    primary key(food_id, lod_date_id)
    )""")