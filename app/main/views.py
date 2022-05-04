from flask import render_template
from app import app
from ..requests import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = get_news()
    return render_template('index.html', news =news)