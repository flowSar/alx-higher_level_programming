#!/usr/local/bin/python3
"""this module if for querying data from databbase """
import MySQLdb
import sys

args = sys.argv[1:]

db = MySQLdb.connect(host="localhost", port=3360, user=f"{args[0]}",
                     passwd=f"{args[1]}", db=f"{args[2]}", charset="utf8")
cursor = db.cursor()
if __name__ == "__main__":
    cursor.execute("select * from students ORDER BY student_id")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
