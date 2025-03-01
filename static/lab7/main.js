function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (data){
        return data.json();
    })
    .then(function (films){
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for(let i = 0; i < films.length; i++){
            let tr = document.createElement('tr');

            let tdTitleRus = document.createElement('td');
            let tdTitle = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            tdTitleRus.innerText = films[i].title_ru;
            tdTitle.innerHTML = films[i].title === films[i].title_ru ? '' : `<span class="original-title">(${films[i].title})</span>`;
            tdYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'Редактировать';
            editButton.onclick = function(){
                editFilm(i);
            }
            let delButton = document.createElement('button');
            delButton.innerText = 'Удалить';
            delButton.onclick = function(){
                deleteFilm(i, films[i].title_ru);
            }

            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdTitleRus);
            tr.append(tdTitle);
            tr.append(tdYear);
            tr.append(tdActions);
            
            tbody.append(tr);
        }
    });
}
function deleteFilm(id, title){
    if(! confirm(`Вы точно хотите удалить фильм "${title}"?`))
        return;

    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
        .then(function () {
            fillFilmList();
        });

}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    // Очистка полей формы
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: parseInt(document.getElementById('year').value), // Преобразуем год в число
        description: document.getElementById('description').value
    };

    const url = id === '' ? '/lab7/rest-api/films/' : `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; }); // Обрабатываем ошибку сервера
        }
        return response.json(); // Обрабатываем успешный ответ
    })
    .then(data => {
        fillFilmList(); // Обновляем список фильмов
        hideModal(); // Скрываем модальное окно
    })
    .catch(error => {
        console.error('Ошибка:', error);
        if (error.description) {
            document.getElementById('description-error').innerText = error.description;
        } else {
            alert('Не удалось добавить фильм: ' + (error.message || 'Неизвестная ошибка'));
        }
    });
}
function editFilm(id){
    fetch(`/lab7/rest-api/films/${id}`)
    .then(function (data) {
        return data.json();
    })
    .then(function (film){
        document.getElementById('id').value = id;
        document.getElementById('title').value = film.title;
        document.getElementById('title-ru').value = film.title_ru;
        document.getElementById('year').value = film.year;
        document.getElementById('description').value = film.description;
        showModal();
    })
}