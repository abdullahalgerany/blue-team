
import os
import time
import requests

class SolanaCMCExporter:
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('COINMARKETCAP_API_KEY')
        self.BASE_URL = "https://pro-api.coinmarketcap.com/v1"
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
    
    def test_connection(self):
        print("Testing connection with httpbin...")
        
        BASE = "https://httpbin.org"
        
        response = requests.get(
            f"{BASE}/user-agent",
            timeout=5
        )
        response.raise_for_status()
        
        Status = response.status_code
        content = response.headers["content-type"]
        data = response.json()
        
        print(data)
        print(response.json)
        print(response.json()["user-agent"])
        print("Httpbin test successful!\n")
    
    def get_solana_data(self):
        if not self.api_key:
            print("No API key available. Cannot fetch data.")
            return None
        
        print("Fetching Solana data from CoinMarketCap API...")
        
        try:
            response = requests.get(
                f"{self.BASE_URL}/cryptocurrency/quotes/latest",
                params={'symbol': 'SOL', 'convert': 'USD'},
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            
            Status = response.status_code
            content = response.headers["content-type"]
            data = response.json()
            
            print(f"Status: {Status}")
            print(f"Content type: {content}")
            print("API Response received successfully!")
            
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None