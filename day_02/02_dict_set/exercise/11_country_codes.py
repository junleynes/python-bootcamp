# TODO: Add more country codes
from pip._internal.resolution.resolvelib import reporter

running = True
while running:
    country_codes = {
        "PH": "Philippines",
        "US": "United States",
        "CN": "China",
        "JP": "Japan",
        "KR": "Korea"
    }
    response = input("Choose your destination (PH | US | CN | JP | KR): " )
    # if response in country_codes:
    #     print("Key found.")
    #     print(country_codes.get(response))
    #     running = False
    #     break

    print(country_codes.get(response))

