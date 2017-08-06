# PyConES17

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png)  Workshop: Flask-wallapop-watcher (Application to monitor prices in Wallapop)

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Taller: Flask-wallapop-watcher (Aplicación para vigilar precios en Wallapop)

## Demo

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) Currently implemented on a real site:

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Actualmente esta implementado en un sitio real:

[wallaviso.com](http://wallaviso.com)

## Run (Ejecutar)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) For the impatient, you can play with the finished exercise. You should download the code and execute the following commands.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Para los impacientes, podéis jugar con el ejercicio acabado. Debéis descargar el código y ejecutar los siguientes comandos.

```bash
cd flask-wallapop-watcher
pip3 install virtualenv
virtualenv --python=python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
````

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) Then open in your favorite browser, which will possibly be the fantastic Firefox, a new tab with [http://127.0.0.1:5000](http://127.0.0.1:5000)

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Después abrir en tu navegador favorito, que posiblemente será el fantástico Firefox, una pestaña nueva con [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Workshop (Taller)

### Minimum requirements (Requisitos mínimos)

* python3
* wget
* Editor de texto enriquecido: Vim, Sublime Text, VSCode, Atom...
* sqlite3
* Conexión a internet

### We checked everything (Comprobamos que tenemos todo)

```bash
python3 --help
wget --help
sqlite3 --help
ping -c 5 google.com
```

### Part 1 - Flask Core y Search (Parte 1 - Nucleo de Flask y Buscador) 50 min

#### 1.1 Ready? 

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We prepare our virtual environment.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Preparamos nuestro entorno virtual.

```bash
mkdir flask-wallapop-watcher
cd flask-wallapop-watcher
pip3 install virtualenv
virtualenv --python=python3 .venv
source .venv/bin/activate
wget https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/requirements.txt
pip3 install -r requirements.txt
```

#### 1.1 Hello PyConES17

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) Template Flask. We created a new file called **app.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Plantilla Flask. Creamos un nuevo archivo llamado **app.py**.

```python3
from flask import Flask

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'


@app.route('/')
def buscador():
    return 'Hello PyConES17 !!!'


if __name__ == '__main__':
    app.run()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We run and check that everything works.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Ejecutamos y comprobamos que todo funciona.

```bash
python3 app.py
```

```bash
http://127.0.0.1:5000
```

#### 1.2 Templates

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We created a folder called **templates**. Inside we make two more folders: **layouts** and **items**. In **layouts** we will make a new one with the name **master.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Creamos una carpeta llamada **templates**. Dentro dos más: **layouts** y **items**. En **layouts** haremos uno nuevo con el nombre **master.html**.

```jinja2
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>{% block title %}{% endblock %} | Vigilador de Wallapop</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://bootswatch.com/superhero/bootstrap.css">
    </head>
    <body>
        <div class="container">
            <ul class="nav nav-pills nav-justified">
                <li role="presentation" {% if active_page == "buscador" or not active_page %}class="active"{% endif %}><a href="">Buscador</a></li>
                <li role="presentation" {% if active_page == "programadas" %}class="active"{% endif %}><a href="#">Programadas</a></li>
            </ul>
            {% block body %}{% endblock %}
        </div>
    </body>
</html>
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) In **items** we are going to have our first real page that will inherit from **master.html**. Within **items** we create **searcher.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) En **items** vamos a tener nuestra primera página real que va a heredar de **master.html**. Dentro de **items** creamos **buscador.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "buscador" %}
{% block title %}Buscador{% endblock %}
{% block body %}
<h1>Buscador</h1>
{% endblock %}
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) You update **app.py** to work with our template engine.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Actulizamos **app.py** para que trabaje nuestro motor de plantillas.

```python3
from flask import Flask, render_template

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'


@app.route('/')
def buscador():
    return render_template('items/buscador.html')


if __name__ == '__main__':
    app.run()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We create the second page where we will have our searches stored. Within **items** we create a new file with the name of **programadas.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Creamos la segunda página donde tendremos nuestras busquedas almacenadas. Dentro de **items** creamos un fichero nuevo con el nombre de **programadas.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "programadas" %}
{% block title %}Programadas{% endblock %}
{% block body %}
<h1>Soy la página donde estará las programadas</h1>
{% endblock %}
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We update **app.py** with the new page.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Actulizamos **app.py** con la nueva página.

```python3
from flask import Flask, render_template

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'


@app.route('/')
def buscador():
    return render_template('items/buscador.html')


@app.route('/programadas')
def programadas():
    return render_template('items/programadas.html')


if __name__ == '__main__':
    app.run()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) As a final detail we will make our browser buttons have the correct routes.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Como último detalle haremos que nuestros botones del navegador tengan las rutas correctas.

```jinja2
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>{% block title %}{% endblock %} | Vigilador de Wallapop</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://bootswatch.com/superhero/bootstrap.css">
    </head>
    <body>
        <div class="container">
            <ul class="nav nav-pills nav-justified">
                <li role="presentation" {% if active_page == "buscador" or not active_page %}class="active"{% endif %}><a href="{{ url_for('buscador') }}">Buscador</a></li>
                <li role="presentation" {% if active_page == "programadas" %}class="active"{% endif %}><a href="{{ url_for('programadas') }}">Programadas</a></li>
            </ul>
            {% block body %}{% endblock %}
        </div>
    </body>
