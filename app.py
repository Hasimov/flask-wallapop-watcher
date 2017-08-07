from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SearchForm
# Get data Wallapop
import json
from urllib3 import PoolManager
import urllib.parse
# Database
from models import db, Programado

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'

@app.route('/', methods=('GET', 'POST'))
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
    programado_all = Programado.query.all()
    return render_template('items/programadas.html', programado_all=programado_all)


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


@app.route('/programadas/nuevo', methods=('POST',))
def programadas_nuevo():
    itemId = int(request.form['itemId'])
    title = request.form['title']
    pictureURL = request.form['pictureURL']
    price = request.form['price']
    # We saved in the database
    my_program = Programado(
        item_id=itemId,
        title=title,
        picture_URL=pictureURL,
        price=price 
        )
    db.session.add(my_program)
    try:
        db.session.commit()
        flash('Añadida con éxito.')
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


@app.route('/programadas/borrar', methods=('POST',))
def programadas_borrar():
    my_program = Programado.query.get(request.form['id'])
    db.session.delete(my_program)
    try:
        db.session.commit()
        flash('Borrada "{title}".'.format(title=my_program.title))
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


if __name__ == '__main__':
    app.run()