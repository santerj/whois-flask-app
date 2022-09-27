# whois-flask-app

stupid web app for my stupid degree

## Tech
- [Python](https://www.python.org/)
  - [Flask](https://flask.palletsprojects.com/)
  - [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
  - [python-whois](https://pypi.org/project/python-whois/) 
- [Tailwind CSS](https://tailwindcss.com/)

## Guides
Install dependencies:

```
# python
python -m venv venv
source/venv/python -m pip install -r requirements.txt

# node
npm install
```

Build css:
```
npx tailwindcss -i src/input.css -o src/static/styles.css
```

Run app in localhost:
```
venv/bin/python src/main.py
```

Run app in production:
```
pls don't
```