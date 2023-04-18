from flask import Flask, render_template
 
from BullytingDetector import ApiClient
 
app = Flask(__name__)
 
app.config["api"] = ApiClient('localhost:9091')
 
 
@app.route("/")
def home():
    api = app.config["api"]
    return render_template(
        "index.html",
        name=api.detectComment("fuck you bitch, you are such a bitch idot!")

    )