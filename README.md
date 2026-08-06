# Python Project Assignment: Shodan Scanner

## Objective:
Build a Python CLI tool that interacts with the Shodan free API (using the requests library) to retrieve and display information about internet-connected devices. The project will reinforce API interaction, JSON parsing, error handling, and basic object-oriented design principles.

## Folder Structure

- ShodanClient.py

This should be a client that uses the Python Requests library to avoid relying on SDKs (less dependecy vulnerabilities): https://pypi.org/project/requests/

- shodan_tests.py

This will be where we write unit tests to make sure our ShodanClient.py is functioning correctly.

### Project Use Cases (CLI Tool)

#### Use Case 1: Basic Search Query

- Accept a keyword (e.g., "nginx") as a CLI input.

- Fetch and print a list of IP addresses running that service.

#### Use Case 2: Search by Country

- Accept a keyword and country code (e.g., "apache US").

- Return results only from the specified country.

#### Use Case 3: Filter by Port

- Allow user to filter results by a specific port (e.g., only port 22 for SSH).

#### Use Case 4: Fetch Host Details

- Accept an IP address as input.

- Retrieve and display detailed information about that host.

#### Use Case 5: Save to File

- Add an option to save search results to a JSON or CSV file.

#### Use Case 6: Handle API Errors Gracefully

- Inform the user if the API key is invalid, rate-limited, or if no results are found.

#### Use Case 7: Summary Statistics

- After a search, display a summary: how many results, top ports, and most common ISPs.

## Resources and documentation

Shodan API: https://developer.shodan.io/api
Shodan Search Filters: https://www.shodan.io/search/filters
