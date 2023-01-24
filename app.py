from flask import Flask , request , render_template
app = Flask(__name__)

@app.get("/fizzbuzz")
def practice():
    return render_template("index.html")