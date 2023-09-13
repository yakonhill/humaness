from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    img_url = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            name = name.capitalize().title()
            search_term = name + ' square image'
            url = f"https://www.google.com/images/search?q={search_term}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_url = soup.find('img')['src']
    return render_template("index.html", name=img_url)

if __name__ == "__main__":
    app.run()
