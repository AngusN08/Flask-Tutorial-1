from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    today = datetime.now().strftime("%Y-%m-%d %H: %M: %S")

    html = f"""
        <!doctype html>
        <html>
        <head>
            <title>Clock</title>
        </head>
        <body>
            <h1>Welcome to my clock</h1>
            <p>The current date and time is {today}</p>
        </body>
        </html>
    """
    return html


app.run(debug=True, port=5000)
