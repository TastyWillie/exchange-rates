import requests
import pandas as pd

# Insert your API_KEY below
API_KEY = 'API_KEY HERE'

# The url to get the data
url = f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'

# Send a request and get a response
r = requests.get(url)

# JSON data
data = r.json()

# JSON data to Pandas DataFrame and write it to excel
df = pd.DataFrame(data).to_excel('rates.xlsx')