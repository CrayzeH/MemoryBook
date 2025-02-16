from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

GLOBAL_AUTHORIZE = 0

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form["search-data"])
    return render_template("main.html")

@app.route('/hero-search', methods=["GET", "POST"])
def hero_search():
    if request.method == "POST":
        print(request.form['input-name'])
    return render_template("hero-search.html")

@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        print(request.form)
    return render_template("contacts.html")

@app.route('/full_search', methods=["GET", "POST"])
def full_search():
    if request.method == "POST":
        print(request.form)
    return render_template("full-search.html")

@app.route('/send_data', methods=["GET", "POST"])
def send_data():
    if request.method == "POST":
        print(request.form)
    return render_template("send-data.html")

if __name__ == '__main__':
    app.run()