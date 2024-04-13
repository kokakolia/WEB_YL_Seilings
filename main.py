from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def about():
    return open('static/templates/about.html', encoding='utf8')


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
