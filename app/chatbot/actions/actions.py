# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector

class ActionProfSearch(Action):

    def name(self) -> Text:
        return "action_prof_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here are some West Chester University Professors:")

        mysqldb = mysql.connector.connect(host="mysqldb", user="root", password="basicPassword", database="profs")

        cursor = mydb.cursor()
        cursor.execute("SELECT tname FROM profs LIMIT 5")

        for x in cursor:
            dispatcher.utter_message(text=str(x)[2:-3])
        
        cursor.close()
        mydb.close()

        return []
    
class ActionProfQuery(Action):

    def name(self) -> Text:
        return "action_prof_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mysqldb = mysql.connector.connect(host="mysqldb", user="root", password="basicPassword", database="profs")

        profs = tracker.get_slot("profs")
        cursor = mydb.cursor()
        query = "SELECT tname, tNumRatings, Quality, Difficulty, would_take_again FROM profs WHERE tname=%s"
        cursor.execute(query, (profs))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []
