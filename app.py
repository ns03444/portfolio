from flask import Flask,flash,request,redirect,url_for,send_from_directory,render_template,current_app
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,login_user,current_user,logout_user,login_required,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from file_upload import add_file
from datetime import datetime
# from models import User, BlogPost
# from forms import BlogPostForm,LoginForm,RegistrationForm
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired,Email,EqualTo


app = Flask(__name__)

UPLOAD_FOLDER = '/static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'mysecretkey'

#########################
# LOGIN CONFIGS #########
#########################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader

def load_user(user_id):
    """Loads a user from `User` database table using the given `user_id`."""

    return User.query.get(int(user_id))

###########################
### DATABASE SETUP ########
###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class User(db.Model,UserMixin):
    """`User` database table."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    # USER - BLOG RELATIONSHIP
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username: {self.username} -- {self.email}"


class BlogPost(db.Model):
    """`User` database table."""

    # USER - BLOG RELATIONSHIP
    users = db.relationship(User)

    # Notice how we connect the BlogPost to a particular author
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    # BLOG ATTRIBUTES
    title = db.Column(db.String(140),nullable=False)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    description = db.Column(db.Text,nullable=True)
    file = db.Column(db.String(20), nullable=False)

    def __init__(self,title,file,description, user_id):
        self.title = title
        self.description = description
        self.file = file
        self.user_id = user_id

    def __repr__(self):
        return f"Blog ID: {self.id} -- Date: {self.date} --- {self.title}"


###########################
### FORMS #################
###########################
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description')
    file = FileField('Upload PDF file', validators=[FileAllowed(['pdf'])])
    submit = SubmitField("Post")



#########################
######## VIEWS ##########
#########################
@app.route('/')
def index():
    latest_post = BlogPost.query.all()[-1]
    return render_template('index.html', latest_post=latest_post)

@app.route('/blogs')
def blogs():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('blogs.html',blog_posts=blog_posts)

@app.route('/projects')
def projects():
    return render_template('projects.html')

#########################
### USER VIEWS ##########
#########################
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')

            # If a user tries to visit page that requires login, flask saves as 'next'.
            next = request.args.get('next')

            # if that next does not exists, go to the home page.
            if next == None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create_blog', methods=['GET', 'POST'])
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
        return redirect(url_for('blogs'))

    return render_template('create_blog.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
