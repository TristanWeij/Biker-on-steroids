import functools

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from src.db import database

blueprint = Blueprint('customers', __name__, url_prefix='/customers')


@blueprint.get('/')
def index():
    db = database()

    customers = db.execute(
        'SELECT id, first_name, last_name FROM customers;'
    ).fetchall()

    print(customers)

    return render_template('customers/index.html', customers=customers)


@blueprint.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        error = None

        if not first_name:
            error = 'First name is required!'

        if not last_name:
            error = 'Last name is required!'

        if error is not None:
            flash(error)
        else:
            db = database()

            db.execute(
                'INSERT INTO customers (first_name, last_name)'
                ' VALUES (?, ?)',
                (first_name, last_name)
            )
            db.commit()

            return redirect(url_for('customers.index'))

    return render_template('customers/create.html')
