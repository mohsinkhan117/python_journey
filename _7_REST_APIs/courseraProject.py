from bs4 import BeautifulSoup
import requests 
import pandas as pd
url="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

html=requests.get(url)
html_text= html.text
bs=BeautifulSoup(html_text,'lxml')
#print(bs) #this will print the complete html 
print(bs.h3)
print(bs.title)          # the <title> tag itself
print(bs.title.string)    # just the text inside <title>
print(bs.h1.string)              # the first <h1> tag on the page
print(bs.a) 
first_table=bs.find("table")
all_tables=bs.find_all("table")
print(first_table)

df=pd.DataFrame(first_table)
# df=pd.DataFrame(all_tables)
print(df)

rows_data = []
if first_table:
    rows = first_table.find_all("tr")             # <tr> = table row
    for row in rows:
        cells = row.find_all(["td", "th"])   # <td> = data cell, <th> = header cell
        row_text = [cell.get_text(strip=True) for cell in cells]
        rows_data.append(row_text)

print(rows_data[:3])   # first few rows as plain lists of strings -> team name, year, wins, losses, etc.

# Turning that manually-parsed data into a DataFrame ourselves
manual_df = pd.DataFrame(rows_data[1:], columns=rows_data[0] if rows_data else None)
print(manual_df.head())