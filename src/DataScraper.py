from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

class DataScraper:

    # Initialization of class constructor
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    # Getters and setters
    def getURL(self):
        return self.url

    def setURL(self, url):
        self.url = url

    def getHEADERS(self):
        return self.headers

    def setHEADERS(self, headers):
        self.headers = headers

    # Method to read the searched url
    def readURL(self):
        try:
            r = requests.get(self.url)
            bs = BeautifulSoup(r.text, 'html.parser')
        except AttributeError:
            print("This page is missing something! Continuing.")
         
        return bs
    
    # Method to obtain seeked text  
    def seekText(self, listCode):
        seekedList = []
        for value in listCode:
            seekedList.append(value.text)
        return seekedList
 


