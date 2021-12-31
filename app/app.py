import flask
app = flask.Flask(__name__)


posts = [
    {
        'author': 'Will',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': "December 30, 2021",
    },
{
    'author': 'Will',
    'title': 'Post 2',
    'content': 'Second post content',
    'date_posted': "December 31, 2021",
},
]

def main():
    app.run(debug=True)

@app.route("/")
@app.route("/home")
def home():
    return flask.render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return flask.render_template("about.html", title="About")

if __name__ == "__main__":
    main()