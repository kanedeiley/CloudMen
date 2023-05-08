from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
import mysql.connector
import json


config = {
    'user': 'root',
    'password': 'basicPassword',
    'host': 'mysqldb',
    'port': 3306,
    'database': 'profs'
}
# create a connection to the database
cnx = mysql.connector.connect(**config)

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
cnx.close()

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
jsom_result = json.dumps(result)


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase(json_result)

        super().__init__(knowledge_base)
