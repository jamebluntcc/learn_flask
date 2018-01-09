from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
test = Blueprint('test', __name__, template_folder='../templates', url_prefix='/test')

@test.route('/')
def page():
    try:
        user = 'jamebluntcc'
        return render_template('index.html',user=user)
    except TemplateNotFound:
        abort(404)


    
