from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'PPP':
        abort(404)
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/template/<name>')
def template(name):
    return render_template('user.html', name=name)

@app.route('/context')
def context():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/resp')
def response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', 42)
    return response

@app.route('/redirect')
def redirection():
    return redirect('https://www.google.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)