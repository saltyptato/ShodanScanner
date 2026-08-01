# import statements
import json
from ShodanClient import ShodanClient

# Retrieving items in json file
def load_config(file_path: str):
    print(f"Attempting to load config: {file_path}")
    try:
        with open(file_path) as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading config: {e}")

def main():

    data = load_config("config.default.json")

    client = ShodanClient(api_key=data["api_keys"]["shodan"]["key"])
    print(client.api_key)
    
    print(ShodanClient.basic_search(client,"nginx"))

# defining main function
if __name__ == "__main__":
    main()