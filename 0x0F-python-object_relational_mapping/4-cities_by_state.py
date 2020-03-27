#!/usr/bin/python3
"""Lists all cities from a database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON states.id = cities.state_id\
            ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
