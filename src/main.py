import re

import whois

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/whois")
def returnWhoisData():
    domain = request.args.get('domain')
    if not regexMatch(domain):
        return render_template("error.html", error="Invalid domain")
    else:
        data = whoisData(domain)
        return render_template("whois.html", data=data)


def whoisData(domain: str) -> dict:
    timeFormat = "%-d %B %Y %X %Z"
    data = {
        "Domain": domain,
        "Creation date": "Not Found",
        "Expiration date": "Not Found"
    }
    w = whois.whois(domain)
    createDate = w.creation_date
    expireDate = w.expiration_date

    if createDate:
        if type(createDate) == list:
            createDate = createDate[0]
        data["Creation date"] = createDate.strftime(timeFormat)

    if expireDate:
        if type(expireDate) == list:
            expireDate = expireDate[0]
        data["Expiration date"] = expireDate.strftime(timeFormat)
    
    return data


def regexMatch(domain: str) -> bool:
    pattern = "^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$"
    result = re.match(pattern, domain)
    return True if result else False

if __name__ == '__main__':
	app.run(debug=True)
