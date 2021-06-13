from flask import render_template,url_for,flash,redirect
from flask_blog import app
from flask_blog.forms import SignUpForm,LoginForm
from flask_blog.models import User,Post

posts = [
  {
    "Author": "Farah",
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "Author": "yasin",
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title="Home page")



@app.route('/about')
def about():
     return render_template('about.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if(form.validate_on_submit()):
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('signup.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == "elabe@gmail.com" and form.password.data == "123"):
            flash('You successfully logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password','danger')
    return render_template('login.html',title='Login',form=form)


