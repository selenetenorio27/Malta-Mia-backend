from app import db

class Sabor(db.Model):
    sabor_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    
    cervezas = db.relationship('Cerveza', secondary='cerveza_sabor', back_populates='sabores')

# Tabla intermedia para la relación muchos a muchos entre Cerveza y Sabor
cerveza_sabor = db.Table('cerveza_sabor',
    db.Column('cerveza_id', db.Integer, db.ForeignKey('cerveza.cerveza_id'), primary_key=True),
    db.Column('sabor_id', db.Integer, db.ForeignKey('sabor.sabor_id'), primary_key=True)
)