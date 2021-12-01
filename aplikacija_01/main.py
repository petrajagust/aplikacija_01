#Python flask aplikacija

from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/o_nama")
def O_nama():
    return "Ovo je stranica o nama!"

if __name__ == "__main__":
    app.run(use_reloader=True)

