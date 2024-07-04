DEBUG = True

USERNAME = 'root'
PASSWORD = 'mk875'
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
