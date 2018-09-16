from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home'

@app.route('/hello')
def hello_index():
    return 'Hello, World'

@app.route('/bye')
def bye():
    return 'Bye bye!'

@app.route('/puppies')
def puppies():
    return 'Hello puppies'

@app.route('/cats')
def cats():
    return 'Hello cats'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, my name is {}'.format(name)

@app.route('/search/<keyword>')
def search(keyword):
    return 'You searched {}'.format(keyword)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)