# blog_posts/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint, abort
from flask_login import current_user,login_required
from portfolio import db
from models import BlogPost
from blogs.forms import BlogPostForm
from file_upload import add_file
blogs = Blueprint('blogs',__name__)

# GET
@blogs.route('/blogs')
def all_blogs():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('blogs.html',blog_posts=blog_posts)
# CREATE
@blogs.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                            description=form.description.data,
                            file = add_file(form.file.data),
                            user_id=current_user.id
                            )
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('home.index'))

    return render_template('create_blog.html', form=form)




# BLOG POST (VIEW)
@blogs.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,description=blog_post.description,
                            date=blog_post.date,post=blog_post
    )



# UPDATE
@blogs.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    form = BlogPostForm()
    if form.validate_on_submit():
        if form.file.data:
            blog_post.file = add_file(form.file.data)
        blog_post.title = form.title.data
        blog_post.description = form.description.data

        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blogs.blog_post',blog_post_id=blog_post.id))

    elif request.method == 'GET':
        form.title.data = blog_post.title

    return render_template('create_blog.html',title='Update',form=form)


# DELETE
@blogs.route('/<int:blog_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('home.index'))
