import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

# Define the base URL and API key
base_url = 'https://www.sahibinden.com/fiat'#you can edit this link which brand car or model need.
api_key = 'Your Scrapper API Key'

# Initialize an empty list to store the JSON data
all_json_data = []

# Define the number of pages you want to scrape
num_pages =26  # Adjust this based on how many pages you need to scrape

# Loop through the pages
for page in range(1, num_pages + 1):
    # Define the payload with the page parameter
    payload = { 
        'api_key': api_key, 
        'url': f'{base_url}?pagingOffset={(page-1)*20}',  # Assuming 20 listings per page
        'premium': 'true'
    }

    # Send the request via ScraperAPI
    response = requests.get('https://api.scraperapi.com/', params=payload)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all script tags with type="application/ld+json"
    json_scripts = soup.find_all("script", type="application/ld+json")

    # Loop through the found scripts and parse the JSON content
    for script in json_scripts:
        try:
            json_content = json.loads(script.string)  # Load the JSON string
            all_json_data.append(json_content)  # Append the JSON object to the list
        except json.JSONDecodeError:
            continue  # If there's an error in decoding, skip the script

    print(f"Page {page} scraped successfully.")
    
    # Wait for a short period between requests to avoid being blocked
    time.sleep(1)

# Save the extracted JSON data to a file
with open("SahibindenScrapedData.json", "w", encoding="utf-8") as json_file:
    json.dump(all_json_data, json_file, ensure_ascii=False, indent=4)

print("JSON verisi başarıyla kaydedildi.")

# ----- VERİYİ PANDAS TABLOSUNA DÖNÜŞTÜRME KISMI -----

# Extract the necessary data
vehicles = []
for item in all_json_data:
    if isinstance(item, list):
        for car in item:
            descriptionPart = car.get("description", "").split(" / ")
            vehicle = {
                "Brand": car.get("brand", {}).get("name", ""),  # Brand
                "Model": descriptionPart[1] if len(descriptionPart) > 1 else "ERROR",  # Model
                "Engine": car.get("vehicleEngine", {}).get("name", ""),  # Engine
                "Fuel Type": car.get("fuelType", ""),  # Fuel Type
                "Transmission": car.get("vehicleTransmission", ""),  # Transmission
                "Color": car.get("color", ""),  # Color 
                "Mileage (KM)": car.get("mileageFromOdometer", [{}])[0].get("value", ""),  # KM
                "Description": car.get("name", ""),
                "Price (TRY)": car.get("offers", {}).get("price", ""),  # Price
                "Currency": car.get("offers", {}).get("priceCurrency", ""),
                "Seller": car.get("offers", {}).get("seller", {}).get("name", ""),  # Seller
                "Contact": car.get("offers", {}).get("seller", {}).get("telephone", "")  # Phone Number
            }
            vehicles.append(vehicle)

# Convert to a table
df = pd.DataFrame(vehicles)

# Display the table
print(df)

# Save the table as an Excel file 
df.to_excel('SahibindenScrapedData.xlsx', index=False)

print("Data has been converted to a table and saved to an Excel file.")

