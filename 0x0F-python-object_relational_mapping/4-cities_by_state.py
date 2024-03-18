#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    db.close()
