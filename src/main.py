from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import DataScraper as sc
import DataOrganizer as og
import pandas as pd
import urllib.robotparser

# We must diference two classes: 1) DataScraper class, use to scrap data 2) DataOrganizer class, to organize the scraping data to convert them in csv file
# My header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
# URL to scrap
url = 'https://finance.yahoo.com/gainers/'

# Create a DatasScraper object to use its methods
scraper = sc.DataScraper(url, headers)
# Create a list for future scraping. In this case all tags are the same, byt in other examples the tags could be diferent
tags = ['td', 'td', 'td', 'td', 'td', 'td', 'td', 'td', 'td']
# Atributes list
atributes = [{'aria-label' : 'Symbol'}, {'aria-label' : 'Name'}, {'aria-label' : 'Price (Intraday)'}, {'aria-label' : 'Change'}, {'aria-label' : '% Change'},
            {'aria-label' : 'Volume'}, {'aria-label' : 'Avg Vol (3 month)'}, {'aria-label' : 'Market Cap'}, {'aria-label' : 'PE Ratio (TTM)'}]
# List of table main headers 
tableHeaders = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)']

# Get a list of list with the seeked info
# For it, we use DataScraper class in order to obtain the raw data
outputsList = []

for i in range(0, (len(tags))):
    listCode = scraper.readURL().find_all(tags[i], atributes[i])
    outputsList.append(scraper.seekText(listCode))

# Print the list list of outputs
print(outputsList)

# Create a DataOrganizer object
org = og.DataOrganizer(tableHeaders, outputsList)
dataf = org.convertDFData()

# Print dataframe with scraping data
print(dataf)
# Print csv string
print(org.printCSV(dataf))

# Create csv file in the current directory
org.convertToCSVFile(dataf)


