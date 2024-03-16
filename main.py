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


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                   'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
                   'пилот дронов']
    return render_template('professions.html', title='Профессии', list_type=list_type, profs=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    ans = {
        'title': 'ответы',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'выше среднего',
        'profession': 'пилот',
        'sex': 'мужчина',
        'motivation': 'осваивание Марса',
        'ready': 'Да'
    }
    return render_template('auto_answer.html', **ans)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
