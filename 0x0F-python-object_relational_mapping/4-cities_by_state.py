#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    myDataBase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = myDataBase.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM states \
           LEFT JOIN cities ON states.id = state_id \
           ORDER BY cities.id"

    # Use execute() once to fetch all cities and sort by cities.id
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    myDataBase.close()
