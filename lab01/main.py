from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def home_post():
    url = request.form['url']
    processed_text = text.upper()
    return render_template('home.html', result=processed_text)


if __name__ == '__main__':
    app.run(debug=True)
