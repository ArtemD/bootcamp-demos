import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

def get_games():
    url = 'https://muropaketti.com/kategoria/pelit/peliarvostelut/'
    result = requests.get(url, allow_redirects=True)

    html = result.text

    soup = BeautifulSoup(html, 'html.parser')

    main = soup.find('main')

    result = ''

    for i in main.find_all('a', href=True):
        if "Arvostelu" in i.text:
            output = f"<a href='{i['href']}'>{i.text}</a><br/><hr>"
            result = result + output
    
    markup = f"<html><head><title>Games from Muropaketti</title></head><body>{result}</body></html>"

    return markup

@app.route('/')
def index():
    return get_games()

if __name__ == "__main__":
    app.run(port=5000)