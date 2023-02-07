import requests
from bs4 import BeautifulSoup
def imdb_top(imdb_top_movies):
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count={imdb_top_movies}"
    )
    fetch_details = BeautifulSoup(requests.get(base_url).content, "html.parser")
    for details in fetch_details.findAll("div", class_="lister-item mode-advanced"):
        print("\n" + details.h3.a.text)                           # movie's name
        print(details.find("span", attrs={"class": "genre"}).text)  # genre
        print(details.strong.text)                                  # movie's rating
        print(f"https://www.imdb.com{details.a.get('href')}")       # movie's page link
        print("\n","*" * 40)
if __name__ == "__main__":
    imdb_top(input("How many movie details would you like to see? "))