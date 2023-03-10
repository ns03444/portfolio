# users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from portfolio import db
from models import User, BlogPost
from users.forms import RegistrationForm,LoginForm,UpdateUserForm
# from nicks_app.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

# login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next ==None or not next[0]=='/':
                next = url_for('home.index')

            return redirect(next)

    return render_template('login.html',form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.index"))


# account (update UserForm)
# @users.route('/account',methods=['GET','POST'])
# @login_required
# def account():
#     form = UpdateUserForm()
#     if form.validate_on_submit():
#         # if form.picture.data:
#         #     username = current_user.username
#             # pic = add_profile_pic(form.picture.data,username)
#             # current_user.profile_image = pic

#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('User Account Updated!')
#         return redirect(url_for('users.account'))

#     elif request.method == "GET":
#         form.username.data = current_user.username
#         form.email.data = current_user.email

#     return render_template('account.html',form=form)


# @users.route("/<username>")
# def user_posts(username):
#     page = request.args.get('page',1,type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
#     return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user)











# user's list of Blog posts
