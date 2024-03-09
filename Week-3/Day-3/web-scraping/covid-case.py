import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"

covid_data = requests.get(url)
# print(covid_data)


soup = BeautifulSoup(covid_data.content,"html.parser")
# print(soup.prettify())


print(soup.title)

world_data = soup.find('tbody').find_all('tr')
# print(world_data)

# for data in world_data:
#     print(data)
#     break

print(len(world_data))
print(world_data[8])


complete_data = []
for i in range (8,len(world_data)):
    data = []
    list_data = world_data[i].find_all("td")

    for i in list_data:
        data.append(i.text)
    complete_data.append(data)



# print(complete_data)
    
mapped_data = list(map(lambda x: x[1:10] + [x[12]] + [x[14]], complete_data))
# print(mapped_data)



sample_list = [1, 2]

square_lambda = lambda x: x**2

# print(square_lambda)

squared_values = map(square_lambda, sample_list)

for item in squared_values:
    print(item)

column_names = [
    "Names",
    "Total Cases",
    "New Cases",
    "Total Deaths",
    "New Deaths",
    "Total Recovered",
    "New Recovered",
    "Active Cases",
    "Serious Cases",
    "Total tests",
    "Population"
]

import pandas as pd

df = pd.DataFrame(mapped_data, columns = column_names)
df.to_csv('covid_data.csv', index=False)

print(df.head())



# world_data1 = [wd.get_text() for wd in world_data]
# print(world_data1)



# df = pd.DataFrame(columns = column_names)

# complete_data = world_data.find_all('tr')

# for row in complete_data:
#     row_data =  row.find_all('td')
#     individual_data = [data.text for data in row_data]
   
# print(individual_data)






# file = open('case.txt', 'w')
# for x in world_data:
#     file.write(str(x) + ','+ '\n')

# file.close()