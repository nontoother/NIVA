import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from core.db import get_db
from core.utils import verify_user_login_info

bp = Blueprint("auth", __name__)


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from the database into ``g.user``."""
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM userAccount WHERE id = ?", (user_id,)).fetchone()
        )


@bp.route("/register", methods=["GET", "POST"])
def register():
    print(request.method)
    """Register a new user. Validates that the username is not already taken. Hashes the password for security."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        ssn = request.form["ssn"]
        phone_number = request.form["phone_number"]
        address = request.form["address"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not verify_user_login_info(username):
            error = "Invalid username. (Restricted to '_', '-', '.', digits, and lowercase alphabetical characters)"
        elif not password:
            error = "Password is required."
        elif not verify_user_login_info(password):
            error = "Invalid password. (Restricted to '_', '-', '.', digits, and lowercase alphabetical characters)"
        elif not first_name:
            error = 'First name required.'
        elif not last_name:
            error = 'Last name required.'
        elif not ssn.isnumeric():
            error = 'Invalid SSN.'
        elif not phone_number.isnumeric():
            error = 'Invalid phone number.'
        elif not address:
            error = 'Address required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO userAccount (username, password, firstName, lastName, SSN, phoneNumber, address) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (username, generate_password_hash(password),
                     first_name, last_name, ssn, phone_number, address),
                )
                db.commit()

            except db.IntegrityError:
                # The username was already taken, which caused the commit to fail. Show a validation error.
                error = f"User {username} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("register.html")


@ bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        target = request.args.get('target')
        if target is not None:
            return redirect(target)
        request_username = request.form["username"]
        request_password = request.form["password"]

        db = get_db()
        error = None

        ''' BAD CODE START ======================================================

        sql_query = "SELECT * FROM userAccount WHERE username = '" + \
            request_username + "' and password='" + request_password + "'"
        user = db.execute(
            sql_query,
        ).fetchone()

        BAD CODE END   =========================================================='''

        user = db.execute(
            "SELECT * FROM userAccount WHERE username = ?", (request_username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], request_password):
            error = "Incorrect password."

        if user is None:
            error = "Incorrect login information."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("login.html")


@ bp.route("/resetPwd", methods=("GET", "POST"))
def reset():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        request_username = request.form["username"]
        request_ssn = request.form["ssn"]
        request_password = request.form["password"]
        re_request_password = request.form["repassword"]

        db = get_db()
        error = None
        if (request_password != re_request_password):
            error = "Different Passwords"
        else:
            user = db.execute(
                "SELECT * FROM userAccount WHERE username = ? AND ssn = ?",
                (request_username,request_ssn)
            ).fetchone()

            if user is None:
                error = "Incorrect User Info."
            else:
                try:
                    db.execute(
                        "UPDATE userAccount SET password = ? WHERE username =?", (generate_password_hash(
                            request_password), request_username,)
                    )
                    db.commit()
                except db.Error as e:
                    # The username was already taken, which caused the commit to fail. Show a validation error.
                    error = "error"
                else:
                    # Success, go to the login page.
                    return redirect(url_for("auth.login"))

        flash(error)

    return render_template("resetPwd.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("auth.login"))
