
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  
import pandas as pd
import tkinter as tk


url = 'https://gratuitos.netlify.app/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


dados= soup.find_all('table',class_= 'table')

for n in dados:
    print(n.text)





