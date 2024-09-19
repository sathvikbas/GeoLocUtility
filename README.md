# GeoLocUtil Command Line Tool

## About

The purpose of this tool is to take in either a zip code or city and state combination and return information about the inputted place.

Important Notes and Considerations:

- This README File contains instructions on how to run the ``geoloc-util`` command line utility for Mac and Linux devices. Additional steps may be required when trying to run this on a Windows machine.
- When passing variables to the ``geoloc-util`` command line utility, make sure that location variables are enclosed in double straight quotes, not curly quotes (Also Known As Smart Quotes).
- Passing variables without using quotes may provide unsatisfactory results. It is important to sure the Zip Code and Location variables are surrounded by double quotes

## Api Key Setup

To get an API Key, please visit [Open Weather](https://home.openweathermap.org) and create an account.

Once you have an API key, please run the command below with your key in between the quotes with the {yourkey} placeholder:

```bash
echo "export GEO_LOC_UTIL_KEY='{yourkey}'" >> ~/.zshrc
```

Once Api keys are set, proceed to the next section.

## Installation

To begin installation, clone the project and cd into the directory with the following commands:

```bash
git clone https://github.com/sathvikbas/GeoLocUtility.git
cd GeoLocUtility
```

Once cloned create a virtual environment to install dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

Then to install dependencies, install the command line utility and necessary dependencies using the following pip commands:

```bash
pip install .
pip install -r requirements.txt
```

``requirements.txt`` will install necessary packages for both the command line utility tool as well as the testing script.

## Usage

The Command line utility is now ready to run! To get started, simply run the command in the current directory. Here's an example of what a command may look like:

```bash
geoloc-util --locations "Madison, WI" "12345"
```

Note: The ``--locations`` flag is not necessary and the command line utility will produce the same results without it.

## Testing

The integration testing script is located in the file, ``test_geolocutil.py``. The necessary dependancies for this file are located in ``requirements.txt`` and should have been installed earlier when the command, ``pip install -r requirements.txt`` was run. In order to run the testing script, simply run the command below in the command line:

```bash
pytest test_geolocutil.py
```

To run the script and print important values to conosle, run the pytest command with the ``-s`` flag.

Any additional commands that may be added can be done so by adding the command as a string using single quotes inside a tuple within the ``input_commands`` list. An example of how a command may look like is provided below:

```python
input_commands = [
    ('geoloc-util "94582" "19102"'),
    ('geoloc-util "Chicago, IL" "Madison, WI"'),
    ('geoloc-util "San Ramon, CA" "Philadelphia, PA"'),
    ('geoloc-util --location "San Ramon, CA" "19102" "12345"'),
]
```

It is important to note that your command must be inside of a tuple, surrounded by single quotes, and the list must be comma seperated.
