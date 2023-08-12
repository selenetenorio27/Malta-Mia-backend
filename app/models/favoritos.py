from app import db

class Favoritos(db.Model):
    favoritos_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.String)
    cerveza_id = db.Column(db.Integer, db.ForeignKey('cerveza.cerveza_id'))

    cerveza = db.relationship('Cerveza', back_populates='favoritos')

