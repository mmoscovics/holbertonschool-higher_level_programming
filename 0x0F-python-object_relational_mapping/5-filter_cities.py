#!/usr/bin/python3
"""Lists all cities from a database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    city_list = []
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s ORDER BY cities.id ASC", [argv[4]])
    for row in cursor.fetchall():
        city_list.append(row[0])
    print(", ".join(city_list))
    cursor.close()
    db.close()
