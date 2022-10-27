# SWE 266P - Bank App

Tech stack: 

- Flask
- SQLite3

## Setup Instructions

### Clone the Project

```shell
git clone https://github.com/JiayiLi1999/bankapp_group15.git
cd bankapp_group15
```

### Setup Python Virtual Environment

```shell
# MacOS/Linux
python3 -m venv venv
. venv/bin/activate
pip install Flask

# Windows
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
```

### Set Environment Variables

```shell
# Bash (MacOS/Linux)
export FLASK_APP=core
export FLASK_ENV=development

# Fish
set -x FLASK_APP core
set -x FLASK_ENV development

# CMD
set FLASK_APP=core
set FLASK_ENV=development

# Powershell
$env:FLASK_APP = "core"
$env:FLASK_ENV = "development"
```

### Initialize the Database

```shell
flask init-db
```

### Run the Application

```shell
flask run
```

Now the bank app is running on http://127.0.0.1:5000
