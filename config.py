import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
migrate = Migrate()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:@localhost:3306/exam_richi')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'hola')  # Cambia esto!
    PROPAGATE_EXCEPTIONS = True