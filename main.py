from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta
from pprint import pprint

load_dotenv()
SERPAPI_KEY = os.getenv("API_KEY")

def generate_flexible_date_pairs(days_ahead=3, max_trip_length=10):
    today = datetime.today()
    date_pairs = []

    for i in range(days_ahead):
        outbound = today + timedelta(days=i)
        for j in range(1, max_trip_length + 1):
            return_ = outbound + timedelta(days=j)
            date_pairs.append((
                outbound.strftime("%Y-%m-%d"),
                return_.strftime("%Y-%m-%d")
            ))
    
    return date_pairs

def search_flights(outbound_date, return_date):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_flights",
        "departure_id": "IAH",  
        "arrival_id": "MCO",     
        "outbound_date": outbound_date,
        "return_date": return_date,
        "type": "1",             
        "currency": "USD",
        "api_key": SERPAPI_KEY,
        "no_cache": "true"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"❌ HTTP Error for {outbound_date}: {response.text}")
        return None

    data = response.json()
    if "error" in data:
        error_msg = data["error"]
        print(f"❌ API Error for {outbound_date}: {error_msg}")
        if "run out of searches" in error_msg.lower():
            return "QUOTA_EXCEEDED"
        return None

    return data

def find_cheap_flights(data, max_price=125):
    results = []
    flights = data.get("flights_results", [])
    for flight in flights:
        price_str = flight.get("price", "")
        if price_str.startswith("$"):
            try:
                price = float(price_str[1:].replace(",", ""))
                if price <= max_price:
                    results.append(flight)
            except ValueError:
                continue
    return results

if __name__ == "__main__":
    date_pairs = generate_flexible_date_pairs()

    found_any = False
    for outbound, return_ in date_pairs:
        print(f"\nSearching... {outbound} → {return_}")
        data = search_flights(outbound, return_)

        if data == "QUOTA_EXCEEDED":
            print("🚫 Search quota exceeded. Stopping further requests.")
            break

        if not data:
            continue

        cheap_flights = find_cheap_flights(data)
        if cheap_flights:
            print(f"✅ Found {len(cheap_flights)} cheap flight(s) under $125:")
            for flight in cheap_flights:
                pprint({
                    "price": flight["price"],
                    "airline": flight.get("airline", "Unknown"),
                    "departure": outbound,
                    "return": return_
                })
            found_any = True

    if not found_any:
        print("\n😕 No cheap flights found under $125 in the date range.")