</html>
```

#### 1.3 Forms

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We make the new file **forms.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Realizamos el nuevo archivo **forms.py**.

```python3
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class SearchForm(FlaskForm):
    name = StringField('Nombre', [Length(min=1, max=100, message='Es demasiado largo'), DataRequired(message='Campo obligatorio')])
    price_max = IntegerField('Precio', [NumberRange(1, message='No puede ser inferior a 1'), Optional()])
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We load it and pass it to the template.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Lo cargamos y se lo pasamos a la plantilla.

```python3
from flask import Flask, render_template
from forms import SearchForm

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'

@app.route('/', methods=['GET', 'POST'])
def buscador():
    form = SearchForm()
    if form.validate_on_submit():
        pass
    return render_template('items/buscador.html', form=form)


@app.route('/programadas')
def programadas():
    return render_template('items/programadas.html')


if __name__ == '__main__':
    app.run()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We print the fields with a **loop** in our template **buscador.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Imprimimos los campos con un **bucle** en nuestra plantilla **buscador.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "buscador" %}
{% block title %}Buscador{% endblock %}
{% block body %}
<h1>Buscador</h1>
<div class="row">
    <div class="col-xs-12">
        <form method="post">
            {{ form.csrf_token }}
            {% for input in form %}
                {% if input.type != 'CSRFTokenField' %}
                    <div class="form-group">
                        {# Label #}
                        {{ input.label }}
                        {# Input #}
                        {{ input(class="form-control") }}
                        {# Errors #}
                        {% if input.errors %}
                            <div class="has-error">
                            {% for error in input.errors %}
                                <label class="help-block">
                                    {{ error }}
                                </label>
                            {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                {% endif %}
            {% endfor %}
            <input type="submit" class="btn btn-primary" value="Buscar">
        </form>
    </div>
</div>
{% endblock %}
```

#### 1.4 Search

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) It's time for fun. First we update our **app.py** to get the form data if you pass the validations. Then, with that information, we will make a call to the Wallapop API. We will only need the URL that they use in your APP. With **urllib3** we will have all the results in a simple dictionary. Which is great, since it is easy to iterate within our template.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Ha llegado la hora de lo divertido. Primero actulizamos nuestro **app.py** para obtener los datos del formulario si pasa las validaciones. Después, con esa información, haremos una llamada al API de Wallapop. Solo necesitaremos la URL que utilizan en su APP. Con *urllib3* tendremos todos los resultados en un sencillo diccionario. Lo cual es magnífico, ya que es fácil de iterar dentro de nuestra plantilla.

```python3
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
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) And in our template of **buscador.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Y en nuestra plantilla de **buscador.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "buscador" %}
{% block title %}Buscador{% endblock %}
{% block body %}
<h1>Buscador</h1>
<div class="row">
    <div class="col-xs-12">
        <form method="post">
            {{ form.csrf_token }}
            {% for input in form %}
                {% if input.type != 'CSRFTokenField' %}
                    <div class="form-group">
                        {# Label #}
                        {{ input.label }}
                        {# Input #}
                        {{ input(class="form-control") }}
                        {# Errors #}
                        {% if input.errors %}
                            <div class="has-error">
                            {% for error in input.errors %}
                                <label class="help-block">
                                    {{ error }}
                                </label>
                            {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                {% endif %}
            {% endfor %}
            <input type="submit" class="btn btn-primary" value="Buscar">
        </form>
    </div>
</div>
{% if results %}
    <table class="table">
        {% for item in results %}
        <tr>
            <td><img class="img-responsive" src="{{ item.pictureURL }}" alt="{{ item.title }}"></td>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
            <td><a href="#" class="btn btn-success">+</a></td>
        </tr>
        {% endfor %}
    </table>
{% endif %}
{% endblock %}
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) And ... *Voilá*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Y... *Voilá*.


### Break (Descanso) - 10 min

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We debug bugs and prepare for the next point.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Depuramos bugs y nos preparamos para el siguiente punto.

### Part 2 - Databases and CRUD with Flask (Bases de datos y CRUD elementos con Flask)

### Break (Descanso) - 10 min

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/en.png) We take air for the last part. Otherwise, we make as we go to the bathroom and do not come back.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/static/es.png) Cogemos aire para la última parte. En caso contrario, hacemos como que vamos al baño y nos piramos.

### Part 3 - Sending emails with new items (Envío de emails con nuevos elementos)