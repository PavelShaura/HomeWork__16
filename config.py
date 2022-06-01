import os.path


DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'test.db')
FIXTURE_BASE_DIR = 'fixtures'


class Config:
    # ORM settings
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Fixtures themselves
    USER_ROLES_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'user_roles.json')
    USER_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'users.json')
    ORDERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'orders.json')
    OFFERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'offers.json')