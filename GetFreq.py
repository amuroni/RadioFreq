import requests
import pandas as pd
from bs4 import BeautifulSoup

urls_list = ("https://diretta.frequence-radio.com/frequenza-radio-abruzzo.html",
             "https://diretta.frequence-radio.com/frequenza-radio-basilicata.html",
             "https://diretta.frequence-radio.com/frequenza-radio-calabria.html",
             "https://diretta.frequence-radio.com/frequenza-radio-campania.html",
             "https://diretta.frequence-radio.com/frequenza-radio-emilia-romagna.html",
             "https://diretta.frequence-radio.com/frequenza-radio-friuli-venezia-giulia.html",
             "https://diretta.frequence-radio.com/frequenza-radio-lazio.html",
             "https://diretta.frequence-radio.com/frequenza-radio-liguria.html",
             "https://diretta.frequence-radio.com/frequenza-radio-lombardia.html",
             "https://diretta.frequence-radio.com/frequenza-radio-marche.html",
             "https://diretta.frequence-radio.com/frequenza-radio-molise.html",
             "https://diretta.frequence-radio.com/frequenza-radio-piemonte.html",
             "https://diretta.frequence-radio.com/frequenza-radio-puglia.html",
             "https://diretta.frequence-radio.com/frequenza-radio-san-marino.html",
             "https://diretta.frequence-radio.com/frequenza-radio-sardegna.html",
             "https://diretta.frequence-radio.com/frequenza-radio-sicilia.html",
             "https://diretta.frequence-radio.com/frequenza-radio-toscana.html",
             "https://diretta.frequence-radio.com/frequenza-radio-trentino-alto-adige.html",
             "https://diretta.frequence-radio.com/frequenza-radio-umbria.html",
             "https://diretta.frequence-radio.com/frequenza-radio-valle-daosta.html",
             "https://diretta.frequence-radio.com/frequenza-radio-veneto.html")

# we load the url list from which we will scrape the data all at once instead of doing it for every single url
writer = pd.ExcelWriter("Frequencytable.xlsx", engine="xlsxwriter")
row = 0
for url in urls_list:
    page = requests.get(url)                          # get data from each url
    soup = BeautifulSoup(page.content, "lxml")        # let BSoup load the raw html with html.parser
    table = soup.findAll("table")[0]                  # get the tables from the htlm raw
    dfs = pd.read_html(str(table))                    # read the str items in the tables; contains ALL tables.
    df = dfs[0]                                       # generate the dataframe to use for .to_excel pandas mehtod
    df.to_excel(writer, "Frequencies", startrow=row)  # print the dataframe into the excel sheet
    row = row + len(df.index) + 1                     # starting row for each df: len(df.index) = n. rows of each df)
writer.save()