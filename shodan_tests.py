# import statements
import json, os
from ShodanClient import ShodanClient

def main():
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
    client = ShodanClient(api_key=SHODAN_API_KEY)
    
    print(ShodanClient.basic_search(client,"product:nginx"))

# defining main function
if __name__ == "__main__":
    main()