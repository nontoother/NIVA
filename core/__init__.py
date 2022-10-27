import os
from flask import Flask
from core import auth, transaction, account  # apply the blueprints to the app
from core import db  # register the database commands


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,template_folder='../templates',static_folder="../static")
    app.config.from_mapping(
        SECRET_KEY="dev",  # a default secret that should be overridden by instance config
        DATABASE=os.path.join(app.instance_path, "bank_database.sqlite"),  # store the database in the instance folder
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)  # load the instance config, if it exists, when not testing
    else:
        app.config.update(test_config)  # load the test config if passed in

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(transaction.bp)

    app.add_url_rule("/", endpoint="index")

    return app
