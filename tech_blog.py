from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd37836b284dedee931e81f275733bd9d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =  SQLAlchemy(app)

class User(db.Model):
    pass

posts = [
    {
        'author' : 'Fatima Askerova',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'October 16, 2020'   
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'October 17, 2020'   
    }
]

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/database')
def database():
    return render_template('about.html', title='Database')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

