from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

class DataOrganizer:

    # Initialization of class constructor
    def __init__(self, tableHeaders, outputsList):
        self.tableHeaders = tableHeaders
        self.outputsList = outputsList
        self.numRows = len(outputsList[0])

    # Print csv string
    def printCSV(self, df):
        csvFile = df.to_csv()   
        print('\ncsv String:\n', csvFile) 

    # To create csv file in the fixed directory 
    def convertToCSVFile(self, df):
        try:
            csvF = open("D:/Master Ciencia de Datos/Tipología y ciclo de vida de datos/Practica Web Scraping/Proyecto Web Scraping/gainers.csv", "wb")
            df.to_csv(csvF, index = False)
            csvF.close()
        except FileNotFoundError as e:
            print(e)
        finally:
            csvF.close()

    # Data will be received as list list. Each element of this list corresponds to one table header
    def convertDFData(self):
        df = pd.DataFrame()
        for i in range(0, len(self.tableHeaders)):
            df[str(self.tableHeaders[i])] = self.outputsList[i]        
        return df