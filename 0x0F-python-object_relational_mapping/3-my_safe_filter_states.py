#!/usr/bin/python3
"""this module if for querying data from databbase """
import MySQLdb
import sys


def main():
    """main method fo queryring states from database safe from ijection"""
    args = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=f"{args[0]}",
                         passwd=f"{args[1]}", db=f"{args[2]}", charset="utf8")
    user_input = args[3]
    query = "select * from states WHERE name=%s ORDER BY states.id"
    cursor = db.cursor()
    cursor.execute(query, (user_input,))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()
