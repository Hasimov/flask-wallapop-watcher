# PyConES17

![Title](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/title.png)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png)  Workshop: Vigilante de Wallapop (Application to monitor prices in Wallapop)

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Taller: Vigilante de Wallapop (Aplicación para vigilar precios en Wallapop)

## Demo

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Currently implemented on a real site:

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Actualmente esta implementado en un sitio real:

[wallaviso.com](http://wallaviso.com)

## Run (Ejecutar)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) For the impatient, you can play with the finished exercise. You should download the code and execute the following commands.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para los impacientes, podéis jugar con el ejercicio acabado. Debéis descargar el código y ejecutar los siguientes comandos.

```bash
git clone https://github.com/tanrax/flask-wallapop-watcher.git
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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And... we already have an unofficial search engine.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y... ya tenemos un buscador no oficial.


### Break (Descanso) - 10 min

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We debug bugs and prepare for the next point.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Depuramos bugs y nos preparamos para el siguiente punto.

---
### Part 2 - Databases and CRUD with Flask (Bases de datos y CRUD elementos con Flask)

#### 2.1 Models

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) With **Flask-alquemy** we will define the structure of our database. In this case we will have a single table called *Programdo* with the fields: *id*, *title* and *last_item*. To do this we will create a new file with the name **models.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Con **Flask-alquemy** vamos a definir la estructura de nuestra base de datos. En este caso tendremos una única tabla llamada *Programado* con los campos: *id*, *title* y *last_item*. Para ello crearemos un nuevo archivo con el nombre **models.py**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) This clean way of working lacks several basic functionalities, such as migrations or the possibility of executing orders through the terminal. To do this, we'll add **Flask-Migrate** for automatic migrations and **Flask-Script** for managing them.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Esta forma de trabajar tan limpia carece de varias funcionalidades básicas, como migraciones o la posibilidad de ejecutar ordenes por medio del terminal. Para ello le sumaremos **Flask-Migrate** para las migraciones automáticas y **Flask-Script** para su gestión.


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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We opened our terminal and started the database, created the first migration and updated the database.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Abrimos nuestro terminal e iniciamos la base de datos, creamos la primera migración y actualizamos la base de datos.

```bash
python3 models.py db init
python3 models.py db migrate
python3 models.py db upgrade
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We found that everything went well.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Comprobamos que todo ha ido bien.

```bash
sqlite3 database.sqlite
.schema Programado
.exit
```

---
#### 2.2 Save item


![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) To save an element we need to modify our template **buscador.html**. We will send a *POST*. How simply a **<form>** with the hidden variables will be. In this case we will only display the button visible when we receive a *POST* request. Its purpose will be to make a request to the *programadas_nuevo()* page with the name we have searched.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para guarda un elemento necesitamos modificar nuestra plantilla **buscador.html**. Enviaremos un *POST*. Qué sencillamente será un **<form>** con las variables ocultas. En este caso lo que haremos será mostrar el botón solamente visible cuando recibamos una petición *POST*. Su finalidad será realizar una petición a la página *programadas_nuevo()* con el nombre que hemos buscado.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Now, it's time to create the function for *programdas_nuevo()* in **app. py**. The first thing we tell you is that you can only accept *POST* requests. We then create variables to save the form information. We then create the record in the database. Finally we redirect to the previous page to see the new element.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ahora, es el momento de crear la función para *programadas_nuevo()* en **app.py**. Lo primero que le indicamos es que solo puede aceptar peticiones *POST*. A continuación creamos variables para guardar la información del formulario. Después creamos el registro en la base de datos. Por último redireccionamos a la anterior página para ver el nuevo elemento.

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Let's go in parts. We import **db** that will be our *ORM*, and **Programado** that will be the table to manipulate.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Vayamos por partes. Importamos **db** que será nuestro *ORM*, y **Programado** que será la tabla a manipular.

```python3
from models import db, Programado
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We created the new record.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos el nuevo registro.

```python3
my_program = Programado(
    title=title
    )
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We added it to the queue.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Lo añadimos a la cola.

```python3
db.session.add(my_program)
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And we execute the modifications. In case he failed, I'd leave the data as it was. 

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y ejecutamos las modificaciones. En caso que fallara, dejaría los datos como estaban. 

```python3
try:
    db.session.commit()
except:
    db.session.rollback()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Everything together will be like this.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Todo junto quedará así.

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

@app.route('/programadas')
def programadas():
    return render_template('items/programadas.html')

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Unfortunately, we will see the empty page. For now. We will query the database to give us all the records in the **Programado** table, and pass it on to the template. To do this, we will modify the function that renders the template **programadas.html**, which in our case is called **programadas()** and is in **app. py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Lamentablemente veremos la página vacía. Por ahora. Haremos una consulta a la base de datos para que nos de todos los registros de la tabla **Programado**, y se lo pasaremos a la plantilla. Para ello modificaremos la función que renderiza la plantilla **programadas.html**, que en nuestro caso se llama **programadas()** y esta en **app.py**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We updated the **programadas.html** template with a *loop* to display all the results in an HTML table.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Actualizamos la plantilla **programadas.html** con un *bucle* para mostrar todos los resultados en una tabla de HTML.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We will repeat the previous strategy. In the *loop* that shows all the results in **programdas.html**, we add a form that sends us an *id* to a future function that we will define in **app.py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Repetiremos la estrategia anterior. En el *bucle* que muestra todos los resultados en **programadas.html**, añadimos un formulario que nos envíe un *id* a una futura función que definiremos en **app.py**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) The way to delete a record is to search for the items you want to delete, and then put it in the queue to remove them. Finally you execute the order as before.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) La manera de eliminar un registro consiste en realizar una busqueda de los elementos que quieres eliminar, y luego ponerlo en la cola para eliminarlos. Por último ejecutas la orden como antes.

