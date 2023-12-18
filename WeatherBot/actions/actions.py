from typing import Any, Text, Dict, List
from .config import API_KEY
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = next(tracker.get_latest_entity_values("city"), None)
        weather_data = self.get_weather(city)

        print(f"city: {city}")
        print(f"weather_data: {weather_data}")

        if weather_data:
            response = (f"The weather in {city} is {weather_data['current']['temp_f']} Fahrenheit "
                        f"with a high of {weather_data['forecast']['forecastday'][0]['day']['maxtemp_f']}"
                        f" and a low of {weather_data['forecast']['forecastday'][0]['day']['mintemp_f']}. ")
        else:
            response = f"Sorry, I couldn't find the weather for {city}"

        dispatcher.utter_message(text=response)

        return []

    def get_weather(self, city):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no"
        try:
            response = requests.get(url)
            api_response = response.json()
            return api_response
        except requests.exceptions.RequestException as e:
            print(e)

        return 3
