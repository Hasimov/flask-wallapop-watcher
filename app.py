from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('items/buscador.html')

if __name__ == '__main__':
    app.run()