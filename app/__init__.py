import os
from flask import (
    Flask,
    render_template,
    send_from_directory,
    json,
    request,
    flash,
    redirect,
    session,
    url_for,
    logging,
)
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from app.db import get_db

# from . import auth

load_dotenv()

# Init App
app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")
# Init db
db.init_app(app)
# app.register_blueprint(auth.bp)

# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return render_template("health.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (
            db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone()
            is not None
        ):
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # session.clear()
            # session["user_id"] = user["id"]
            # return redirect(url_for("index"))
            return "Login Successful", 200
        else:
            return error, 418
    return render_template("login.html")
