from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


@app.route('/')
def index():

    params = {

        "q": "trump",

        "apikey": '69c0ff694a324f2d88e70206ce4b1718',

        "pageSize": 50,

        "country": 'us'
        }
    r = requests.get('https://newsapi.org/v2/top-headlines?', params=params)
    content = r.json()


    return content['articles'][0]


if __name__ == "__main__":
    app.run(debug=True)
