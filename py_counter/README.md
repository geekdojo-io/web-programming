### Counter app using Python / Flask
Let's build a web site that counts number of visits using Flask, a simple Pythonweb server. 

1. Open Terminal
```
pwd # Find your present working directtory.
pwd # View the list of the current directory.
mkdir SourceControl # Create a "SourceControl" directory.
cd SourceControl
ls
mkdir py_counter
cd py_counter
code .
touch app.py
```

2. Run Flask
```
pip install Flask --user
flask run
```
3. Test the app
- Open web browser and go to `http://127.0.0.1:5000`
- Find your IP address by typing `ifconfig | grep --inet`
- Open a web browser from your Window (host computer).
- Type `http://[the_ip_address_of_linux]:5000` (It doesn't work)
- From Linux, press <kbd>Ctrl+C</kbd> to kill the Flask.
- Type `flask run --host=0.0.0.0`
- Open a web browser from your Window again to verify it works.
