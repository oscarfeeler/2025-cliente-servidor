from flask import Flask
import prueba3

app = Flask(__name__)


panel = prueba3.crear_panel(10, 10)


@app.route("/")
def hello_world():
    global panel
    panel = prueba3.siguiente_generacion(panel)
    return f"{panel}"

if __name__ == '__main__':
    app.run(host='192.168.1.15', port=5000, debug=False)
    
    # ahora tenemos que importar el juego de la vidita mi niiiiiiiiiinio!!!
    # metiendo nuestro juguetito de la vidiña en una jugosa y deliciosa funcion
    # y luego importarlo aqui para que la funcion main lo corra
    # magia borrás, ni lo ves ni    lo veras tris tras 