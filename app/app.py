from flask import Flask, render_template, url_for
app = Flask(__name__)


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
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    main()