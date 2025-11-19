from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    html = """
        <!doctype html>
        <html>
        <head>
            <title>My styled page</title>
            <link rel="stylesheet" type="text/css" href="/static/css/style.css">
        </head>
        <body>
            <h1>Welcome to my stylish page</h1>
            <p>This should look nice</p>
            <p>All made with Flask</p>
            <img src="/static/images/Flask_logo.svg" alt="Flask logo">
        </body>
        </html>
    """

    return html


app.run(debug=True, port=5000)
