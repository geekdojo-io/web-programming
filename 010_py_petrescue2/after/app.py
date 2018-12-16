from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/dogs')
def dogs():
    return render_template('dogs.html')

@app.route('/adopted')
def adopted():
    return render_template('adopted.html')

@app.route('/application')
def application():
    return render_template('application.html')

@app.route('/specials')
def specials():
    return render_template('specials.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')    

if __name__ == '__main__':
    app.run(debug=True)