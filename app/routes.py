from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(url_for('index.html'), title="home", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data},\
              remember_me={form.remember_me.data}')
        return redirect(url_for('index.html'))
    return render_template(url_for('login'), title="Sign In", form=form)