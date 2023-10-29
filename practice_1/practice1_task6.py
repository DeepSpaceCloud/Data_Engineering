import requests
from bs4 import BeautifulSoup

base_url = 'https://fakestoreapi.com'
response = requests.get(f"{base_url}/products")

data = response.json()

soup = BeautifulSoup('<html><body><table></table></body></html>', 'html.parser')
table = soup.table
tr = soup.new_tag('tr')
table.append(tr)
for title in data[0].keys():
        th = soup.new_tag('th')
        th.string = title
        tr.append(th)

for line in data:
    tr = soup.new_tag('tr')
    table.append(tr)
    for col in line.values():
        td = soup.new_tag('td')
        td.string = str(col)
        tr.append(td)

with open('r_text_6.html', 'w', encoding='utf-8') as result:
    result.write(soup.prettify(formatter = None))
