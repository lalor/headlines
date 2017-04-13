from __future__ import unicode_literals

import feedparser
from flask import Flask


app = Flask(__name__)

ZHIHU_FEED = "https://www.zhihu.com/rss"


@app.route('/')
def get_news():
    feed = feedparser.parse(ZHIHU_FEED)
    first_content = feed['entries'][0]
    html_format = """
    <html> <body>
        <h1> Zhihu Headlines </h1>
        <b> {0} </b> <br/>
        <i> {1} </i> <br/>
        <p> {2} </p> <br/>
    <body> </html>"""

    return html_format.format(first_content.get('title'),
                              first_content.get('published'),
                              first_content.get('summary'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
