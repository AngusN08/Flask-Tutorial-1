from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    html = """
        <h1>Welcome to my home page</h1>
        <p>Click the link below to navigate</p>
        <a href="/about">Go to about page</a>
    """

    return html


@app.route("/about")
def about():
    html = """
        <h1>Welcome to my about page</h1>
        <p>I'm an epic coder</p>
        <a href="/">Go to home page</a>
    """

    return html


app.run(debug=True, port=5000)
