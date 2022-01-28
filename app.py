from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=8bf195703295444291a6f9d4a95b3137"
    r = requests.get(url).json()

    cases = {
        'articles' : r['articles']
    }

    return render_template("index.html", case = cases)

if __name__ == "__main__":
    app.run(debug = True)