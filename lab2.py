from flask import Blueprint, url_for, redirect, render_template, abort

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')    
def a():
    return 'ok'


@lab2.route('/lab2/a/')    
def a2():
    return 'ok'


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "Такого цветка нет", 404
    else:
        flower_name = flower_list[flower_id]
        return f'''
        <!doctype html>
        <html>
            <body>
                <h1>Цветок: {flower_name}</h1>
                <p><a href="/lab2/flowers">Список всех цветков</a></p>
            </body>
        </html>
        '''


@lab2.route('/lab2/add_flower/', defaults={'name': None})
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    if name:
        flower_list.lab2end(name)
        return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p>Название нового цветка: {name}</p>
            <p>Всего цветков: {len(flower_list)}</p>
            <p>Полный список: {flower_list}</p>
        </body>
    </html>
    '''
    else:
        abort(400, description="Вы не задали имя цветка")


@lab2.route('/lab2/flowers')
def all_flowers():
    flower_items = ""
    for flower in flower_list:
        flower_items += f'<li>{flower}</li>'
        
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <ul>
                {flower_items}
            </ul>
            <p>Всего цветков: {len(flower_list)}</p>
            <p><a href="/lab2/clear_flowers">Очистить список цветов</a></p>
        </body>
    </html>
    '''
    

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Список цветов очищен!</h1>
            <p><a href="/lab2/flowers">Список всех цветков</a></p>
        </body>
    </html>
    '''


@lab2.route('/lab2/example')
def example():
    course = '3'
    lab_num = '2'
    group = 'ФБИ-22'
    name = 'Марк Чернышов'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name = name, 
                           course = course, 
                           lab_num = lab_num, 
                           group=group, fruits = fruits )


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b if b != 0 else "не определено (деление на ноль)"
    pow_result = a ** b

    return render_template('calc.html', 
                           a=a, 
                           b=b, 
                           sum_result=sum_result, 
                           sub_result=sub_result, 
                           mul_result=mul_result, 
                           div_result=div_result, 
                           pow_result=pow_result)



# Перенаправление на маршрут с двумя единицами
@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))


# Перенаправление на маршрут с одним числом
@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(url_for('calc', a=a, b=1))

books = [
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 672},
    {"author": "Антон Чехов", "title": "Рассказы", "genre": "Классика", "pages": 350},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451° по Фаренгейту", "genre": "Фантастика", "pages": 256},
    {"author": "Джоан Роулинг", "title": "Гарри Поттер и философский камень", "genre": "Фэнтези", "pages": 432},
    {"author": "Джон Толкин", "title": "Властелин колец", "genre": "Фэнтези", "pages": 1178},
    {"author": "Агата Кристи", "title": "Убийство в Восточном экспрессе", "genre": "Детектив", "pages": 256},
    {"author": "Артур Конан Дойл", "title": "Шерлок Холмс", "genre": "Детектив", "pages": 307},
]


# Обработчик для отображения списка книг
@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)


@lab2.route('/lab2/cars')
def cars():
    b1 = url_for('static', filename='lab2/b1.jpeg')
    b2 = url_for('static', filename='lab2/b2.jpg')
    b3 = url_for('static', filename='lab2/b3.jpg')
    b4 = url_for('static', filename='lab2/b4.jpg')
    b5 = url_for('static', filename='lab2/b5.jpg')
    cars = [
        {'name': 'BMW X1', 'img': b1, 'info': 'BMW X1 отличается ярким спортивным дизайном, высокими динамическими характеристиками и универсальностью — эта модель идеально подходит для приключений.'},
        {'name': 'BMW X2', 'img': b2, 'info': 'BMW X2 — среднеразмерный кроссовер от немецкого автопроизводителя BMW. Автомобиль был представлен в 2016 году в Париже.'},
        {'name': 'BMW X3', 'img': b3, 'info': 'BMW X3 представлен моделями BMW X3 M40d, M40i, X3 xDrive20i и xDrive20d, X3 xDrive30i и xDrive30d – цены и полное описание модели на официальном сайте BMW'},
        {'name': 'BMW X5', 'img': b4, 'info': 'Оснащенный новыми технологиями, обеспечивающими больше безопасности и максимум динамики на любых покрытиях, BMW X5 является безусловным лидером.'},
        {'name': 'BMW X6', 'img': b5, 'info': 'BMW X6 отличается уникальным внешним видом и спортивной динамичностью благодаря мощному двигателю, точно настроенной подвеске и широкой комплектации'}
    ]
    return render_template('cars.html', cars = cars)