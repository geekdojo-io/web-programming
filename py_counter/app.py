from flask import Flask
app = Flask(__name__)

counter = 0

@app.route("/")
def home():
    global counter
    counter += 1
    return str(counter)

if __name__ == '__main__':
    app.run()