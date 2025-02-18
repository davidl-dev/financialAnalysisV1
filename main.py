# Imports
import requests
from dotenv import dotenv_values

# Constants and environment variables
CONFIG = dotenv_values(".env")
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

columbia_lat = 34.00071
columbia_long = -81.03481

# payload = {}

# req = requests.get(BASE_URL, params=payload)

# data = req.json()