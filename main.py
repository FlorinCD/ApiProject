from flask import Flask, request, jsonify
from flask_restful import Api
import feedparser


rss_url = 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'

app = Flask(__name__)
api = Api(app)


def get_news():
    feed = feedparser.parse(rss_url)
    news = []
    for entry in feed.entries:
        news_item = {
            'title': entry.title,
            'link': entry.link,
            'description': entry.summary,
            'pub_date': entry.published
        }
        news.append(news_item)
    return news


def get_sorted_news(sort_by, news):
    if sort_by == 'pub_date_asc':
        news.sort(key=lambda x: x['pub_date'])
    elif sort_by == 'pub_date_desc':
        news.sort(key=lambda x: x['pub_date'], reverse=True)
    elif sort_by == 'title_asc':
        news.sort(key=lambda x: x['title'])
    elif sort_by == 'title_desc':
        news.sort(key=lambda x: x['title'], reverse=True)
    return news


def search_news(search_term, news):
    results = []
    for item in news:
        if search_term.lower() in item['title'].lower() or search_term.lower() in item['description'].lower():
            results.append(item)
    return results


@app.route('/news')
def news():
    sort_by = request.args.get('sort', default='pub_date_desc', type=str)
    search_term = request.args.get('search', default='', type=str)
    news = get_news()
    if search_term:
        news = search_news(search_term, news)
    news = get_sorted_news(sort_by, news)
    return jsonify(news)


if __name__ == '__main__':
    app.run(debug=True)



