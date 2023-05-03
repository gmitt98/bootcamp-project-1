def get_zip_coordinates(zipcode):
    
    import json
    from pprint import pprint
    import pandas as pd
    import requests

    from config import geoapify_key
    
    params = {
        "apiKey": geoapify_key,
        "country":"United States",
        "postcode": zipcode
    }
    
    # Build URL using the geocode endpoint
    base_url = f"https://api.geoapify.com/v1/geocode/search?text={zipcode}&lang=en&type=postcode&filter=countrycode:us" 
    
    # Run request
    response = requests.get(base_url, params=params).json()
    
    # Extract latitude and longitude from the response
    lat, lon = response['features'][0]['properties']['lat'], response['features'][0]['properties']['lon']
     
    return lat, lon