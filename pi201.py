from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return('Я люблю питон')


@app.route('/help/')
def hel():
    return '<h1>Скорая помощь выехала</h1>'


@app.route('/lol/')
def lo():
    return '<h1>внимание, анекдот</h1>'

if __name__ == '__main__':
    app.run(debug=True)