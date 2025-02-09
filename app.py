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

if __name__ == '__main__':
    app.run(debug=True)