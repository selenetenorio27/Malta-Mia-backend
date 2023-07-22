from sqlalchemy import DateTime
from app import db

class Encuesta(db.Model):
    encuesta_id = db.Column(db.Integer, primary_key=True)
    consumo_previo = db.Column(db.Boolean)
    pref_estilo = db.Column(db.String)
    gusta_amarga = db.Column(db.Boolean)
    pref_sabor = db.Column(db.String)
    pref_alcohol = db.Column(db.Integer)
    ingrediente_adic = db.Column(db.String)
    completed_at = db.Column(db.DateTime, default=None)

    # cerveza_id = db.Column(db.Integer, db.ForeignKey('cerveza.cerveza_id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'))

    cliente = db.relationship('Cliente', back_populates='encuestas')
    # cerveza = db.relationship('Cerveza', back_populates='encuesta')

#falta fecha 

    def to_dict(self):
        encuesta_dict = {
            "encuesta_id" : self.encuesta_id,
            "consumo_previo" : self.consumo_previo,
            "pref_estilo" : self.pref_estilo,
            "gusta_amarga" : self.gusta_amarga,
            "pref_sabor" : self.pref_sabor,
            "pref_alcohol" : self.pref_alcohol,
            "ingrediente_adic" : self.ingrediente_adic,
            "completed_at" : self.completed_at
        }

        return encuesta_dict
    
    @classmethod
    def from_dict(cls, encuesta_data):
        new_encuesta = Encuesta(consumo_previo=encuesta_data["consumo_previo"],
                                pref_estilo=encuesta_data["pref_estilo"],
                                gusta_amarga=encuesta_data["gusta_amarga"],
                                pref_sabor=encuesta_data["pref_sabor"],
                                pref_alcohol=encuesta_data["pref_alcohol"],
                                completed_at=encuesta_data["completed_at"],
                                ingrediente_adic=encuesta_data["ingrediente_adic"])
        return new_encuesta
