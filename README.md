Flexible Flight Price Finder
Absolutely! Here's a professional, well-structured README.md tailored for your flight search script using SerpAPI:


A Python script that searches for round-trip flights between Houston (IAH) and Orlando (MCO) using SerpAPI's Google Flights engine. It scans multiple date combinations and flags flights under a specified price threshold.

Features
- Generates flexible outbound/return date pairs
- Queries SerpAPI for flight data
- Filters results by price (default: $125)
- Handles API errors and quota limits gracefully
- Outputs matching flights with airline and pricing info

Requirements
- Python 3.7+
- SerpAPI account with an active API key
  
Installation
- Clone the repository

- Install dependencies
pip install -r requirements.txt

- Set up environment variables
Create a .env file in the root directory:
API_KEY=your_serpapi_key_here

Usage
Run the script directly:
python main.py


By default, it:
- Searches 3 days ahead from today
- Checks trip lengths from 1 to 10 days
- Filters flights under $125
You can customize these parameters by modifying:
generate_flexible_date_pairs(days_ahead=30, max_trip_length=10)
find_cheap_flights(data, max_price=125)


Sample Output
Searching... 2025-08-07 → 2025-08-10
✅ Found 2 cheap flight(s) under $125:
{'price': '$119', 'airline': 'Southwest', 'departure': '2025-08-07', 'return': '2025-08-10'}
{'price': '$110', 'airline': 'Spirit', 'departure': '2025-08-07', 'return': '2025-08-10'}


Security Notes
- Your API key is loaded securely via python-dotenv. Never hardcode it.
- Ensure .env is listed in .gitignore to avoid accidental exposure.

Technologies Used
| Tool | Purpose | 
| requests | API communication | 
| dotenv | Secure environment variable load | 
| datetime | Date range generation | 
| pprint | Clean console output | 




