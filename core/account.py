from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from core.auth import login_required
from core.db import get_db
from core.utils import verify_amount

bp = Blueprint("account", __name__)


@bp.route('/')
def dashboard():
    db = get_db()
    accounts_send_to_html = []
    if g.user is not None:
        accounts = db.execute(
            'SELECT ba.id, balance'
            ' FROM bankAccount ba JOIN userAccount ua ON ba.userAccountId = ua.id'
            ' WHERE userAccountId = ?', (g.user['id'],)
        ).fetchall()

        for account in accounts:  # a user could have multiple bank accounts
            account_info = {'id': account['id'], 'balance': "{:.2f}".format(account['balance'])}
            accounts_send_to_html.append(account_info)

    return render_template("dashboard.html", accounts=accounts_send_to_html)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    error = None
    if request.method == 'POST':
        initial_deposit = request.form["initial_deposit"]
        db = get_db()

        # initial_deposit = float(initial_deposit)

        if not initial_deposit:
            error = 'Initial deposit required.'
        elif not verify_amount(initial_deposit):
            error = "Invalid amount."

        if error is None:
            db.execute(
                'INSERT INTO bankAccount (userAccountId, balance)'
                ' VALUES (?, ?)',
                (g.user['id'], initial_deposit)
            )
            db.commit()
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template('createAccount.html')


@bp.route('/remove/<id>', methods=('GET', 'POST'))
@login_required
def remove(id):
    db = get_db()
    db.execute('DELETE FROM bankAccount WHERE id = ?', (id))
    db.commit()
    return redirect(url_for('index'))
