import requests
# Helper function performating API request given a URL
def api_request(url):
      response = requests.get(url)
      if response.status_code == 200:
            return response.json()
      else:
            print(f"Error: Unable to fetch data (Status Code:{response.status_code})")
            return None
