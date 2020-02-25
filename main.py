from flask import Blueprint, render_template, request, Flask
from flask_login import login_required, current_user
import requests
# from . import db
main = Blueprint('main', __name__)
auth = Blueprint('main', __name__)


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/signup')
def signup():
	return render_template('signup.html')


@app.route('/news-sources')
def source():
	return render_template("news-sources.html")


@app.route('/search-result', methods=["POST"])
def results():
	source_list = request.form.getlist("news_source")
	sources = ""
	for source in source_list:
		if source == source_list[len(source_list)-1]:
			sources = sources+source
		else:
			sources = sources+source+", "
	params = {
	"q": request.form.get("keyword"),
	"sources": sources,
	"apikey": '69c0ff694a324f2d88e70206ce4b1718',
	"pageSize": 50,
	}
	r = requests.get('https://newsapi.org/v2/top-headlines?', params=params)
	content = r.json()

	# print(content)

	if content['articles'] == []:
		return "<h1>BRUH</h1>"

	article_list = content['articles']
	return render_template("search-result.html", article_list= article_list)

@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return value.strftime(format)



if __name__ == "__main__":
    app.run(debug=True)
