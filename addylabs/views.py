from addylabs import app
from flask import render_template, request
import urllib
import simplejson

def retrieveStock(symbol):
    query = 'select * from yahoo.finance.quotes where symbol = "' + symbol + '"'
    params = urllib.urlencode({'env':'http://datatables.org/alltables.env','q':query,'format':'json'})
    f = urllib.urlopen('http://query.yahooapis.com/v1/public/yql', params)
    data = simplejson.load(f)
    return data['query']['results']['quote']

@app.route('/finance', methods=['GET', 'POST'])
def finance():
    if request.method == 'POST':
        symbol = request.form['symbol']
        return render_template('finance.html', data = retrieveStock(symbol))
    else:
        return render_template('finance.html', data = None)

@app.route('/')
def index():
    return render_template('index.html')


