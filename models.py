"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    '''User'''

    __tablename__ = "cupcake"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
                    
    flavor = db.Column(db.String(50), nullable=False, unique=False)

    size = db.Column(db.String(50), nullable=False, unique=False)

    rating = db.Column(db.Integer(), nullable=False)
    
    image = db.Column(db.String(350), nullable=False, default="https://tinyurl.com/demo-cupcake")