import sys
import requests
from bs4 import BeautifulSoup as bs

def title(text):
    sys.stdout.write("\033[1;34m")
    print(text)
    sys.stdout.write("\033[0;0m")

class Movie:
    def __init__(self, name, rating, votes, gross, position):
        self.name = name
        self.rating = rating
        self.votes = votes
        self.gross = gross
        self.position = position

    def show(self, space):
        text = "Ranking: {:2}".format(str(self.position))
        text += " Title: "
        spaces = len(self.name) - space
        for i in range(spaces):
            text += " "
        text += self.name
        text += " Rating: {0}".format(self.rating)
        text += " Votes: {0}".format(self.votes)
        if self.gross != None:
            text += " Values: {0}".format(self.gross)
        else:
            text += " Values: unknown"

movies = []
longest_title = 0

imdb_web = requests.get('https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=1%27')
imdb_content = imdb_web.text
scraper = bs(imdb_content, 'html.parser')

movies_container = scraper.find_all('div', class_="lister-item mode-advanced")
if len(movies_container) == 50:
    for i, movie_element in enumerate(movies_container):
        name = ""
        rating = 0
        votes = 0
        gross = ""

        # TITLE
        a_tags = movie_element.find_all('a', href=True)
        for i in range(len(a_tags)):
            if i < 2:
                a_tag = a_tags[i]
                if a_tag["href"].find('/title') > -1:
                    name += a_tag.get_text() + " "

        # RATING
        rating_container = movie_element.find("div", class_="ratings-imdb-rating")
        rating = float(rating_container.find("strong").get_text())

        # VOTES & GROSS
        span_tags = movie_element.find_all("span", {"name" : "nv"})
        votes = span_tags[0].get_text()
        
        if len(span_tags) == 2:
            gross = span_tags[1].get_text()
        else:
            gross = None

        if len(name) > longest_title:
            longest_title = len(name)

        movie = Movie(name, rating, votes, gross, i + 1)
        movies.append(movie)


for movie in movies:
    movie.show(longest_title)





