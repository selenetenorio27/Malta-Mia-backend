from app import db
from app.models.cerveza import Cerveza
from app.models.sabor import Sabor

def agregar_cervezas():
    # Crea sabores y agrégales a la base de datos
    sabores_data = ["Dulce", "Amargo", "Ácido", "Afrutado", "Caramelo", "Especiado"]
    sabores = []
    for sabor_nombre in sabores_data:
        sabor = Sabor.query.filter_by(nombre=sabor_nombre).first()
        if not sabor:
            sabor = Sabor(nombre=sabor_nombre)
            db.session.add(sabor)
        sabores.append(sabor)
    
    db.session.commit()
    
    # Crea cervezas y agrégales a la base de datos
    cervezas_data = [
        {
            "nombre":"Dark Lager",
            "marca":"Principia",
            "porcentaje_alcohol":4.0,
            "estilo":"lager",
            "ibus":22,
            "color":"obscura",
            "sabor":['caramel','toasted'],
            "ingrediente_adicional":"coffee"
        },
        {
            "nombre":"American Wheat Ale",
            "marca":"Principia",
            "porcentaje_alcohol":4.3,
            "estilo":"wheat_ale",
            "ibus":18,
            "color":"clara",
            "sabor":"light_and_refreshing",
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Extrasolar", 
            "marca":"Principia",
            "porcentaje_alcohol":6.5, 
            "estilo":"ipa", 
            "ibus":30, 
            "color":"clara turbia", 
            "sabor":"fruity", 
            "ingrediente_adicional":"fruit"
        },
        {
            "nombre":"Spectra", 
            "marca":"Principia",
            "porcentaje_alcohol":6.7, 
            "estilo":"ipa", 
            "ibus":60, 
            "color":"clara dorada", 
            "sabor":"citric", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Asimetria", 
            "marca":"Principia",
            "porcentaje_alcohol":5.5, 
            "estilo":"stout", 
            "ibus":20, 
            "color":"obscura", 
            "sabor":['caramel','toasted'], 
            "ingrediente_adicional":"peanut_butter"   
        },
        {
            "nombre":"Craft Pilsner", 
            "marca":"Principia",
            "porcentaje_alcohol":4.1, 
            "estilo":"pilsner", 
            "ibus":27, 
            "color":"clara", 
            "sabor":"citric", 
            "ingrediente_adicional":"fruit"    
        },
        {
            "nombre":"Lunada", 
            "marca":"De la Costa",
            "porcentaje_alcohol":5.0, 
            "estilo":"dunkel", 
            "ibus":23, 
            "color":"obscura", 
            "sabor":"toasted", 
            "ingrediente_adicional":"chocolate"  
        },
        {
            "nombre":"Bahia", 
            "marca":"De la Costa",
            "porcentaje_alcohol":3.8, 
            "estilo":"lager", 
            "ibus":14, 
            "color":"muy clara", 
            "sabor":"light_and_refreshing", 
            "ingrediente_adicional":"none"  
        },
        {
            "nombre":"Harry Polanco", 
            "marca":"Wendlandt",
            "porcentaje_alcohol":5.5, 
            "estilo":"red_ale", 
            "ibus":50, 
            "color":"rojiza", 
            "sabor":['caramel','toasted'], 
            "ingrediente_adicional":"none"  
        },
        {
            "nombre":"Perro del mar", 
            "marca":"Wendlandt",
            "porcentaje_alcohol":7.0, 
            "estilo":"ipa", 
            "ibus":60, 
            "color":"clara", 
            "sabor":"intense_bitter", 
            "ingrediente_adicional":"none"   
        },
        {
            "nombre":"Foca parlante", 
            "marca":"Wendlandt",
            "porcentaje_alcohol":5.5, 
            "estilo":"stout", 
            "ibus":38, 
            "color":"obscura", 
            "sabor":"toasted", 
            "ingrediente_adicional":['coffee','chocolate'] 
        },
        {
            "nombre":"Vaquita marina",
            "marca":"Wendlandt",
            "porcentaje_alcohol":5.2, 
            "estilo":"pale_ale", 
            "ibus":42, 
            "color":"clara", 
            "sabor":"citric", 
            "ingrediente_adicional":"none" 
        },
        {
            "nombre":"Veraniega", 
            "marca":"Wendlandt",
            "porcentaje_alcohol":4.7, 
            "estilo":"pale_ale", 
            "ibus":20, 
            "color":"muy clara", 
            "sabor":"light_and_refreshing", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Frambuesa", 
            "marca":"Stiegl",
            "porcentaje_alcohol":2.0, 
            "estilo":"lager_frutal", 
            "ibus":8, 
            "color":"clara", 
            "sabor":"fruity", 
            "ingrediente_adicional":"fruit"
        },
        {
            "nombre":"Toronja",
            "marca":"Stiegl",
            "porcentaje_alcohol":2.0, 
            "estilo":"lager_frutal", 
            "ibus":8, 
            "color":"clara", 
            "sabor":"fruity", 
            "ingrediente_adicional":"fruit"
        },
        {
            "nombre":"Limon", 
            "marca":"Stiegl",
            "porcentaje_alcohol":2.0, 
            "estilo":"lager_frutal", 
            "ibus":8, 
            "color":"clara", 
            "sabor":"light_and_refreshing", 
            "ingrediente_adicional":"fruit"
        },
        {
            "nombre":"Lagrimas negras", 
            "marca":"Ramuri",
            "porcentaje_alcohol":10.0, 
            "estilo":"imperial_cacao_stout", 
            "ibus":34, 
            "color":"muy obscura", 
            "sabor":"toasted", 
            "ingrediente_adicional":"chocolate"
        },
        {
            "nombre":"Lagrimas de cacahuate", 
            "marca":"Ramuri",
            "porcentaje_alcohol":8.0, 
            "estilo":"imperial_cacao_stout", 
            "ibus":38, 
            "color":"muy obscura", 
            "sabor":"none", 
            "ingrediente_adicional":"peanut_butter"
        },
        {
            "nombre":"Odin", 
            "marca":"Ramuri", 
            "porcentaje_alcohol":9.3, 
            "estilo":"imperial_coffee_stout", 
            "ibus":74, 
            "color":"muy obscura", 
            "sabor":"none", 
            "ingrediente_adicional":"coffee"
        },
        {
            "nombre":"Estrella Galicia", 
            "marca":"Estrella de Galicia",
            "porcentaje_alcohol":5.5, 
            "estilo":"helles_export_bierr",
            "ibus":25, 
            "color":"dorado", 
            "sabor":"light_and_refreshing", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Spring IPA", 
            "marca":"19 Norte",
            "porcentaje_alcohol":7.5, 
            "estilo":"ipa", 
            "ibus":60, 
            "color":"clara", 
            "sabor":"caramel", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Dakota Stout", 
            "marca":"19 Norte",
            "porcentaje_alcohol":7.8, 
            "estilo":"stout", 
            "ibus":40, 
            "color":"obscura", 
            "sabor":"none", 
            "ingrediente_adicional":['coffee','chocolate']
        },
        {
            "nombre":"Summer Daze", 
            "marca":"19 Norte",
            "porcentaje_alcohol":6, 
            "estilo":'wheat_ale', 
            "ibus":29, 
            "color":"clara", 
            "sabor":"citric", 
            "ingrediente_adicional":"fruit"
        },
        {
            "nombre":"Latin Lager", 
            "marca":"19 Norte",
            "porcentaje_alcohol":5.5, 
            "estilo":"lager", 
            "ibus":40, 
            "color":"clara", 
            "sabor":"light_and_refreshing", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"caramel Brown", 
            "marca":"19 Norte",
            "porcentaje_alcohol":7.6, 
            "estilo":"brown_ale", 
            "ibus":22, 
            "color":"caramel", 
            "sabor":"caramel", 
            "ingrediente_adicional":"chocolate"
        },
        {
            "nombre":"Porter", 
            "marca":"Xinampa",
            "porcentaje_alcohol":6, 
            "estilo":"porter", 
            "ibus":45, 
            "color":"obscura", 
            "sabor":"toasted", 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Amber Ale", 
            "marca":"Xinampa",
            "porcentaje_alcohol":5.5, 
            "estilo":"amber_ale", 
            "ibus":40, 
            "color":"clara", 
            "sabor":['caramel','citric'], 
            "ingrediente_adicional":"none"
        },
        {
            "nombre":"Pale Ale", 
            "marca":"Xinampa",
            "porcentaje_alcohol":5.5, 
            "estilo":"pale_ale", 
            "ibus":40, 
            "color":"clara", 
            "sabor":"none", 
            "ingrediente_adicional":"none"
        }
    ]


    for cerveza_data in cervezas_data:
        sabores_cerveza = []
        for sabor_nombre in cerveza_data.pop("sabores", []):
            sabor = Sabor.query.filter_by(nombre=sabor_nombre).first()
            if sabor:
                sabores_cerveza.append(sabor)
        cerveza = Cerveza(**cerveza_data)
        cerveza.sabores = sabores_cerveza
        db.session.add(cerveza)
    
    db.session.commit()

if __name__ == "__main__":
    agregar_cervezas()