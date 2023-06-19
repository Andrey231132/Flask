from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
@app.route('/')
def hello():
    return render_template("index.html")

