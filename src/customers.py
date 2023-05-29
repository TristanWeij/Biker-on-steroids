from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from src.db import database

blueprint = Blueprint("customers", __name__, url_prefix="/customers")


@blueprint.get("/")
def index():
    customers = (
        database()
        .execute("SELECT id, first_name, last_name, email FROM customers;")
        .fetchall()
    )

    return render_template("customers/index.html", customers=customers)


@blueprint.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        error = None

        if not first_name:
            error = "First name is required!"

        if not last_name:
            error = "Last name is required!"

        if not email:
            error = "Email is required!"

        if error is not None:
            flash(error)
        else:
            database().execute(
                "INSERT INTO customers (first_name, last_name, email)"
                " VALUES (?, ?, ?)",
                (first_name, last_name, email),
            )
            database().commit()

            return redirect(url_for("customers.index"))

    return render_template("customers/create.html")


@blueprint.post("/<int:identifier>/delete")
def delete(identifier):
    customer = (
        database()
        .execute("SELECT * FROM customers WHERE id = ?;", (identifier,))
        .fetchone()
    )

    if customer is None:
        abort(404, f"Customer doesn't exist.")

    database().execute("DELETE FROM customers WHERE id = ?", (identifier,))
    database().commit()

    return redirect(url_for("customers.index"))
