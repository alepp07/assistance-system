from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetFunding(Action):
    def name(self) -> Text:
        return "action_get_funding"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the country entity
        country_entity = next(tracker.get_latest_entity_values("countries"), None)

        if country_entity:
            # Make a request to your Flask API to get the funding information for the specified country
            api_url = "http://127.0.0.1:5000/api/funding"
            response = requests.get(api_url)
            countries_data = response.json()

            # Find the funding rate for the specified country
            funding_rate = next((country_data['rate'] for country_data in countries_data if country_data['name'] == country_entity), None)

            if funding_rate is not None:
                message = f"The funding rate in {country_entity} is {funding_rate} Euro per month."
            else:
                message = f"Sorry, I couldn't find funding information for {country_entity}."
        else:
            message = "I couldn't determine the country you're asking about."

        dispatcher.utter_message(message)

        return []


