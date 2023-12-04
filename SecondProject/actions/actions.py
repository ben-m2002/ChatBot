from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values("food"), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected that you want {food_entity} as your food choice.")
        else:
            dispatcher.utter_message(text="I am sorry but I could not detect what food you want")

        return []


class OrderFoodAction(Action):
    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Which kind of food would you like to get?")

        return []

class ConfirmOrderAction (Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values("food"), None)

        if food_entity:
            dispatcher.utter_message(text=f"Your order for the {food_entity} has been sent to be made in the kitchen")
        else:
            dispatcher.utter_message(text="I am sorry but I could not detect what food you want")

        return []