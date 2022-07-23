# Импорт модуля базы данных
# Импортируйте фреймворк Flask, этот фреймворк может быстро реализовать приложение WSGI
from flask import Flask
# По умолчанию flask ищет модули в подпапке шаблонов в папке с программой
from flask import render_template
# Импорт модуля запроса, запрошенного на стойке регистрации
# Пропустить корневой каталог
app = Flask(__name__, template_folder='templates')


# Путь по умолчанию для доступа к странице входа
@app.route('/')
def login():
    return render_template('singin.html')

# Путь по умолчанию для доступа к странице регистрации
# @app.route('/regist')
# def regist():
#     return render_template('regist.html')

if __name__ == "__main__":
    app.run()
