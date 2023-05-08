from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
#from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

#class action_query_knowledge_base(ActionQueryKnowledgeBase):
#    def __init__(self):
#        knowledge_base = InMemoryKnowledgeBase("data.json")
#        super().__init__(knowledge_base)
                 
import mysql.connector
    
class action_teacher_tdept(Action):

    def name(self) -> Text: return "action_teacher_tdept"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="that teacher works in the:")

        mydb = mysql.connector.connect(host="mysqldb ", user="root", password="basicPassword", database="profs ")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT tdept, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x) + "department") 

        cursor.close()
        mydb.close()

        return []
    
class action_teacher_tNumRatings(Action):

    def name(self) -> Text: return "action_teacher_tNumRatings"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="that teacher has:")

        mydb = mysql.connector.connect(host="mysqldb ", user="root", password="basicPassword", database="profs ")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT tNumRatings, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x) + "Ratings(")

        cursor.close()
        mydb.close()

        return []

class action_teacher_Quality(Action):

    def name(self) -> Text: return "action_teacher_Quality"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="that teacher has a listed quality of:")

        mydb = mysql.connector.connect(host="mysqldb ", user="root", password="basicPassword", database="profs ")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT Quality, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []
    
class action_teacher_Difficulty(Action):

    def name(self) -> Text: return "action_teacher_Difficulty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="that teacher has a average difficulty of:")

        mydb = mysql.connector.connect(host="mysqldb ", user="root", password="basicPassword", database="profs ")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT Difficulty, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []

class action_teacher_WTA(Action):

    def name(self) -> Text: return "action_teacher_WTA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="the students that would take that class again come out to:")

        mydb = mysql.connector.connect(host="mysqldb ", user="root", password="basicPassword", database="profs ")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT WTA, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []
    
class action_teacher_WTA(Action):

    def name(self) -> Text: return "action_teacher_WTA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="the students that would take that class again come out to:")

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT WTA, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x))

        cursor.close()
        mydb.close()

        return []
    
class action_teacher_Name(Action):

    def name(self) -> Text: return "action_teacher_Name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        teacher = tracker.get_slot("tSid")
        cursor = mydb.cursor()
        query = "SELECT tSid, FROM events WHERE name=%s"
        cursor.execute(query, (teacher))
        for x in cursor:
            dispatcher.utter_message(text=str(x) + " is a teacher at WCU")

        cursor.close()
        mydb.close()

        return []