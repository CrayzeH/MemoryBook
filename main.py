from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

GLOBAL_AUTHORIZE = 0

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form["search-data"])
    return render_template("main.html")

if __name__ == '__main__':
    app.run()