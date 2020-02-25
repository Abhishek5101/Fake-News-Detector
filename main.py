from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests
# from . import db
main = Blueprint('main', __name__)
auth = Blueprint('main', __name__)


@main.route('/')
def index():
	return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)


@auth.route('/login')
def login():
	return render_template('login.html')


@auth.route('/signup')
def signup():
	return render_template('signup.html')


@main.route('/news-sources')
def source():
	return render_template("news-sources.html")


@main.route('/search-result', methods=["POST"])
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

	if content['articles'] == []:
		return "<h1>BRUH</h1>"

	article_list = content['articles']
	return render_template("search-result.html", article_list= article_list)
