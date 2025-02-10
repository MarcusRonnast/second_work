from flask import Blueprint, url_for, redirect

lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def lab():
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


@lab1.route("/lab1/web")
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


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/oak')
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

@lab1.route('/lab1/counter')
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


@lab1.route('/lab1/cleaner')
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


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
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

