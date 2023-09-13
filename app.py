from flask import Flask, render_template, request
from datetime import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    img_url = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            search_url = f"https://www.google.com/search?q={name}"
            search_page = requests.get(search_url)
            search_soup = BeautifulSoup(search_page.content, 'html.parser')

            # Get the first search result link
            first_result = search_soup.find('a')
            if first_result:
                wiki_url = first_result['href']

                # Scrape the Wikipedia page for the first image
                wiki_page = requests.get(wiki_url)
                wiki_soup = BeautifulSoup(wiki_page.content, 'html.parser')
                first_img = wiki_soup.find('img')
                if first_img:
                    img_url = first_img['src']

    return render_template("index.html", name=img_url)

if __name__ == "__main__":
    app.run()
