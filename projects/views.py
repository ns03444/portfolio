from flask import request, render_template, Blueprint
from models import BlogPost
projects = Blueprint('projects', __name__)

@projects.route('/projects')
def all_projects():
    return render_template('projects.html')