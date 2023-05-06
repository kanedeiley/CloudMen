import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

with open('/html_code.html', 'rb') as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")
teachers = soup.find_all('a', {'class': 'TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx'})
teachers_data = []

for teacher in teachers:
    tdept = teacher.find('div', {'class': 'CardSchool__Department-sc-19lmz2k-0 haUIRO'})
    Stdept = tdept.text.strip()
    institution_name = teacher.find('div', {'class': 'CardSchool__School-sc-19lmz2k-1 iDlVGM'})
    Sinstitution_name = institution_name.text.strip()
    tname = teacher.find('div', {'class': 'CardName__StyledCardName-sc-1gyrgim-0 cJdVEK'})
    Stname = tname.text.strip()
    tNumRatings = teacher.find('div', {'class': 'CardNumRating__CardNumRatingCount-sc-17t4b9u-3 jMRwbg'})
    StNumRatings = tNumRatings.text.strip()
    quality = teacher.find('div', {'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 icXUyq'})
    qualityTwo = teacher.find('div', {'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk'})
    qualityThree = teacher.find('div', {'class': 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 gcFhmN'})
    if quality is not None and quality.text.strip():
        Squality = quality.text.strip()
    elif qualityTwo is not None and qualityTwo.text.strip():
        Squality = qualityTwo.text.strip()
    elif qualityThree is not None and qualityThree.text.strip():
        Squality = qualityThree.text.strip()
    else:
        Squality = 0
    lad = teacher.find('div', {'class': 'CardFeedback__StyledCardFeedback-lq6nix-0 frciyA'}).find_all('div', {'class': 'CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf'})
    wta = lad[0].text.strip()
    difficulty = lad[1].text.strip()

    teachers_data.append({
        "tdept": Stdept,
        "institutiion_name": Sinstitution_name,
        "tname": Stname,
        "tNumRatings": StNumRatings,
        "Quality": Squality,
        "Difficulty": difficulty,
        "would take again" : wta
    })

df = pd.DataFrame.from_dict(teachers_data)

import mysql.connector

config = {
    'user': 'root',
    'password': 'basicPassword',
    'host': 'mysqldb',
    'port': 3306,
    'database': 'profs'
}
# create a connection to the database
cnx = mysql.connector.connect(**config)

# create a cursor
cursor = cnx.cursor()

# iterate over the rows of the dataframe and insert each row into the professors table
cursor.execute('CREATE TABLE IF NOT EXISTS profs (id INT NOT NULL AUTO_INCREMENT, tdept VARCHAR(255), institution_name VARCHAR(255), tname VARCHAR(255), tNumRatings VARCHAR(255), Quality VARCHAR(255), Difficulty VARCHAR(255), would_take_again VARCHAR(255), PRIMARY KEY (id))')

# Insert the DataFrame data into the table
for _, row in df.iterrows():
    query = 'INSERT INTO profs (tdept, institution_name, tname, tNumRatings, Quality, Difficulty, would_take_again) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query, tuple(row))

# commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
