from app import db
from app.models.cerveza import Cerveza

def agregar_cervezas():
    cerveza1 = Cerveza(nombre='Dark Lager', marca='Principia',porcentaje_alcohol=4.0, estilo='lager', ibus=22, color='obscura', sabor='Caramelo y tostado', ingrediente_adicional='cafe')
    cerveza2 = Cerveza(nombre='American Wheat Ale', marca='Principia',porcentaje_alcohol=4.3, estilo='wheat ale', ibus=18, color='clara', sabor='Ligero y refrescante', ingrediente_adicional='ninguno')

    db.session.add(cerveza1)
    db.session.add(cerveza2)

    db.session.commit()

if __name__ == "__main__":
    from app import create_app

    app = create_app()
    with app.app_context():
        agregar_cervezas()