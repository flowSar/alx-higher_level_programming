#!/usr/bin/python3
"""this module if for querying data from databbase """
import MySQLdb
import sys


def main():
    """main method from queryring states from database"""
    args = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=f"{args[0]}",
                         passwd=f"{args[1]}", db=f"{args[2]}", charset="utf8")
    cursor = db.cursor()
    cursor.execute("select * from states WHERE BINARY name='{}'\
                   ORDER BY states.id".format(args[3]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()
