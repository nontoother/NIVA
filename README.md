# SWE 276P - Capstone Project
## Non-human Intelligent Virtual Assistant

Tech stack: 
- Flask
- React
- NLP

## Setup Instructions

### Clone the Project

```shell
git clone https://github.com/nontoother/NIVA.git
cd NIVA
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
export FLASK_APP=backend/base.py
export FLASK_ENV=development

# Fish
set -x FLASK_APP backend/base.py
set -x FLASK_ENV development

# CMD
set FLASK_APP=backend/base.py
set FLASK_ENV=development

# Powershell
$env:FLASK_APP = "backend/base.py"
$env:FLASK_ENV = "development"
```
### Initialize the NPM
```
npm install
```

### Initialize the Backend

```
npm run start-backend
```

### Run the Application

```
npm start
```

Now the bank app is running on http://localhost:3000
the backend is at http://127.0.0.1:5000/
