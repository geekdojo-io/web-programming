from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/puppies')
def puppies():
    return 'Hello puppies'

@app.route('/cats')
def cats():
    return 'Hello cats'

@app.route('/search/<keyword>')
def search(keyword):
    return 'You searched {}'.format(keyword)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)