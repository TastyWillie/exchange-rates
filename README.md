# exchange-rates

Beginner project - Currency enxchange rates

Python 3.9.5

Requirements:
Install requests
Install pandas
Register to https://exchangeratesapi.io to get your API_KEY.
# -------------------------------------------------------- #

Insert your API_KEY to the assigned variable
Run python script to get the latest currency exchange rates, create a Pandas DataFrame and finally write it to excel file named 'rates.xlsx'

Default base currency is EUR. If your exchangeratesapi.io- subscription plan is something else than free, you can change the base currency. To do this, write &base=yourcurrency after the API_KEY.
(For example 'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=USD')

If you want to limit results to certain currencies, insert 
&symbols=yourcurrencies after the API_KEY.
(for example 'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&symbols=USD,CAD,AUD,GBP')