import requests
import json

def extract_countries():
    # The exact URL you found in the Network tab
    api_url = "https://api.first.global/v1"
    
    print(f"Connecting directly to the API: {api_url} ...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Fetch the data
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        # Parse the raw text into a Python dictionary
        data = response.json()
        
        print("\n✅ Successfully downloaded the data!")
        
        # Since we don't know the exact dictionary keys yet (e.g., if it's called 'teams' or 'data'),
        # let's print out the very beginning of the JSON so we can see the exact labels they used.
        print("\n--- Raw Data Preview ---")
        print(json.dumps(data, indent=2)[:800]) # Prints the first 800 characters safely
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the API data: {e}")
    except json.JSONDecodeError:
        print("❌ The server responded, but the data wasn't in JSON format.")

if __name__ == "__main__":
    extract_countries()