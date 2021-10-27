from flask import Flask, render_template
import requests
from requests_html import HTML
from requests_html import HTMLSession

app = Flask(__name__)

def get_rss():
    url = 'https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_UUTISET'
    session = HTMLSession()
    response = session.get(url)
    rss = []

    with response as r:
        items = r.html.find("item", first=False)
        
        for item in items:
            title = item.find('title', first=True).text
            pubDate = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            description = item.find('description', first=True).text

            row = {'title': title, 'pubDate': pubDate, 'guid': guid, 'description': description}
            rss.append(row)
    
    return rss

@app.route('/')
def index():
    return render_template('index.html', body=get_rss())

if __name__ == "__main__":
    app.run(port=5000)