from flask import render_template
from app import app
from ..requests import get_news,get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = get_news()
    return render_template('index.html', news =news)

@app.route('/source')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_source()
    return render_template('source.html', source =source)