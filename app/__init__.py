from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app import routes

        db.drop_all()
        db.create_all()

        from app import migrate

        migrate.migrate_user_roles(app.config['USER_ROLES_FIXTURE_PATH'])
        migrate.migrate_users(app.config['USER_FIXTURE_PATH'])
        migrate.migrate_orders(app.config['ORDERS_FIXTURE_PATH'])
        migrate.migrate_offers(app.config['OFFERS_FIXTURE_PATH'])

        return app




