from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/caseiro')
def caseiro():
    return render_template("caseiro.html")