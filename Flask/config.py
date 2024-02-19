import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql+psycopg2',
        # SGBD = 'mysql+mysqlconnector',
        usuario = 'postgres',
        senha = 'root',
        servidor = 'localhost:5433',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'