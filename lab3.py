from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    if not name:  # если name пустое или None
        name = "Неизвестный"
    
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    if not age:  # если age пустое или None
        age = "Возраст не указан"
    
    return render_template('lab3/lab3.html', name=name,
                            name_color=name_color, age=age)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3'))
    resp.set_cookie('name', 'Max', max_age=5)
    resp.set_cookie('age', '21')
    resp.set_cookie('name_color', 'red')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')

    if user == '':
        errors['user'] = 'Заполните поле имени!'
    if age == '':
        errors['age'] = 'Заполните поле возраста!'

    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)