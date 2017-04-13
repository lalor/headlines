#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime

import requests
import feedparser
from flask import Flask, render_template, request, make_response


app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml"}

DEFAULTS = {'city': '北京',
            'publication': 'songshuhui'}

WEATHERS = {"北京": 101010100,
            "上海": 101020100,
            "广州": 101280101,
            "深圳": 101280601}


def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]


@app.route('/')
def home():
    publication = get_value_with_fallback('publication')
    city = get_value_with_fallback('city')

    weather = get_weather(city)
    articles = get_news(publication)

    response = make_response(render_template('home.html', articles=articles,
                                             weather=weather))

    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie('publication',  publication, expires=expires)
    response.set_cookie('city',  city, expires=expires)

    return response


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(city):
    code = WEATHERS.get(city, 101010100)
    url = "http://www.weather.com.cn/data/sk/{0}.html".format(code)

    r = requests.get(url)
    r.encoding = 'utf-8'

    data = r.json()['weatherinfo']
    return dict(city=data['city'], temperature=data['temp'],
                description=data['WD'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
