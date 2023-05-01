import requests
import pandas as pd
from typing import List
from config import geoapify_key

def get_schools_in_zip(zipcode: str) -> pd.DataFrame:
    
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

    if (places_response["features"])==[""]:
        return pd.DataFrame()

    else:
        # Extract the relevant properties from each feature and append to a list
        rows = []
        for feature in features_list:
            properties = feature['properties']
            rows.append(properties)

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(rows)
        
        # Drop rows with missing data
        df = df.dropna(subset=['name', 'postcode'],how=any)
        
        if df.empty:
            return pd.DataFrame

        # Drop unnecessary columns
        df = df.drop(columns=['country','country_code','street','lon','lat','state_code','formatted',
                          'address_line1','address_line2','categories','details','datasource','place_id',
                          'housenumber','district','suburb','quarter','old_name','county'])

        # Rename the 'postcode' column to 'zipcode'
        df = df.rename(columns={'postcode': 'zipcode'})

        area_df = df
        zip_df = area_df.loc[area_df['zipcode'] == zipcode]

        # Return the filtered DataFrame
        return (area_df, zip_df)