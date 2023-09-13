from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            name = name.capitalize().title()
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run()
