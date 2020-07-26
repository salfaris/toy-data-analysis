import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Historical_mortality_rates_of_puerperal_fever'

# create get requests
page = requests.get(url)

# create soup object
soup = BeautifulSoup(page.text, 'lxml')
soup.title

# find table
table = soup.find('table', {'class': 'wikitable sortable'})

# getting table headers

table_header = table.find_all('th')

table_header_names = [th.text.strip() for th in table_header]
table_header_names.pop()  # only interested in the first 5 columns

# getting table contents
# generates a list of <tr> </tr> 
table_content = table.find_all('tr')

# exclude the header row
table_content = table_content[1:]

# initialize dictionary to pass in columns
table_dict = dict([(name, '') for name in table_header_names])
print(table_dict)

# initialize empty 'columns' lists
year = []
month = []
births = []
deaths = []
rate = []

def appending_td_to_list(td, lst, index):
    return lst.append(td[index].find(text=True))

for tr in table_content:
    # generates a list of <td> </td>
    td = tr.find_all('td')

    appending_td_to_list(td, year, 0)
    appending_td_to_list(td, month, 1)
    appending_td_to_list(td, births, 2)
    appending_td_to_list(td, deaths, 3)
    appending_td_to_list(td, rate, 4) 

# pass in columns into dictionary
table_dict['Year'] = year
table_dict['Month'] = month
table_dict['Births'] = births
table_dict['Deaths'] = deaths
table_dict['Rate (%)'] = rate

# from wiki table to DataFrame
wiki_table = pd.DataFrame(table_dict)