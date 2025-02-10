from flask import Flask, url_for, redirect

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
                        <a href="/lab1">Первая лабораторная</a>
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

flower_list = ('роза', 'тюльпан', 'незабудка', 'ромашка')

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

if __name__ == '__main__':
    app.run(debug=True)