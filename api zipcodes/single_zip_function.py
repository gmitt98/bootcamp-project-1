import sys
print(sys.executable)


import requests
import pandas as pd
from typing import List

def get_schools_in_zip(zipcode: str, geoapify_key: str) -> pd.DataFrame:
    
    # Set parameters for geocode search
    params = {
        "apiKey": geoapify_key,
        "country": "United States",
        "postcode": zipcode
    }
    # Build URL using the geocode endpoint
    geocode_url = f"https://api.geoapify.com/v1/geocode/search?text={zipcode}&lang=en&type=postcode&filter=countrycode:us"

    # Make request to geocode endpoint
    geocode_response = requests.get(geocode_url, params=params).json()

    # Extract latitude, longitude, and place ID from geocode response
    lat = geocode_response["features"][0]["properties"]["lat"]
    lon = geocode_response["features"][0]["properties"]["lon"]
    place_id = geocode_response["features"][0]["properties"]["place_id"]

    # Set parameters for type of place
    categories = "education.school"

    # Set parameters for type of search
    bias = f"proximity:{lon},{lat}"
    filters = f"place:{place_id}"

    # Set parameters dictionary for places search
    params = {
        "categories": categories,
        "bias": bias,
        "filter": filters,
        "apiKey": geoapify_key    
    }

    # Set base URL for places search
    places_url = f"https://api.geoapify.com/v2/places?filter=place:{place_id}"

    # Make request to places search endpoint
    places_response = requests.get(places_url, params=params).json()

    # Extract list of features from places response
    features_list = places_response['features']

    # Extract the relevant properties from each feature and append to a list
    rows = []
    for feature in features_list:
        properties = feature['properties']
        rows.append(properties)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(rows)

    # Drop rows with missing data
    df = df.dropna(subset=['name', 'postcode'])

    # Drop unnecessary columns
    df = df.drop(columns=['country','country_code','state','street','lon','lat','state_code','formatted',
                          'address_line1','address_line2','categories','details','datasource','place_id',
                          'housenumber','district','suburb','quarter','old_name','city'])

    # Rename the 'postcode' column to 'zipcode'
    df = df.rename(columns={'postcode': 'zipcode'})

    # Filter the DataFrame to only include schools within the target zip code
    zip_df = df.loc[df['zipcode'] == zipcode]

    # Return the filtered DataFrame
    return zip_df
