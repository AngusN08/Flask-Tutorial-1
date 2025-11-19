from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def Home():
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", name=nameValue, time=timeValue)


app.run(debug=True, port=5000)
