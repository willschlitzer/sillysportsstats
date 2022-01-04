from flask import render_template, url_for, flash, redirect
from silly_sports_stats import app
from silly_sports_stats.forms import RegistrationForm, LoginForm
from silly_sports_stats.models import User, Post



posts = [
    {
        "author": "Will",
        "title": "Post 1",
        "content": "First post content",
        "date_posted": "December 30, 2021",
    },
    {
        "author": "Will",
        "title": "Post 2",
        "content": "Second post content",
        "date_posted": "December 31, 2021",
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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check e-mail and password", "danger")
    return render_template("login.html", title="Login", form=form)