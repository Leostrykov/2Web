from flask import Flask, render_template, request, redirect
from config import SECRET_KEY
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


class LoginForm(FlaskForm):
    id_aust = StringField('id астронавта', validators=[DataRequired()])
    password_aust = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


class LoadFileForm(FlaskForm):
    photo = FileField('Загрузите фото', validators=[DataRequired()])
    submit = SubmitField('Отправить')


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


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_page.html', title='Вход', form=form)


@app.route('/success')
def success():
    return 'Форма отправлена'


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', title='Пассажиры', passengers=['Ридди Скот',
                                                                               'Энди Уир', 'Марк Уотни'])


images = ['image-1.jpg', 'image-2.jpg', 'image-3.jpg']


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    form = LoadFileForm()
    if form.validate_on_submit():
        f = form.photo.data
        f.save(os.path.join('static/img', f.filename))
        images.append(f.filename)
        return redirect('/galery')
    return render_template('images.html', title='Галерея', images=images, form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
