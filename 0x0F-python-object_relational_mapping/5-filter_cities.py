#!/usr/bin/python3
"""this module if for querying data from databbase """
import MySQLdb
import sys


def main():
    """main method fo queryring states from two tables using join"""
    args = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=f"{args[0]}",
                         passwd=f"{args[1]}", db=f"{args[2]}", charset="utf8")

    user_input = args[3]
    query = "SELECT cities.name from cities join states\
    on cities.state_id = states.id WHERE states.name=%s"
    cursor = db.cursor()
    cursor.execute(query, (user_input,))
    query_rows = cursor.fetchall()
    for i in range(len(query_rows)):
        print(query_rows[i][0], end="")
        if i != len(query_rows) - 1:
            print(', ', end="")
    print('')


if __name__ == "__main__":
    main()
