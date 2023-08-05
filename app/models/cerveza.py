from app import db


class Cerveza(db.Model):
    cerveza_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    marca = db.Column(db.String)
    porcentaje_alcohol = db.Column(db.Float)
    estilo = db.Column(db.String)
    ibus = db.Column(db.Integer)
    color = db.Column(db.String)
    sabor = db.Column(db.String)
    ingrediente_adicional = db.Column(db.String)


    favoritos = db.relationship('Favoritos', back_populates='cerveza')


    def to_dict(self):
        cerveza_dict = {
            "cerveza_id" : self.cerveza_id,
            "nombre" : self.nombre,
            "marca" : self.marca,
            "porcentaje_alcohol" : self.porcentaje_alcohol,
            "estilo" : self.estilo,
            "ibus" : self.ibus,
            "color" : self.color,
            "sabor" : self.sabor,
            "ingrediente_adicional": self.ingrediente_adicional
        }

        return cerveza_dict
    
    @classmethod
    def from_dict(cls, cerveza_data):
        new_cerveza = Cerveza(nombre=cerveza_data["nombre"],
                            marca=cerveza_data["marca"],
                            porcentaje_alcohol=cerveza_data["porcentaje_alcohol"],
                            estilo=cerveza_data["estilo"],
                            ibus=cerveza_data["ibus"],
                            color=cerveza_data["color"],
                            sabor=cerveza_data["sabor"],
                            ingrediente_adicional=cerveza_data["ingrediente_adicional"])
        return new_cerveza
    


