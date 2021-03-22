from flask import Flask, url_for, request

from random import choice

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def speech():
    return 'И на Марсе будут яблони цвести!'


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="Что-то пошло не так :(">
                    <div>Вот такая она, красная планета!</div>
                  </body>
                </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                 <html>
                   <head>
                     <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Пейзажи Марса</title>
                   </head>
                   <body>
                     <h1>Пейзажи Марса</h1>
                     <div>
                       <form class="login_form">
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename="img/frame-30_1.jpg")}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename="img/frame-5_1.jpg")}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename="img/frame-13_1.jpg")}" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
                       </form>
                     </div>
                   </body>
                 </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype>
                 <html lang="en" method="get">
                   <head>
                     <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                   </head>
                   <body>
                     <h1>Результаты отбора</h1>
                     <h2>Претендента на участие в миссии {nickname}:</h2>
                     <p>Поздравляем, ваш рейтинг после <mark>{level}</mark> отбора</p>
                     <p>составляет <u>{rating}</u></p>
                     <p><strong>Желаем удачи!</strong></p>
                   </body>
                 </html>'''


@app.route('/choice/<planet_name>')
def chs(planet_name):
    base = {
        'Марс': ['Хорошая планета', 'Реально хорошая', 'Думаю можно слетать'],
        'Венера': ['Гулял я по ней уже', 'Желтовая больно', 'Не знаю, что еще написать']
    }

    exc = ['Нечего сказать', 'Есть плюсы и минусы', 'Давайте дальше уже...']

    group = ''.join(map(lambda it: f'<li class="list-group-item">{it}</li>', base.get(planet_name, exc)))
    return f'''<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                   </head>
                   <body>
                     <h1>Мое предложение: {planet_name}</h1>
                     <ul class="list-group list-group-flush">
                       {group}
                     </ul>
                   </body>
                 </html>'''


@app.route('/promotion_image')
def pr_img():
    keywords = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!']

    colors = [
        'primary',
        'secondary',
        'dark',
        'danger',
        'warning',
        'info',
        'success'
    ]

    lines = ' '.join(map(lambda ln: f'<div class="alert alert-{choice(colors)}" role="alert">{ln}</div>',
                         keywords))

    return f'''<!doctype html>
               <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename="img/mars.jpg")}" alt=""Auch>
                    {lines}
                  </body>'''


@app.route('/promotion')
def promotion():
    keywords = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(keywords)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
      <img src="{url_for('static', filename="img/frame-30_1.jpg")}" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename="img/frame-5_1.jpg")}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename="img/mars.jpg")}" class="d-block w-100" alt="...">
    </div>
  </div>
</div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=6363, host='127.0.0.1')
