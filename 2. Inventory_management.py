"""
Inventory Management Script (Mock for Replit or Local Use)

Simulates retrieving and displaying mock network device inventory using REST APIs.

✔️ How it meets project requirements:
- Simulates inventory management by retrieving device data from a mock REST API.
- Demonstrates use of external APIs using HTTP GET requests.
- Presents the data as network devices with status and type (mocked).

📦 Tools Used:
- Python 3
- requests module (for HTTP requests)
- jsonplaceholder.typicode.com (free mock API for demo/testing)

🔧 Techniques Applied:
- REST API interaction via GET method
- Parsing JSON response
- Iterating through and formatting device entries for readable output
"""

import requests  # Import the requests module to perform HTTP GET requests

# URL of the mock REST API used to simulate a list of network devices
INVENTORY_ENDPOINT = "https://jsonplaceholder.typicode.com/users"

def get_inventory():
    """
    Sends a GET request to the mock API to retrieve fake device data.
    Parses and prints key attributes like ID, hostname, and simulated device info.
    """
    response = requests.get(INVENTORY_ENDPOINT)  # Make the HTTP GET request
    devices = response.json()  # Parse the JSON response into a Python list of dicts

    # Loop through each 'device' (simulated user) in the mock response
    for device in devices:
        print(f"Device ID: {device['id']}")              # Simulated device ID
        print(f"Hostname: {device['username']}")         # Simulated hostname
        print(f"Device Type: Router")                    # Hardcoded type to simulate routers
        print(f"Status: Active")                         # Hardcoded operational status
        print("-----")                                   # Separator for readability

# Main execution block – runs when the script is executed directly
if __name__ == "__main__":
    print("Fetching mock network inventory...")  # Announce action to user
    get_inventory()  # Call function to retrieve and display the inventory
