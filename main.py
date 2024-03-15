from flask import Flask, render_template
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Симуляторы', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')