# import statements
import json, os
from ShodanClient import ShodanClient

def main():
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
    client = ShodanClient(api_key=SHODAN_API_KEY)

    product = input("What software do you want to scan? ")
    search_results = ShodanClient.basic_search(client,f"product:{product}")

    for result in search_results["matches"]:
        print(f'IP: {result["ip_str"]}, Domain: {result["domains"]}, Product: {result["product"]}')


# defining main function
if __name__ == "__main__":
    main()