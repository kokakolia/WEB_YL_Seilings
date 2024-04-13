from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')


@app.route('/')
@app.route('/about')
def about():
    return open('static/templates/about.html', encoding='utf8')


@app.route('/reviews')
def reviews():
    reviews = ['1', '2']
    return render_template('reviews.html', encoding='utf8', reviews=reviews)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
