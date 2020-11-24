import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ox.ac.uk/admissions/undergraduate/colleges/do-I-pay-to-live-in-my-college'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup.title

# Find table.
table = soup.find('table', {'class': 'table-striping'})

table_header_names = [
    "college",
    "average_cost (175 days)",
    "common_cost_pay",
    "rent_days",
    "meals_cost (175 days)",
    "total_cost (175 days)",
]

# Generates a list of <tr> </tr> .
table_content = table.find_all('tr')

# Exclude the header row.
table_content = table_content[1:]
    
# Initialize dictionary to pass in columns.
table_dict = dict([(name, '') for name in table_header_names])

college = []
avg_cost = []
common_cost = []
rent_days = []
meals_cost = []
total_cost = []

def appending_td_to_list(td, lst, index):
    res = td[index].find(text=True).replace('*', '')
        
    if index != 0:
        res = res.replace('£', '').replace(',', '').rstrip()
        try:
            res = int(res)
        except ValueError:
            res = None
        except TypeError:
            res = None
        
    lst.append(res)
    return

for tr in table_content:
    # Generates a list of <td> </td>.
    td = tr.find_all('td')

    appending_td_to_list(td, college, 0)
    appending_td_to_list(td, avg_cost, 1)
    appending_td_to_list(td, common_cost, 2)
    appending_td_to_list(td, rent_days, 3)
    appending_td_to_list(td, meals_cost, 4) 
    appending_td_to_list(td, total_cost, 5) 

# Pass in columns into dictionary.
table_dict[table_header_names[0]] = college
table_dict[table_header_names[1]] = avg_cost
table_dict[table_header_names[2]] = common_cost
table_dict[table_header_names[3]] = rent_days
table_dict[table_header_names[4]] = meals_cost
table_dict[table_header_names[5]] = total_cost

oxford_table = pd.DataFrame(table_dict)