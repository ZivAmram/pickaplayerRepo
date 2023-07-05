from flask import Flask, render_template
from flask import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
def base_page():
    return render_template('base.html')


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')


@app.route('/login')
def news_page():
    return render_template('login.html')


@app.route('/draft')
def draft_page():
    players = [
        {'id': 1, 'name': 'Ronaldo', 'number': 7, 'position': 'ST'},
        {'id': 2, 'name': 'Messi', 'number': 30, 'position': 'RW'},
        {'id': 3, 'name': 'Mbappe', 'number': 10, 'position': 'ST'},
        {'id': 4, 'name': 'Vinicius Jr.', 'number': 7, 'position': 'LW'},
        {'id': 5, 'name': 'Haaland', 'number': 10, 'position': 'ST'}
    ]
    return render_template('draft.html', players=players)
