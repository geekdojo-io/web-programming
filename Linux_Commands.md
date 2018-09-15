
# Linux commands
### Brief list of linux commands
| Command  | Description  | Example |
|---|---|---|
| `mkdir`  | Make directory   | `$ mkdir py_hello` |
| `pwd`    | Display the current directory | `$ pwd` |
| `ls`     | List files in the current directory | `$ ls` |
| `cd`     | Create a directory | `$ cd home` |
| `touch`  | Create an empty file if it doesn't exist. | `$ touch hello.py` |

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

#### Examples of Creating a new Flask project
Open the Terminal.
Verify that you are on the home directory.
```
$ pwd
```
Go to the SourceControl directory
```
$ cd SourceControl
```
Create a new project directory, 'my_project'
```
$ mkdir my_project
```
Go to the new directory.
```
$ cd my_project
```
Install Flask
```
pip install flask --user
```
Create 'app.py' file.
```
touch app.py
```
Launch the Visual Studio Code
```
code .
```