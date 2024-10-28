import os

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from main import app

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orin_name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(80), unique=True, nullable=False)
    durration = db.Column(db.Integer)  # minutes
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
   

    def __repr__(self):
        return f'<Student {self.orin_name}>'