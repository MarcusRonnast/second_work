from flask import Blueprint, render_template, request, jsonify, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "Fight Club",
        "title_ru": "Бойцовский клуб",
        "year": 1999,
        "description": "Сотрудник страховой компании страдает хронической бессонницей и отчаянно пытается вырваться из мучительно скучной жизни. Однажды в очередной командировке он встречает некоего Тайлера Дёрдена — харизматического торговца мылом с извращенной философией. Тайлер уверен, что самосовершенствование — удел слабых, а единственное, ради чего стоит жить, — саморазрушение."
    },
    {
        "title": "Salò o le 120 giornate di Sodoma",
        "title_ru": "Сало, или 120 дней Содома",
        "year": 1975,
        "description": "Экранизируя роман маркиза де Сада, Пазолини переносит действие в 1944-45-е годы, в фашистскую «республику Сало» на севере Италии, где группа лиц из высшего общества во главе с принцем унижает, издевается, мучает, пытает юношей и девушек, собранных для услаждения извращённой элиты, чувствующей свою погибель. Четыре месяца длится эта экзекуция. Для взрослых это последняя возможность удовлетворить свои низменные инстинкты, для молодых людей - расплата за свою юность и желание жить."
    },
    {
        "title": "Intouchables",
        "title_ru": "1+1",
        "year": 2011,
        "description": "Пострадав в результате несчастного случая, богатый аристократ Филипп нанимает в помощники человека, который менее всего подходит для этой работы, – молодого жителя предместья Дрисса, только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений."
    },
    {
        "title": "American Psycho",
        "title_ru": "Американский психопат",
        "year": 2000,
        "description": "Днем он ничем не отличается от окружающих, и в толпе вы не обратите на него внимания. Но ночью этот благовидный гражданин превращается в изощренного убийцу."
    },
    {
        "title": "Blade Runner 2049",
        "title_ru": "Бегущий по лезвию 2049",
        "year": 2017,
        "description": "В недалеком будущем мир населен людьми и репликантами, созданными выполнять самую тяжелую работу. Работа офицера полиции Кей — держать репликантов под контролем в условиях нарастающего напряжения. Он случайно становится обладателем секретной информации, которая ставит под угрозу существование всего человечества. Желая найти ключ к разгадке, Кей решает разыскать Рика Декарда — бывшего офицера специального подразделения полиции Лос-Анджелеса, который бесследно исчез много лет назад."
    }
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    # Проверка, что id находится в допустимом диапазоне
    if id < 0 or id >= len(films):
        abort(404)  # Возвращаем ошибку 404, если id выходит за пределы
    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    # Проверка, что id находится в допустимом диапазоне
    if id < 0 or id >= len(films):
        abort(404)  # Возвращаем ошибку 404, если id выходит за пределы
    del films[id]
    return '', 204  # Возвращаем пустой ответ с кодом 204 (No Content)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    film = request.get_json()
    films[id] = film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()  # Получаем данные из запроса

    # Проверяем, что все необходимые поля присутствуют
    if not film or not all(key in film for key in ['title', 'title_ru', 'year', 'description']):
        return jsonify({"error": "Неверные данные", "description": "Все поля должны быть заполнены"}), 400

    # Если оригинальное название пустое, используем русское название
    if not film['title']:
        film['title'] = film['title_ru']

    # Проверяем, что год является числом
    if not isinstance(film['year'], int):
        return jsonify({"error": "Неверные данные", "description": "Год должен быть числом"}), 400

    # Добавляем фильм в список
    films.append(film)

    # Возвращаем ID добавленного фильма (индекс в списке)
    return jsonify({"id": len(films) - 1}), 201


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def update_film(id):
    if id >= len(films):
        return "Такого фильма нет!", 404
    film = request.get_json()
    if 'description' in film and film['description'] == '':
        return {'error': 'Заполните описание'}, 400
    films[id].update(film)
    return jsonify(films[id])