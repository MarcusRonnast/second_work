from flask import Flask, url_for, redirect, render_template, abort

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_page():
    return '''
        <!doctype html>
            <html>
                <head>
                    <title>НГТУ, ФБ, Лабораторные работы</title>
                </head>
                <body>
                    <header>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</header>
                    <main>
                        <ul>
                            <li>
                                <a href="/lab1">Первая лабораторная</a>
                            </li>
                            <li>    
                                <a href="/lab2">Вторая лабораторная</a>
                            </li>
                        </ul>
                    </main>
                    <footer>Чернышов Марк Сергеевич, ФБИ-22, 3 курс, 2024</footer>
                </body>
            </html>
        '''

@app.route("/lab1")
def lab1():
    return '''
        <!doctype html>
            <html>
                <head>
                    <title>Лабораторная 1</title>
                </head>
                <body>
                    <p>Flask — фреймворк для создания веб-приложений на языке
                        программирования Python, использующий набор инструментов
                        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                        называемых микрофреймворков — минималистичных каркасов
                        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
                    <a href="/">Корень сайта</a>
                    <h2>Список роутов</h2>
                    <ul>
                        <li><a href="/">Главная страница</a></li>
                        <li><a href="/lab1">Лабораторная 1</a></li>
                        <li><a href="/lab1/web">Web-сервер на Flask</a></li>
                        <li><a href="/lab1/author">Автор</a></li>
                        <li><a href="/lab1/oak">Дуб</a></li>
                        <li><a href="/lab1/counter">Счетчик</a></li>
                        <li><a href="/lab1/cleaner">Сброс счетчика</a></li>
                        <li><a href="/lab1/info">Информация (редирект)</a></li>
                        <li><a href="/lab1/created">Страница Created</a></li>
                        <li><a href="/football">Статья о футболе</a></li>
                        <li><a href="/400">Ошибка 400</a></li>
                        <li><a href="/401">Ошибка 401</a></li>
                        <li><a href="/402">Ошибка 402</a></li>
                        <li><a href="/403">Ошибка 403</a></li>
                        <li><a href="/405">Ошибка 405</a></li>
                        <li><a href="/418">Ошибка 418 (Я чайник!)</a></li>
                        <li><a href="/error">Создать ошибку 500</a></li>
                    </ul>
                </body>
            </html>
        '''

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")
    css_path = url_for("static", filename="lab1.css")    
    return f'''
        <!doctype html>
            <html>
                <head>
                    <title>Ошибка всей твоей жизни</title>
                    <link rel="stylesheet" href="{css_path}">
                </head>
                <body>
                    <div class="error-container">
                        <h1>Нет такой станицы и никогда не сущетвовало и никогда и не появится! Ты ошибся! Не вижу смысла тебе продолжать свое бренное существование в этом злом и порочном мире!</h1>
                        <p>Возможно тебе стоит поменять приоритеты в жизни и найти новое занятие, которое будет приносить тебе удовольствие. Держись!</p>
                        <img class="img_styles" src="{path}">
                    </div>
                </body>
            </html>
        ''', 404

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
           <body>
               <h1>web-сервер на flask</h1>
               <a href="/lab1/author">author</a>
           </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/html; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Чернышов Марк Сергеевич"
    group = "ФБИ-22"
    faculty = "ФБ"

    return f"""<!doctype html>
        <html>
            <body>
                <p>Студент: {name}</p>
                <p>Группа: {group}</p>
                <p>Факультет: {faculty}</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    css_path = url_for("static", filename="lab1.css")
    return f'''
        <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" href="{css_path}">
                </head>
                <body>
                    <h1>Дуб</h1>
                    <img src="{path}">
                </body>
            </html>
        '''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return f'''
        <!doctype html>
            <html>
                <body>
                    Сколько раз вы сюда заходили: {count}
                </body>
            </html>
        '''

@app.route('/lab1/cleaner')
def cleaner():
    global count
    count = 0
    return '''
        <!doctype html>
            <html>
                <body>
                    <p>Счётчик сброшен успешно</p>
                    <a href="/lab1/counter">Вернуться к счетчику</a>
                </body>
            </html>
        '''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>Создано успешно</h1>
                    <div><i>что-то создано...</i></div>
                </body>
            </html>
        ''', 201

def error_page(code, description):
    return f'''
        <!doctype html>
            <html>
                <body>
                    <h1>{code}: {description}</h1>
                </body>
            </html>
        ''', code
# Страница с кодом 400 (Bad Request)
@app.route('/400')
def bad_request():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>400: Bad Request:Сервер не может обработать запрос из-за клиентской ошибки.</h1>
                </body>
            </html>
        ''', 400

# Страница с кодом 401 (Unauthorized)
@app.route('/401')
def unauthorized():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>401: Unauthorized:Для доступа к ресурсу требуется аутентификация.</h1>
                </body>
            </html>
        ''', 401

# Страница с кодом 402 (Payment Required)
@app.route('/402')
def payment_required():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>402: Payment Required:Необходима оплата для доступа к ресурсу.</h1>
                </body>
            </html>
        ''', 402

# Страница с кодом 403 (Forbidden)
@app.route('/403')
def forbidden():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>403: Forbidden:Доступ к ресурсу запрещён.</h1>
                </body>
            </html>
        ''', 403

# Страница с кодом 405 (Method Not Allowed)
@app.route('/405')
def method_not_allowed():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>405: Method Not Allowed:Используемый метод HTTP не поддерживается для данного ресурса.</h1>
                </body>
            </html>
        ''', 405

# Страница с кодом 418 (I'm a Teapot)
@app.route('/418')
def teapot():
    return '''
        <!doctype html>
            <html>
                <body>
                    <h1>418: I'm a Teapot:Я — чайник, и я не могу заваривать кофе.</h1>
                </body>
            </html>
        ''', 418



@app.route('/error')
def cause_error():
    # Намеренно вызываем ошибку деления на ноль
    result = 10 / 0
    return "Этот код никогда не выполнится."

# Перехватчик ошибки 500
@app.errorhandler(500)
def internal_server_error(error):
    # Пользовательская страница с сообщением об ошибке
    return '''
        <!doctype html>
            <html>
                <head>
                    <title>Ошибка 500</title>
                </head>
                <body>
                    <h1>Ошибка 500: Внутренняя ошибка сервера</h1>
                    <p>Что-то пошло не так на сервере. Пожалуйста, попробуйте позже.</p>
                    <a href="/">Вернуться на главную</a>
                </body>
            </html>
        ''', 500

@app.route('/football')
def football():
    image_path = url_for("static", filename="football.jpg")  
    css_path = url_for("static", filename="lab1.css")
    return f'''
        <!doctype html>
            <html>
                <head>
                    <title>Статья о футболе</title>
                    <link rel="stylesheet" href="{css_path}">
                </head>
                <body>
                    <h1 style="text-align: center;">Футбол — король спорта</h1>
                    <img src="{image_path}" alt="Футбол" class="football">
                    <p>
                        Футбол — это самая популярная игра в мире, объединяющая миллионы болельщиков и игроков.
                        Это не просто спорт, а настоящая страсть, которая заставляет сердца биться чаще.
                    </p>
                    <p>
                        Великие футболисты, такие как Пеле, Марадона и Месси, вдохновляют новые поколения на достижение
                        высоких спортивных результатов. Командная игра, тактика, скорость и техника делают футбол
                        невероятно зрелищным.
                    </p>
                    <p>
                        Каждые четыре года миллионы фанатов собираются, чтобы наблюдать за чемпионатом мира по футболу.
                        Этот турнир определяет лучшую национальную сборную и приносит незабываемые эмоции.
                    </p>
                    <p>
                        Футбол учит нас работать в команде, быть настойчивыми и никогда не сдаваться. Он объединяет людей
                        по всему миру, независимо от возраста, национальности и социального статуса.
                    </p>
                    <a href="/">Вернуться на главную</a>
                </body>
            </html>
    '''
    return html_content, 200, {
            'Content-Language': 'ru-RU',
            'Link': 'https://example.com',
            'Info': 'Info'
        }

@app.route('/lab2/a')    
def a():
    return 'ok'

@app.route('/lab2/a/')    
def a2():
    return 'ok'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@app.route('/lab2/flowers/<int:flower_id>')
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
    
@app.route('/lab2/add_flower/', defaults={'name': None})
@app.route('/lab2/add_flower/<name>')
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

@app.route('/lab2/flowers')
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
    
@app.route('/lab2/clear_flowers')
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

@app.route('/lab2/example')
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

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
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
@app.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

# Перенаправление на маршрут с одним числом
@app.route('/lab2/calc/<int:a>')
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
@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

@app.route('/lab2/cars')
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

if __name__ == '__main__':
    app.run(debug=True)