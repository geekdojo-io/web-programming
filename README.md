# Web Programming Course

## Curriculum
At high-level, this course follows the following curriculum: 
1. Learn how computer network, Internet and World Wide Web work.
2. Learn Linux and use it in VirtualBox
3. Learn the Python Flask programming
4. Learn Git and GitHub
5. Use Google App Engine (GAE) to deploy your code to Internet
6. Learn Node.js / Express

![alt text](images/curriculum.png)
*High-level overview of this course*

---

## Week 1 - Introduction to Network & History of Internet

- Homework: Write a research paper about what happens when you type an URL (example: www.google.com) in a web browser and press enter.

---

## Week 2 - Introduction to Network & History of Internet (Cont.)

- Homework: Write a research paper on an IP address. Topics should cover:
    - What is IP address (IPv4)?
    - What is subnetting?
    - What are private addresses?
    - What is a dynamic IP address?
    - What is port 53 used for?

---

## Week 3 & Week 4 - Python / Flask Programming with Http Request and Response

### Linux commands
#### Brief list of linux commands
| Command  | Description  | Example |
|---|---|---|
| `mkdir`  | Make directory   | `$ mkdir py_hello` |
| `pwd`    | Display the current directory | `$ pwd` |
| `ls`     | List files in the current directory | `$ ls` |
| `cd`     | Create a directory | `$ cd home` |
| `touch`  | Create an empty file if it doesn't exist. | `$ touch hello.py` |

---

### Examples of CD (Change Directory)
Go to a home directory
```
$ cd ~ 
```

Go to the SourceControl directory
```
$ cd SourceControl 
```
Move up to a parent directory (..)
```
$ cd .. 
```

Go to the root directory (/)
```
$ cd / 
``` 

---

### Flask Web Server
Flask is a simple yet powerful Python web server.
![alt text](images/ws_flask.png)


### 'Hello World' project
Open the Terminal.
Verify that you are on the home directory.
```
$ pwd
```
Go to the SourceControl directory.
```
$ cd SourceControl
```
Create a new project directory, 'py_hello'.
```
$ mkdir py_hello
```
Go to the py_hello directory.
```
$ cd py_hello
```
Install Flask.
```
$ pip install flask --user
```
Create 'app.py' file.
```
$ touch app.py.
```
Launch the Visual Studio Code.
```
$ code .
```

Type the following lines of code in the app.py using the Visual Studio Code editor.
![alt text](images/py_hello.png)


From the Terminal, run $`python app.py`.
```
$ python app.py
```

Then, open a web browser from the VM, and type `http://127.0.0.1:5000` to verify that your program is working.

Find the IP address for your VM using the following command:
```
$ ifconfig | grep inet
```

Then, from your host (Windows), open a web browser, and type the address (Example: `http://192.168.2.101:5000`), and verify that you cannot access the app. This is because the app only allows the local connection. This diagram illustrates that:
![alt text](images/flask_access0.png)

From the Terminal, press <kbd>Ctrl+C</kbd> to kill the app.

#### Quiz

- Create `flask_quiz1` directory under the `SourceControl` directory, and create a Flask app that returns your name. Verify that it works.

### 'Hello World' project (Part 2)

To allows the access outside your VM and debugging, change Line 9 to the following:

```python
app.run(host="0.0.0.0", port="5000", debug=True)
```

So, the changed code should look like this:
![alt text](images/py_hello2.png)


From the Terminal, run $`python app.py`.

```shell
$ python app.py
```

Then, open a web browser from the VM, and type `http://127.0.0.1:5000` to verify that your program is working.

From your host (Windows), open a web browser, and type the address (Example: `http://192.168.2.101:5000`), and verify that you can access the app. This diagram illustrates that:
![alt text](images/flask_access1.png)

From the Terminal, press <kbd>Ctrl+C</kbd> to kill the app.


#### Quiz

- Create `flask_quiz2` directory under the `SourceControl` directory, and create a Flask app that returns your name. Access the website from your Windows machine. Verify that it works.

---


### Routing
Use `@app.route()` to bind a function to a specific URL path.

#### Basic routing

![alt text](images/py_basic_routing.png)


#### Quiz

- Create `flask_quiz3` directory under the `SourceControl` directory, and copy the code inside app.py from [003_py_counter](003_py_counter/) example. Add `/reset` path which binds to a `reset()` method which resets the counter to `0`.

#### Dynamic routing
You can make the URL path dynamic by accepting a `<name>`, and pass the `name` variable as an input parameter to the method bound to the route. Here is an example:
![alt text](images/py_dynamic_routing.png)

#### Quiz
- Enhance the `flask_quiz3` by creating a path `/set/<new_counter>` which binds to a `set(new_counter)` method which sets the counter to the `new_counter` variable if the `new_counter` is an unsigned integer (non-negative integer).

---

## Python App Examples

| Code  | Type | Examples  | 
|---|---|---|
|[000_py_google](000_py_google/) | Client | Build a simple client to get HTML from a web site |
|[001_py_slack](001_py_slack/) | Client | Build a slack client to post a message in a Slack |
| [002_py_hello](002_py_hello/) | Server | Build a simple web application that displays 'Hello World' using `Flask` |
| [003_py_counter](003_py_counter/) | Server | Build a simple counter web application using `Flask` |
| [004_py_routes](004_py_routes/) | Server | Build a web app with multiple routes |
| [005_py_requirements](005_py_requirements/) | Server | Use Requirements.txt for dependencty management |