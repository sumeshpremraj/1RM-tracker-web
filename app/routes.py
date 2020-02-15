from flask import request, render_template, redirect, url_for, flash
from app import app, db
from flask_login import current_user, login_required, login_user, logout_user
from app.forms import LoginForm, RegistrationForm, MaxForm
from app.models import User, Lift
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return "Index page"

@app.route('/max', methods=['GET', 'POST'])
@login_required
def max():
    form = MaxForm()
    if form.validate_on_submit():
        lift = Lift(user_id=current_user.get_id(),\
                    lift_name=form.lift_name.data,\
                    max=form.max.data,\
                    weight=form.weight.data,\
                    reps=form.reps.data,\
                    timestamp=form.timestamp.data)
        db.session.add(lift)
        db.session.commit()
        flash('Saved data')
        return redirect(url_for('max'))
    return render_template('max.html', title='Max', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)