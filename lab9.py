from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

# Шаг 1 - Ввод имени
@lab9.route('/lab9/', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('lab9.age', username=username))
    return render_template('lab9/step1.html')


# Шаг 2 - Ввод возраста
@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    username = request.args.get('username')
    if request.method == 'POST':
        age = request.form['age']
        return redirect(url_for('lab9.gender', username=username, age=age))
    return render_template('lab9/step2.html', username=username)


# Шаг 3 - Выбор пола
@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    username = request.args.get('username')
    age = request.args.get('age')
    if request.method == 'POST':
        gender = request.form['gender']
        return redirect(url_for('lab9.preferences', username=username, age=age, gender=gender))
    return render_template('lab9/step3.html', username=username, age=age)


# Шаг 4 - Выбор предпочтений
@lab9.route('/lab9/preferences', methods=['GET', 'POST'])
def preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if request.method == 'POST':
        preference = request.form['preference']
        return redirect(url_for('lab9.subpreference', username=username, age=age, gender=gender, preference=preference))
    return render_template('lab9/step4.html', username=username, age=age, gender=gender)


# Шаг 5 - Выбор подкатегории предпочтений
@lab9.route('/lab9/subpreferences', methods=['GET', 'POST'])
def subpreference():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference = request.args.get('preference')
    if request.method == 'POST':
        subpreference = request.form['subpreference']
        return redirect(url_for('lab9.congratulations', username=username, age=age, gender=gender, preference=preference, subpreference=subpreference))
    return render_template('lab9/step5.html', username=username, age=age, gender=gender, preference=preference)


# Шаг 6 - Поздравление
@lab9.route('/lab9/congratulations', methods=['GET'])
def congratulations():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference = request.args.get('preference')
    subpreference = request.args.get('subpreference')

    # Логирование значений для отладки
    print(f"Username: {username}, Age: {age}, Gender: {gender}, Preference: {preference}, Subpreference: {subpreference}")

    # Проверяем, что все параметры получены корректно
    if not username or not age or not gender or not preference or not subpreference:
        print("Ошибка: отсутствуют необходимые параметры")
        return "Ошибка: отсутствуют необходимые параметры", 400

    # Формируем поздравление и выбираем картинку
    if gender == 'male':
        if age.isdigit() and int(age) < 18:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы ты быстро вырос, был умным..."
        else:
            greeting = f"Поздравляю тебя, {username}, желаю успехов и удачи в жизни!"

        if preference == 'tasty' and subpreference == 'sweet':
            image = url_for('static', filename='lab9/candies.jpg')  # Картинка с конфетами
            gift = "Вот тебе подарок — мешочек конфет!"
        elif preference == 'tasty' and subpreference == 'savory':
            image = url_for('static', filename='lab9/savory.jpg')  # Картинка с чем-то сытным
            gift = "Вот тебе подарок — порция сытного угощения!"
        else:
            image = url_for('static', filename='lab9/cake.jpg')  # Картинка с тортиком
            gift = "Вот тебе подарок — вкусный тортик!"

    else:  # для женщин
        if age.isdigit() and int(age) < 18:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы ты быстро выросла, была умной..."
        else:
            greeting = f"Поздравляю тебя, {username}, желаю успехов и удачи в жизни!"

        if preference == 'tasty' and subpreference == 'sweet':
            image = url_for('static', filename='lab9/candies.jpg')  # Картинка с конфетами
            gift = "Вот тебе подарок — мешочек конфет!"
        elif preference == 'tasty' and subpreference == 'savory':
            image = url_for('static', filename='lab9/savory.jpg')  # Картинка с чем-то сытным
            gift = "Вот тебе подарок — порция  угощения!"
        else:
            image = url_for('static', filename='lab9/kitten.jpg')  # Картинка с котиками
            gift = "Вот тебе подарок — прекрасные котики!"

    return render_template('lab9/step6.html', greeting=greeting, gift=gift, image=image)