import sys
import os
import requests
import json
import re
from error_handlers import *

OPEN_WEATHER_API_KEY = os.environ["GEO_LOC_UTIL_KEY"]
COUNTRY = "US"


def get_details(location, zip_code):
    if zip_code:
        response = requests.get(
            'http://api.openweathermap.org/geo/1.0/zip',
            params = {
                "zip": location + "," + COUNTRY, 
                "appid": OPEN_WEATHER_API_KEY
            },
        )

    else:
        response = requests.get(
            'http://api.openweathermap.org/geo/1.0/direct',
            params = {
                "q": location + "," + COUNTRY, 
                "limit": 1, 
                "appid": OPEN_WEATHER_API_KEY
            },
        )

    # For setting api data
    data = {}
    if response.status_code == 200:
        try:
            # print(f"RESPONSE.TEXT: {response.text}")
            data = json.loads(response.text)
            if not zip_code:
                if len(data) == 0:
                    raise LocationError(f"{location} - Invalid Location")
                
                data = data[0]

            return data
        
        except LocationError as e:
            print(e)
    
    else:            
        raise RequestFailedError(f"Request failed: {response.reason}\n{response.text}")


def main():
    args = sys.argv[1:]
    zip_pattern = "^\d{5}$"

    # Get rid of location tags
    if len(args) >= 1:
        if args[0] == "--locations":
            args.pop(0)
    
    try:
        # Check if arguments are being passed
        if len(args) == 0:
            raise NoArgumentsError("No Locations Passed")
    
    except NoArgumentsError as e:
        print(e)

    for arg in args:    
        # print("ARG: ", arg)

        try:
            if "--" in arg:
                raise InvalidInputError(f"{arg} - Invalid Input")

        
            # For Zip Code
            if arg.isdigit():
                if re.match(zip_pattern, arg):
                    output = get_details(arg, True)
                    if output:
                        print(output)

                else:
                    raise ZipCodeError(f"{arg} - Invalid Zip Code")

            # For text location
            else:
                output = get_details(arg, False)
                if output:
                    print(output)
        
        except (ZipCodeError, InvalidInputError) as e:
            print(e)

if __name__ == '__main__':
    main()









