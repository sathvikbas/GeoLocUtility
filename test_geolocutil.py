import subprocess
import os
import requests
import json
import pytest
import shlex
from error_handlers import *


OPEN_WEATHER_API_KEY = os.environ["GEO_LOC_UTIL_KEY"]

# Test commands
input_commands = [
    ('geoloc-util "94582" "19102"'),
    ('geoloc-util "Chicago, IL" "Madison, WI"'),
    ('geoloc-util "San Ramon, CA" "Philadelpasdfasdhia, PA"'),
    ('geoloc-util --locations "San Ramon, CA" "12345" "CHICAGO, IL" "193284932458" "Pietown, CO" "PhIlaDelpHia, PA" "90210"'),
    ('geoloc-util --locations'),
    ('geoloc-util --loca'),
    ('geoloc-util --loca --randomflag'),
    ('geoloc-util'),
    ('geoloc-util "Madison, WI" "12345" "Chicago, IL" "10001"'),
    ('geoloc-util --locations "Madison, WI" "12345"'),
]


@pytest.mark.parametrize("command", input_commands)
def test_geoloc_util(command):
    try:
        locations = use_geoloc_util(command)

    # Catching expected errors from the utility tool
    except (LocationError, ZipCodeError, RequestFailedError, NoArgumentsError, InvalidInputError) as e:
        pytest.xfail(f"Expected Failiure: {e}")

    name_l = []
    rev_name_l = []
    for location in locations:
        # print("STRING LOCATION: ", type(string_location))
        # location = json.loads(string_location)
        print("LOCATION: ", location)        
        lat = location['lat']
        lon = location['lon']

        # Making reverse api request (takes in latitude and longitude and returns city name)
        rev_request_output = make_rev_request(lat, lon)
        
        name = location['name']
        rev_request_name = rev_request_output['name']

        # Checking if name in rev_name (edge case ex."12345")
        if name in rev_request_name or rev_request_name in name:
            name = location['name']
            rev_request_name = location['name']

        # getting both city names (rev api and reg api) to compare
        name_l.append(name)
        rev_name_l.append(rev_request_name)

    print("NAME_L: ", name_l)
    print("REV_NAME_L: ", rev_name_l)
    assert name_l == rev_name_l


def use_geoloc_util(command):
    result = subprocess.run(shlex.split(command), capture_output=True, text=True)

    # Split data on new lines
    output_list_strings = result.stdout.strip().split('\n')

    output_list_json = []
    for output in output_list_strings:
        try:
            valid_json_str = output.replace("'", '"')
            output_list_json.append(json.loads(valid_json_str))

        except json.JSONDecodeError as jde:
            print(jde)
            continue
    
    # Returns list with data on all parameters
    return output_list_json


def make_rev_request(latitude, logitude):
    # Reverse api call
    response = requests.get(
        'http://api.openweathermap.org/geo/1.0/reverse',
        params = {
            "lat": latitude, 
            # "limit": 1, 
            "lon": logitude,
            "limit": 1,
            "appid": OPEN_WEATHER_API_KEY,
        },
    )

    if response.status_code == 200:
        try:
            # print(response.text)
            data = json.loads(response.text)[0]
            # print(data)

        except IndexError:
            print(f"{latitude}, {logitude} - Invalid Location")

    elif response.status_code == 401:
            print("Invalid API Key, Request Failed")

    else:            
        print(f"Request failed: {response.reason}")
        print(response.text)

    return data



# if __name__ == '__main__': 




