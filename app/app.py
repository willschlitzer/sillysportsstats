import flask

app = flask.Flask(__name__)


def main():
    app.run(debug=True)

@app.route("/")
@app.route("/home")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "About page"

if __name__ == "__main__":
    main()