from app import db

class Favoritos(db.Model):
    favoritos_id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'))
    cerveza_id = db.Column(db.Integer, db.ForeignKey('cerveza.cerveza_id'))

    cliente = db.relationship('Cliente',backref=db.backref('favoritos',lazy=True))
    cerveza = db.relationship('Cerveza', backref=db.backref('favoritos', lazy=True))