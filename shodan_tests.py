# import statements
import json, os
from ShodanClient import ShodanClient

def main():
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
    client = ShodanClient(api_key=SHODAN_API_KEY)

    filter = input("Please provide a search filter from https://www.shodan.io/search/filters: ")
    search_results = ShodanClient.basic_search(client,filter)

    for result in search_results["matches"]:
        print(f'IP: {result["ip_str"]}, Domain: {result["domains"]}, Product: {result["product"]}')
        


# defining main function
if __name__ == "__main__":
    main()