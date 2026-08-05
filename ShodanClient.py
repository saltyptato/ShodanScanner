# import statements
import json, requests

class ShodanClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def basic_search(self, query):
        search_results = requests.get(f"https://api.shodan.io/shodan/host/search?key={self.api_key}&query={query}").json()
        return search_results
