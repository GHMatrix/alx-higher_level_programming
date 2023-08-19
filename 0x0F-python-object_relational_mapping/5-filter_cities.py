#!/usr/bin/env python3
"""Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with sanitized inputs
    query = "SELECT cities.name FROM cities\
             JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s\
             ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
