from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

GLOBAL_AUTHORIZE = 0

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form["search-data"])
    return render_template("main.html", is_authorized=GLOBAL_AUTHORIZE)

@app.route('/hero-search', methods=["GET", "POST"])
def hero_search():
    if request.method == "POST":
        print(request.form['input-name'])
    return render_template("hero-search.html", is_authorized=GLOBAL_AUTHORIZE)

@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        print(request.form)
    return render_template("contacts.html", is_authorized=GLOBAL_AUTHORIZE)

@app.route('/full_search', methods=["GET", "POST"])
def full_search():
    if request.method == "POST":
        print(request.form)
    return render_template("full-search.html", is_authorized=GLOBAL_AUTHORIZE)

@app.route('/send_data', methods=["GET", "POST"])
def send_data():
    if request.method == "POST":
        print(request.form)
    return render_template("send-data.html", is_authorized=GLOBAL_AUTHORIZE)

@app.route('/authorization', methods=["GET", "POST"])
def authorize():
    global GLOBAL_AUTHORIZE
    if request.method == "POST":
        GLOBAL_AUTHORIZE = 1
    return render_template("authorization.html", is_authorized=GLOBAL_AUTHORIZE)

if __name__ == '__main__':
    app.run()