from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', encoding='utf8')


@app.route('/reviews')
def reviews():
    reviews = [{'images': [
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
        'text': 'YYYYeeeee haaaAaaaa'}, {'images': [
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
        'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'}, {'images': [],
                                                                                      'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'},
        {'images': [
            'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
            'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'}]
    return render_template('reviews.html', encoding='utf8', reviews=reviews)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
