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

    favoritos = db.relationship('Favoritos',back_populates='cerveza')

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
    


def agregar_cervezas_iniciales():
    cervezas = [
        {"nombre":"Dark Lager", "marca":"Principia","porcentaje_alcohol":4.0, "estilo":"lager", "ibus":22, "color":"obscura", "sabor":["caramelo","tostado"], "ingrediente_adicional":"cafe"},
        {"nombre":"American Wheat Ale", "marca":"Principia","porcentaje_alcohol":4.3, "estilo":"wheat ale", "ibus":18, "color":"clara", "sabor":"ligero y refrescante", "ingrediente_adicional":"ninguno"},
        {"nombre":"Extrasolar", "marca":"Principia","porcentaje_alcohol":6.5, "estilo":"ipa", "ibus":30, "color":"clara turbia", "sabor":"frutal y dulce", "ingrediente_adicional":"frutas"},
        {"nombre":"Spectra", "marca":"Principia","porcentaje_alcohol":6.7, "estilo":"ipa", "ibus":60, "color":"clara dorada", "sabor":"citrico", "ingrediente_adicional":"ninguno"},
        {"nombre":"Asimetria", "marca":"Principia","porcentaje_alcohol":5.5, "estilo":"stout", "ibus":20, "color":"obscura", "sabor":["caramelo","tostado"], "ingrediente_adicional":"mantequilla de mani"},
        {"nombre":"Craft Pilsner", "marca":"Principia","porcentaje_alcohol":4.1, "estilo":"pilsner", "ibus":27, "color":"clara", "sabor":"citrico", "ingrediente_adicional":"frutas"},
        {"nombre":"Lunada", "marca":"De la Costa","porcentaje_alcohol":5.0, "estilo":"dunkel", "ibus":23, "color":"obscura", "sabor":"tostado", "ingrediente_adicional":"chocolate"},
        {"nombre":"Bahia", "marca":"De la Costa","porcentaje_alcohol":3.8, "estilo":"lager", "ibus":14, "color":"muy clara", "sabor":"ligero y refrescante", "ingrediente_adicional":"ninguno"},
        {"nombre":"Harry Polanco", "marca":"Wendlandt","porcentaje_alcohol":5.5, "estilo":"red ale", "ibus":50, "color":"rojiza", "sabor":["caramelo","tostado"], "ingrediente_adicional":"ninguno"},
        {"nombre":"Perro del mar", "marca":"Wendlandt","porcentaje_alcohol":7.0, "estilo":"ipa", "ibus":60, "color":"clara", "sabor":"amargo intenso", "ingrediente_adicional":"ninguno"},
        {"nombre":"Foca parlante", "marca":"Wendlandt","porcentaje_alcohol":5.5, "estilo":"stout", "ibus":38, "color":"obscura", "sabor":"tostado", "ingrediente_adicional":["cafe","chocolate"]},
        {"nombre":"Vaquita marina", "marca":"Wendlandt","porcentaje_alcohol":5.2, "estilo":"pale ale", "ibus":42, "color":"clara", "sabor":"citrico", "ingrediente_adicional":"ninguno"},
        {"nombre":"Veraniega", "marca":"Wendlandt","porcentaje_alcohol":4.7, "estilo":"pale ale", "ibus":20, "color":"muy clara", "sabor":"ligero y refrescante", "ingrediente_adicional":"ninguno"},
        {"nombre":"Frambuesa", "marca":"Stiegl","porcentaje_alcohol":2.0, "estilo":"lager frutal", "ibus":8, "color":"clara", "sabor":"frutal y dulce", "ingrediente_adicional":"frutas"},
        {"nombre":"Toronja", "marca":"Stiegl","porcentaje_alcohol":2.0, "estilo":"lager frutal", "ibus":8, "color":"clara", "sabor":"frutal y dulce", "ingrediente_adicional":"frutas"},
        {"nombre":"Limon", "marca":"Stiegl","porcentaje_alcohol":2.0, "estilo":"lager frutal", "ibus":8, "color":"clara", "sabor":"ligero y refrescante", "ingrediente_adicional":"frutas"},
        {"nombre":"Lagrimas negras", "marca":"Ramuri","porcentaje_alcohol":10.0, "estilo":"imperial cacao stout", "ibus":34, "color":"muy obscura", "sabor":"tostado", "ingrediente_adicional":"chocolate"},
        {"nombre":"Lagrimas de cacahuate", "marca":"Ramuri","porcentaje_alcohol":8.0, "estilo":"imperial cacao stout", "ibus":38, "color":"muy obscura", "sabor":"ninguno", "ingrediente_adicional":"mantequilla de mani"},
        {"nombre":"Odin", "marca":"Ramuri","porcentaje_alcohol":9.3, "estilo":"imperial coffee stout", "ibus":74, "color":"muy obscura", "sabor":"ninguno", "ingrediente_adicional":"cafe"},
        {"nombre":"Estrella Galicia", "marca":"Estrella de Galicia","porcentaje_alcohol":5.5, "estilo":"helles export bierr", "ibus":25, "color":"dorado", "sabor":"ligero y refrescante", "ingrediente_adicional":"ninguno"},
        {"nombre":"Spring IPA", "marca":"19 Norte","porcentaje_alcohol":7.5, "estilo":"ipa", "ibus":60, "color":"clara", "sabor":"caramelo", "ingrediente_adicional":"ninguno"},
        {"nombre":"Dakota Stout", "marca":"19 Norte","porcentaje_alcohol":7.8, "estilo":"stout", "ibus":40, "color":"obscura", "sabor":"ninguno", "ingrediente_adicional":["cafe","chocolate"]},
        {"nombre":"Summer Daze", "marca":"19 Norte","porcentaje_alcohol":6, "estilo":"wheat ale", "ibus":29, "color":"clara", "sabor":"citrico", "ingrediente_adicional":"frutas"},
        {"nombre":"Latin Lager", "marca":"19 Norte","porcentaje_alcohol":5.5, "estilo":"lager", "ibus":40, "color":"clara", "sabor":"ligero y refrescante", "ingrediente_adicional":"ninguno"},
        {"nombre":"Caramelo Brown", "marca":"19 Norte","porcentaje_alcohol":7.6, "estilo":"brown ale", "ibus":22, "color":"caramelo", "sabor":"caramelo", "ingrediente_adicional":"chocolate"},
        {"nombre":"Porter", "marca":"Xinampa","porcentaje_alcohol":6, "estilo":"porter", "ibus":45, "color":"obscura", "sabor":"tostado", "ingrediente_adicional":"ninguno"},
        {"nombre":"Amber Ale", "marca":"Xinampa","porcentaje_alcohol":5.5, "estilo":"amber ale", "ibus":40, "color":"clara", "sabor":["caramelo","citrico"], "ingrediente_adicional":"ninguno"},
        {"nombre":"Pale Ale", "marca":"Xinampa","porcentaje_alcohol":5.5, "estilo":"pale ale", "ibus":40, "color":"clara", "sabor":"ninguno", "ingrediente_adicional":"ninguno"}
    ]
    for cerveza_data in cervezas:
        cerveza = Cerveza(**cerveza_data)
        db.session.add(cerveza)
    db.session.commit()
    