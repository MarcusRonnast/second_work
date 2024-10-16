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
                    <footer>(Чернышов Марк Сергеевич, ФБИ-22, 3 курс, 2024</footer>
                </body>
            </html>
        '''

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

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

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""    
@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    css_path = url_for("static", filename="lab1.css")
    return '''
        <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" href="''' + css_path + '''">
                </head>
                <body>
                    <h1>Дуб</h1>
                    <img scr="'''+ path +'''">
                </body>
            </html>
        '''        

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
        <!doctype html>
            <html>
                <body>
                    Сколько раз вы сюда заходили: ''' + str(count) + '''
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
                    <p> Счетчит сброшен успешно</p>
                    <a href="/lab1/counter"> Вернуться к счетчику </a>
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