from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/girassol')
def girassol():
    return render_template("girassol.html")

@app.route('/painco')
def painco():
    return render_template("painco.html")

if __name__== "__main__":
    app.run(debug=True)
