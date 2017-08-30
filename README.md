# PyConES17

![Title](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/title.png)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png)  Workshop: Flask-wallapop-watcher (Application to monitor prices in Wallapop)

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Taller: Flask-wallapop-watcher (Aplicación para vigilar precios en Wallapop)

## Demo

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Currently implemented on a real site:

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Actualmente esta implementado en un sitio real:

[wallaviso.com](http://wallaviso.com)

## Run (Ejecutar)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) For the impatient, you can play with the finished exercise. You should download the code and execute the following commands.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para los impacientes, podéis jugar con el ejercicio acabado. Debéis descargar el código y ejecutar los siguientes comandos.

```bash
cd flask-wallapop-watcher
pip3 install virtualenv
virtualenv --python=python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 models.py db init
python3 models.py db migrate
python3 models.py db upgrade
python3 app.py
````

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Then open in your favorite browser, which will possibly be the fantastic Firefox, a new tab with [http://127.0.0.1:5000](http://127.0.0.1:5000)

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Después abrir en tu navegador favorito, que posiblemente será el fantástico Firefox, una pestaña nueva con [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
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

---
### Part 1 - Flask Core y Search (Parte 1 - Nucleo de Flask y Buscador) 50 min

#### 1.1 Ready? 

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We prepare our virtual environment.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Preparamos nuestro entorno virtual.

```bash
mkdir flask-wallapop-watcher
cd flask-wallapop-watcher
pip3 install virtualenv
virtualenv --python=python3 .venv
source .venv/bin/activate
wget https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/requirements.txt
pip3 install -r requirements.txt
```

---
#### 1.1 Hello PyConES17

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Template Flask. We created a new file called **app.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Plantilla Flask. Creamos un nuevo archivo llamado **app.py**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We run and check that everything works.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ejecutamos y comprobamos que todo funciona.

```bash
python3 app.py
```

```bash
http://127.0.0.1:5000
```

---
#### 1.2 Templates

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We created a folder called **templates**. Inside we make two more folders: **layouts** and **items**. In **layouts** we will make a new one with the name **master.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos una carpeta llamada **templates**. Dentro dos más: **layouts** y **items**. En **layouts** haremos uno nuevo con el nombre **master.html**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) In **items** we are going to have our first real page that will inherit from **master.html**. Within **items** we create **searcher.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) En **items** vamos a tener nuestra primera página real que va a heredar de **master.html**. Dentro de **items** creamos **buscador.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "buscador" %}
{% block title %}Buscador{% endblock %}
{% block body %}
<h1>Buscador</h1>
{% endblock %}
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) You update **app.py** to work with our template engine.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Actulizamos **app.py** para que trabaje nuestro motor de plantillas.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We create the second page where we will have our searches stored. Within **items** we create a new file with the name of **programadas.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos la segunda página donde tendremos nuestras busquedas almacenadas. Dentro de **items** creamos un fichero nuevo con el nombre de **programadas.html**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "programadas" %}
{% block title %}Programadas{% endblock %}
{% block body %}
<h1>Soy la página donde estará las programadas</h1>
{% endblock %}
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We update **app.py** with the new page.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Actulizamos **app.py** con la nueva página.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) As a final detail we will make our browser buttons have the correct routes.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Como último detalle haremos que nuestros botones del navegador tengan las rutas correctas.

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

---
#### 1.3 Forms

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We make the new file **forms.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Realizamos el nuevo archivo **forms.py**.

```python3
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class SearchForm(FlaskForm):
    name = StringField('Nombre', [Length(min=1, max=100, message='Es demasiado largo'), DataRequired(message='Campo obligatorio')])
    price_max = IntegerField('Precio', [NumberRange(1, message='No puede ser inferior a 1'), Optional()])
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We load it and pass it to the template.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Lo cargamos y se lo pasamos a la plantilla.

```python3
from flask import Flask, render_template
from forms import SearchForm

# Flask
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mi secreto'

@app.route('/', methods=('GET', 'POST'))
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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We print the fields with a **loop** in our template **buscador.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Imprimimos los campos con un **bucle** en nuestra plantilla **buscador.html**.

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

---
#### 1.4 Search

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) It's time for fun. First we update our **app.py** to get the form data if you pass the validations. Then, with that information, we will make a call to the Wallapop API. We will only need the URL that they use in your APP. With **urllib3** we will have all the results in a simple dictionary. Which is great, since it is easy to iterate within our template.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ha llegado la hora de lo divertido. Primero actulizamos nuestro **app.py** para obtener los datos del formulario si pasa las validaciones. Después, con esa información, haremos una llamada al API de Wallapop. Solo necesitaremos la URL que utilizan en su APP. Con *urllib3* tendremos todos los resultados en un sencillo diccionario. Lo cual es magnífico, ya que es fácil de iterar dentro de nuestra plantilla.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And in our template of **buscador.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y en nuestra plantilla de **buscador.html**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And ... *Voilá*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y... *Voilá*.


### Break (Descanso) - 10 min

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We debug bugs and prepare for the next point.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Depuramos bugs y nos preparamos para el siguiente punto.

---
### Part 2 - Databases and CRUD with Flask (Bases de datos y CRUD elementos con Flask)

#### 2.1 Models

[ES] Con **Flask-alquemy** vamos a definir la estructura de nuestra base de datos. En este caso tendremos una única tabla llamada *Programado* con los campos: *id*, *title* y *last_item*. Para ello crearemos un nuevo archivo con el nombre **models.py**.

```python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Programado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    last_item = db.Column(db.Integer)
```

[ES] Esta forma de trabajar tan limpia carece de varias funcionalidades básicas, como migraciones o la posibilidad de ejecutar ordenes por medio del terminal. Para ello le sumaremos **Flask-Migrate** para las migraciones automáticas y **Flask-Script** para su gestión.


```python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Programado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    last_item = db.Column(db.Integer)

if __name__ == "__main__":
    manager.run()
```

[ES] Abrimos nuestro terminal e iniciamos la base de datos, creamos la primera migración y actualizamos la base de datos.

```bash
python3 models.py db init
python3 models.py db migrate
python3 models.py db upgrade
```

[ES] Comprobamos que todo ha ido bien.

```bash
sqlite3 database.sqlite
.schema Programado
.exit
```

---
#### 2.2 Save item

[ES] Para guarda un elemento necesitamos modificar nuestra plantilla **buscador.html** para enviar la información que queremos guardar usando *POST*. Qué sencillamente será un **<form>** con las variables ocultas. En este caso lo que haremos será mostrar un botón solo visible cuando recibamos una petición *POST*. Su finalidad será realizar una petición a la página *programadas_nuevo()* con el nombre que hemos buscado.

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
            {% if results %}
                <form action="{{ url_for('programadas_nuevo') }}" method="post">
                    <input type="hidden" name="title" value="{{ form.name.data }}">
                    <input type="submit" class="btn btn-success" value="Programar">
                </form>
            {% endif %}
    </div>
</div>
{% if results %}
    <table class="table">
        {% for item in results %}
        <tr>
            <td><img class="img-responsive" src="{{ item.pictureURL }}" alt="{{ item.title }}"></td>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
        </tr>
        {% endfor %}
    </table>
{% endif %}
{% endblock %}
```

[ES] Ahora, tendremos que crear la función para *programadas_nuevo()* en **app.py**. Lo primero que le decimos es que solo puede aceptar peticiones *POST*. A continuación creamos variables para guardar la información del formulario. Después creamos el registro en la base de datos. Por último redireccionamos a la anterior página para ver el nuevo elemento.

[ES] Por partes. Importamos **db** que será nuestro *ORM*, y **Programado** que será la tabla a manipular.

```python3
from models import db, Programado
```

[ES] Creamos el nuevo registro.

```python3
my_program = Programado(
    title=title
    )
```

[ES] Lo añadimos a la cola.

```python3
db.session.add(my_program)
```

[ES] Y ejecutamos las modificaciones. En caso que fallara, dejaría los datos como estaban. 

```python3
try:
    db.session.commit()
except:
    db.session.rollback()
```

[ES] Todo junto quedará así.

```python3
from flask import Flask, render_template, request, redirect, url_for
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
    title = request.form['title']
    # We saved in the database
    my_program = Programado(
        title=title
        )
    db.session.add(my_program)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


if __name__ == '__main__':
    app.run()
```
---
#### 2.3 View items

[ES] Lamentablemente veremos la página vacía. Por ahora. Haremos una consulta a la base de datos para que nos de todos los registros de la tabla **Programado**, y se lo pasaremos a la plantilla. Para ello modificaremos la función que muestra la plantilla **programadas.html**, que en nuestro caso se llama **programadas** y esta en **app.py**.

```python3
from flask import Flask, render_template, request, redirect, url_for
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
    title = request.form['title']
    # We saved in the database

    my_program = Programado(
        title=title
        )
    db.session.add(my_program)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


if __name__ == '__main__':
    app.run()
```

[ES] Actualizamos la plantilla **programadas.html** con un *bucle* que muestre todos los resultados en una tabla.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "programadas" %}
{% block title %}Programadas{% endblock %}
{% block body %}
<h1>Programadas</h1>
<table class="table">
    <thead>
        <tr>
            <th scope="col">Titulo</th>
        </tr>
    </thead>
    <tbody>
        {% for item in programado_all %}
        <tr>
            <td>{{ item.title }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---
#### 2.4 Delete item

[ES] Repetiremos la estrategia anterior. En el *bucle* que muestra todos los resultados en **programadas.html**, añadimos un formulario que nos envíe un *id* a una futura función que definiremos en **app.py**.

```jinja2
{% extends 'layouts/master.html' %}
{% set active_page = "programadas" %}
{% block title %}Programadas{% endblock %}
{% block body %}
<h1>Programadas</h1>
<table class="table">
    <thead>
        <tr>
            <th scope="col">Titulo</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        {% for item in programado_all %}
        <tr>
            <td>{{ item.title }}</td>
            <td>
                <form action="{{ url_for('programadas_borrar') }}" method="post">
                    <input type="hidden" name="id" value="{{ item.id }}">                    
                    <input type="submit" class="btn btn-danger" value="-">
                </form>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

[ES] La manera de eliminar un registro consiste en realizar una busqueda de los elementos que quieres eliminar, y luego ponerlo en la cola para eliminarlos. Por último ejecutas la orden como antes.


```python3
db.session.delete(my_program)
try:
    db.session.commit()
except:
    db.session.rollback()
```

[ES] Quedaría así.

```python3
from flask import Flask, render_template, request, redirect, url_for
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
        title = request.form['title']
    # We saved in the database

    my_program = Programado(
        title=title
        )
    db.session.add(my_program)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


@app.route('/programadas/borrar', methods=('POST',))
def programadas_borrar():
    my_program = Programado.query.get(request.form['id'])
    db.session.delete(my_program)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    return redirect(url_for('programadas'))


if __name__ == '__main__':
    app.run()
```

---
#### 2.5 Flash messages

[ES] Tenemos un problema de usabilidad: ¡El usuario esta a ciegas cuando añade o borra! Tenemos que informarle de que ha ocurrido. Para ello nos haremos uso de los **Fash messages**. Como queremos que se vean en todas nuestras páginas, modificamos **master.html**.

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
            {# Flashed messages #}
			{% with messages = get_flashed_messages() %}
			  {% if messages %}
				{% for message in messages %}
				  <div class="alert alert-success" role="alert">{{ message }}</div>
				{% endfor %}
			  {% endif %}
			{% endwith %}
            {# End Flashed messages #}
            {% block body %}{% endblock %}
        </div>
    </body>
</html>
```

[ES] Ahora ya será visible todos los mensajes en cajas elegantes de *Bootstrap*. Ahora importamos **flash**.

```python3
from flask import Flask, render_template, request, redirect, url_for, flash
```

[ES] Y añadimos los mensajes que deseamos ver. Por ejemplo.

```python3
try:
    db.session.commit()
    flash('Añadida con éxito.')
except:
    db.session.rollback()
```

[ES] Nuestro **app.py** se nos quedaría así.

```python3
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
        title = request.form['title']
    # We saved in the database

    my_program = Programado(
        title=title
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
```

---
### Break (Descanso) - 10 min

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We take air for the last part. Otherwise, we make as we go to the bathroom and do not come back.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Cogemos aire para la última parte. En caso contrario, hacemos como que vamos al baño y nos piramos.

---
### Part 3 - Sending emails with new items (Envío de emails con nuevos elementos)

#### 3.1 Command

[ES] Ya tenemos montado nuestra interfaz para gestionar nuestras busquedas. Lo siguiente será crear un *script* que se encargue de verificar si hay nuevos resultados. Y si es así, enviarnos un *email*. El primer paso será crear con Flask un comando personalizado. Creamos un nuevo archivo llamado **avisador.py**.

```python3
#!/usr/bin/env python3
from flask_script import Manager
from app import app

manager = Manager(app)

@manager.command
def hello():
    print('hello PyConES17')

if __name__ == "__main__":
    manager.run()
```

[ES] Para probar que funciona ejecutamos, siempre con el entorno virtual activo, lo siguiente.

```bash
chmod +x avisador.py
./avisador.py hello
```

[ES] Si todo ha ido bien nos responderá.

```bash
hello PyConES17
```

#### 3.2 SMTP Server

[ES] Para enviar un email si o si necesitaremos una servidor SMTP. Podéis usar GMail, Hotmail, Fastmail... o cualquier cuenta de correo. Para el taller, usaremos Mailgun. Un poderoso servicio profesional para el envío de emails. Nos permite 10.000 envíos mensuales gratuitos. Suficientes para lo que necesitamos. Creamos una cuenta.

[Mailgun](https://signup.mailgun.com/new/signup)

[ES] Creamos una nueva cuenta.

![step 1](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/1.jpg)

[ES] Confirmamos nuestra cuenta por el enlace que nos han enviado a nuestro email.

![step 2](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/2.jpg)

[ES] Al pulsar sobre el enlace nos llevará a esta página. Pulsamos en *Domains*.

![step 3](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/3.jpg)

[ES] Entramos en nuestro dominio activo.

![step 4](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/4.jpg)

[ES] Aquí tendremos los accesos que necesitaremos. Dejamos abierta esta página.

![step 5](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/5.jpg)

#### 3.3 Send email

[ES] Ya tenemos nuestro servidor de email. Ahora vamos a enviar un correo de prueba. Abrimos **avisador.py** para importar **flask-mail**.

```python3
from flask_mail import Mail, Message
```

[ES] Configuramos **flask-mail**. **MAIL_USERNAME** será **Default SMTP Login** de *mailgun*. Y **MAIL_PASSWORD** será **Default Password** de *mailgun*.

```python3
app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='tu_default_smtp_login',
    MAIL_PASSWORD='tu_default_password'
)
mail = Mail(app)
```

[ES] Creamos un comando para que nos envíe un *email* de prueba.

```python3
@manager.command
def send_email():
    msg = Message(
        "Nuevo aviso",
        sender="no-reply@pycon17.es",
        recipients=["tu_email"]
        )
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
```

[ES] Todo junto quedaría así.

```python3
#!/usr/bin/env python3
from flask_script import Manager
from app import app
from flask_mail import Mail, Message

app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='tu_default_smtp_login',
    MAIL_PASSWORD='tu_default_password'
)
mail = Mail(app)

manager = Manager(app)

@manager.command
def send_email():
    msg = Message(
        "Nuevo aviso",
        sender="no-reply@pycon17.es",
        recipients=["tu_email"]
        )
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)


if __name__ == "__main__":
    manager.run()
```

[ES] Lo ejecutamos.

```bash
./avisador.py send_email
```

[ES] Revisamos nuestra bandeja de entrada. En caso contrario buscamos en *spam*.


#### 3.4 Notification

[ES] Estamos listos para realizar el sistema de notificación. La lógica será de lo más sencilla: buscamos todos los productos que tenga la palabra que tenemos guarda. Nos quedamos con la primera *id*. Si la *id* es la misma que tenemos en la misma de la base de datos, no hacemos nada. Si es diferente, actualizamos la base de datos y enviamos un email. 

[ES] Abrimos **avisador.py**. Primero, importamos nuestra funcion para obtener los elementos del API de Wallapop.

```python3
from app import app, get_resultados
```

[ES] Además, importamos nuestra tabla con las palabras guardadas.

```python3
from models import db, Programado
```

[ES] Recorremos todas las palabras almacenadas.

```python3
@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
```

[ES] Obtenemos el primer *id*. Que lo usaremos para comparar.

```python3
@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
    # Get last id
    results = get_resultados(item.title)
    itemId = results[0]['itemId']
    if int(itemId) != item.last_item:
```

[ES] Para actualizar en SQLAlchemy hay que obtener el resultado, modificar el objeto, y volverlo. El siguiente ejemplo modifico la columna *gana* que es un *boolean* y la columna *nombre* que es un *string*.

```python3
spartano = User.query.filter_by(id=1).first()
spartano.gana = False
spartano.nombre = 'Leónidas'
db.session.add(spartano)
db.session.commit()
```

[ES] En nuestro código quedaría implementado de la siguiente forma.

```python3
@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
    # Get last id
    results = get_resultados(item.title)
    itemId = results[0]['itemId']
    # Update last item in database
    if int(itemId) != item.last_item:
        programado_update = Programado.query.filter_by(id=item.id).first()
        programado_update.last_item = itemId
        db.session.add(programado_update)
        try:
            db.session.commit()
        except:
            db.session.rollback()
```

[ES] Ya solo nos queda enviar el *email*.

```python3
@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
        # Get last id
        results = get_resultados(item.title)
        itemId = results[0]['itemId']
        # Update last item in database
        if int(itemId) != item.last_item:
            programado_update = Programado.query.filter_by(id=item.id).first()
            programado_update.last_item = itemId
            db.session.add(programado_update)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            # Send email
            msg = Message(
                "Nuevo aviso",
                sender="no-reply@pycon17.es",
                recipients=["tu email"]
            )
            msg.body = render_template('emails/notificacion.txt', title=results[0]['title'], id=itemId)
            msg.html = render_template('emails/notificacion.html', title=results[0]['title'], id=itemId)
            mail.send(msg)
```

[ES] Todo junto quedaría.


```python3
#!/usr/bin/env python3
from flask import render_template
from flask_script import Manager
from app import app, get_resultados
from flask_mail import Mail, Message
from models import db, Programado

app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='tu_default_smtp_login',
    MAIL_PASSWORD='tu_default_password'
)
mail = Mail(app)

manager = Manager(app)

@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
        # Get last id
        results = get_resultados(item.title)
        itemId = results[0]['itemId']
        # Update last item in database
        if int(itemId) != item.last_item:
            programado_update = Programado.query.filter_by(id=item.id).first()
            programado_update.last_item = itemId
            db.session.add(programado_update)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            # Send email
            msg = Message(
                "Nuevo aviso",
                sender="no-reply@pycon17.es",
                recipients=["tu email"]
            )
            msg.body = render_template('emails/notificacion.txt', title=results[0]['title'], id=itemId)
            msg.html = render_template('emails/notificacion.html', title=results[0]['title'], id=itemId)
            mail.send(msg)

if __name__ == "__main__":
    manager.run()
```

[ES] Ya no estoy enviando un texto sencillo en el *email*. Necesito la magia de *flask* con su *render_template*. Puedes observar como hago uso de dos plantillas donde paso dos variables. El *titulo* y la *id* del item.

[ES] Creamos una carpeta nueva dentro de *templates* con el nombre *emails*. Y dentro de esta, el archivo *notificacion.html* y *notificacion.txt*. Quedará la siguiente estructura.

```bash
--> templates
        --> emails
            --> notificacion.html
            --> notificacion.txt
        --> items
            --> buscador.html
            --> programadas.html
        --> layouts
            --> master.html
```

[ES] Abrimos *notificacion.txt* e introducimos.

```txt
Aviso

{{ title }}

http://p.wallapop.com/i/{{ id }}?_pid=web&_me=www&campaign=mobile_item
```

[ES] Y en *notificacion.html* lo siguiente.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Notificacion</title>
</head>
<body>
   <h1>Aviso</h1> 
   <h2>{{ title }}</h2>
   <a href="http://p.wallapop.com/i/{{ id }}?_pid=web&_me=www&campaign=mobile_item">Ver</a>
</body>
</html>
```

[ES] ¡E voilà! Ya hemos terminado. Solo tendrás que ejecutar el comando personalizado en cada ocasion que desees revisar nuevos items. De la misma forma que antes.

```bash
./avisador.py send_email
```

[ES] Mi recomendación es ejecutarlo en un *cron* cada hora y listo.

![aplausos](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/aplausos.jpg)
