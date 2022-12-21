from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
 
 
@app.route("/")
def run_app():
    return render_template("base.html")
 
 
app.run()