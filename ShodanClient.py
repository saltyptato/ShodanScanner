# import statements
import requests

class ShodanClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def basic_search(self, query):
        search_url = f"https://api.shodan.io/shodan/host/search?key={self.api_key}&query={query}"
        print(f"search_url: {search_url}")
        data = requests.get(search_url)
        # print(type(data))
        print(data.text)
        return data
