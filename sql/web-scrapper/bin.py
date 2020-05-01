from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv

class Scrapper:
    def __init__(self):
        self.url = "https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2019-2020"
        self.raw_webby = self.get_webby()
        # Parse web page
        self.webby = bs(self.raw_webby, "html.parser")
        self.data = []

    def get_webby(self):
        web_page = None
        with urlopen(self.url) as web:
            web_page = web.read()

        return web_page

    def get_covid_table(self, tables):
        covid_table = None
        for table in tables:
            caption = table.find("caption")
            if caption != None:
                # There is more than one table, and they have no
                # special id, so i will search for the key words
                # casos registrados
                if str(caption).find("Casos registrados a fecha") > 0:
                    covid_table = table
                    break

        return covid_table

    def parse_int(self, a):
        b = ""
        for char in a:
            if ord(char) != 160:
                b += char
                
        c = int(b)
        return c

    def get_them_sweet_data(self):
        # I'm not going to use all colums, 
        # so my columns will be already defined
        tables = self.webby.findAll("table") 
        covid_table = self.get_covid_table(tables)
        covid_table_info = covid_table.find("tbody").findAll("tr") # Informatio lies here
        covid_table_info = covid_table_info[:len(covid_table_info) - 4] # The three last lines are useless

        self.data = []
        for covid_table_row in covid_table_info:
            covid_head = covid_table_row.findAll("th")
            covid_data = covid_table_row.findAll("td")

            if covid_head == None or covid_data == None:
                continue

            if len(covid_head) > 0 and len(covid_data) > 0:
                country = covid_head[0].find("a")
                if country != None:
                    country = country.decode_contents()
                else:
                    continue

                if country.find("<img") >= 0:
                    continue

                cases = self.parse_int(covid_data[0].decode_contents())
                deaths =  self.parse_int(covid_data[2].decode_contents())
                recovered = self.parse_int(covid_data[5].decode_contents())

                self.data.append([country, cases, deaths, recovered])

        return self.data

    def save_sweet_data(self):
        with open("covid_stats.csv", 'w', newline='') as csvfile:
            wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for row in self.data:
                wr.writerow(row)


scrappy = Scrapper()
scrappy.get_them_sweet_data()
scrappy.save_sweet_data()
    