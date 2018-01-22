# Polling App

This is a demo app for polling users on random questions. 

## Running locally

Server is using MySQL and is written in Python and uses Flask framework. You'll need to install MySQL, Python, pip and Python Virtual Environemt:

### MySQL

Use `brew` in Mac to install MySQL:

```bash
brew install mysql
```

### Python
**Python 3** is required. 

```bash
# make sure you have Python 3
python3 --version
```
### PIP

```bash
# make sure pip3 is installed
pip3 --version

# install pip3 otherwise
python3 -m pip --version
```

### Virtual Environment (`virtualenv`)

```bash
# make sure virtualenv is installed 
python3 -m pip install --user virtualenv
```

### Activate virtual environment

```bash
source env/bin/activate
```

### Install dependencies
```bash
(venv) pip3 install -r requirements.txt
```

### Start MySQL database

```bash
mysql.server start
```

### Start the app 

```bash
FLASK_APP=app/__init__.py flask run
```

#### VSCode
If you are using Microsoft Visual Studio Code you can use the IDE debugger to start the app as well. Launch the `Flask` task to start the app.
