from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Mrs.B</h1>"




if __name__ == "__main__":
    app.run(debug=True)
