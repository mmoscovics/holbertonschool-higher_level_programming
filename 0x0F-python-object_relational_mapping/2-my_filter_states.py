#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name = '{}'\
                ORDER BY id ASC".format(argv[4]))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
