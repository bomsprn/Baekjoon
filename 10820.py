import requests
from bs4 import BeautifulSoup
def crawler(): 
    
    url = 'https://www.google.com'
    html = requests.get(url)
    print(html.text)
crawler()