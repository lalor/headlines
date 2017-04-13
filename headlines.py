from __future__ import unicode_literals

import feedparser
from flask import Flask, render_template


app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml"}


@app.route('/')
@app.route('/<publication>')
def get_news(publication="zhihu"):
    feed = feedparser.parse(RSS_FEED[publication])
    return render_template('home.html', articles=feed['entries'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
