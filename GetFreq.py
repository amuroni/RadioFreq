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

# load url list to scrape data all at once, not for every single url

# writer = pd.ExcelWriter("Frequencytable.xlsx", engine="xlsxwriter")  # xslx name and the engine for df.to_excel

# row = 0                                               # row starts at 0, see below
for url in urls_list:
    page = requests.get(url)                          # get data from each url
    soup = BeautifulSoup(page.content, "lxml")        # let BSoup load the raw html with html.parser
    table = soup.findAll("table")[0]                  # get the tables from the html raw
    dfs = pd.read_html(str(table))                    # read the str items in the tables; contains ALL tables.
    df = dfs[0]
    df2 = df.loc[(df["Province"] == "Cagliari")]      # made a search in the df for Province
    if not df2.empty:                                 # avoid empty df (province != selected one)
        print(df2)                                    # print only df with values
#     df.to_excel(writer, "Frequencies", startrow=row)  # print the dataframe into the excel sheet
#     row = row + len(df.index) + 1                     # starting row for each df: len(df.index) = n. rows of each df)
# writer.save()                                         # close the .to_excel by saving

