from flask import Flask


app = Flask(__name__)


@app.route('/')
def get_news():
    return "no news is good news"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
