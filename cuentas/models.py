from application import db

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)