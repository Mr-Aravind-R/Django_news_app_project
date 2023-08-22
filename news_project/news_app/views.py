from django.shortcuts import render
from newsapi import NewsApiClient


"""
# Create your views here.
def index(request):
    newsapi = NewsApiClient(newsapi = NewsApiClient(api_key='d2ff4b4c2adb4fad8b2ce4f930eec233'))
    top = newsapi.get_top_headlines(sources = 'bbc-news')
    my_articles = top['articles']
    news = []
    desc = []
    img = []
    for i in range(len(my_articles)):
        f = my_articles[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(news, desc, img)
    return render(request, 'index.html', context = {'mylist': mylist})
"""

def index(request):
    newsapi = NewsApiClient(api_key='d2ff4b4c2adb4fad8b2ce4f930eec233')
    top = newsapi.get_top_headlines(sources='bbc-news, the-next-web, the-wall-street-journal')
    my_articles = top['articles']
    news = []
    desc = []
    img = []
    for i in range(len(my_articles)):
        f = my_articles[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(news, desc, img)
    return render(request, 'index.html', context={'mylist': mylist})
