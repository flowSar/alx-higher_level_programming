#!/usr/local/bin/python3
"""this module if for querying data from databbase """
import MySQLdb
import sys


def main():
    """main method fo queryring states from two tables using join"""
    args = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=f"{args[0]}",
                         passwd=f"{args[1]}", db=f"{args[2]}", charset="utf8")

    query = "SELECT cities.id , cities.name, states.name\
    from cities join states on cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()
