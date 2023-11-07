from flask import Flask, render_template, request
import feedparser
import validators as val

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', status='success')


@app.route('/', methods=['POST'])
def home_post():
    url = request.form['url']
    if not url:
        url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
    feed = feedparser.parse(url)
    entries = feed.entries

    if entries:

        return render_template('home.html', entries=entries, status='success')

    else:
        return render_template('home.html', status='error')


if __name__ == '__main__':
    app.run(debug=True)
