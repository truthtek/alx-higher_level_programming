#!/usr/bin/python3
"""Script to list states matching the given name from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Get arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    db.close()
