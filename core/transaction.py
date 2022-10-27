from flask import Blueprint, render_template
from flask import flash
from flask import redirect
from flask import request
from flask import url_for

from core.auth import login_required
from core.db import get_db
from core.utils import verify_amount, get_bank_account

bp = Blueprint("transaction", __name__)


@bp.route('/deposit/<id>', methods=('GET', 'POST'))
@login_required
def deposit(id):
    error = None
    bank_account = get_bank_account(id)

    if request.method == 'POST':
        deposit_amount = request.form["deposit_amount"]
        if not deposit_amount:
            error = "Deposit amount is required."
        elif not verify_amount(deposit_amount):
            error = "Invalid deposit amount."
        update_balance = bank_account['balance'] + float(deposit_amount)

        if error is None:
            db = get_db()
            db.execute(
                'UPDATE bankAccount SET balance = ?'
                ' WHERE id = ?',
                (update_balance, id)
            )
            db.commit()
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template('deposit.html', account=bank_account)


@bp.route('/withdraw/<id>', methods=('GET', 'POST'))
@login_required
def withdraw(id):
    error = None
    bank_account = get_bank_account(id)

    if request.method == 'POST':
        withdraw_amount = request.form["withdraw_amount"]
        if not withdraw_amount:
            error = "Withdraw amount is required."
        elif not verify_amount(withdraw_amount):
            error = "Invalid withdraw amount."
        update_balance = bank_account['balance'] - float(withdraw_amount)

        if update_balance < 0:
            error = "Cannot withdraw, not enough balance."

        if error is None:
            db = get_db()
            db.execute(
                'UPDATE bankAccount SET balance = ?'
                ' WHERE id = ?',
                (update_balance, id)
            )
            db.commit()
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template('withdraw.html', account=bank_account)
