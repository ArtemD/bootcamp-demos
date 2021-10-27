import requests
import json
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

def weather():
    url = 'https://api.weatherbit.io/v2.0/current?key=3544ad&city=Tallinn&country=Estonia'
    result = requests.get(url)
    data = json.loads(result.text)
    return data['data'][0]['temp']

def news():
    url = 'https://yle.fi/uutiset/18-193572'
    response = requests.get(url)
    items = []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    for item in soup.find_all('a', href=True):
        if "/uutiset/" in item['href'] and "viro" in item.text:
            title = item.text
            link = item['href']

            row = {'title': title, 'link': link}
            items.append(row)
        
    return items

@app.route('/')
def index():
    return render_template('index.html', weather=weather(), news=news())

if __name__ == "__main__":
    app.run(port=5000)