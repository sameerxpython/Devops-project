from flask import Flask

app = Flask(__name__)
@app.route("/info")
def lwinfo():
    return "i am lw from india"
@app.route("/phone")
def lwphone():
    return "8302666102"
app.run(host="0.0.0.0")