import json
from pprint import pprint
import pandas as pd
import requests

from config import geoapify_key 

def get_schools_in_zip(zipcode):
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
    
    # Set paramaters for type of place
    categories = "education.school"

    # Set parameters for type of search
    bias = f"proximity:{lon},{lat}"
    filters = f"place:{response['features'][0]['properties']['place_id']}"
    
    # Parameters dictionary
    params = {
        "categories": categories,
        "bias": bias,
        "filters":filters,
        "apiKey": geoapify_key    
    }   
    # Set base URL
    base_url = "https://api.geoapify.com/v2/places?"
    
    # Run request
    response = requests.get(base_url, params=params).json()             
    
    # Extract the features list from the dictionary
    features_list = response['features']

    # Extract the relevant properties from each feature
    rows = []
    for feature in features_list:
        properties = feature['properties']
        rows.append(properties)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(rows)
    df = df.dropna(subset=['name', 'postcode'])
    df = df.drop(columns=['country','country_code','state','street','state_code','formatted','address_line1',
                         'address_line2','categories','details','datasource','place_id','housenumber','district','suburb',
                          'quarter','old_name','city','hamlet'], errors="ignore")
    df = df.rename(columns={'postcode': 'zipcode'})
    area_df = df
    zip_df = area_df.loc[area_df['zipcode'] == zipcode]
    
    return area_df, zip_df