#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == "N":
            print(row) 
    cursor.close()
    db.close()