```python3
db.session.delete(my_program)
try:
    db.session.commit()
except:
    db.session.rollback()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) It would look like this.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Quedaría así.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We have a usability problem: The user is blind when adding or deleting! We need to let him know what's going on when he presses buttons. We will use the **Fash messages**. As we want them to be seen on all our pages, we modify **master.html**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Tenemos un problema de usabilidad: ¡El usuario esta a ciegas cuando añade o borra! Tenemos que informarle de que esta pasando cuando apreta botones. Para ello nos haremos uso de los **Fash messages**. Como queremos que se vean en todas nuestras páginas, modificamos **master.html**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) All messages will now be visible in elegant boxes of *Bootstrap*. We import **flash**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ahora ya será visible todos los mensajes en cajas elegantes de *Bootstrap*. Importamos **flash**.

```python3
from flask import Flask, render_template, request, redirect, url_for, flash
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And we add the messages we want to see. For example.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y añadimos los mensajes que deseamos ver. Por ejemplo.

```python3
flash('Añadida con éxito.')
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Our **app.py** would stay that way.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Nuestro **app.py** se nos quedaría así.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We already have our interface set up to manage our searches. Next, create a *script* to check for new results. And if so, send us an *email*. The first step is to create a custom command with Flask. We made a new file called **avisador. py**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ya tenemos montado nuestra interfaz para gestionar nuestras busquedas. Lo siguiente será crear un *script* que se encargue de verificar si hay nuevos resultados. Y si es así, enviarnos un *email*. El primer paso será crear con Flask un comando personalizado. Realizamos un nuevo archivo llamado **avisador.py**.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) To prove that it works, we run, always with the virtual environment active, the following.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para probar que funciona ejecutamos, siempre con el entorno virtual activo, lo siguiente.

```bash
chmod +x avisador.py
./avisador.py hello
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) If everything has gone well, he will answer us.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Si todo ha ido bien nos responderá.

```bash
hello PyConES17
```

---
#### 3.2 SMTP Server

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) To send an email if we need an SMTP server or if we need one. You can use GMail, Hotmail, Fastmail... or any email account. For the workshop, we'll use Mailgun. A powerful professional service for sending emails. It allows us to send 10,000 free monthly mailings. Enough for what we need. We come in here.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para enviar un email si o si necesitaremos una servidor SMTP. Podéis usar GMail, Hotmail, Fastmail... o cualquier cuenta de correo. Para el taller, usaremos Mailgun. Un poderoso servicio profesional para el envío de emails. Nos permite 10.000 envíos mensuales gratuitos. Suficientes para lo que necesitamos. Entramos aquí.

