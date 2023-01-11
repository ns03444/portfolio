from flask import request, render_template, Blueprint
from models import BlogPost
home = Blueprint('home', __name__)
# blogs = Blueprint('blogs', __name__)

@home.route('/')
def index():
    latest_post = BlogPost.query.all()[-1]
    return render_template('index.html', latest_post=latest_post)
@home.route('/testnav')
def testnav():
    blog_posts = BlogPost.query.all()
    return render_template('testnav.html', blog_posts=blog_posts)
# @blogs.route('/blogs')
# def my_blogs():
#     page = request.args.get('page', 1, type=int)
#     blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
#     return render_template('my_blogs.html',blog_posts=blog_posts)