import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://zulu:zuludf345@64.225.100.209/chaplin"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)