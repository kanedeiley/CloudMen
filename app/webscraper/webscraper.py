from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql

# Create a new instance of the Chrome driver with ad blocker extension
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
ad_blocker_path = "4.1.55_0.crx"
options.add_extension(ad_blocker_path)
driver = webdriver.Chrome(options=options)

# Load the search results page
driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1162")

# Get the ID of the ratemyprofessor page
target_tab_id = driver.current_window_handle

# Close all tabs other than the ratemyprofessor page
for tab_id in driver.window_handles:
    if tab_id != target_tab_id:
        driver.switch_to.window(tab_id)
        driver.close()

# Switch back to the ratemyprofessor page
driver.switch_to.window(target_tab_id)

# Close any overlays or iframes that may appear
try:
    close_button = driver.find_element(By.CSS_SELECTOR, "button.CCPAModal__StyledCloseButton-sc-10x9kq-2.gvGrz")
    close_button.click()
    time.sleep(1)
except:
    pass

# Scroll to the bottom of the page to load all professors
while True:
    prev_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        break

# Click the "Show More" button multiple times until it is no longer visible
while True:
    try:
        show_more_button = driver.find_element(By.CSS_SELECTOR, "button.PaginationButton__StyledPaginationButton-txi1dr-1.gjQZal")
        if show_more_button.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView();", show_more_button)
            time.sleep(1)
            show_more_button.click()
            time.sleep(1)
        else:
            break
    except:
        # Handle any exceptions that may occur during the loop, such as element not found errors
        pass

# Get the complete HTML code of the page
html_code = driver.page_source

# Close the driver
driver.quit()

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

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

# Create a connection to the MySQL database
cnx = mysql.connector.connect(user='root', password='basicPassword',
                              host='mysqldb', database='profs')

# Create a cursor object
cursor = cnx.cursor()

# Define the SQL query to create a table
create_table_query = '''
CREATE TABLE teachers (
  id INT NOT NULL AUTO_INCREMENT,
  tdept VARCHAR(255),
  institution_name VARCHAR(255),
  tname VARCHAR(255),
  tNumRatings INT,
  Quality FLOAT,
  Difficulty FLOAT,
  would_take_again FLOAT,
  PRIMARY KEY (id)
)
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Export the DataFrame to the MySQL table
for _, row in df.iterrows():
    add_teacher_query = '''
    INSERT INTO teachers (tdept, institution_name, tname, tNumRatings, Quality, Difficulty, would_take_again)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    data = (row['tdept'], row['institutiion_name'], row['tname'], row['tNumRatings'], row['Quality'], row['Difficulty'], row['would take again'])
    cursor.execute(add_teacher_query, data)

# Commit the changes to the database
cnx.commit()

# Close the connection and cursor objects
cursor.close()
cnx.close()

conn = pymysql.connect(
    host='root',
    port=3306,
    user='mysqldb',
    password='basicPassword',
    db='profs',
    charset='utf8mb4')

data.to_sql(name='profs', con=conn, if_exists='replace', index=False)
