from flask import render_template, flash, redirect, url_for
from app import app, db
from forms import LoginForm, RegistrationForm, DeleteUserButton
from flask_login import current_user, login_user, logout_user, login_required
from models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('manage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        flash('Login successfully. Hi, {}!'.format(form.username.data))
        return redirect(url_for('manage'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
    form = RegistrationForm()
    users = User.query.all()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User added.')
        return redirect(url_for('manage'))
    return render_template('manage.html', title='Management', form=form, users=users)

@app.route('/delete/<string:user>')
@login_required
def delete_user(user):
    u = User.query.filter_by(username=user).first()
    if u.username == 'admin':
        flash('This superuser can not be deleted.')
        return redirect(url_for('manage'))
    db.session.delete(u)
    db.session.commit()
    flash('User {} deleted.'.format(user))
    return redirect(url_for('manage'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
