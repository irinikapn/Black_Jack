from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CARD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10))
    type = db.Column(db.String(15))
    
