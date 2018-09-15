### Hello World for Flask
Simple Flask app for displaying 'Hello World'.

#### Pre-requisite
If Flask is not installed yet, run the following command from Terminal:
```
pip install flask
```

#### How to run the app
To run, from Terminal, type:
```
python app.py
```
Then, open a web browser, and go to `http://127.0.0.1:5000`.

---

Alternatively, you can completely remove the following lines of code:
```
if __name__ == '__main__':
    app.run()
```
, rename hello.py to app.py, and then run the following command from Terminal:

```
flask run
```
Then, open a web browser, and go to `http://127.0.0.1:5000`.

From Terminal, press <kbd>Ctrl+C</kbd> to kill the Flask app.