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