[Mailgun](https://signup.mailgun.com/new/signup)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We created a new account.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos una nueva cuenta.

![step 1](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/1.jpg)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We confirm our account by clicking on the link sent to our email.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Confirmamos nuestra cuenta por el enlace que nos han enviado a nuestro email.

![step 2](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/2.jpg)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Clicking on the link will take us to this page. We confirm our phone number and press *Domains*. Watch out! If you do not confirm your phone number, Mailgun will not work.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Al pulsar sobre el enlace nos llevará a esta página. Confirmamos nuestro teléfono y pulsamos en *Domains*. ¡Ojo! Si no confirmáis vuestro teléfono, Mailgun no funcionará.

![step 3](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/3.jpg)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We entered our active domain.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Entramos en nuestro dominio activo.

![step 4](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/4.jpg)

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Here we will have the accesses we will need. We leave this page open for later.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Aquí tendremos los accesos que necesitaremos. Dejamos abierta esta página para más adelante.

![step 5](https://github.com/tanrax/flask-wallapop-watcher/raw/master/workshop/mailgun/5.jpg)

---
#### 3.3 Send email

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We already have our email server. Now let's send a test email. We open **avisador.py** to import **flask-mail**.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ya tenemos nuestro servidor de email. Ahora vamos a enviar un correo de prueba. Abrimos **avisador.py** para importar **flask-mail**.

```python3
from flask_mail import Mail, Message
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We configure **flask-mail**. **MAIL_USERNAME** will be **Default SMTP Login**. And **MAIL_PASSWORD** will be **Default Password** from *mailgun*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Configuramos **flask-mail**. **MAIL_USERNAME** será **Default SMTP Login** de *mailgun*. Y **MAIL_PASSWORD** será **Default Password** de *mailgun*.

```python3
app.config.update(
    MAIL_SERVER='smtp.mailgun.org',
    MAIL_PORT=587,
    MAIL_USERNAME='tu_default_smtp_login',
    MAIL_PASSWORD='tu_default_password'
)
mail = Mail(app)
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We created a command for you to send us a test *email*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos un comando para que nos envíe un *email* de prueba.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) All together would be like this.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Todo junto quedaría así.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We execute.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ejecutamos.

```bash
./avisador.py send_email
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We checked our inbox. Otherwise we look in *spam*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Revisamos nuestra bandeja de entrada. En caso contrario buscamos en *spam*.

---
#### 3.4 Notification


![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We are ready to perform the notification system. The logic will be basic: we look for all the products that have the word we have guard. We get the first *id*. If the *id* is the same one we have in the database, we don't do anything. If different, we update the database and send an email. 

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Estamos listos para realizar el sistema de notificación. La lógica será básica: buscamos todos los productos que tenga la palabra que tenemos guarda. Nos quedamos con la primera *id*. Si la *id* es la misma que tenemos en la base de datos, no hacemos nada. Si es diferente, actualizamos la base de datos y enviamos un email. 

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We Open **avisador.py**. First, we import our functionality to get the Wallapop API elements.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Abrimos **avisador.py**. Primero, importamos nuestra funcion para obtener los elementos del API de Wallapop.

```python3
from app import app, get_resultados
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) In addition, we import our table with the saved words.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Además, importamos nuestra tabla con las palabras guardadas.

```python3
from models import db, Programado
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We go through all the stored words.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Recorremos todas las palabras almacenadas.

```python3
@manager.command
def send_email():
    programados = Programado.query.all()
    for item in programados:
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We get the first *id*. That we'll use it to compare if we've got it stashed away.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Obtenemos el primer *id*. Que lo usaremos para comparar si la tenemos guardada.

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


![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) To update in SQLAlchemy, you must obtain the result, modify the object, and return it. To illustrate the way of working I leave an example. I change the *gana* column which is a *boolean* and the *nombre* column which is a *string* column.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para actualizar en SQLAlchemy hay que obtener el resultado, modificar el objeto, y devolverlo. Para ilustrar la forma de trabajar dejo un ejemplo. Modifico la columna *gana* que es un *boolean* y la columna *nombre* que es un *string*.

```python3
spartano = User.query.filter_by(id=1).first()
spartano.gana = False
spartano.nombre = 'Leónidas'
db.session.add(spartano)
db.session.commit()
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) In our code it would be implemented as follows.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) En nuestro código quedaría implementado de la siguiente forma.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We just have to send the *email*.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ya solo nos queda enviar el *email*.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) All together would remain.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Todo junto quedaría.

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

---
#### 3.5 View email

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) I am no longer sending a simple text in the *email*. I need the magic of *flask* with its *render_template*. You can see how I use two templates where I pass two variables. The *titulo* and the *id* of the item.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Ya no estoy enviando un texto sencillo en el *email*. Necesito la magia de *flask* con su *render_template*. Puedes observar como hago uso de dos plantillas donde paso dos variables. El *titulo* y la *id* del item.

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) We created a new folder inside *templates* with the name *emails*. And within this, the *notificacion.html* and *notificacion.txt* file. The structure will stay that way.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Creamos una carpeta nueva dentro de *templates* con el nombre *emails*. Y dentro de esta, el archivo *notificacion.html* y *notificacion.txt*. Quedará la estructura así.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) Open *notificacion.txt* and enter.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Abrimos *notificacion.txt* e introducimos.

```txt
Aviso

{{ title }}

http://p.wallapop.com/i/{{ id }}?_pid=web&_me=www&campaign=mobile_item
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) And in *notificacion.html* the following.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Y en *notificacion.html* lo siguiente.

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

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) E voilà! We're all done now. When the new notices arrive we will be able to click on the link to see the product file. And if we're on the smartphone, the official application will open.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) ¡E voilà! Ya hemos terminado. Cuando nos llegue los nuevos avisos podremos pulsar en el enlace para ver la ficha del producto. Y si estamos en el smartphone, se nos abrirá la aplicación oficial.

---
#### 3.6 Automation

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) To check and receive emails, just run the custom command. Same way as before.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Para revisar y recibir los emails solo tendrás que ejecutar el comando personalizado. De la misma forma que antes.

```bash
./avisador.py send_email
```

![English](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/en.png) My recommendation is to run it on *cron* every hour.

![Castellano](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/es.png) Mi recomendación es ejecutarlo en un *cron* cada hora y listo.

![aplausos](https://raw.githubusercontent.com/tanrax/flask-wallapop-watcher/master/workshop/aplausos.jpg)
