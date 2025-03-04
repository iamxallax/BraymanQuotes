from flask import Flask, g, render_template
import time

app = Flask(__name__)

@app.before_request
def load_data():
    with open('quotes.txt') as f:
        g.quotes = f.readlines()

@app.route('/')
def home_page():
    curtime = time.gmtime()
    day = curtime.tm_yday
    index = day % len(g.quotes)
    quote = g.quotes[index]

    return render_template('page.html', quote=quote)