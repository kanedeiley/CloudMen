import mysql.connector
import json

# Set up MySQL connection parameters
HOST = 'mysqldb'
PORT = 3306
USER = 'root'
PASSWORD = 'basicPassword'
DB = 'profs'

# Connect to the MySQL database
connection = mysql.connector.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DB
)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM profs"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Close the cursor and connection to free up resources
cursor.close()
connection.close()

# Convert the rows to a list of dictionaries
teachers = []
for row in rows:
    teacher = {
        'id': row[0],
        'tdept': row[1],
        'institution_name': row[2],
        'tname': row[3],
        'tNumRatings': row[4],
        'Qualtiy': row[5],
        'Difficulty': row[6],
        'would_take_again': row[7]
    }
    teachers.append(teacher)

# Convert the list of dictionaries to a JSON object with a single "teachers" object
result = {'teachers': teachers}

# Save the JSON object to a file in the current directory
with open('knowledge_base_data.json', 'w') as file:
    json.dump(result, file)
