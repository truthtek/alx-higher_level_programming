#!/usr/bin/python3
"""Script to list states matching the given name
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE name = '{}'
    ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    db.close()
