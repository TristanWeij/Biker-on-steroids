import functools

from flask import Blueprint, render_template

blueprint = Blueprint('customers', __name__, url_prefix='/customers')


@blueprint.route('/')
def index():
    return render_template('customers/index.html')
