from flask import Flask, url_for, redirect, render_template, abort
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


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


def error_page(code, description):
    return f'''
        <!doctype html>
            <html>
                <body>
                    <h1>{code}: {description}</h1>
                </body>
            </html>
        ''', code


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


if __name__ == '__main__':
    app.run(debug=True)