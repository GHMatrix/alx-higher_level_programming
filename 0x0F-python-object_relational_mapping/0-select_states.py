#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
a list of states from the 'states' table.
The results are sorted in ascending order by states.id and displayed as tuples.

Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys


def main():
    """
    Main function that connects to the MySQL server
    and retrieves and displays state data.
    """
    # Check for correct usage
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py
              < mysql_username > < mysql_password > < database_name >")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
