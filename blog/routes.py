from flask import render_template
from . import blog_bp

# Datos de ejemplo (simulando una base de datos)
entradas = {
    1: "Mi primera entrada de blog",
    2: "Aprendiendo Flask con Blueprints",
    3: "Cómo organizar proyectos grandes"
}

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = entradas.get(id, "Entrada no encontrada")
    return render_template('blog/entrada.html', titulo=titulo, id=id)