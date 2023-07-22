from app import db

class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    user_name = db.Column(db.String)
    password = db.Column(db.String)

    encuestas = db.relationship('Encuesta', back_populates='cliente')
    favoritos = db.relationship('Favoritos', back_populates='cliente')

    def to_dict(self):
        cliente_dict = {
            "cliente_id" : self.cliente_id,
            "nombre": self.nombre,
            "user_name" : self.user_name,
            "password" : self.password,
        }

        return cliente_dict
    
    @classmethod
    def from_dict(cls, cliente_data):
        new_cliente = Cliente(nombre=cliente_data["nombre"],
                            user_name=cliente_data["user_name"],
                            password=cliente_data["password"])
        return new_cliente