from flask import Flask
from admin import admin_bp
from blog import blog_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(blog_bp)

@app.route('/')
def index():
    return '''
    <h1>Proyecto AppBlue - Blueprints en Flask</h1>
    <p>Visita el <a href="/panel">Panel de Administración</a></p>
    <p>Visita una <a href="/entrada/1">Entrada del Blog</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)