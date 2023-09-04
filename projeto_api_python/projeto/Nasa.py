import os
import requests
class Nasa():

    
    def __init__(self) -> None:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        api_key_path = os.path.join(script_directory, "key.key")
        with open(api_key_path,"r") as key_file:
            
            self.api_key = key_file.read().strip()
            print(self.api_key)
        self.URL = "https://api.nasa.gov/planetary/apod?api_key=ctFgKejXT8FkqABbyognWwbwIyFzaZglgT9orgbm"
    
    def get_apod(self):
        response = requests.get(self.URL)
        return response.json()


    def get_apod_by_date(self,date):
        url = f"{self.URL} + &date= + {date}"
        response = requests.get(url)
        return response.json()
