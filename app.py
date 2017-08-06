from flask import Flask, render_template, request
from forms import SearchForm
# Get data Wallapop
import json
from urllib3 import PoolManager
import urllib.parse

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'

@app.route('/', methods=['GET', 'POST'])
def buscador():
    form = SearchForm()
    results = None
    if form.validate_on_submit():
        name = form.name.data
        price_max = form.price_max.data or ''
        # Search in Wallapop
        results = get_resultados(name, price_max)
    return render_template('items/buscador.html', form=form, results=results)


@app.route('/programadas')
def programadas():
    return render_template('items/programadas.html')


def get_resultados(name='', price_max=''):
    http = PoolManager()
    url_api = 'http://es.wallapop.com/rest/items?minPrice=&maxPrice={price_max}&dist=&order=creationDate-des&lat=41.398077&lng=2.170432&kws={kws}'.format(
        kws=urllib.parse.quote(name, safe=''),
        price_max=price_max
    )
    results = http.request('GET', url_api)
    results = json.loads(
        results.data.decode('utf-8')
    )
    return results['items']


if __name__ == '__main__':
    app.run()