from app import app
import urllib.request,json
from .models import News

api_url = 'https://newsapi.org/v2/everything?q=apple&apiKey=338b3acd04e94ca08029f617b628e5b4'

def get_news():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(api_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        content = movie_item.get('content')
        img = movie_item.get('urlToImage')

        movie_object = News(content,img)
        movie_results.append(movie_object)

    return movie_results