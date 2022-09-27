# whois-flask-app

stupid web app for my stupid degree

## Tech
- Python
  - Flask, Jinja2
- Tailwindcss

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